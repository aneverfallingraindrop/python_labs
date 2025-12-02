import pytest  # type: ignore
import sys
import os

sys.path.insert(
    0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)
from src.lab05.json_csv import json_to_csv, csv_to_json


# json_csv test
@pytest.mark.parametrize(
    "path_in, path_out, expected",
    [
        (
            "././data/tests/samples/people.json",
            "././data/tests/out/people07.csv",
            None,
        ),
        (
            "././data/tests/samples/empty07.json",
            "././data/tests/out/empty07.csv",
            ValueError,
        ),  # empty file
        (
            "././data/tests/samples/no_file07.json",
            "././data/tests/out/no_file07.csv",
            FileNotFoundError,
        ),  # no file
    ],
)
def test_json_to_csv_basic(path_in, path_out, expected):
    if expected is None:  # if expected behavior is correct
        assert json_to_csv(path_in, path_out) == expected
    else:
        with pytest.raises(expected):
            json_to_csv(path_in, path_out)


# csv_json test
@pytest.mark.parametrize(
    "path_in, path_out, expected",
    [
        (
            "././data/tests/samples/people.csv",
            "././data/tests/out/people07.json",
            None,
        ),
        (
            "././data/tests/samples/empty07.csv",
            "././data/tests/out/empty07.json",
            ValueError,
        ),  # empty file
        (
            "././data/tests/samples/no_file07.csv",
            "././data/tests/out/no_file07.json",
            FileNotFoundError,
        ),  # no file
    ],
)
def test_csv_to_json_basic(path_in, path_out, expected):
    if expected is None:  # if expected behavior is correct
        assert csv_to_json(path_in, path_out) == expected
    else:
        with pytest.raises(expected):
            csv_to_json(path_in, path_out)


import json
import csv
from pathlib import Path


def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())


def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    initorder = data[0].keys()
    with src.open("w", encoding="utf-8") as filecsv:
        writer = csv.DictWriter(filecsv, fieldnames=initorder, extrasaction="raise")
        writer.writeheader()
        writer.writerows(data)
    with src.open("r", encoding="utf-8") as filecsv:
        reader = csv.DictReader(filecsv)
        data = []
        for row in reader:
            data.append(row)
    with dst.open("w", newline="", encoding="utf-8") as filejson:
        json.dump(data, filejson, ensure_ascii=False, indent=2)

    assert len(data) == 2
    assert {"name", "age"} <= set(data[0].keys())
