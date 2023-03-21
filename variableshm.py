
if __name__ == "__main__":
    try:
        first_num = input("Enter the first digit: ")
        second_num = input("Enter the second digit: ")
        third_num = input("Enter the third digit: ")
        number = int(first_num + second_num + third_num)
        print(f'{number}')
    except Exception as ex:
        print(f'log: {ex}')
