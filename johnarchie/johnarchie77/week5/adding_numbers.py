import sys


def add_them_all(filename):
    numbers = 0

    with open("a.txt", "r"), open("b.txt", "r"),open("c.txt", "r"),open("d.txt", "r"),open("e.txt", "r") as Processing:
        for line in Processing.readline():
         line = line.strip()
        sum.append({Processing})
    
 

    return sum

if__name__=="__main__":
    fname=sys.argv[1]
    print(f"Processing {faname}")
    print(add_them_all(fname))