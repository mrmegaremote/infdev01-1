while True:
    #resetting scores
    score = 0
    ups = 0
    lws = 0
    dig = 0
    non = 0
    pss = raw_input("insert your password here: \n")

    #checking all characters
    for i in range (0, len(pss)):
        if pss[i].isupper():
            ups += 1
        elif pss[i].islower():
            lws += 1
        elif pss[i].isdigit():
            dig += 1
        else:
            non += 2

    #adding character point to score
    score += (ups + lws + dig + non / 2)

    #counting value of length
    if len(pss) <= 6:
        score += 4
    elif len(pss) >= 6 and len(pss) <= 10:
        score += 8
    elif len(pss) > 10:
        score += 10

    #calculation
    if score <= 14:
        print "your password is weak"
    elif score >= 14 and score <= 18:
        print "your password is medium"
    elif score > 18:
        print "your password is strong"
        