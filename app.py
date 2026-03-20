"""
Hidden Gem Digitals — Local website by and for Columbia students.
Run:  python app.py
Then open: http://127.0.0.1:5000
"""

import os
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "hgd-secret-2026"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/examples")
def examples():
    return render_template("examples.html")

@app.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "POST":
        name    = request.form.get("name", "").strip()
        email   = request.form.get("email", "").strip()
        business= request.form.get("business", "").strip()
        message = request.form.get("message", "").strip()
        if name and email and message:
            flash("Thank you! I will be in touch within 24 hours.", "success")
        else:
            flash("Please fill in all required fields.", "error")
        return redirect(url_for("about") + "#contact")
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
