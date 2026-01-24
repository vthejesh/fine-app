from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
DB_NAME = "database.db"


def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            course TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


@app.route("/")
def index():
    conn = get_db_connection()
    students = conn.execute("SELECT * FROM students").fetchall()
    conn.close()
    return render_template("index.html", students=students)


@app.route("/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        course = request.form["course"]

        conn = get_db_connection()
        conn.execute("INSERT INTO students (name, email, course) VALUES (?, ?, ?)",
                     (name, email, course))
        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("add.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_student(id):
    conn = get_db_connection()

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        course = request.form["course"]

        conn.execute("UPDATE students SET name=?, email=?, course=? WHERE id=?",
                     (name, email, course, id))
        conn.commit()
        conn.close()

        return redirect("/")

    student = conn.execute("SELECT * FROM students WHERE id=?", (id,)).fetchone()
    conn.close()

    return render_template("edit.html", student=student)


@app.route("/delete/<int:id>")
def delete_student(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return redirect("/")


if __name__ == "__main__":
    create_table()
    app.run(debug=True)
