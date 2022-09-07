def triangle_area(a: float, b: float, c: float) -> float: # herons formula
    s = (a + b + c) / 2
    A_2 = s * (s - a) * (s - b) * (s - c)
    A = A_2**(1/2)
    return A

def main():
    print(triangle_area(3, 4, 5))

if __name__ == '__main__':
    main()