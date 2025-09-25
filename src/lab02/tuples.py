def format_record(rec: tuple[str, str, float]) -> str:
    fio_parts = rec[0].split()
    fam = fio_parts[0].capitalize()
    name_init = fio_parts[1][0].upper()
    otch_init = [p[0].upper() for p in fio_parts[2:]]
    initials = name_init + ''.join('.' + i for i in otch_init) + '.'
    gpa_str = f"{rec[2]:.2f}"
    return f"{fam} {initials}, гр. {rec[1]}, GPA {gpa_str}"

# test format_record
# print('1:', format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
# print('2:', format_record(("Петров Пётр", "IKBO-12", 5.0)))
# print('3:', format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
# print('4:', format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
