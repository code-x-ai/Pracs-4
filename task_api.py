from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task Management API")

class Task(BaseModel):
    id: int
    title: str
    status: str
    priority: str

tasks = [
    {"id": 1, "title": "Complete Cloud Computing Assignment",
     "status": "Pending", "priority": "High"},
    {"id": 2, "title": "Prepare RESTAPI practical",
     "status": "In Progress", "priority": "Medium"},
]

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for t in tasks:
        if t["id"] == task_id:
            return t
    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task.model_dump())
    return {"message": "Task created successfully", "task": task}

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated: Task):
    for i, t in enumerate(tasks):
        if t["id"] == task_id:
            tasks[i] = updated.model_dump()
            return {"message": "Task updated successfully", "task": updated}
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for t in tasks:
        if t["id"] == task_id:
            tasks.remove(t)
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")
