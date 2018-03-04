def find_biggest_sum_in_dict(data):
    biggest_sum = 0
    biggest_key = ''
    for key, count in data.items():
        if biggest_sum < count:
            biggest_key = key
            biggest_sum = count
    return {"name": biggest_key, "sum": biggest_sum}