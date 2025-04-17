from flask import Flask, render_template, request, redirect

app = Flask(__name__)
tasks = []  # Temporary list to store tasks

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks.append(task)
    return render_template("index.html", tasks=tasks)

@app.route("/delete/<int:task_id>")
def delete(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect("/")

@app.route("/update/<int:task_id>", methods=["POST"])
def update(task_id):
    new_task = request.form.get("new_task")
    if new_task:
        tasks[task_id] = new_task
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
