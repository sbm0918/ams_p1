from stack import Stack


class ThreerBasicOperations:
  operator = ["+", "-", "*"]

  def precedence(op):
    if op == '*': return 1
    elif op == '+' or op == '-': return 0
    else: return -1

  def make_postfix(infix):
    postfix = Stack()
    output = []
    for item in infix:
      if item in ThreerBasicOperations.operator:
        while not postfix.isEmpty():
          op = postfix.peek()
          if ThreerBasicOperations.precedence(
              item) <= ThreerBasicOperations.precedence(op):
            output.append(op)
            postfix.pop()
          else:
            break
        postfix.push(item)
      else:
        output.append(item)

    while not postfix.isEmpty():
      output.append(postfix.pop())

    return output

  def make_infix():
    infix = []
    while True:
      userInput = input('입력하세요: ')
      if userInput == '=':
        break
      infix.append(userInput)
    return infix

  def calculate(postfix):
    s = Stack()
    for token in postfix:
      if token in ThreerBasicOperations.operator:
        val2 = s.pop()
        val1 = s.pop()

        if token == '+': s.push(val1 + val2)
        elif token == '-': s.push(val1 - val2)
        elif token == '*': s.push(val1 * val2)
      else:
        s.push(int(token))
    return s.pop()
