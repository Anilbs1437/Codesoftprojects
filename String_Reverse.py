def reverse(p):
    if len(p) == 0:
        return p
    else:
        return reverse(p[1:]) + p[0]
 
 
q = "Engineering"
 
print("The original string is : ", end="")
print(q)
 
print("The reversed string(using recursion) is : ", end="")
print(reverse(q))