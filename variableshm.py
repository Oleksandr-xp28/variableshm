try:
    number = int(input("Enter a four-digit number: "))
    thousands = number // 1000
    hundreds = (number // 100) % 10
    tens = (number // 10) % 10
    ones = number % 10

    flipped_number = ones * 1000 + tens * 100 + hundreds * 10 + thousands

    print(f"The flipped number is {flipped_number}")
    pass
except :
    pass

