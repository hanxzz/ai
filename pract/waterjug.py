print("Water jug problem")
x=int(input("Enter X : "))
y=int(input("Enter Y : "))
while True:
 rn=int(input("Enter the rule no. : "))
 if rn==2:
 if y<3:
 x=0
 y=3
 if rn==3:
 if x>0:
 x=0
 y=3
 if rn==5:
5 | Page if x+y>4:
 x=4
 y=y-(4-x)
 if rn==7:
 if x+y<4:
 x=x+y
 y=0
 if rn==9:
 x=2
 y=0
 print("X=",x)
 print("Y=",y)
 if x==2:
 print("The result is a goal state")
 break
