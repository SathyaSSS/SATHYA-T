def oddnumber_series(a: int):
    if a % 2 == 0:
        a -= 1
    series = [2 * i + 1 for i in range(a)]
    return series

a = int(input("Enter value for a: "))
result = oddnumber_series(a)
print("Output:", ", ".join(map(str, result)))
