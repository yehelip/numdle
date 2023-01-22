import random as ra
from colorama import Back, Style


def guess_once():
    validity = 0
    guess = 0
    while validity == 0:
        try:
            guess = int(input("\nMake your guess: "))
            if guess < 10000 or guess > 99999:
                raise ValueError
            validity += 1
        except ValueError:
            print("do it right!")
    return guess


def attempt2arr(att):
    ret = []
    for cnt in range(5):
        ret.append(int(str(att)[cnt]))
    return ret


def print_dig(num, arr, i):
    num_arr = attempt2arr(num)
    if num_arr[i] == arr[i]:
        return Back.GREEN + str(arr[i])
    elif arr[i] in num_arr:
        return Back.RED + str(arr[i])
    else:
        return str(arr[i])


if __name__ == '__main__':
    num = ra.randint(10000,99999)
    attempt_num = 5
    attempt = 0
    while attempt != num:
        if attempt_num == 0:
            print(Style.RESET_ALL + '\n\n' + Back.BLACK + 'YOU LOST.\n the number was:',num)
            exit()
        attempt = guess_once()
        attempt_num -= 1
        arr = attempt2arr(attempt)
        for i in range(5):
            print(print_dig(num, arr, i) + Style.RESET_ALL, end='')

    print("\n\nYOU WON!!!\n With",attempt_num,'attempts extra!\U0001f600')
