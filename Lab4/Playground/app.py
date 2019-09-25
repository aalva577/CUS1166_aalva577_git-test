from flask import Flask, render_template

app = Flask(__name__)
class_roster =
                [("Manny","F","Freshman"),
                ("Oscar","D","Junior"),
                ("Cristiano","C","Junior"),
                ("Trevor","B","Sophomore"),
                ("Nick","A","Senior"),
                ("Nathan","F","Freshman"),
                ("Julissa","A","Senior"),
                ("Kipper","A","Junior"),
                ("Hamstee","F","Senior")]
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/welcome/<string:student_name>")
def welcome(students_name):
    return render_template("welcome.html", students_name=students_name)

@app.route("/roster/<int:grade_view>")
def roster(grade_view):
    return render_template("roster.html", class_roster=class_roster, grade_view=grade_view)

if __name__ == '__main__':
    app.run()
