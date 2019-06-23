def calcSum(length, num):
    sumofDigits=0
    while(length>0):
        quotient=int(num/(10**(length-1)))
        num=num-10*quotient
        sumofDigits=sumofDigits+quotient
        length-=1
    return sumofDigits




def findLength(num):
    length=0
    while(int(num/(10**length))!=0):
        length+=1
    return length



num=int(input("Enter number \n"))
length=int(findLength(num))
sOD=int(calcSum(length, num))
tries=1
while(sOD>=10):
    length=int(findLength(sOD))
    sOD=int(calcSum(length,sOD))
    tries+=1
print(str(tries))
