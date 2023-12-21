
"""
def Jockey(x):
    if x == 1: return 1
    else: return x * (Jockey(x - 1))
print(Jockey(4))

def Jockey(n):
    x = 1

    for i in range(1, n+1):
        x *= i
    return x

"""

my_list = [1,2,3,4,5,6]

for i in my_list:
    my_list.remove(i)

print(my_list)