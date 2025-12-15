from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC_PATH = ROOT / "src"


def get_input_path(year: int, day: int) -> Path:
    year_path = SRC_PATH / f"aoc{year}"
    input_path = year_path / f"day{day}"
    return input_path


def get_input(input_path: Path, day: int) -> str:
    try:
        with open(f"{input_path}/day{day}.txt", "r") as f:
            file = f.read()
    except FileNotFoundError as e:
        print(e)

    return file


if __name__ == "__main__":
    path = get_input_path(2025)
    data = get_input(input_path=path, day=1)
    print(data)
