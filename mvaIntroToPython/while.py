total = 0
j = 1
while j < 5:
  total += j
  j+=1
print(total)

givenList = [5, 4, 4, 3, 1]
total2 = 0
i = 0
while i < len(givenList) and givenList[i] > 0:
  total2 += givenList[i]
  i += 1
print(total2)

givenList2 = [7, 6, 4, 3, 1, -1, -2, -4, -5, -6]
total4= 0
i = len(givenList2) - 1
while i < len(givenList2) and givenList2[i] < 0:
  total4 += givenList2[i]
  i -= 1
print(total4)