from pathlib import Path
import json
import csv

def json_to_csv(json_path: str, csv_path: str) -> None:
    from pathlib import Path
    import json
    import csv
    if not Path(json_path).exists(): raise FileNotFoundError
    if not(json_path[-5:] == ".json" and csv_path[-4:] == ".csv"): raise ValueError

    file = open(json_path, "r", encoding="utf-8")
    strng = file.read()
    file.close()
    if len(strng) == 0:
        raise ValueError 
    with open(json_path, "r", encoding="utf-8") as filejson:
        data = json.load(filejson)
    with open(csv_path, "w", newline='', encoding="utf-8") as filecsv:
        writer = csv.DictWriter(filecsv, fieldnames=data[0].keys(), extrasaction="raise")
        writer.writeheader()
        writer.writerows(data)

# a = json_to_csv("././data/lab05/samples/jsonPeople.json", "././data/lab05/out/jsonPeople.csv")

# data = [{"name": "Alice", "age": 22}, {"name": "Bob", "age": 25}]
# path = Path("././data/lab05/out/jsonPeople.json")
# with open(path, "w", encoding="utf-8") as fj:
#     json.dump(data, fj,  ensure_ascii=False, indent=2)


def csv_to_json(csv_path: str, json_path: str) -> None:
    from pathlib import Path
    import json
    import csv
    if not Path(csv_path).exists(): raise FileNotFoundError 
    if not (json_path[-5:] == ".json" and csv_path[-4:]) == ".csv": raise ValueError
    file = open(csv_path, "r", encoding="utf-8")
    strng = file.read()
    file.close()
    if len(strng) == 0:
        raise ValueError 
    with open(csv_path, "r", encoding="utf-8") as filecsv:
        data = []
        for row in csv.DictReader(filecsv):
            data.append(row)
    with open(json_path, "w", newline='', encoding="utf-8") as filejson:
        json.dump(data, filejson, ensure_ascii=False, indent=2) #список словарей, только ASCII символы, отступ уровня важности 2
a = csv_to_json("././data/lab05/samples/csvPeople.csv", "././data/lab05/out/csvPeople.json")