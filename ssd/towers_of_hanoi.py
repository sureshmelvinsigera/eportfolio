"""A recursive solution for the Towers of Hanoi problem."""


def hanoi(n, A, C, B):
    if n == 1:
        print(f'{n} from {A} to {C}')

    else:
        hanoi(n-1, A, B, C)
        print(f'{n} from {A} to {C}')
        hanoi(n-1, B, C, A)


# 2^n - 1 moves.
# this solution allows that positions can be passed over.
# i.e. you can pass from A to C without having to stop on B first.

hanoi(10, 'A', 'C', 'B')
