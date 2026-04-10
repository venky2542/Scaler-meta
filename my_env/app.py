from fastapi import FastAPI
from my_env.env import MyEnv
from my_env.models import Action

app = FastAPI()

env = MyEnv()

@app.post("/reset")
def reset():
    obs = env.reset()
    return {"observation": obs.dict(), "done": False}

@app.post("/step")
def step(action: Action):
    result = env.step(action)
    return {
        "observation": result.observation.dict(),
        "reward": result.reward,
        "done": result.done,
        "info": result.info
    }

@app.get("/state")
def state():
    return env.state()
