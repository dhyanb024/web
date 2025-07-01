from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/book", methods=["POST"])
def book():
    name = request.form.get("name")
    email = request.form.get("email")
    car = request.form.get("car")
    date = request.form.get("date")
    
    return render_template("confirmation.html", name=name, email=email, car=car, date=date)

if __name__ == "__main__":
    app.run(debug=True)
