# import turtle
# nmb = int(input('How many sides?'))

# for steps in range(nmb):
#   turtle.color('blue')
#   turtle.forward(20)
#   turtle.right(360/nmb)
#   turtle.color('red')
#   for steps in range(nmb):
#     turtle.right(360/nmb)
#     turtle.forward(20)
# input()

guests = ['Devin','Mom','Dad','Jensen', 'Toccara']
age = ['27', '60', '60', '32', '29']

fileName = 'GuestLists.txt'
WRITE = 'w'
READ = 'r'
APPEND = 'a'
READWRITE = 'r+'

def writeFile():
  myFile = open(fileName, WRITE)
  for i in range(len(guests)):
    myFile.write(guests[i])
    myFile.write(': ')  
    myFile.write(age[i])
    myFile.write('\n')
  print('File has been written')
  myFile.close()
  return

writeFile()


myFile = open(fileName, READ)
allFileContents = myFile.read()
myFile.close()
print('File contents:\n',allFileContents)