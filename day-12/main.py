import heapq
import math

with open("input.txt") as file:
    lines = file.read().splitlines()
    grid = [list(x) for x in lines]
    max_y = len(grid)
    max_x = len(grid[0])

    for y in range(max_y):
        for x in range(max_x):
            char = grid[y][x]
            if char == "S":
                start = (y, x)
            if char == "E":
                end = (y, x)


    def get_height(char: str) -> int:
        if char == "S":
            return 0
        if char == "E":
            return ord('z') - ord('a')
        return ord(char) - ord('a')


    # Valid neighbors are those at most 1 above the current height
    def get_neighbors(point: tuple[int, int]):
        y, x = point
        cur_height = get_height(grid[y][x])

        # Calculate the differentials
        for dy, dx in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            neighbor_y = y + dy
            neighbor_x = x + dx

            if not (0 <= neighbor_y < max_y and 0 <= neighbor_x < max_x):
                continue

            neighbor_height = get_height(grid[neighbor_y][neighbor_x])

            if neighbor_height <= cur_height + 1:
                yield neighbor_y, neighbor_x


    # Get the fewest number of steps from origin to destination using Dijkstra's algorithm
    def get_steps(origin: tuple[int, int], destination: tuple[int, int]):
        visited: set[tuple[int, int]] = set()
        distances = [(0, origin)]

        while True:
            if not distances:
                return math.inf

            distance_to_point, current_point = heapq.heappop(distances)
            if current_point == destination:
                return distance_to_point

            if current_point in visited:
                continue
            visited.add(current_point)

            for neighbor in get_neighbors(current_point):
                heapq.heappush(distances, (distance_to_point + 1, neighbor))


    part1 = get_steps(start, end)
    print(part1)

    fewest = part1

    candidates = []
    for y in range(max_y):
        for x in range(max_x):
            char = grid[y][x]
            if char == "a":
                candidates.append((y, x))

    for candidate in candidates:
        steps = get_steps(candidate, end)
        fewest = min(fewest, steps)

    print(fewest)
