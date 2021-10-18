import sys, argparse

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('n', type = int)

    return parser

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()

print('The fibonacci number you are looking for is ', fibonacci(namespace.n))
