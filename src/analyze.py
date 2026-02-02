def read_sensor_data(file_path):
    with open(file_path, 'r') as file:
        values = [int(line.strip()) for line in file]
    return values

def analyze_data(values):
    return {
        "min": min(values),
        "max": max(values),
        "average": sum(values) / len(values)
    }

if __name__ == "__main__":
    data = read_sensor_data("../data/sensor_data.txt")
    result = analyze_data(data)

    print("Sensor Data Analysis")
    print("Min:", result["min"])
    print("Max:", result["max"])
    print("Average:", result["average"])
