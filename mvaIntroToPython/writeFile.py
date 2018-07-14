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