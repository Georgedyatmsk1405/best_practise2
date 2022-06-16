from datetime import datetime
list1=[]
with open('log.txt') as f:
    for i in f:
        i=i.split('\n')
        for j in i:
            j=j.split(' - ')
            list1.append(j)

start=[]
end=[]
for bb in range(len(list1)-1):
    if len(list1[bb])==3:
        if list1[bb][2]=='Enter measure_me':
            start.append(list1[bb][0])
        elif list1[bb][2]=='Leave measure_me':
            end.append(list1[bb][0])
        else:
            pass
    else:
        pass
final=[]
for ff in range(len(start)-1):
    a=datetime.strptime(end[ff], '%H:%M:%S')
    b=datetime.strptime(start[ff], '%H:%M:%S')
    c=a-b
    final.append(c)
print(start)
print(end)
print(final)

