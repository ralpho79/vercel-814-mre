import csv
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        text = request.form["input_text"]
        list_to_csv(text,"/tmp/example.csv")
        return redirect(url_for("index"))
    
    my_list=csv_to_list("/tmp/example.csv")
    return render_template("index.html",list=my_list)


def list_to_csv(list,name):
    with open(name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(list)

def csv_to_list(f):
    lst=[*csv.reader(open(f))]; return(lst)


if __name__ == "__main__":
    my_bands=["Foo Fighters", "The Killers", "Greta Van Fleet"]
    list_to_csv(my_bands,"example.csv")
