from fastapi import FastAPI
from pydantic import BaseModel
from workflows import graph_app

app = FastAPI()

class RequestModel(BaseModel):
    prompt: str

@app.post("/generate")
async def generate(request: RequestModel):
    try:
        # Initialize graph state properly
        state = {"messages": [request.prompt]}
        result = await graph_app.ainvoke(state)
        return {"response": result["messages"][-1]}  # return last message
    except Exception as e:
        return {"error": str(e)}
