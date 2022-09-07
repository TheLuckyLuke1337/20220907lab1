def line_slope(point_1: tuple, point_2: tuple) -> float:
    return (point_1[1] - point_2[1]) / (point_1[0] - point_2[0])

def main():
    print(line_slope((0, 0),(2, 1)))

if __name__ == '__main__':
    main()