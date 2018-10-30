def sort(data):
    length = len(data)
    i = 1
    while i < length:
        if not data[i] >= data[i - 1]:
            del(data[i])
            length -= 1
        else:
            i += 1
    return data
