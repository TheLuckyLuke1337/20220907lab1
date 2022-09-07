from math import factorial

def compute_pi(n: int) -> float: # Ramanujan–Sato series
    terms = 0
    for k in range(n):
        term = factorial(4 * k) * (1103 + 26390 * k)
        term /= factorial(k) ** 4 * 396 ** (4 * k)
        terms += term
    inverse_pi = 8 ** (1/2) * terms / 9801
    return 1 / inverse_pi

def main():
    for i in range(1, 11):
        print(compute_pi(i))

if __name__ == '__main__':
    main()