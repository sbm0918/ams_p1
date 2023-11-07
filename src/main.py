from three_operations import ThreerBasicOperations

infix= ThreerBasicOperations.make_infix()
ThreerBasicOperations.infix_check(infix)
postfix = ThreerBasicOperations.make_postfix(infix)
result = ThreerBasicOperations.calculate(postfix)



