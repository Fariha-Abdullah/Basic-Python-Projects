import random as rand
import array as arr
max_len=10
digits=['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
lower=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols=['!', '@', '#', '$', '%', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '[', ']', ':', ';', '~', ',', '.','<', '>', '?', '/', '^']

combination= digits+upper+lower+symbols

rand_digit=rand.choice(digits)
rand_upper=rand.choice(upper)
rand_lower=rand.choice(lower)
rand_sym=rand.choice(symbols)

temp_pass=rand_digit+rand_upper+rand_lower+rand_sym
for i in range(max_len-4):
    temp_pass= temp_pass + rand.choice(combination)
    temp_pass_list=arr.array('u', temp_pass)
    rand.shuffle(temp_pass_list)


password= ""
for i in temp_pass_list:
    password=password+i
print("YOUR RANDOM PASSWORD GENERATED SUCCESSFULLY!!!\nGENERATED PASSWORD: ", password)

