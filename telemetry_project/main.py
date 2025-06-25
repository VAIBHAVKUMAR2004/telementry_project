import json
from datetime import datetime, timezone

# IMPLEMENT: function to convert data-1.json entries to unified format
def transform_data1(entry):
    return {
        "timestamp": entry["timestamp"],
        "sensor": entry["sensor"],
        "value": entry["value"]
    }

# IMPLEMENT: function to convert data-2.json entries to unified format
def transform_data2(entry):
    dt = datetime.fromisoformat(entry["time"].replace("Z", "+00:00"))
    timestamp_ms = int(dt.timestamp() * 1000)
    return {
        "timestamp": timestamp_ms,
        "sensor": entry["type"],
        "value": entry["reading"]
    }

def main():
    with open('data-1.json') as f1, open('data-2.json') as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

    result1 = [transform_data1(entry) for entry in data1]
    result2 = [transform_data2(entry) for entry in data2]
    final_result = result1 + result2
    final_result.sort(key=lambda x: x["timestamp"])

    with open('output.json', 'w') as fout:
        json.dump(final_result, fout, indent=2)

    print(json.dumps(final_result, indent=2))

if __name__ == '__main__':
    main()