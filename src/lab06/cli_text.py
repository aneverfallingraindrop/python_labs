import argparse


def main():
    parser = argparse.ArgumentParser(description="lab06 CLI utils")  # --help
    subparsers = parser.add_subparsers(
        dest="command", help="Available CMDs"
    )  # subparsers
    # cat subcommand
    cat_parser = subparsers.add_parser("cat", help="print file content")  # cat
    cat_parser.add_argument(
        "--input", required=True, help="input CSV file link"
    )  # --input
    cat_parser.add_argument("-n", action="store_true", help="enumerate strings")  # -n
    # stats subcommand
    stats_parser = subparsers.add_parser("stats", help="word stats")  # stats
    stats_parser.add_argument("--input", required=True, help="txt file link")  # --input
    stats_parser.add_argument("--top", type=int, default=5, help="set top")  # -top

    args = parser.parse_args()  # get attribute and write into args

    if args.command == "cat":
        csv_path = args.input
        from pathlib import Path
        import csv

        if not Path(csv_path).exists():
            raise ValueError
        if not csv_path[-4:] == ".csv":
            raise FileNotFoundError

        file = open(csv_path, "r", encoding="utf-8")
        strng = file.read()
        file.close()
        if len(strng) == 0:
            raise ValueError

        with open(csv_path, "r", encoding="utf-8") as filecsv:
            reader = csv.DictReader(filecsv)
            counts = 1
            if args.n == True:  # if enumerate
                for row in reader:
                    print(f"{counts} {row}")
                    counts += 1
            else:  # Если не нумируем строки
                for row in reader:
                    print(row)

    elif args.command == "stats":  # if stats cmd
        txt_path = args.input
        from pathlib import Path
        import sys
        import os

        project_root = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        )
        sys.path.insert(0, project_root)
        import src.libs.text as text  # normalize, tokenize, count_freq, top_n

        if not Path(txt_path).exists():
            raise FileNotFoundError
        if not txt_path[-4:] == ".txt":
            raise ValueError
        file = open(txt_path, "r", encoding="utf-8")
        strng = file.read()
        file.close()
        if len(strng) == 0:
            raise ValueError
        with open(txt_path, "r", encoding="utf-8") as filetxt:
            strngs = filetxt.read()
            strngs = str(strngs)
            print(strngs)
            top_n = args.top
            ans = text.normalize(strngs, casefold=True, yo2e=True)
            ans = text.tokenize(ans)
            ans = text.count_freq(ans)
            ans = text.top_n(ans, top_n)
            for x, y in ans:
                print(f"{x}: {y}")


b = main()

# python src/lab06/cli_text.py --help
# python src/lab06/cli_text.py cat --help
# python src/lab06/cli_text.py cat --input ././data//lab06/samples/csvPeople.csv -n
# python src/lab06/cli_text.py stats --input ././data/lab06/samples/txtPeople.txt --top 3


# import argparse

# parser = argparse.ArgumentParser(description="Простая программа приветствия")
# parser.add_argument("--name", required=True, help="Имя пользователя")
# args = parser.parse_args()
# print(f"Привет, {args.name}!")
# python src/lab06/cli_text.py --name Ali # В визал студио
# python Desktop/python_labs/src/lab06/cli_text.py --name Ali # В терминале виндоус
