with open("control.txt", "r") as f:
    for line in f:
        print(' '.join(line.split()))
