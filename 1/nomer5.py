x=int(input("координата x:"))
y=int(input("координата y:"))
if x>0 and y>0:
  print("Находится в первой четверти")
if x>0 and y<0:
  print("Находится во второй четверти")
if x<0 and y<0:
  print("Находится в третьей четверти")
if x<0 and y>0:
  print("находится в четвёртой четверти")
if x>0 and y==0:
  print("Точка находится на оси абцисс")
if x<0 and y==0:
  print("Точка находится на оси абцисс")