from abc import ABC, abstractmethod


class AOC2025:
    class Day1(ABC):
        @abstractmethod
        def part1(self) -> int:
            pass

        @abstractmethod
        def part2(self):
            pass

    class Day2(ABC):
        @abstractmethod
        def part1(self) -> int:
            pass

        @abstractmethod
        def part2(self) -> int:
            pass
