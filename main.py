from flask import Flask, render_template, request, redirect, send_file
from wanted import playwirghtGO as startwanted
from file import writeCSV

app = Flask("JobScrapper")

# Fake database for test
db = {}

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("home.html", year="2024 Spring", version="ver 2")

@app.route("/search")
def render():
    keyword = request.args.get("job_keyword")
    if keyword == None:
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:
        jobs = startwanted([keyword])
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)

@app.route("/export")
def export():
    keyword = request.args.get("job_keyword")
    if keyword == None:
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    writeCSV(keyword, db[keyword])
    return send_file(f"{keyword}_jobs.csv", as_attachment=True)

app.run("127.0.0.1", debug=True)