#이스터에그에 들어갈 숫자들
number_list=[7503,1111]
#그 숫자에 맞는 이스터에그들
easter_list=["Sofrware Interaction Lab.","빼빼로"]

#이스터에그에 있는지 확인
def able_easter(i):
    i = int(i)
    if i in number_list:
        return True
    else:
        return False

#이스터에그 값 출력
def find_easter(i):
    i = int(i)
    f = number_list.index(i)
    print("->"+easter_list[f])

