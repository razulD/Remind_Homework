import json
import sys
import os
from flask import Flask, render_template, request, redirect, url_for

FILE = "homework.json"
SUBJECTS = ["ITS", "ENTERPRISE IN IT", "WEBSITE DEVELOPMENT", "STUDY SKILLS", "PROGRAMMING", "HISTORY", "OTHERS"]

def load_tasks():
    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

if len(sys.argv) > 1 and sys.argv[1] == "show":
    tasks = load_tasks()
    active_tasks = [t for t in tasks if t.get("status", "active") == "active"]
    
    if not active_tasks:
        print("Nothing to do!")
    else:
        print("Here is everything you currently need to complete:\n")
        for t in active_tasks:
            print(f"• [{t['subject']}] {t['task']}")
    sys.exit()

app = Flask(__name__)

@app.route("/")
def index():
    tasks = load_tasks()
    active_tasks = [(i, t) for i, t in enumerate(tasks) if t.get("status", "active") == "active"]
    return render_template("index.html", subjects=SUBJECTS, tasks=active_tasks)

@app.route("/add", methods=["POST"])
def add():
    subj = request.form.get("subject")
    if subj == "OTHERS":
        subj = request.form.get("custom_subject", "").strip()
    
    task_text = request.form.get("task", "").strip()
    
    if subj and task_text:
        tasks = load_tasks()
        tasks.append({"subject": subj, "task": task_text, "status": "active"})
        save_tasks(tasks)
        
    return redirect(url_for("index"))

@app.route("/done/<int:task_id>")
def mark_done(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks[task_id]["status"] = "done"
        save_tasks(tasks)
    return redirect(url_for("index"))

@app.route("/archive")
def archive():
    tasks = load_tasks()
    done_tasks = [(i, t) for i, t in enumerate(tasks) if t.get("status") == "done"]
    return render_template("archive.html", tasks=done_tasks)

if __name__ == "__main__":
    app.run(debug=True, port=5000)