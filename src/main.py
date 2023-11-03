from three_operations import ThreerBasicOperations


infix= ThreerBasicOperations.make_infix()
postfix = ThreerBasicOperations.make_postfix(infix)

for item in infix:
    print(item, end='')
print("")
for item in postfix:
    print(item, end ='')

result = ThreerBasicOperations.calculate(postfix)
print("")
print(result)
