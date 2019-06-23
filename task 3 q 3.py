integer=int(input("Enter n \n"))+1
out=0
increment=1
var=0
for i in range(2,integer):
    if(i>2):
        for j in range(2,i):
            if(i%j==0):
                var=1
                break
        
    if(var==0):
        out=out+increment
        increment=increment+1
    else:
        var=0
print(str(out))
    
            
