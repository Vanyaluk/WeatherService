from flask import Flask, request, render_template, redirect, url_for


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        field1 = request.form.get("field1")
        field2 = request.form.get("field2")

        # запрос за данными


        return redirect(url_for("result", field1=field1, field2=field2))
    return render_template("index.html")


@app.route("/result")
def result():
    field1 = request.args.get("field1", "")
    field2 = request.args.get("field2", "")

    return render_template("result.html", field1=field1, field2=field2)


if __name__ == "__main__":
    app.run()