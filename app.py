from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Todo model
class Todo(db.Model):
    SNo = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.SNo} - {self.title}"

# Home route with GET + POST
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":   # ✅ Must be uppercase "POST"
        title = request.form.get('title')   # ✅ get title from form
        desc = request.form.get('desc')     # ✅ get desc from form

        # Only add todo if both title and desc are provided
        if title and desc:
            todo = Todo(title=title, desc=desc)
            db.session.add(todo)
            db.session.commit()

    # Fetch all todos to display
    allTodo = Todo.query.all()
    return render_template("index.html", allTodo=allTodo)

# Update a todo
@app.route('/update/<int:SNo>', methods=['GET', 'POST'])
def update(SNo):
    todo = Todo.query.get_or_404(SNo)

    if request.method == "POST":
        todo.title = request.form.get('title')
        todo.desc = request.form.get('desc')
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("update.html", todo=todo)

# Delete a todo
@app.route('/delete/<int:SNo>')
def delete(SNo):
    todo = Todo.query.get_or_404(SNo)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)
