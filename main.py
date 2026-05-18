import numpy as np 

ar1 = np.array([10,20,30,40,50])
print(ar1[2])
                # slicing operator :

print(ar1[0:3])
print(ar1[:3])
print(ar1[2:5])
print(ar1[2:])

print(ar1[0:5:2])
# reversing array :  ::-1
print(ar1[::-1])

da3d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(da3d)
print(da3d[0:2,0:2])

print("\n")


arra1 = np.arange(1,50).reshape(7,7)
print(arra1)
print(arra1[2:5,2:5])

arra2 = np.array([1,2,3,4,5,6,7,8,9,10])

even_array = arra2[arra2%2 == 0]
print(even_array)
odd_array = arra2[arra2%2 != 0]
print(odd_array)

a = arra2[arra2 == 5]
print(a) 
a2 = arra2[arra2 == 11]
print(a2)

print(arra2[[2,4,6]])

print(arra2[arra2<5])
print(arra2[arra2>5])

array1 = np.array([1,2,3,4,5])
array2 = np.array([6,7,8,9,10])

result = array1 + array2
print(result)

matricA = np.random.permutation(np.arange(16)).reshape(4,4)
print(matricA)

matric2 = np.random.permutation(np.arange(16)).reshape(4,4)
print(matric2)

results2 = matric2 + matricA
print(results2)

def linear_eq(x):
    y = (2*x)+3
    print(y)

linear_eq(5)
x= np.array([1,2,3,4,5,6,7,8,9])
linear_eq(x)