import utils.set_paths as sp
from aoc2025.aoc2025 import AOC2025
from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Node:
    data: Any
    prev: "Optional[Node]" = None
    next: "Optional[Node]" = None


class DoublyCircularLinkedList:
    def __init__(self, iterable=None):
        self.head: Optional[Node] = None
        self._size = 0
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def append(self, value: Any) -> None:
        new_node = Node(value)
        if self.head is None:
            new_node.next = new_node.prev = new_node
            self.head = new_node
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node
        self._size += 1

    def find(self, value: Any) -> Optional[Node]:
        if self.head is None or self._size == 0:
            return None
        cur = self.head
        for _ in range(self._size):
            if cur.data == value:
                return cur
            cur = cur.next
        return None

    def step(self, direction: int) -> int:
        if self.head is None:
            raise RuntimeError("List is empty")
        if direction > 0:
            self.head = self.head.next
        elif direction < 0:
            self.head = self.head.prev
        return self.head.data

    def move_k(self, k: int) -> int:
        if self.head is None or self._size == 0:
            raise RuntimeError("List is empty")
        if k == 0:
            return self.head.data
        steps = abs(k) % self._size
        if steps == 0:
            return self.head.data

        if k > 0:
            for _ in range(steps):
                self.head = self.head.next
        else:
            for _ in range(steps):
                self.head = self.head.prev
        return self.head.data

    def __len__(self):
        return self._size

    def __repr__(self):
        out = []
        if self.head:
            cur = self.head
            for _ in range(min(20, self._size)):
                out.append(cur.data)
                cur = cur.next
            if self._size > 20:
                out.append("...")
        return f"DCLL({out})"


class Day1(AOC2025.Day1):
    def __init__(self):
        super().__init__()
        self.YEAR = 2025
        self.DAY = 1

    def _make_base_dll(self) -> DoublyCircularLinkedList:
        dll = DoublyCircularLinkedList(range(100))
        node50 = dll.find(50)
        if node50 is None:
            raise RuntimeError("Value 50 not found in initial list")
        dll.head = node50
        return dll

    def _read_lines(self, part_letter: str) -> list[str]:
        path = sp.get_input_path(year=self.YEAR, day=self.DAY)
        raw = sp.get_input(path, self.DAY, part_letter)
        return [ln.strip() for ln in raw.splitlines() if ln.strip()]

    def part1(self) -> int:
        count_zeros = 0
        dll = self._make_base_dll()
        lines = self._read_lines("a")

        for instr in lines:
            rotation = instr[0]
            value = int(instr[1:])
            if rotation == "L":
                landing = dll.move_k(-value)
            elif rotation == "R":
                landing = dll.move_k(value)
            else:
                raise ValueError(f"Unknown rotation: {rotation}")

            if landing == 0:
                count_zeros += 1

        return count_zeros

    def part2(self) -> int:
        count_zeros = 0
        dll = self._make_base_dll()
        lines = self._read_lines("b")

        for instr in lines:
            rotation = instr[0]
            value = int(instr[1:])
            steps = abs(value)

            if rotation == "L":
                for _ in range(steps):
                    pos = dll.step(-1)
                    if pos == 0:
                        count_zeros += 1
            elif rotation == "R":
                for _ in range(steps):
                    pos = dll.step(1)
                    if pos == 0:
                        count_zeros += 1
            else:
                raise ValueError(f"Unknown rotation: {rotation}")

        return count_zeros


if __name__ == "__main__":
    day1 = Day1()
    print("part1 (landings only):", day1.part1())

    day1 = Day1()
    print("part2 (count every pass):", day1.part2())
