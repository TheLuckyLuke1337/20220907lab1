def distance_points(point_1: tuple, point_2: tuple) -> float:       # compute distance between points
    return ((point_1[1] - point_2[1])**2 + (point_1[0] - point_2[0])**2)**(1/2)

def main():
    print(distance_points((0, 0), (0, 1)))

if __name__ == '__main__':
    main()