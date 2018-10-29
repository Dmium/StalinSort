def sort(data):
    length = len(data)
    i = 1
    while i < length:
        print(data[i], data[i-1])
        if not data[i] >= data[i - 1]:
            del(data[i])
            i -= 1
            length -= 1
        i += 1
    return data
