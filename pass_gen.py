import string
import random

if __name__ ==  "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3= string.digits
    s4= string.punctuation
    p_len = int(input("Enter The Length of Your Password\n"))
    list_s=[]
    list_s.extend(list(s1))
    list_s.extend(list(s2))
    list_s.extend(list(s3))
    list_s.extend(list(s4))
    # This is our First Method
    # random.shuffle(list_s)
    # print("Your PassWord is :")
    # print("".join(list_s[0:p_len]))

    # This is our second  Method
    print("".join(random.sample(list_s,p_len)))