### Functions Practice ###

### Guess where in the array is the cup with the ball ###
### After 3 a few tries, it shuffles the cups ###
### Tells you if close when within 2 cups of the right spot, not close otherwise ###
### Shows your the cup array after winning ###


from random import shuffle

def shuffle_cup(my_cups):
    shuffle(my_cups)
    #print(my_cups)
    return my_cups


def num_cups(cups):
    num_of_cups = ['O']+[' ']*cups
    return num_of_cups


def user_guess(cups):
    return input("Guess between 1 and {}: ".format(cups+1))


cups = int(input("Choose number of cups: "))-1
cups_arr = shuffle_cup(num_cups(cups))
index = int(cups_arr.index('O')+1)
#print("index", index)
choice = int(user_guess(cups))
#print("user", choice)

limit=3
count=0
while choice!=index:
    if abs(index - choice)<=2 and limit>0:
        print("Very Close!")
        limit -= 1
        print(f"{limit} attempts remaining before the cups shuffle.")
        choice = choice = int(user_guess(cups))
    elif abs(index - choice)>=2 and limit>0:
        print("Not Close!")
        limit -= 1
        print(f"{limit} attempts remaining before the cups shuffle.")
        choice = choice = int(user_guess(cups))
    elif limit==0:
        cups_arr = shuffle_cup(num_cups(cups))
        print("Oops! Wrong answer, it's been shuffled!")
        index = int(cups_arr.index('O')+1)
        choice = choice = int(user_guess(cups))
        limit=3
    count += 1
    if count%10==0:
        answer = input("Would you like to give up?(y/n) You've already guessed {} times. \n".format(count))
        if answer=='y':
            print("Bye bye loser!")
            quit()
        else:
            print("Sigh.. okay then.")
    

print(cups_arr)
print("Well Done! You found the right cup!")
print("... only took you {} tries.".format(count))
