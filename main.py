year = int(input("Введите год: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
  print(f"{year} - високосный год.")
else:
  print(f"{year} - не високосный год.")
