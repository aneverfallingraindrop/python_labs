import argparse
import sys
import os
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)
from src.lab05.json_csv import *
from src.lab05.csv_xlxs import *

def main():
    parser = argparse.ArgumentParser(description="data converters")
    sub = parser.add_subparsers(dest="cmd")

    jscsv = sub.add_parser("json_csv", help="convert .json to .csv")
    jscsv.add_argument("--input", dest="input", required=True, help="json file link")
    jscsv.add_argument("--output", dest="output", required=True, help="csv file link")

    csvjs = sub.add_parser("csv_json", help="convert .csv to .json")
    csvjs.add_argument("--input", dest="input", required=True, help="csv file link")
    csvjs.add_argument("--output", dest="output", required=True, help="json file link")

    csvxl = sub.add_parser("csv_xlsx", help="convert .csv to .xlsx")
    csvxl.add_argument("--input", dest="input", required=True, help="csv file link")
    csvxl.add_argument("--output", dest="output", required=True, help="xlsx file link")

    args = parser.parse_args()

    if args.cmd == "json_csv":
        answer = json_to_csv(args.input, args.output)

    elif args.cmd == "csv_json":
        answer = csv_to_json(args.input, args.output) 

    elif args.cmd == "csv_xlsx":
        answer = csv_to_xlsx(args.input, args.output)

d = main()

# CMD EXAMPLES
# python src/lab06/cli_convert.py json_csv --input ././data/lab06/samples/jsonPeople.json --output ././data/lab06/out/jsonPeople.csv
# python src/lab06/cli_convert.py csv_json --input ././data/samples/csvPeople.csv --output ././data/lab06/out/csvPeople.json
# python src/lab06/cli_convert.py csv_xlsx --input ././data/samples/csvPeople.csv --output ././data/lab06/out/csvPeople.xlsx