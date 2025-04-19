def oddnumber_series(a: int):
    odd_series = []
    for i in range(a):
        odd_series.append(2 * i + 1)
    return odd_series

a = int(input("Enter value for a: "))
result = oddnumber_series(a)
print("Output:", ", ".join(map(str, result)))
