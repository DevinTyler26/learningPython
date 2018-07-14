g = 9
h = 8
if g < h:
    print('g < h')
else:
    if g == h:
        print('g == h')
    else:
        print('g > h')

name = 'Devin'
height = 2
weight = 110

bmi = weight / (height ** 2)
print('bmi: ')
print(bmi)
if bmi < 25:
  print(name)
  print('is not overweight')
else:
  print(name)
  print('is overweight')