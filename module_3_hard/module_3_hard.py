def calculate_structure_sum(data_structure):
    total_sum = 0
    for item in data_structure:
        if isinstance(item, list):
            total_sum += calculate_structure_sum(item)
        elif isinstance(item, dict):
            total_sum += calculate_structure_sum(list(item.values()))
            total_sum += calculate_structure_sum(list(item.keys()))
        elif isinstance(item, tuple):
            total_sum += calculate_structure_sum(list(item))
        elif isinstance(item, str):
            total_sum += len(item)
        elif isinstance(item, set):
            total_sum += calculate_structure_sum(list(item))
        else:
            total_sum += item
    return total_sum


data_structure = [
    [1, 2, 3],
    {"a": 4, "b": 5},
    (6, {"cube": 7, "drum": 8}),
    "Hello",
    ((), [{(2, "Urban", ("Urban2", 35))}]),
]

result = calculate_structure_sum(data_structure)
print(result)