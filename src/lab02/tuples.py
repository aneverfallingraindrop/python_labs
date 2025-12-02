def format_record(rec: tuple[str, str, float]) -> str:
    fio = rec[0]
    group = rec[1]
    gpa = rec[2]

    if fio == "":
        raise ValueError
    if group == "":
        raise ValueError
    if type(gpa) != float:
        raise TypeError

    fio = fio.split()
    if len(fio) == 3:
        fio[0] = fio[0][0].upper() + fio[0][1:]
        fio[1] = fio[1][0].upper() + "."
        fio[2] = fio[2][0].upper() + "."
        fio = " ".join(fio)
    else:
        fio[0] = fio[0][0].upper() + fio[0][1:]
        fio[1] = fio[1][0].upper() + "."
        fio = " ".join(fio)
    group = "гр. " + group
    gpa = "GPA " + str(round(gpa, 2)) + "0"
    return f"{fio}, {group}, {gpa}"


student1 = ("Иванов Иван Иванович", "BIVT-25", 4.6)
student2 = ("Петров Пётр", "IKBO-12", 5.0)
student3 = ("Петров Пётр Петрович", "IKBO-12", 5.0)
student4 = ("  сидорова  анна   сергеевна ", "ABB-01", 3.999)
print(format_record(student1))
print(format_record(student2))
print(format_record(student3))
print(format_record(student4))
