setq default-tab-width 4)

def calculate(arg):
    stack = list()
    for token in arg.split():
        stack.append(token)
    print(stack)

def main():
    while True:
        calculate(input('rpn calc> '))

if _name_ == '__main__':
    main()
