import math

def Minmax(cd, node, maxt, scr, td):
    if(cd == td):
        return scr[node]
    if(maxt):
        return max(Minmax(cd + 1 , node*2, False, scr, td ),
                    Minmax(cd + 1, node*2 + 1, False, scr, td))
    else : 
        return min(Minmax(cd + 1, node*2, True, scr, td),
                    Minmax(cd + 1, node*2+1, True, scr, td))

    
scr = []

x = int (input("Enter the total no. of nodes : "))
for i in range(x):
    y = int(input("Enter Leaf Value : "))
    scr.append(y)

td = math.log(len(scr), 2)
cd = int(input("Enter Current Depth Value : ")) 
nodev = int(input("Enter Node Value : "))

maxt = True

print("The answer is : ", end="")
answer = Minmax(cd,nodev,maxt,scr,td)
print(answer)
