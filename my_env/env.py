from .models import Observation, Action, StepResult

class MyEnv:
    def __init__(self):
        self.done = False
        self.last_message = ""

    def reset(self):
        self.done = False
        self.last_message = ""
        return Observation(echoed_message="")

    def step(self, action: Action):
        message = action.message
        self.last_message = message

        reward = min(len(message) * 0.01, 1.0)

        if len(message) > 50:
            self.done = True

        return StepResult(
            observation=Observation(echoed_message=message),
            reward=reward,
            done=self.done,
            info={}
        )

    def state(self):
        return {"last_message": self.last_message}
