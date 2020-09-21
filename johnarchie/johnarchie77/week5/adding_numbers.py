import sys


def add_them_all(filename):
    sum = 0

    with open("a.txt, b.txt, c.txt, d.txt, e.txt", "r") as f:
        for line in f.readline():
         line = line.strip()
        part = line.split(",")
        sum.append({})
    Processing = sum(sum)
    print(Processing)

    return sum

if__name__=="__main__":
    fname=sys.argv[1]
    print(f"Processing {faname}")
    print(add_them_all(fname))
