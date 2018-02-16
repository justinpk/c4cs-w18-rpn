def calculate(arg):
    stack = list()
    for token in arg.split():
        try:
            value = int(token)
            stack.append(token)
        except ValueError:
            arg1 = stack.pop()
            arg2 = stack.pop()
            print(arg1 + arg2)

def main():
    while True:
        calculate(input('rpn calc> '))

if __name__ == '__main__':
    main()
