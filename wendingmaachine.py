stock=10
i=1
pen=int(input("How many pen u want"))
while i <= pen:
    if stock<i:
        print("out of stock")
        break
    print(i, "=collect pen")
    i+=1
else:
    print("Thank you visit again")