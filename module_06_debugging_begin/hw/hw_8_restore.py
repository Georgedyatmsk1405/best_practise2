a=[]
file=open('hw_8_walk_log_1.txt')

for i in file:
    ii=i.split('\n')
    a.append(ii[0])
print(a)
#Вывод от потомков к корню(родителю)

finalque=[]
for i in a:

    if i.startswith('INFO'):
        if i[30] not in finalque:

            finalque.append(i[30])
    elif 'left' in i:
        if i[68] not in finalque:

            finalque.append(i[68])
    elif 'right' in i:
        if i[69] not in finalque:
            finalque.append(i[69])

print(finalque)



