""" x = 3
y = float(3)
print(x,y)
"""

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
def spaces(N,Y,T):
    x = 0
    for i in range(N):
        if Y[i] == "C" and T[i] == "C":
            x += 1
    print(x)
spaces(5, "CC..C", ".CC..")


"""values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)

x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z)

counter = str(input("Input any sentence of your choosing please."))
print(counter)
y = counter.split()
print(y)
print(len(y)) """

""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """

""" def wizard(owner,N,duels):
    #who owns the wand
    last_owner = owner
    #number of times changes
    changes = 0
    #check one single battle
    #print(duels[0])
    #check first character
    print(duels[0][0])
    if duels[0][1] == owner:
        owner = duels[0][0]
        changed_hands += 1
    #check if wand changed hands
    if owner == duels[0][0]: """

""" wizard("A",3,["BA", "CB", "DA"]) """

def wizards(N, start, duels):
    owner = start
    num_owners = 1
    for i in range(N):
        if duels[i][1] == owner:
                owner = duels[i][0]
                num_owners += 1
    print(owner, num_owners)

wizards(3, "A", ["BA", "CB", "DA"])

def language(N):
    t = 0 
    s = 0
    
    for i in range(N):
        text = input()

        for letter in text:
             if letter == "t" or letter == "T":
                  t += 1
             elif letter == "s" or letter == "S":
                  s += 1
    if t > s:
         print("English")
    else:
         print("French")
language(3)