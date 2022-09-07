def compute_pi(n: int) -> float:
    result = 0
    for i in range(n):
        term = 4 / (i * 2 + 1)
        if i % 2 == 0:
            result += term
        else:
            result -= term
    return result

def main():
    print(compute_pi(1000))

if __name__ == '__main__':
    main()