
def calculator():
    num_list = [] #숫자배열
    operator_list = [] #연산자배열
    result = 0 #결과값
    type = 999  #해야할 연산 타입
    isPossible = True #다른 연산자가 섞였는가?
    i = 0
    while True:
        i1= input()
        #i1값이 int형인지 확인
        try:
            num1 = int(i1)
        except ValueError:
            isPossible = False
        i2= input()
        if isPossible == True:
            num_list.append(num1)
        operator_list.append(i2)
        if i == 0:  #처음 들어오는 거라면
            if isPossible == True:
                result = num_list[i]  # 결과에 첫값을 기록 및 연산 타입 기록
            if i2 == "+":
                type = 0
            elif i2 == "-":
                type = 1
            elif i2 == "*":
                type = 2
            else: #연산자가 +, -, *이 아니면 타입 3번, 연산불가능 처리
                type = 3
                isPossible = False
        else:  #처음이 아니라면 타입에 맞는 연산시작
            if isPossible == True:
                if type == 0:
                    result = result + num_list[i]
                elif type == 1:
                    result = result - num_list[i]
                elif type == 2:
                    result = result * num_list[i]
            #전과 지금의 연산자가 다를시 처리
            if operator_list[i-1] != operator_list[i]:
                if i2 != "=":
                    isPossible = False
                if i2 == "=":
                    if isPossible == True:
                        print(result)
                    else:
                        print("Error!")
                    break
        i += 1


if __name__ == '__main__':
    calculator()
