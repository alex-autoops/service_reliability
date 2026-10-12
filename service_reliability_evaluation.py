import json

with open("incidents.json") as file:
    data = json.load(file)

observation = data["observation_minutes"]
incidents = data["incidents"]

downtime = sum(
    i["restored_minute"] - i["failure_minute"]
    for i in incidents
)

failures = len(incidents)
operating_time = observation - downtime

availability = (operating_time / observation) * 100
mttr = downtime / failures
mtbf = operating_time / failures

print(f"Total Downtime = {downtime} minutes")
print(f"Operating Time = {operating_time} minutes")
print(f"Availability = {availability:.2f}%")
print(f"MTTR = {mttr:.2f} minutes")
print(f"MTBF = {mtbf:.2f} minutes")
