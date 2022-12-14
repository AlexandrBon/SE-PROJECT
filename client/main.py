
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />

    <title>Todo App</title>

    <link rel="icon" type="image/png" href="favicon.png" />
    <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
    <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
  </head>

  <body class="container">
  <py-script>
from datetime import datetime as dt

def remove_class(element, class_name):
    element.element.classList.remove(class_name)


def add_class(element, class_name):
    element.element.classList.add(class_name)


tasks = []

# define the task template that will be use to render new templates to the page
task_template = Element("task-template").select(".task", from_content=True)
task_list = Element("list-tasks-container")
new_task_content = Element("new-task-content")


def add_task(*ags, **kws):
    # ignore empty task
    if not new_task_content.element.value:
        return None

    # create task
    task_id = f"task-{len(tasks)}"
    task = {
        "id": task_id,
        "content": new_task_content.element.value,
        "done": False,
        "created_at": dt.now(),
    }

    tasks.append(task)

    # add the task element to the page as new node in the list by cloning from a
    # template
    task_html = task_template.clone(task_id, to=task_list)
    task_html_content = task_html.select("p")
    task_html_content.element.innerText = task["content"]
    task_html_check = task_html.select("input")
    task_list.element.appendChild(task_html.element)

    def check_task(evt=None):
        task["done"] = not task["done"]
        if task["done"]:
            add_class(task_html_content, "line-through")
        else:
            remove_class(task_html_content, "line-through")

    new_task_content.clear()
    task_html_check.element.onclick = check_task


def add_task_event(e):
    if e.key == "Enter":
        add_task()


new_task_content.element.onkeypress = add_task_event
  </py-script>

  <main class="max-w-xs mx-auto mt-4">
    <section>

    <div class="text-center w-full mb-8">
      <h1 class="text-3xl font-bold text-gray-800 uppercase tracking-tight">To Do List</h1>
    </div>
    <div>
      <input id="new-task-content" class="border flex-1 mr-3 border-gray-300 p-2 rounded" type="text">
      <button id="new-task-btn" class="p-2 text-white bg-blue-600 border border-blue-600 rounded" type="submit" pys-onClick="add_task">
        Add task
      </button>
    </div>

    <py-list id="myList"></py-list>
    <div id="list-tasks-container" class="flex flex-col-reverse mt-4">
  </div>

    <template id="task-template">
        <section class="task bg-white my-1">
            <label for="flex items-center p-2 ">
                <input class="mr-2" type="checkbox" class="task-check">
                <p class="m-0 inline"></p>
            </label>
        </section>
    </template>

  </section>
  </main>
</body>
</html>