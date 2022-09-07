from math import pi, sin

def ladder_length(height: float, angle: float) -> float:
    angle = angle * pi / 180
    length = height / sin(angle)
    return length

def main():

    print(ladder_length(5, 70))

if __name__ == '__main__':
    main()