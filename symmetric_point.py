def compute_symmetric_point():
    coordinates = []
    for _ in range(int(input())):
        coordinates.append(list(map(int,input().split())))

    for coordinate in coordinates:
        print("{0} {1}".format(2*coordinate[2]-coordinate[0],2*coordinate[3]-coordinate[1]))

if __name__ == "__main__":
    compute_symmetric_point()

