N = int(input())
def solution():
    s = input()
    a = ""
    b = ""
    c = (int)((int)(len(s)) / 2)
    ttl1 = 0
    ttl2 = 0
    a1 = ""
    b1 = ""
    a2 = ""
    for i in range(0, (int)(c)):
        a += s[i]
        b += s[i + c]
        ttl1 += (int)(ord(s[i])) - 65
        ttl2 += (int)(ord(s[i + c])) - 65
    for i in range(0, c):
        x = (int)(ord(a[i]) - ord('A'))
        x += ttl1
        x %= 26
        a1 += chr(x + ord('A'))
        x = (int)(ord(b[i]) - ord('A'))
        x += ttl2
        x %= 26
        b1 += chr(x + ord('A'))
        x = ord(a1[i]) - ord('A') + x
        x %= 26
        a2 += chr(x + ord('A'))
    print(a2)


def main():
    for i in range(0, N):
        solution()

if __name__ == "__main__":
    main()