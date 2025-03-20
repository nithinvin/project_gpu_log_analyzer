import csv


total_rows = 0  # Count total data rows
cpu_temperature_counts = {
    "50-59 deg c": 0,
    "60-69 deg c": 0,
    "70-79 deg c": 0,
    "80-89 deg c": 0,
    "90-99 deg c": 0,
    "100+ deg c": 0,
    "max_temp": float('-inf')
}
gpu_temperature_counts = {
    "50-59 deg c": 0,
    "60-69 deg c": 0,
    "70-79 deg c": 0,
    "80-89 deg c": 0,
    "90-99 deg c": 0,
    "100+ deg c": 0,
    "max_temp": float('-inf')
}

def process_temperature_field(row, field, counts_dict):
    try:
        global total_rows
        temperature = float(row[field])  # Can use row[3] for GPU temperature
        total_rows += 1  # Count valid data rows

        # Update memory usage counts
        if 50 <= temperature < 59.9:
            counts_dict["50-59 deg c"] += 1
        elif 60 <= temperature < 69.9:
            counts_dict["60-69 deg c"] += 1
        elif 70 <= temperature < 79.9:
            counts_dict["70-79 deg c"] += 1
        elif 80 <= temperature < 89.9:
            counts_dict["80-89 deg c"] += 1
        elif 90 <= temperature < 99.9:
            counts_dict["90-99 deg c"] += 1
        elif temperature >= 100:
            counts_dict["100+ deg c"] += 1

        counts_dict['max_temp'] = max(counts_dict['max_temp'], temperature)

    except ValueError:
        #print(f"Skipping invalid row: {row}")  # Handle non-numeric values
        pass

def process_cpu_temperature_field(row):
    process_temperature_field(row, -2, cpu_temperature_counts)

def process_gpu_temperature_field(row):
    process_temperature_field(row, 3, gpu_temperature_counts)

def print_temperature_stats():
    # Print results
    max_cpu_temp = cpu_temperature_counts['max_temp']
    print(f"Maximum CPU Temperature: {max_cpu_temp:.2f} degree Celsius")
    print(f"Total Rows: {total_rows/2}")
    for key, value in cpu_temperature_counts.items():
        if key != 'max_temp':
            print(f"\t{key}: {value} times")
    max_gpu_temp = gpu_temperature_counts['max_temp']
    print(f"Maximum GPU Temperature: {max_gpu_temp:.2f} degree Celsius")
    for key, value in gpu_temperature_counts.items():
        if key != 'max_temp':
            print(f"\t{key}: {value} times")

