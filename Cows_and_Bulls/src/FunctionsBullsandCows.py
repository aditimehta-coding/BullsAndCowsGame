def generateCode() -> list:
    import random
    n = 9
    my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    code = []
    for i in range(4):
        x = random.randint(0, n)
        code.append(my_list[x])
        my_list.pop(x)
        n -= 1
    # print(code)
    return code


def construct_validate_user_input(a: str, b: str, c: str, d: str) -> bool:
    from collections import Counter
    x = a + b + c + d
    repeats = Counter(x).values()
    if not(any(value > 1 for value in repeats)):
        return True
    else:
        return False


def calculate_Cows_and_Bulls(a: str, b: str, c: str, d: str, code: list) -> list[int]:
    x = a + b + c + d
    bulls_cows_output = [0, 0]
    list_user_input = [int(char) for char in x]
    for i in range(4):
        if list_user_input[i] in code:
            if list_user_input[i] == code[i]:
                bulls_cows_output[0] += 1
            else:
                bulls_cows_output[1] += 1
    return bulls_cows_output