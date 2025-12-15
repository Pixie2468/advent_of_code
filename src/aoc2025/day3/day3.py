from aoc2025.aoc2025 import AOC2025
import utils.set_paths as sp


class Day3(AOC2025.Day3):
    def __init__(self):
        super().__init__()
        self.YEAR = 2025
        self.DAY = 3

    def _read_lines(self):
        path = sp.get_input_path(year=self.YEAR, day=self.DAY)
        raw = sp.get_input(path, self.DAY)
        return [ln.strip() for ln in raw.split("\n") if ln.strip()]

    def max_number_from_bank(self, bank: str, k: int) -> int:
        stack = []
        remove = len(bank) - k

        for digit in bank:
            while stack and remove > 0 and stack[-1] < digit:
                stack.pop()
                remove -= 1
            stack.append(digit)

        return int("".join(stack[:k]))

    def part1(self):
        inp = self._read_lines()
        return sum(self.max_number_from_bank(line, 2) for line in inp)

    def part2(self):
        inp = self._read_lines()
        return sum(self.max_number_from_bank(line, 12) for line in inp)


if __name__ == "__main__":
    day3 = Day3()
    print("Part 1:", day3.part1())
    print("Part 2:", day3.part2())
