import sys

def opr_error(op1, op2):
    if op1 != op2:
        print('Error!')
        sys.exit(0)
def correct_opr_error(op):
    if not(op == "+" or op == "-" or op == "*"):
        print('Error!')
        sys.exit(0)
def val_error(val):
    try:
        int(val)
    except ValueError:
        print('Error!')
        sys.exit(0)
def number_of_inputs_error(length):
    if not(length % 2):
        print('Error!')
        sys.exit(0)