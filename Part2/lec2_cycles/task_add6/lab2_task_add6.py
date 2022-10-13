period_type = int(input("Выберите период - до н.э.(введите 1) или н.э.(введите 2):"))
day = int(input("Введите день:"))
month = int(input("Введите порядковый номер месяца:"))
year = int(input("Введите год:"))
ol_year_primary = 0;
ol_year_secondary = 0;
if period_type == 1:
  year = 776 - year;
elif period_type == 2:
  year += 776;
def olymp_date(day, month, year, ol_year_primary, ol_year_secondary):
  if year % 4 == 0:
    if month < 7:
      year += 3;
    elif month == 7:
      if day > 1:
        year += 1;
    elif month > 7:
      year += 1;
  ol_year_primary += (year // 4) + 1;
  ol_year_secondary += (year % 4);
  print(f"Дата по календарю Тимея: OL {ol_year_primary}.{ol_year_secondary} .")
olymp_date(day, month, year, ol_year_primary, ol_year_secondary)