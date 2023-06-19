'''def profit(a):
    n=len(a)
    d1=int(input('enter buy day '))
    d2=int(input('enter sold day'))
    for i in range(n):
        
           p=a[d2]-a[d1]
    print (p)
a=profit([100,180,260,310,40,535,695]) '''
'''array = [int(element) for element in input("Enter the elements of the array separated by spaces: ").split()]
print(array)'''
a = [int(i) for i in input("Enter the elements of the array separated by spaces: ").split()]
#print(a)

n=len(a)
d1=int(input('enter buy day '))
d2=int(input('enter sold day'))
for i in range(n):
     p=a[d2]-a[d1]
print (p)


'''
n=len(a)
d1=int(input('enter buy day '))
d2=int(input('enter sold day'))
for i in range(n):
     p=a[d2]-a[d1]
print (p)'''
