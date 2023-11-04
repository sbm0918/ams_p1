import sys

def opr_error(op1, op2):
    if op1 !=op2:
        print('Error!')
        sys.exit(0)
def val_error(val):
    try:
        int(val)
    except ValueError:
        print('Error!')
        sys.exit(0)
