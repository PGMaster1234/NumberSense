import random
import math

answers = []
count = 0


def RoundCheck(n, d):
    return int(n/d) == float(n/d)


print(RoundCheck(5, 2))


def ImproperToMixed(n, d):
    whole = 0
    while n > d:
        whole += 1
        n -= d
    if n == d:
        whole += 1
        n = 0
    if n == 0:
        return str(whole)

    else:
        if whole != 0:
            return str(whole) + " " + str(n) + "/" + str(d)
        else:
            return str(n) + "/" + str(d)


def AddSub(ans):
    global count
    count += 1

    a = random.randint(3000, 5000)
    b = random.randint(300, 500)
    if random.randint(0, 1) == 0:
        c = "-"
        ans.append(a - b)
    else:
        c = "+"
        ans.append(a + b)
    print(str(count) + ": " + str(a) + " " + str(c) + " " + str(b) + "    " + "INTEGER")


def AddSubMixedFrac(ans):
    global count
    count += 1

    a = random.randint(3, 11)
    b = random.randint(3, 11)
    c = random.randint(6, 9)

    ans.append(ImproperToMixed(a*2+b, c*2))
    print(str(count) + ": " + str(a) + "/" + str(c) + " + " + str(b) + "/" + str(c * 2) + "    " + "MIXED FRACTION")


def FOIL(ans):
    global count
    count += 1

    a = random.randint(20, 99)
    b = random.randint(20, 99)

    ans.append(a*b)
    print(str(count) + ": " + str(a) + " " + "x" + " " + str(b) + "    " + "INTEGER")


def MulMixedFrac(ans):
    global count
    count += 1

    whole = random.randint(3, 11)
    d = random.randint(4, 9)
    n = random.randint(1, d-1)
    n_2 = d-n

    ans.append(str((whole ** 2) + whole) + " " + ImproperToMixed(n*n_2, d**2))
    print(str(count) + ": " + str(whole) + " " + str(n) + "/" + str(d) + "  x  " + str(whole) + " " + str(n_2) + "/" + str(d) + "    " + "MIXED FRACTION")


# ---------------------- Questions
AddSub(answers)
AddSubMixedFrac(answers)
FOIL(answers)
MulMixedFrac(answers)

# ---------------------- Answers
ct = 0
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")

for answer in answers:
    ct += 1
    print(str(ct) + ": " + str(answer))
