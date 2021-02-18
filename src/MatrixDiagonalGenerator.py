def createMatrix(n):
    matrix = ""
    for i in range(n):
        one = i % n
        for u in range(n):
            if u == one:
                matrix += '1  '
            else: matrix += '0  '

        matrix += "\n"
    return matrix


print(createMatrix(10))