#a generic nim player
import random

#creates random board with between 1 and 4 tokens in each bucket
def initialize_nim(number_of_buckets):
    return [random.randint(1,4) for bucket in range(number_of_buckets)]

#plays a nim move given a set of nim buckets
#returns whether the move could be made
def play_nim(buckets, player):
    #withdraw a certain number, if possible
    bucket_no, amount = player(buckets)
    if buckets[bucket_no] < amount: 
        return False
    buckets[bucket_no] -= amount
    return True

#a dumb nim algorithm: can you do better?
def dumb_player(buckets):
    bucket_no = 0
    while buckets[bucket_no] == 0:
        bucket_no += 1
    return (bucket_no, 1)

#the main routine
if __name__ == "__main__":
    buckets = initialize_nim(5)
    players = ["Alice", "Bob"]
    can_play = True
    counter = 0
    while can_play:
        raw_input(players[counter % 2] + " to move")
        if not play_nim(buckets, dumb_player):
            print("Bad move, try again!")
        else:
            all_empty = True
            for bucket in buckets:
                if bucket > 0:
                    all_empty = False
                    break
            if all_empty:
                print(players[counter % 2] + " wins!")
                break
            counter += 1
        print(buckets)
    
