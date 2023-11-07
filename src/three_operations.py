from stack import Stack
from error_check import opr_error, correct_opr_error, val_error, number_of_inputs_error

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

    # 입력 체크
    op = ""
    if len(infix) > 1:
      op = infix[1]
    number_of_inputs_error(len(infix)) # 저장된 값의 개수가 짝수일 때(마지막 입력 숫자 X) Error!
    for index, item in enumerate(infix):
      if index % 2:
        correct_opr_error(item) # 홀수 인덱스의 값이 "+", "-", "*" 가 아닐 시 Error!
        opr_error(op, item) # 사용되는 연산자가 1개 초과 시 Error!
      else:
        val_error(item) # 짝수 인덱스의 값이 정수가 아닐 시 Error!
    
    return infix

  # 후위표기법 적용 ex) 532*+
  def make_postfix(infix):
    postfix = Stack()
    output = []
    for item in infix:
      if item in ThreerBasicOperations.operator:
        while not postfix.isEmpty():
          op = postfix.peek()
          
          #우선순위 높은 연산자 먼저 꺼내기
          if ThreerBasicOperations.precedence(item) <= ThreerBasicOperations.precedence(op):
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
  


