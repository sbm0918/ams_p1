from stack import Stack
from error_check import opr_error,val_error

class ThreerBasicOperations:
  operator = ["+", "-", "*"]

  def precedence(op):
    if op == '*': return 1
    elif op == '+' or op == '-': return 0
    else: return -1

  #사용자 입력 ex) 5+3*2
  def make_infix():
    infix = []
    while True:
      userInput = input('입력하세요: ')
      if userInput == '=':
        break
      infix.append(userInput)
    return infix

  # 후위표기법 적용 ex) 532*+
  def make_postfix(infix):
    postfix = Stack()
    output = []
    for item in infix:
      if item in ThreerBasicOperations.operator:
        while not postfix.isEmpty():
          op = postfix.peek()
          
          #에러처리
          opr_error(item, op)
          #우선순위 높은 연산자 먼저 꺼내기
          if ThreerBasicOperations.precedence(item) <= ThreerBasicOperations.precedence(op):
            output.append(op)
            postfix.pop()
          else:
            break
        postfix.push(item)
      else:
        #에러처리
        val_error(item)
        output.append(item)

    while not postfix.isEmpty():
      output.append(postfix.pop())

    return output

  #연산결과 출력
  def calculate(postfix):
    s = Stack()
    for token in postfix:
      #연산자 만나면
      if token in ThreerBasicOperations.operator:
        val2 = s.pop()
        val1 = s.pop()
        if token == '+': s.push(val1 + val2)
        elif token == '-': s.push(val1 - val2)
        elif token == '*': s.push(val1 * val2)
      #피연산자는 스택으로 출력
      else:
        item = int(token)
        s.push(item)
    return print(s.pop())
  


