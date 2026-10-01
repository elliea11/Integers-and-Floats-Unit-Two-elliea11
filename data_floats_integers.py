""" x = 3
y = float(3)
print(x,y)
 """
""" Create variables representing at the bill, tip and total amount paid
Receive user input and assign that user input to the variables in step 1 (excluding total)
Change the data type of bill from String to Float
Change the data type of tip to Integer (int)
Calculate the total that needs to be paid
Print the f string after the user has input data"""

""" bill = float(input("How much was your bill?"))
service = int((input("Rate your service 1-5, 5 being the best, 1 being the worst. ")))
if service == 1:
    tip = 1.00
elif service == 2:
    tip = 1.10
elif service == 3:
    tip = 1.15
elif service == 4:
    tip = 1.20
elif service == 5:
    tip = 1.30
total = bill* tip
print(total)
 """
""" def spaces(N,Y,T,):
    x = 0
    for i in range(N):
        if Y[i] == "C" and T[i] == "C":
            x += 1
    print(x)
spaces(5, "CC..C", ".CC..") """

values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)