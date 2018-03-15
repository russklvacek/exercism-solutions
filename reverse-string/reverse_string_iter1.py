def reverse(input=''):
    reversed = list(input)
    for i in range(len(input)):
        reversed[i] = input[len(input) -1 - i]
    return ''.join(reversed)
