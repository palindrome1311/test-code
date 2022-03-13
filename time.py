import datetime

a = datetime.datetime.now()
i = 0
c = 0 
total = 88569924*2
while(i<total):
    b = datetime.datetime.now()
    i+=1
    c = b-a
    c = c.total_seconds()
name = 'seconds took is ' + str(c) + 'total is ' + str(total)
print(name)