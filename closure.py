# Closure is parent function (nested function lesson of scope )nested function havong acces to scope of parent function
# closure is created when the parent function is retured 


def parent_function(person , coins):
    #coins = 3
    
    def play_game():
        nonlocal coins 
        coins -= 1

        if coins > 1:
            print(" \n " + person + " has " + str (coins) + " coins left." )
        elif coins == 1:
            print(" \n " + person + " has " + str (coins) + " coin left.")
        else:
            print(" \n " + person + " Is out of coins. ")
    return play_game

tommy = parent_function("Tommy", 3)
jenny = parent_function("Jemmy", 5)

tommy()
tommy()

jenny()
tommy()

