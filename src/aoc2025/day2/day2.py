from aoc2025.aoc2025 import AOC2025
import utils.set_paths as sp


class Day2(AOC2025.Day2):
    def __init__(self):
        super().__init__()
        self.YEAR = 2025
        self.DAY = 2
        self.invalid_numbers = []

    def check_even(self, number: str) -> bool:
        return len(number) % 2 == 0

    @classmethod
    def sum_invalid_numbers(cls, invalid_numbers):
        return sum(invalid_numbers)

    def _read_lines(self):
        path = sp.get_input_path(year=self.YEAR, day=self.DAY)
        raw = sp.get_input(path, self.DAY)
        return [ln.strip() for ln in raw.split(",") if ln.strip()]

    # Part 1

    def check_invalid(self, start: int, end: int):
        number = str(start)

        while int(number) <= int(end):
            if not self.check_even(number):
                number = str(10 ** len(number))
                continue

            half = len(number) // 2
            left = number[:half]
            right = number[half:]

            if left == right:
                self.invalid_numbers.append(int(number))
                number = str(int(left) + 1) * 2
            elif int(left) > int(right):
                number = left * 2
            else:
                number = str(int(left) + 1) * 2

    def part1(self):
        self.invalid_numbers = []
        inp = self._read_lines()

        for line in inp:
            start, end = line.split("-")
            self.check_invalid(start=start, end=end)

        return Day2.sum_invalid_numbers(self.invalid_numbers)

    # Part 2

    @classmethod
    def check_pattern(cls, num) -> bool:
        num = str(num)
        length = len(num)

        for size in range(1, length):
            if length % size != 0:
                continue

            pattern = num[:size]
            if pattern * (length // size) == num:
                return True

        return False

    def part2(self):
        self.invalid_numbers = []
        inp = self._read_lines()

        for line in inp:
            start, end = line.split("-")

            for num in range(int(start), int(end) + 1):
                if Day2.check_pattern(num):
                    self.invalid_numbers.append(num)

        return sum(self.invalid_numbers)


if __name__ == "__main__":
    day2 = Day2()
    ans = day2.part2()

    print(ans)
