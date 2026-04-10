from pydantic import BaseModel

class Observation(BaseModel):
    echoed_message: str

class Action(BaseModel):
    message: str

class StepResult(BaseModel):
    observation: Observation
    reward: float
    done: bool
    info: dict = {}
