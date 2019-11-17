def power(max):
    result = []
    for element in range(1, max+1):
        result.append(2**element)
    return result


new = power(10)
print(new)