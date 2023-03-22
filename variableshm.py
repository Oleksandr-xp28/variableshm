if __name__ == "__main__":
    try:
        meters = float(input("Enter a distance in meters: "))

        centimeters = meters * 100
        decimeters = meters * 10
        millimeters = meters * 1000
        miles = meters / 1609.34

        print(f"{meters} meters is equal to:")
        print(f"{centimeters} centimeters")
        print(f"{decimeters} decimeters")
        print(f"{millimeters} millimeters")
        print(f"{miles} miles")

    except Exception as ex:
        print(f'log: {ex}')

