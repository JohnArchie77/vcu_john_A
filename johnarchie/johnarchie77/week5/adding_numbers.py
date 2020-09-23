import sys


def add_them_all(filename):
    sum = 0

    with open("a.txt", "r") as a, open("b.txt", "r") as b,open("c.txt", "r") as c, open("d.txt", "r") as d, open("e.txt", "r") as e:
        for line in fname.readline():
         line = line.strip()
        sum.extend(a, b, c, d, e)
    
 

    return sum

if__name__=="__main__":
    fname=sys.argv[1]
    print(f"Processing {faname}")
    print(add_them_all(fname))