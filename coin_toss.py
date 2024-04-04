import random

def coin_toss():
    toss = random.random()
    
    if toss < 0.5 :
        return 'Heads'
    else:
        return 'Tails'

for i in range(10):
    print(f"Toss {i+1} : {coin_toss()}")