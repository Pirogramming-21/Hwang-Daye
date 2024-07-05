import random
num = 0
count = 0

def brGame(player):
    global count
    if player == "computer":
        num = random.randint(1, 3)
        for i in range(num):
            count += 1
            print(f"{player}: {count}")
            if count >= 31:
                return True
    elif player == "PlayerA":
        while True:
            try:
                num = int(input(f"{player}: 부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): "))
                if num < 1 or num > 3:
                    print("1, 2, 3 중 하나를 입력하세요.")
                else:
                    break
            except ValueError:
                print("정수를 입력하세요")

        for i in range(num):
            count += 1
            print(f"{player}: {count}")
            if count >= 31:
                return True
    return False

while count < 31:
    if brGame("computer"):
        print("Player A wins!")
        break
    if brGame("PlayerA"):
        print("computer wins!")
        break

