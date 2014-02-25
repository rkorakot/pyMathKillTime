#!/usr/bin/python
# """
# ====================
# Simple Math Practice
# ====================
# Programmed By: Korakot Rakhuang 
# Purpose: for practice the Python2 skill.
# Features: 
#   1. Determine number of questions.
#   2. Determine math symbols. (+, -)
#   3. Generate question by random number and symbols.
#   4. Check answer.
#   5. Summary score.
#   6. Report Score.
# Version: beta1
# """

import sys
import os
import random

# clear screen function
def funcClearScreen():
    # print "\n" * 50
    os.system("clear")
# ========================================

# bye-bye function
def funcByeBye():
    print "\n\nBye-Bye!" # say good bye
    sys.exit() # and exit program
# ========================================

# function check input number only
def funcIntInput(msgs):
    while True:
        try:
            i_input = int(raw_input(msgs))
            break
        except ValueError:
            print "\tOops! That was no valid number. Try again..."
    return i_input
# ========================================

# function check input y or n only
def funcChrInput(msgs):
    while True:
        try:
            c_input = raw_input(msgs)[0].lower()
            if c_input in ['y','n']:
                break
            else:
                print "\tOpps! Please answer y or n again..."
        except ValueError:
            print "\tOops! That was no valid char. Try again..."
    return c_input
# ========================================

# function for get answer then pass to funcAnswerCal
def funcAnsInput(msgs, n1, n2, symb):
    try:
        intAnswer = int(raw_input(msgs))
        return funcAnsCal(n1, n2, symb, intAnswer)
    except ValueError:
        return False
# ========================================

# cal function
def funcAnsCal(n1, n2, symb, ans):
    if symb == "+":
        if n1 + n2 == ans:
            return True
        else:
            return False
    elif symb == "-":
        if n1 - n2 == ans:
            return True
        else:
            return False
# ========================================
# main function
def main():
    funcClearScreen() # Clear screen

    print "Are you raedy for burn your brain?"
    print "(Press Ctrl-c to quit program.)"
    print
    print "Practice Settings"
    print "================="
    setQuestions = funcIntInput("Questions: ") # got number of questions
    setAddition = funcChrInput("Addition(y/n): ") # need '+' y/n?
    setSubtraction = funcChrInput("Subtraction(y/n): ") # need '-' y/n?

    lstMathSymbols = [] # create empty list for keep symbols
    if setAddition == 'y':
        lstMathSymbols.append('+') # if Addition = y add '+' into list
    if setSubtraction == 'y':
        lstMathSymbols.append('-') # if Subtraction = y add '-' into list

    if len(lstMathSymbols) > 0:
        cntCorrect = 0 # count correct answers
        for i in range(1, setQuestions+1):
            randSymbol = random.choice(lstMathSymbols) # random symbol
            randNum2 = random.randint(0,30)
            if randSymbol == "-":
                randNum1 = random.randint(randNum2, randNum2+30)
            else:
                randNum1 = random.randint(0,30)
            msgQ = "Q%i\t: %i %s %i = " % (i,randNum1,randSymbol,randNum2)
            answer = funcAnsInput(msgQ, randNum1, randNum2, randSymbol)
            # print answer
            if answer == True:
                cntCorrect += 1
                print "Correct"
            else:
                print "Incorrect\a"
        print
        print "Finish, Your score is %i/%i" % (cntCorrect, setQuestions)
    else:
        print "You do not define math symbols."
        print "Come back when you ready."
        funcByeBye()
# ========================================

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        funcByeBye()
