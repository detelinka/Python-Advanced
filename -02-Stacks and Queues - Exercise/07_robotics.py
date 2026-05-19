from collections import deque

def parse_time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(":"))
    return hours * 3600 + minutes * 60 + seconds

def format_time_from_seconds(total_seconds):
    total_seconds %= 24 * 3600
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

robots_input = input().split(";")
robots = []
for r in robots_input:
    name, time_str = r.split("-")
    robots.append({
        "name": name,
        "process_time": int(time_str),
        "busy_until": 0
    })

start_time_str = input()
current_time = parse_time_to_seconds(start_time_str)

products = deque()
while True:
    line = input()
    if line == "End":
        break
    products.append(line)

while products:
    current_time += 1
    product = products.popleft()

    assigned = False
    for robot in robots:
        if current_time >= robot["busy_until"]:
            robot["busy_until"] = current_time + robot["process_time"]
            time_str = format_time_from_seconds(current_time)
            print(f"{robot['name']} - {product} [{time_str}]")
            assigned = True
            break

    if not assigned:
        products.append(product)