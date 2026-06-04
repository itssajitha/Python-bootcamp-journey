def create_dict(keys, values):
    return dict(zip(keys, values))
keys = ["name", "age", "city"]
values = ["Ali", "20", "calicut"]
result = create_dict(keys, values)
print(result)