import csv


max_memory = float('-inf')
header = None
total_rows = 0  # Count total data rows
memory_counts = {
    "12-13 GB": 0,
    "13-14 GB": 0,
    "14-15 GB": 0,
    "15-16 GB": 0,
    "16+ GB": 0
}

def process_row(row):
    if row == header:
        return   # Skip repeated headers

    row = [col.strip() for col in row if col.strip()]  # Remove empty fields due to trailing commas

    if not row:
        return  # Skip empty rows

    try:
        global total_rows
        global max_memory
        global memory_counts
        memory_mb = float(row[-1])  # Convert last valid column to float (MB)
        memory_gb = memory_mb / 1024  # Convert MB to GB
        total_rows += 1  # Count valid data rows

        # Update memory usage counts
        if 12 <= memory_gb < 13:
            memory_counts["12-13 GB"] += 1
        elif 13 <= memory_gb < 14:
            memory_counts["13-14 GB"] += 1
        elif 14 <= memory_gb < 15:
            memory_counts["14-15 GB"] += 1
        elif 15 <= memory_gb < 16:
            memory_counts["15-16 GB"] += 1
        elif memory_gb >= 16:
            memory_counts["16+ GB"] += 1

        max_memory = max(max_memory, memory_gb)
        return total_rows

    except ValueError:
        # print(f"Skipping invalid row: {row}")  # Handle non-numeric values
        pass

def process():
    file_path = "file.csv"  # Replace with your actual file path
    with open(file_path, newline='', encoding="ISO-8859-1") as csvfile:
        reader = csv.reader(csvfile)

        first_row = True
        for row in reader:
            if first_row:
                header = row
                first_row = False
                continue  # Skip the first header row
            process_row(row)
    # Print results
    print(f"Total Rows: {total_rows}")
    print(f"Maximum System Memory Used: {max_memory:.2f} GB")
    for key, value in memory_counts.items():
        print(f"{key}: {value} times")


process()
