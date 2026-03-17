from flask import Flask, request, jsonify
from scheduler import Surgery, add_surgery
from queue import PriorityQueue

app = Flask(__name__)

@app.route("/schedule", methods=["POST"])
def schedule_surgeries():
    data = request.json
    
    pq = PriorityQueue()
    counter = 0

    for s in data["surgeries"]:
        pq.put((s["priority"], counter,
                Surgery(s["id"], s["type"], s["experience"], s["condition"], s["priority"])))
        counter += 1

    schedule = []

    while not pq.empty():
        _, _, surgery = pq.get()
        add_surgery(surgery, schedule)

    return jsonify(schedule)

if __name__ == "__main__":
    app.run(debug=True)