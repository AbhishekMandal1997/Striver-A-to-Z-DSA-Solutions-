num1 = int(input("Enter first digit:"))
num2 = int(input("enter second digit:"))

fac1 = []
fac2 = []
GCD = []
for i in range(1,num1 + 1):
    if num1 % i == 0:
         fac1.append(i)
for j in range(1,num2 + 1):
    if num2 % j == 0:   
        fac2.append(j)    
        
for fac in fac1:
    if fac in fac2:
        GCD.append(fac)
GCD_str = ','.join(map(str, GCD))
print(GCD_str)
