import sys, argparse

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('n', type = int)
    parser.add_argument('-a', '--all', action='store_const', const=True)
    parser.add_argument('-f', '--file', type=argparse.FileType(mode='w', encoding=None, errors=None))

    return parser

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()

res = []
for i in range(1, namespace.n + 1):
    res.append(fibonacci(i))

with open('task_3.txt', 'w') as f:
    sys.stdout = f
    print(res)

