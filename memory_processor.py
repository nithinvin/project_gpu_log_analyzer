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

def process_memory_field(row):
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

    except ValueError:
        # print(f"Skipping invalid row: {row}")  # Handle non-numeric values
        pass

def print_memory_stats():
    # Print results
    print(f"Maximum System Memory Used: {max_memory:.2f} GB")
    print(f"Total Rows: {total_rows}")
    for key, value in memory_counts.items():
        print(f"\t{key}: {value} times")
