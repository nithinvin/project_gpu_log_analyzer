import csv

file_path = "file.csv"  # Replace with your actual file path

max_board_power = float('-inf')
first_row = True
header = None
total_rows = 0  # Count total data rows
board_power_counts = {
    "0-50 W": 0,
    "51-100 W": 0,
    "101-150 W": 0,
    "151-200 W": 0,
    "201-300 W": 0,
    "301-400 W": 0,
    "400+ W": 0
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
            board_power = float(row[14])
            total_rows += 1  # Count valid data rows

            # Update memory usage counts
            if 0 <= board_power < 50:
                board_power_counts["0-50 W"] += 1
            elif 51 <= board_power < 100:
                board_power_counts["51-100 W"] += 1
            elif 101 <= board_power < 150:
                board_power_counts["101-150 W"] += 1
            elif 151 <= board_power < 200:
                board_power_counts["151-200 W"] += 1
            elif 201 <= board_power < 300:
                board_power_counts["201-300 W"] += 1
            elif 301 <= board_power < 400:
                board_power_counts["301-400 W"] += 1
            elif board_power >= 400:
                board_power_counts["400+ W"] += 1

            max_board_power = max(max_board_power, board_power)

        except ValueError:
            # print(f"Skipping invalid row: {row}")  # Handle non-numeric values
            pass

# Print results
print(f"Total Rows: {total_rows}")
print(f"Maximum board_power: {max_board_power:.2f} Watts")
for key, value in board_power_counts.items():
    print(f"{key}: {value} times")

