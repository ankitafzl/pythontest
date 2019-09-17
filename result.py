H=int(input("enter the marks of hindi:"))
E=int(input("Enter the marks of english:"))
M=int(input("Enter the marks of math:"))
S=int(input("Enter the marks of social studies:"))
D=int(input("Enter the marks of drawing:"))
C=int(input("Enter the marks of computer:"))
obtained=H+E+M+S+D+C
per=(obtained*100)/600
if per<33:
    print("fail")
elif per>=33 and per<45:
    print("third division")
elif per>=45 and per<60:
    print("second division")
elif per>=60:
    print("first division")
