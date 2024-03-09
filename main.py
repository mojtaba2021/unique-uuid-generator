### Write custom-generated unique UUIDs to a text file
import random
import string
import time
def generate_random_uuid():
    try:
        amount = input("please enter your amount of UUIDs ? ") or 0
        amount = int(amount)
        characters = input("please enter each UUID characters ? ") or 0
        characters = int(characters)
        prefix = input("please enter prefix characters ? ") or ''
        if (amount == 0 and prefix == '' and characters == 0 ):
            raise Exception("\ncharacters, amount , prefix cant be empty ! ")
        elif amount > 10000000 :
            raise Exception("Too many UUIDs!")
    except Exception as e:
        print("Error : ", e)
    else: 
        file_name = "{}-{}-unique-UUIDs.txt".format(int(time.time()),amount)
        list_items = set()
        with open(file_name,"w") as file:
            while len(list_items) < amount :
                random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=characters))
                full_text = prefix+random_chars
                if(full_text not in list_items):
                    list_items.add(full_text)
                    file.write(full_text+"\n")
        print("\nCongratulation!")
        print("{:,} unique UUIDs with {} characters generated and saved in {} file.".format(amount,characters,file_name))
while True:
    generate_random_uuid()
    play_again = input("\n \nDo you want to generate more unique UUIDs ? (yes/no)  \n").lower() or 'yes'
    if play_again !='yes':
        break
input()