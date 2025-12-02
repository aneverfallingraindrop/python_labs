def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    from pathlib import Path
    import csv
    import openpyxl # type: ignore
    if not Path(csv_path).exists(): raise FileNotFoundError
    if not csv_path[-4:] == ".csv": raise ValueError
    file = open(csv_path, "r", encoding="utf-8")
    strng = file.read()
    file.close()
    if len(strng) == 0: raise ValueError
    workbook = openpyxl.Workbook()
    worksheet = workbook.active 
    worksheet.title = "Sheet1" 
    with open(csv_path, "r", encoding="utf-8") as filecsv:
        for row in csv.reader(filecsv):
            worksheet.append(row)
            workbook.save(xlsx_path)
    for col in worksheet.columns:
        max_len = 8 
        for cell in col: 
            val = cell.value 
            len_cell = len(str(val)) 
            max_len = max(max_len, len_cell) 
        format = (max_len) 
        worksheet.column_dimensions[str(col)].width = format 
                
# a = csv_to_xlsx("././data/lab05/samples/csvPeople.csv", "././data/lab05/out/csvPeople.xlsx")