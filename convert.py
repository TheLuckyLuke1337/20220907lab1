#convert.py
# convert Celsius temperature to Fahrenheit and vice versa.

def convert_celsius(celsius: float) -> float:
    fahrenheit = 9 / 5 * celsius + 32
    return fahrenheit

def convert_farenheit(farenheit: float) -> float:
    celsius = (farenheit - 32) * 5 / 9
    return celsius

def convert_km(km: float) -> float:
    return km * 0.62

def convert_miles(miles: float) -> float:
    return miles/0.62

def main():
    print("C    |   F")
    for celsius in range (0, 101, 10):
        farenheit = convert_celsius(celsius)
        print(f"{celsius:<4} |   {farenheit}")
    print()

    print("F    |   C")
    for farenheit in range (0, 101, 10):
        celsius = convert_farenheit(farenheit)
        print(f"{farenheit:<4} |   {celsius}")

if __name__ == '__main__':
    main()
