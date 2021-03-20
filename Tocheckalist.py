#to check the element of the list is number and it is greater than 6

items = [int, float,"Harry", "Gul", 4 ,6 ,78 ,98 ,45 ,98 ]
for item in items:
    if str(item).isnumeric() and item>6:
        print(item)
