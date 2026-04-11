from fastapi import FastAPI
from .env import MyEnv
from .models import Action

try:
    # This works when running from the root of the project (local/dev)
    from .env import MyEnv
    from .models import Action
except ImportError:
    # This works when the app is installed as a package or run from inside the folder
    from .env import MyEnv
    from .models import Action
    
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
