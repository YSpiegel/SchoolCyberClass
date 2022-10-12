
def sum_nums_divisible_by_5(numbers):
    number = ","
    total = 0

    for i, char in enumerate(numbers):
        if number == ",":
            number = char
            if i == len(numbers) - 1 and int(number) % 5 == 0:
                total += int(number)
        else:
            if char == "," or i == len(numbers) - 1:
                if i == len(numbers) - 1:
                    number += char
                if int(number) % 5 == 0:
                    total += int(number)
                if char == ",":
                    number = char
            else:
                number += char

    return total


nums = input("Enter Numbers: ")
print(f"The sum of the numbers that are divisible by 5 is: {sum_nums_divisible_by_5(nums)}")
