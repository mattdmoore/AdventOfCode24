from typing import Iterable, List, Self


class Coordinate:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __iter__(self) -> Iterable[int]:
        yield (i for i in (self.x, self.y))

    def __add__(self, other: Self) -> Self:
        return Coordinate(self.x + other.x, self.y + other.y)

    def __eq__(self, other: Self) -> bool:
        return self.x == other.x and self.y == other.y

class Guard(Coordinate):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)

class GuardMap:
    def __init__(
        self, grid: List[List[str]], start_point: Coordinate | None = None, d: int = 0
    ) -> None:
        self.grid = grid
        self.size = (len(grid), len(grid[0]))
        self.start_point = start_point or self._find_start()
        self.guard = Guard(*self.start_point)
        self.directions = [Coordinate(*xy) for xy in ((-1, 0), (0, 1), (1, 0), (0, -1))]
        self._d = d

    def __getitem__(self, key: Coordinate) -> str:
        return self.grid[key.x][key.y]

    def __setitem__(self, key: Coordinate, val: str) -> None:
        self.grid[key.x][key.y] = val

    def __contains__(self, coordinate: Coordinate) -> bool:
        m, n = self.size
        return 0 <= coordinate.x <= m and 0 <= coordinate.y <= n

    def turn(self) -> None:
        self._d = (self._d + 1) % 4

    def direction(self):

    def next_tile(self) -> str:
        return self[self.guard + directions[self.d]]

    def _find_start(self) -> Coordinate:
        for i, row in enumerate(self.grid):
            for j, tile in enumerate(row):
                if tile == "^":
                    return Coordinate(i, j)
        raise ValueError("Start point not found.")

    def move_guard(self) -> Coordinate:
        if self.next_tile() == "#":
        return self.guard + direction


def simulate_path(
    guard_map: GuardMap, d: int = 0
) -> tuple[set[Coordinate], set[Coordinate]]:
    visited = set()
    obstacles = set()
    position = guard_map.start_point
    while position in guard_map:
        visited.add(guard_map.guard)
        position = guard_map.move_guard()
        if obstacle := simulate_obstacle(guard_map):
            obstacles.add(obstacle)
    return visited, obstacles


def simulate_obstacle(guard_map: GuardMap) -> Coordinate | None:
    simulated_guard_map = guard_map
    simulated_guard_map[next_position] = "#"
    while position in simulated_guard_map:
        position, d = simulated_guard_map.move_guard(position, d)
        if position == start_point:
            return position + directions[d]
    return None


with open("input.txt") as file:
    guard_map = GuardMap([[row for row in line.strip()] for line in file])

visited, obstacles = simulate_path(guard_map)

print(len(visited))
print(len(obstacles))

with open("output.txt", "w") as file:
    file.write("\n".join(["".join(i) for i in guard_map.grid]))
