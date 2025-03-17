import csv
from memory_processor import process_memory_field, print_memory_stats

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
            process_memory_field(row)
            # process_cpu_temperature_field(row)
            # process_gpu_temperature_field(row)
            # process_board_power_field(row)
    print_memory_stats()
    # print_cpu_temperature_stats()
    # print_gpu_temperature_stats()
    # print_board_power_stats()

process()
