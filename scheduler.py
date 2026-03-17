import joblib
import pandas as pd

# Load model
data = joblib.load("surgery_model.pkl")

model = data["model"]
le_surgery = data["le_surgery"]
le_condition = data["le_condition"]
features = data["features"]

# Prediction function
def predict_duration(surgery_type, experience, condition):
    s = le_surgery.transform([surgery_type])[0]
    c = le_condition.transform([condition])[0]

    input_df = pd.DataFrame([[s, experience, c]], columns=features)
    return int(round(model.predict(input_df)[0]))

# Surgery class
class Surgery:
    def __init__(self, id, surgery_type, experience, condition, priority):
        self.id = id
        self.surgery_type = surgery_type
        self.experience = experience
        self.condition = condition
        self.priority = priority
        self.duration = predict_duration(surgery_type, experience, condition)

# Conflict check
def check_conflict(start, end, schedule):
    for s in schedule:
        if not (end <= s["start"] or start >= s["end"]):
            return True
    return False

# Add surgery
def add_surgery(surgery, schedule):
    start = 9
    while True:
        end = start + surgery.duration

        if not check_conflict(start, end, schedule):
            schedule.append({
                "id": surgery.id,
                "type": surgery.surgery_type,
                "start": start,
                "end": end
            })
            break
        
        start += 1

# Emergency handling
def handle_emergency(emergency, schedule):
    old = schedule.copy()
    schedule.clear()

    schedule.append({
        "id": emergency.id,
        "type": emergency.surgery_type,
        "start": 9,
        "end": 9 + emergency.duration
    })

    current = 9 + emergency.duration

    for s in old:
        duration = s["end"] - s["start"]
        schedule.append({
            "id": s["id"],
            "type": s["type"],
            "start": current,
            "end": current + duration
        })
        current += duration