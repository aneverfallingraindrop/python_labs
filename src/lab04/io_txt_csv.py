import csv
from pathlib import Path, PosixPath, WindowsPath
from typing import Iterable, Sequence
def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    if type(path) not in [str, PosixPath, WindowsPath]:
        raise TypeError
    if not encoding == "utf-8":
        raise UnicodeDecodeError
    if not Path(path).exists():
        raise FileNotFoundError 
    return Path(path).read_text(encoding) 

def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    path += '.csv'
    if (not rows):
        file = Path(path).open("w", newline="", encoding="utf-8")
        if header == None:
            csv.writer(file).writerow(header)
            file.close()
    else:
        with open(path, mode='w', newline='', encoding='utf-8') as file:
            for j in range(len(rows) - 1):
                if len(rows[j]) != len(rows[j+1]):
                    raise ValueError
            write = csv.writer(file)
            if header is not None:
                write.writerow(header)
            for r in rows: 
                write.writerow(r)

