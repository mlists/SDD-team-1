def get_digit(number: float, n: int) -> int:
    """Return the digit at index n."""
    return int(number // 10 ** n % 10)

def combine(iterable: iter) -> str:
    """Combine each element of an iterable into a single string."""
    combined = ""
    for i in range(len(iterable)):
        combined += str(iterable[i])
    return combined

numbers = []
lengths = []
answer = []
carry_digit = 0

while True:
    next_number = input("Enter a number to add: ")
    if next_number == "":
        break
    else:
        numbers.append(float(next_number))
        lengths.append(len(next_number))

column = 0
while column < max(lengths) or carry_digit != 0:
    # carry digit check allows new columns to be added
    column_answer = 0
    for number in numbers:
        column_answer += get_digit(number, column)
    column_answer += carry_digit
    if column_answer > 9:
        carry_digit = column_answer // 10
        column_answer -= carry_digit * 10
    else:
        carry_digit = 0
    answer.append(column_answer)
    column += 1
answer.reverse()
# since we add units first, reverse to make readable
print(combine(answer))
