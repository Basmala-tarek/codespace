def main():
    x = int(input("whats x ?"))
    if is_even (x):
        print ("even")
    else:
        print ("odd")

def is_even(n):
    if n % 2 == 0:
        print ("True")
    else:
        print ("False")

main()


