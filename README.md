# OpenEnv Project

## Description
This environment simulates a message echo system where reward is based on message length.

## Tasks
- Easy: short message
- Medium: medium message
- Hard: long message

## Action Space
Send a message string.

## Observation Space
Returns echoed message.

## Reward
reward = min(len(message) * 0.01, 1.0)

## Run Locally
```bash
pip install .
uvicorn my_env.app:app --reload

##Inference
python inference.py

---

# 🔥 FINAL STEPS (VERY IMPORTANT)

### 1. Delete old files
- old `app.py`
- old structure

---

### 2. Push new repo
```bash
git add .
git commit -m "fixed openenv structure"
git push