import sys


def add_them_all(filename):
    sum = 0
    
    fname = open(filename, "r")

    for line in fname:
        sum = sum +int(line)
    
    return sum

if __name__ == "__main__":
    fname=sys.argv[1]
    print(f"Processing {fname}")
    print(add_them_all(fname))