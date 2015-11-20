pointp1 = 0
pointp2 = 0

while True:
    choice = raw_input("rock, paper or scissors for player 1?: ")
    choice2 = raw_input("rock, paper or scissors for player 2?: ")
    choice = choice.lower()
    choice2 = choice2.lower()

    if "rock" in choice:
        if "rock" in choice2:
            print "rock is rock, draw"
        elif "paper" in choice2:
            print "paper wraps rock, player 2 wins"
            pointp2 += 1
        elif "scissors" in choice2:
            print "rock smashes scissors, player 1 wins"
            pointp1 += 1
        elif "Spock" in choice2:
            print "Spock vaporizes rock, player 2 wins"
            pointp2 += 1
        elif "lizard" in choice2:
            print "rock smashes lizard, player 1 wins"
            pointp1 += 1
        else:
            continue
    
    elif "paper" in choice:
        if "rock" in choice2:
            print "paper wraps rock, player 1 wins"
            pointp1 += 1
        elif "scissors" in choice2:
            print "scissors cut paper, player 2 wins"
            pointp2 += 1
        elif "paper" in choice2:
            print "paper is paper, draw"
        elif "Spock" in choice2:
            print "paper disproves Spock, player 1 wins"
            pointp1 += 1
        elif "lizard" in choice2:
            print "lizard eats paper, player 2 wins"
            pointp2 += 1
        else:
            continue
    
    elif "scissors" in choice:
        if "scissors" in choice2:
            print "scissors are scissors, draw"
        elif "rock" in choice2:
            print "rock smashes scissors, player 2 wins"
            pointp2 += 1
        elif "paper" in choice2:
            print "scissors cut paper, player 1 wins"
            pointp1 += 1
        elif "Spock" in choice2:
            print "Spock smashes scissors, player 2 wins"
            pointp2 += 1
        elif "lizard" in choice2:
            print "scissors decapitate lizard, player 1 wins"
            pointp1 += 1
        else:
            continue

    elif "Spock" in choice:
        if "scissors" in choice2:
            print "Spock smashes scissors, player 1 wins"
            pointp1 += 1
        elif "rock" in choice2:
            print "Spock vaporizes rock, player 1 wins"
            pointp1 += 1
        elif "paper" in choice2:
            print "paper disproves Spock, player 2 wins"
            pointp2 += 1
        elif "Spock" in choice2:
            print "Spock is Spock, draw"
        elif "lizard" in choice2:
            print "lizard poisons Spock, player 2 wins"
            pointp2 += 1
        else:
            continue

    elif "lizard" in choice:
        if "scissors" in choice2:
            print "scissors decapitate lizard, player 2 wins"
            pointp2 += 1
        elif "rock" in choice2:
            print "rock crushes lizard, player 2 wins"
            pointp2 += 1
        elif "paper" in choice2:
            print "lizard eats paper, player 1 wins"
            pointp1 += 1
        elif "Spock" in choice2:
            print "lizard poisons Spock, player 1 wins"
            pointp1 += 1
        elif "lizard" in choice2:
            print "lizard is lizard, draw"
        else:
            continue
    else:
        print "either '%s' or '%s' was a wrong input" % (choice, choice2) 
    print "player 1 has %s points and player 2 has %s points" % (pointp1, pointp2)