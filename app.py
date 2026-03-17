from scheduler import Surgery, add_surgery, handle_emergency
from queue import PriorityQueue

# 🔹 Time formatter
def format_time(minutes):
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours:02d}:{mins:02d}"

def main():
    pq = PriorityQueue()

    counter = 0  # unique counter

    def push(priority, surgery):
        nonlocal counter
        pq.put((priority, counter, surgery))
        counter += 1

    # Add surgeries (dataset ke exact values)
    push(1, Surgery(1, "Cardio", 10, "critical", 1))
    push(3, Surgery(2, "Ortho", 5, "normal", 3))
    push(2, Surgery(3, "Neuro", 8, "moderate", 2))
    push(4, Surgery(4, "ENT", 6, "normal", 4))
    push(2, Surgery(5, "General", 7, "moderate", 2))

    schedule = []

    # 🔹 Normal Scheduling
    while not pq.empty():
        _, _, surgery = pq.get()
        add_surgery(surgery, schedule)

    print("\n✅ Initial Schedule:")
    for s in schedule:
        print(f"Surgery ID: {s['id']}, Type: {s['type']}, Start: {format_time(s['start'])}, End: {format_time(s['end'])}")

    # 🔹 Emergency case
    emergency = Surgery(99, "Cardio", 12, "critical", 0)
    handle_emergency(emergency, schedule)

    print("\n🚨 After Emergency:")
    for s in schedule:
        print(f"Surgery ID: {s['id']}, Type: {s['type']}, Start: {format_time(s['start'])}, End: {format_time(s['end'])}")


# Run
if __name__ == "__main__":
    main()