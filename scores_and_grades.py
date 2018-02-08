def scoresGrades():
    print "Scores and Grades"
    newArr = []
    import random
    for num in range(10):
        newArr.append(random.randint(60,100))
    # print newArr
    for val in newArr:
        if val < 70:
            print "Score: {}; Your grade is D".format(val)
        elif val < 80:
            print "Score: {}; Your grade is C".format(val)
        elif val < 90:
            print "Score: {}; Your grade is B".format(val)
        else:
            print "Score: {}; Your grade is A".format(val)
    print "End of the program. Bye!"
scoresGrades()