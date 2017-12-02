def lhs(a,b):
    return (a+b)**2

def rhs(a,b):
    return a**2+2*a*b+b**2

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))

l = lhs(a,b)
r = rhs(a,b)

print("The LHS is: {0:.2f}".format(l))
print("The RHS is: {0:.2f}".format(r))
print("Since LHS = RHS, the formula is proved.")
