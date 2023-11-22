
#coins = [1, 2, 3, 4]
#coins = [5, 7, 1, 1, 2, 3, 22]
#coins = [1, 1, 1, 1, 1]
coins = [1, 2, 5]

change = []

def calc(index, total):

    if index == len(coins):
        change.append(total)
        print("-------------")
        print(total)
        return
  
    new_total = total + coins[index]
    print(index, coins[index], new_total)

    calc(index + 1, new_total)
    #calc(index + 1, total)

calc(0, 0)
print(change)
