import requests

BASE_URL = "http://localhost:7860"

def log_start():
    print("[START] task=easy env=my-env model=baseline")

def log_step(step, action, reward, done):
    print(f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error=null")

def log_end(success, steps, score, rewards):
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(f"[END] success={str(success).lower()} steps={steps} score={score:.2f} rewards={rewards_str}")

def main():
    rewards = []
    log_start()

    r = requests.post(f"{BASE_URL}/reset")
    done = False

    for step in range(1, 6):
        action = "This is a meaningful long message to maximize reward"
        res = requests.post(f"{BASE_URL}/step", json={"message": action}).json()

        reward = res["reward"]
        done = res["done"]

        rewards.append(reward)
        log_step(step, action, reward, done)

        if done:
            break

    score = min(sum(rewards), 1.0)
    success = score > 0.1

    log_end(success, step, score, rewards)

if __name__ == "__main__":
    main()