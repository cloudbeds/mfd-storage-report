from glob import glob


def convert_to_python_path(string: str) -> str:
    return string.replace("/", ".").replace("\\", ".").replace(".py", "")


pytest_plugins = [
    convert_to_python_path(fixture)
    for fixture in glob("tests/unit/fixtures/**/*.py", recursive=True)
]
