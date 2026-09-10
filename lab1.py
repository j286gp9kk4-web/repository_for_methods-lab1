import  math

# Лабороторная ЭФБО-01-26. Ахмедов Фейзулах Рахматулаевич 

# 1 задача
#Функция f(x), которая дана в условию каждому варианту.
def f(x):
  past1 = x
  past2 = 1
  past3 = 3 + math.sin(3.6*x)
  return past1 - (past2/past3)

def find_x2(l_border, r_border):
  L = l_border
  R = r_border
  while (R - L > 0.0001): # пока разницы границ > 0.0001
    B = L + (R-L)/2 # считаем промеж знач
    #условия из метода половин деления.
    if f(L)*f(B) < 0:
      R = B
    else:
      L = B
  print(B)
find_x2(0, 1) # отображаем результат

#2 задача
def find_x3(l_border, r_border):
  l = l_border # обозначаем границы
  r = r_border
  while (r-l) > 0.0001: 
    xk = l - ((f(l) * (r - l)) / (f(r) - f(l))) # вычисляем промежуточное знач.
    # рассматриваем несколько условий из метода хорд.
    if f(xk) * f(r) > 0:
      r = xk
    elif f(xk) * f(r) < 0:
      l = xk
    else: 
      break
  # при xk = 0 или 0 < xk <= 0.001 выходим из цикла.
  print(xk)
find_x3(0, 1) # отображаем результат