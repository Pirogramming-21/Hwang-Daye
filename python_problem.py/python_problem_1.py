num = 0

while True:
    try:
        num = int(input("부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능)"))

        if (num < 1) or (num > 3) :
            print("1,2,3 중 하나를 입력하세요.")
        else: 
            break
    except ValueError:
        print("정수를 입력하세요")

for i in range (1, num+1):
    print("playerA:",i)