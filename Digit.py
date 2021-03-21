# Function Initialization :
def digitAwal(a, b):
    c = a**b
    d = str(c)
    print(d[0])
    return d


def digitAkhir(x,y):
    z = x**y
    o = str(z)
    print(o[-1])
    return o

# Use the function
print('Digit Awal')
digitAwal(10,8)
digitAwal(2,3)
digitAwal(6,3)
print()
# Use the function
print('Digit Akhir')
digitAkhir(10,8)
digitAkhir(2,3)
digitAkhir(6,3)
