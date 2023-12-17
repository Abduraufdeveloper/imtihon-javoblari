b = int(input("Foizni kiriting :"))
a = [2,4,9,6,5]
e = []

def foizni (b,a,e):
    for x in a :
        son = ( x * b)/100
        e.append(son)
    return(e)
print(b,a,e)