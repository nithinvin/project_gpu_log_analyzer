import csv

file_path = "file.csv"  # Replace with your actual file path

max_temperature = float('-inf')
first_row = True
header = None
total_rows = 0  # Count total data rows
temperature_counts = {
    "50-59 deg c": 0,
    "60-69 deg c": 0,
    "70-79 deg c": 0,
    "80-89 deg c": 0,
    "90-99 deg c": 0,
    "100+ deg c": 0
}

with open(file_path, newline='', encoding="ISO-8859-1") as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        if first_row:
            header = row
            first_row = False
            continue  # Skip the first header row

        if row == header:  
            continue  # Skip repeated headers

        row = [col.strip() for col in row if col.strip()]  # Remove empty fields due to trailing commas

        if not row:
            continue  # Skip empty rows

        try:
            temperature = float(row[-2])  # Can use row[3] for GPU temperature
            total_rows += 1  # Count valid data rows

            # Update memory usage counts
            if 50 <= temperature < 59.9:
                temperature_counts["50-59 deg c"] += 1
            elif 60 <= temperature < 69.9:
                temperature_counts["60-69 deg c"] += 1
            elif 70 <= temperature < 79.9:
                temperature_counts["70-79 deg c"] += 1
            elif 80 <= temperature < 89.9:
                temperature_counts["80-89 deg c"] += 1
            elif 90 <= temperature < 99.9:
                temperature_counts["90-99 deg c"] += 1
            elif temperature >= 100:
                temperature_counts["100+ deg c"] += 1

            max_temperature = max(max_temperature, temperature)

        except ValueError:
            print(f"Skipping invalid row: {row}")  # Handle non-numeric values

# Print results
print(f"Total Rows: {total_rows}")
print(f"Maximum CPU Temperature: {max_temperature:.2f} degree Celcius")
for key, value in temperature_counts.items():
    print(f"{key}: {value} times")

