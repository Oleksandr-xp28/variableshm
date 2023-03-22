
if __name__ == "__main__":
    try:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = 0.5 * base * height
        print(f"The area of the triangle is {area}")
    except Exception as ex:
        print(f'log: {ex}')
