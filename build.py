import pathlib, json

ROOT = "setups"
COPY = ("name", "description", "group")
OUTFILE = "overview.json"

def get_files(path: pathlib.Path) -> list[pathlib.Path]:
    if isinstance(path, str):
        path = pathlib.Path(path)
    
    return list(path.rglob("*.json"))


def main():
    files = get_files(ROOT)

    overview = list()

    for file in files:
        data = json.loads(file.read_text())
        entry = dict()
        entry["path"] = str(pathlib.Path(*file.parts[1:]))

        for key in COPY:
            entry[key] = data[key]
        overview.append(entry)

    out = pathlib.Path(ROOT).joinpath(pathlib.Path(OUTFILE))
    out.touch()

    json.dump(overview, out.open("w"))

if __name__ == "__main__":
    main()