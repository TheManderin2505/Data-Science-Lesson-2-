import numpy as np 

def quadratic(x):
    y = (x**2)+x+3

def liear_eq(x):
    y = (2*x)+3
    print(y)

x = np.array([0,1,2,3,4,5,6,7,8,9,10])

usrchc = input("Quadratic Or Linear?")
if usrchc == "quadratic":
    quadratic(x)

elif usrchc == "linear":
    liear_eq(x)
