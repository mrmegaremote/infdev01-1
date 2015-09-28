pointp1 = 0
pointp2 = 0

while True:
    choice = raw_input("rock, paper or scissors for player 1?: ").lower()
    choice2 = raw_input("rock, paper or scissors for player 2?: ").lower()

    

    if "rock" in choice:
        if "rock" in choice2:
            print "rock is rock, draw"
        elif "paper" in choice2:
            print "paper wraps rock, player 2 wins"
            pointp2 += 1
        elif "scissors" in choice2:
            print "rock smashes scissors, player 1 wins"
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
        else:
            continue
    else:
        print "either '%s' or '%s' was a wrong input" % (choice, choice2) 

    print "player 1 has %s points and player 2 has %s points" % (pointp1, pointp2)