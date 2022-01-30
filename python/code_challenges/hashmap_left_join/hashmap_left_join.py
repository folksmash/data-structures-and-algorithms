def left_join(data1, data2):
    output = []
    for key in data1:
        joined = [
            key,
            data1.get(key),
            data2.get(key)
        ]
        output.append(joined)
    return output
