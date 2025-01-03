while True:
    unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
    if unit == "C":
        try:
            temp = float(input("Enter the temperature: "))
            temp = round((9 * temp) / 5 + 32, 1)
            print(f"The temperature is {temp}ºF")
            break
        except ValueError:
            print(f"The temperature you entered is invalid (enter numbers only)")
            continue
    elif unit == "F":
        try:
            temp = float(input("Enter the temperature: "))
            temp = round((temp - 32) * 5 / 9, 1)
            print(f"The temperature is {temp}ºC")
            break
        except ValueError:
            print(f"The temperature you entered is invalid (enter numbers only)")
            continue
    else:
        print(f"{unit} is an invalid measurement unit")
