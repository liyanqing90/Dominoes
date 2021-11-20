# Write your code here
import random


def same(alist: list):
    blist = []
    for one in sorted(alist[::-1]):
        if one[0] == one[1]:
            if blist:
                if one[0] > blist[0]:
                    blist = one
            else:
                blist = one
    return blist


def move(anum, alist):
    if anum == 0:
        if Stock_pieces:
            alist.append(Stock_pieces.pop(0))
    elif anum < 0:
        if Domino_snake[0][0] in alist[abs(anum) - 1]:
            avalue = alist.pop(abs(anum) - 1)
            if Domino_snake[0][0] == avalue[0]:
                avalue.reverse()
            Domino_snake.insert(0, avalue)
        else:
            return False
    else:
        if Domino_snake[-1][1] in alist[anum - 1]:
            avalue = alist.pop(anum - 1)
            if Domino_snake[-1][1] == avalue[1]:
                avalue.reverse()
            Domino_snake.append(avalue)
        else:
            return False
    return True


domino_list = []
do_list = []
while True:
    for x in range(8):
        for y in range(8):
            z = [x, y]
            z_lst = sorted(z)
            if z_lst not in do_list:
                do_list.append(z_lst)
                domino_list.append(z)
    random.shuffle(domino_list)
    domino_list = domino_list[:28]
    Stock_pieces = domino_list[:14]
    Computer_pieces = domino_list[14:21]
    Player_pieces = domino_list[21:]

    cum_same = same(Computer_pieces)
    play_same = same(Player_pieces)
    Domino_snake = [max(cum_same, play_same)]
    if cum_same or play_same:
        break

if cum_same > play_same:
    Status = "player"
    Computer_pieces.remove(cum_same)
else:
    Status = 'computer'
    Player_pieces.remove(play_same)
while True:
    print("=" * 70)
    print(f"Stock size: {len(Stock_pieces)}")
    print(f"Computer pieces: {len(Computer_pieces)}")
    if len(Domino_snake) <= 6:
        for item in Domino_snake:
            print(item, end='')
    else:
        for item in Domino_snake[:3]:
            print(item, end='')
        print("...", end='')
        for item in Domino_snake[-3:]:
            print(item, end='')
    print("")
    print("Your pieces:")
    for x, y in enumerate(Player_pieces):
        print(f"{x + 1}:{y}")

    if len(Computer_pieces) == 0:
        print("Status: The game is over. The Computer won!")
        break
    if len(Player_pieces) == 0:
        print("Status: The game is over. You won!")
        break
    if not Stock_pieces:
        print("Status: The game is over. It's a draw!")
        break
    z = Stock_pieces[0][0]
    m = 0
    if z == Stock_pieces[-1][1]:
        for i in Stock_pieces:
            for j in Stock_pieces:
                if j == z:
                    m += 1
    if m == 8:
        print("Status: The game is over. It's a draw!")
        break

    if Status == "player":
        print("Status: It's your turn to make a move. Enter your command.")

        while True:
            num = input()
            if num.isdigit():
                num = int(num)
            elif len(num) > 1 and num[0] == "-" and num[1:].isdigit():
                num = int(num)
            else:
                num = None
            if num or num == 0:
                if abs(num) > len(Player_pieces):
                    print("Invalid input. Please try again..")
                else:
                    x = move(num, Player_pieces)
                    if x:
                        Status = 'computer'
                        break
                    else:
                        print('Illegal move. Please try again.')
                        continue
            else:
                print("Invalid input. Please try again..")

    else:
        print("Status: Computer is about to make a move. Press Enter to continue...")
        all_list = domino_list + Computer_pieces
        all_dict = dict.fromkeys(range(10), 0)
        for i in all_list:
            all_dict[i[0]] += 1
            all_dict[i[1]] += 1
        coumper_list = {}
        for x, y in enumerate(Computer_pieces):
            coumper_list[0] = all_dict[y[0]] + all_dict[y[1]]
        coumper__index_list = sorted(coumper_list.keys(), key=lambda k: coumper_list[k])
        for i in coumper__index_list:
            Domino_snake0 = Domino_snake[0][0]
            Domino_snake1 = Domino_snake[0][1]
            if Domino_snake0 in Computer_pieces[i]:
                value = Computer_pieces.pop(i)
                if Domino_snake0 == Domino_snake[0][0]:
                    value.reverse()
                Domino_snake.insert(0, value)
                break
            elif Domino_snake1 in Computer_pieces[i]:
                value = Computer_pieces.pop(i)
                if Domino_snake1 == Domino_snake[0][1]:
                    value.reverse()
                Domino_snake.append(value)
                break
        else:
            Computer_pieces.append(Stock_pieces.pop(0))
        Status = "player"
        while True:
            if not input():
                break
