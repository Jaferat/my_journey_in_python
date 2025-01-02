#Weight Unit Converter

while True:
    weight_unit = input("Select weight unit (K/P): ")
    weight = input("Enter your weight in the unit selected: ")

    if weight_unit == "K":
        try:
            float_weight = float(weight)
            float_weight *= 2.205
            print(f"Your weight is {round(float_weight, 2)} pounds")
            break
        except ValueError:
            print(f"The weight {weight} is not valid (make sure to use numbers)")

    elif weight_unit == "P":
        try:
            float_weight = float(weight)
            float_weight /= 2.205
            print(f"Your weight is {round(float_weight, 2)} kilograms")
            break
        except ValueError:
            print(f"The weight {weight} is not valid (make sure to use numbers)")
    else:
        print(f"{weight_unit} is not a valid unit")