# числовые значения
def chislo_no_znach(numbers):
    total = 0
    for num in numbers:
        total += num ** 2
    return total
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))

# строковые значения
def is_stroka(string):
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return  False
        left += 1
        right -= 1
    return True

