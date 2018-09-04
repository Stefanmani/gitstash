#Find the rythmic of the numbers
#Ask for n to specify the number og numbers generated
#Put up a generator for the numbers
#Print the numbers
#1,2,3,6,11,20,37
# 1 1 3 5 

n = int(input("Enter the length of the sequence: ")) # Do not change this line
num_list = [1,2]
for x in range(n):
    if x+1 < 3:
        print(x+1)
        continue
    z = 0
    r = num_list[-3:]
    for x in r:
        z += x
    print(z)
    num_list.append(z)



