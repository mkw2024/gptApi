from datetime import datetime as dt

def format_date(dt_, fmt="%m/%d/%Y, %H:%M:%S"):
    return f"{dt_:{fmt}}"

def now(fmt="%m/%d/%Y, %H:%M:%S"):
    return format_date(dt.now(), fmt)

def remove_class(element, class_name):
    element.element.classList.remove(class_name)


def add_class(element, class_name):
    element.element.classList.add(class_name)
	
task_template = Element("outputText").select(".task", from_content=True)
task_list = Element("cont")
new_line_content = Element("inp")
lines = []
	
def add_line(*ags, **kws):
	if not new_task_content.element.value:
        return None
	line_id = f"line-{len(lines)}"
    line = {
        "id": task_id,
        "content": new_line_content.element.value,
        "done": False,
        "created_at": dt.now(),
    }
	lines.append(line)
	
	line_html = line_template.clone(line_id)
    line_html_content = line_html.select("p")
    line_html_content.element.innerText = line["content"]
    line_list.element.appendChild(line_html.element)
	
	new_task_content.clear()

def add_line_event(e):
    if e.key == "Enter":
        add_line()

inp.element.onkeypress = add_line_event

