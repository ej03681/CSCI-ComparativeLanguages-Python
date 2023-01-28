def count(S, ch):
    times = 0
    ch = ch.lower()
    for i in range(1, len(S)):
        if S[i] == ch:
            times += 1
    return times
def main():
    S = input("Enter a string: ")
    ch = input("Enter a character: ")
    print(ch, " appears in Welcome to Python ", count(S, ch), " times")
main()