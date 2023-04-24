import random

random_number=random.randint(1,100)

game_count=1

while True:
    try:
        my_number=int(input("input number  from 1 to 100 :"))
        if my_number>random_number:
            print("down")
        elif my_number<random_number:
            print("up")
        elif my_number==random_number:
            print("Congraturation!!")
            break
        game_count +=1
    except:
        print("error!! input number type")

print("test end")