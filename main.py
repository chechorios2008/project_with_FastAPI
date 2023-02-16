from fastapi import FastAPI

app = FastAPI()

@app.get(path="/")
def home():
    return {"Twitter API":"Hello checho your API is working"}