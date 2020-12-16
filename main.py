import string
import random
if __name__ == '__main__':
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    while True:
        try:
            plen = int(input("Enter Password Length\n")) #Todo1: Handle Gibberish
            break
        except ValueError:
            print("Oops! That's not the valid number.Please try again..")
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    # print(s)
    random.shuffle(s)
    # print(s)
    print("Your Password is:")
    print("".join(s[0:plen]))