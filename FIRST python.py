import array

# Integers: Generate some visitor check-in counts
visitor_counts = [12, 7, 15, 9, 10, 13]

# Compute total, average, min, max
total_visitors = sum(visitor_counts)
avg_visitors = total_visitors / len(visitor_counts)
min_visitors = min(visitor_counts)
max_visitors = max(visitor_counts)

# Strings: Formatted string report with f-strings
report = (
    f"Visitor Check-in Report\n"
    f"------------------------\n"
    f"Total Visitors: {total_visitors}\n"
    f"Average Visitors per Session: {avg_visitors:.2f}\n"
    f"Minimum Visitors in a Session: {min_visitors}\n"
    f"Maximum Visitors in a Session: {max_visitors}\n"
    f"Summary: We had {total_visitors} visitors over {len(visitor_counts)} sessions, with an average of {avg_visitors:.2f} per session."
)
print(report)

# Booleans: Threshold condition and compound condition
threshold = 11
status = "Above Standard" if avg_visitors > threshold and max_visitors > threshold else "Below Standard"
print(f"Status: {status}")

# Lists: Maintain and modify visitor names
visitor_names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
print(f"Original visitor names: {visitor_names}")

# Add a new element
visitor_names.append("Frank")
# Remove one based on a condition (remove first name starting with 'C')
visitor_names = [name for name in visitor_names if not name.startswith("C")]
print(f"Visitor names after addition and removal: {visitor_names}")

# Sort and display
visitor_names.sort()
print(f"Sorted visitor names: {visitor_names}")

# Arrays: Store a fixed-size numeric subset
subset_array = array.array('i', visitor_counts[:4])
array_sum = sum(subset_array)
list_sum = sum(visitor_counts[:4])
print(f"Sum of array subset: {array_sum}")
print(f"Sum of list subset: {list_sum}")
print(f"Array sum matches list sum? {array_sum == list_sum}")

# Dictionaries: List of visitor records
visitor_records = [
    {"id": 1, "name": "Alice", "value": 12},
    {"id": 2, "name": "Bob", "value": 7},
    {"id": 3, "name": "Charlie", "value": 15},
    {"id": 4, "name": "Diana", "value": 9}
]

# Update one record (change Bob's 'value')
for record in visitor_records:
    if record["name"] == "Bob":
        record["value"] = 10

# Delete another record (remove Charlie)
visitor_records = [rec for rec in visitor_records if rec["name"] != "Charlie"]

# Compute total of 'value' fields
total_record_value = sum(rec["value"] for rec in visitor_records)
print(f"Updated visitor records: {visitor_records}")
print(f"Total 'value' in all records: {total_record_value}")
