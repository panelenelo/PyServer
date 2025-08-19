from fastapi import FastAPI
from Task import Task

app = FastAPI()



@app.get("/tasks")
async def read_tasks():
    return {"task1": "task1"}

@app.get("/tasks/{task_id}")
async def read_task_item(task_id):
    return{"task": task_id}

@app.post("/tasks")
async def post_task(task):
    return{"Task created"}

@app.put("/tasks/{task_id}")
async def put_task(task):
    return{"Task updated"}

@app.delete("/tasks/{task_id}")
async def delete_task(task_id):
    return("Task deleted")

