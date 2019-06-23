length=int(input("Enter length of wall \n"))
number=int(input("Enter number of bricks \n"))
strengthList=[]
for j in range(number):
    strength=int(input("Enter brick strength \n"))
    strengthList.append(strength)
    i=j
    while(i>0):
        if(strengthList[i]<strengthList[i-1]):
            strengthList[i]=temp
            strengthList[i]=strengthList[i-1]
            stregnthList[i-1]=temp
            i-=1
        else:
            i=0
for k in range(number-length):
    combi=strengthList[0]+strengthList[1]
    strengthList.pop(0)
    strengthList.pop(0)
    strengthList.append(combi)
    i=number-2
    while(i>0):
        if(strengthList[i]<strengthList[i-1]):
            temp=strengthList[i]
            strengthList[i]=strengthList[i-1]
            strengthList[i-1]=temp
            i-=1
        else:
            i=0
    number=number-1
print(str(strengthList[0]))
