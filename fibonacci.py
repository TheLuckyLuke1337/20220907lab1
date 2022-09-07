def fibonacci(n: int) -> int:
    fib_numbers = [0, 1]
    if n < 3:
        return fib_numbers[n - 1]
    for i in range(2, n):
        fib_numbers.append(fib_numbers[i - 1] + fib_numbers[i - 2])
    return fib_numbers[n - 1]

def main():
    for i in range(100):
        print(fibonacci(i + 1))

if __name__ == '__main__':
    main()