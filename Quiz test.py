#Menu
def Display_Menu():
    global ans
    print('1.Math\n2.Science\n3.History\n4.Ramdom Trivia')
    ans = eval(input('Choose one of these subjects.'))
    return

#Math
    
def Math():
    global answer
    global PointsM
    TPoints = 0
    QuestionTF='True or False'
    Question1='3+5=2'
    Question2='15*2=30'
    Question3='59+10=115'
    Question4='5*12=78'
    Question5='2-1=1'
    x = 1
    while x == 1:
        print(Question1)
        print(QuestionTF)
        answer = str.upper(input('Your Answer: '))
        if answer =='True':
            x = 0
        elif answer == 'False':
            x = 1
        while x == 1:
            print(Question2)
            print(QuestionTF)
            answer = str.upper(input('Your Answer:'))
            if answer == 'FALSE':
                x = 0
            elif answer == 'TRUE':
                PointsM = PointsM + 1
                x = 0
        x = 1
        while x == 1:
            print(Question3)
            print(QuestionTF)
            answer = str.upper(input('Your Answer:'))
            if answer == 'TRUE':
                x = 0
            elif answer == 'FALSE':
                PointsM = PointsM + 1
                x = 0
        x = 1
        while x == 1:
            print(Question4)
            print(QuestionTF)
            answer = str.upper(input('Your Answer:'))
            if answer == 'TRUE':
                x = 0
            elif answer == 'FALSE':
                PointsM = PointsM + 1
                x = 0
        x = 1
        while x == 1:
            print(Question5)
            print('True or False?')
            answer = str.upper(input('Your Answer:'))
            if answer == 'FALSE':
                x = 0
            elif answer == 'TRUE':
                PointsM = PointsM + 1
                x = 0
        
            print('Thank You for Taking the Quiz!')
            print('Your Score is', PointsM,'/5')
            return PointsM

#Science

def Science():
    global answer
    global PointsS
    QuestionTF='True or False'
    Question1='Freezing Point of Water in Celsius = 0'
    Question2='The Force needed to Accelerate a Sled (total mass = 65 kg ) at 1.6 m/s2 on Horizontal Frictionless Ice = 101'
    Question3='The Mitochondria is the Powerhouse of the Cell'
    Question4='A human is a reptile'
    Question5='H20 is water'
    PointsS = 0
    x = 1
    while x == 1:
        print(Question1)
        print(QuestionTF)
        answer = str.upper(input('Your Answer:'))
        if answer == 'FALSE':
            PointsS = PointsS + 1
            x = 0
        elif answer == 'TRUE':
            x = 1
        while x == 1:
            print(Question2)
            print(QuestionTF)
            answer = str.upper(input('Your Answer:'))
            if answer == 'FALSE':
                x = 0
            elif answer == 'TRUE':
                PointsS = PointsS + 1
                x = 0
        x = 1
        while x == 1:
            print(Question3)
            print(QuestionTF)
            answer = str.upper(input('Your Answer:'))
            if answer == 'FALSE':
                x = 0
            elif answer == 'TRUE':
                PointsS = PointsS + 1
                x = 0
        x = 1
        while x == 1:
            print(Question4)
            print(QuestionTF)
            answer = str.upper(input('Your Answer:'))
            if answer == 'TRUE':
                x = 0
            elif answer == 'FALSE':
                PointsS = PointsS + 1
                x = 0
        x = 1
        while x == 1:
            print(Question5)
            print(QuestionTF)
            answer = str.upper(input('Your Answer:'))
            if answer == 'FALSE':
                x = 0
            elif answer == 'TRUE':
                PointsS = PointsS + 1
                x = 0
                
            print('Thank You for Taking the Quiz!')
            print('Your Score is', PointsS,'/5')
            return PointsS
#History
    
def History():
    global answer
    global PointsH
    QuestionTF='True or False'
    Question1='The Triangle Shirtwaist Factory of 1911 of crucial in abolishing slavery'
    Question2='The War of 1812 was fought in 1786'
    Question3='On D-Day American troops landed at Utah and Omaha'
    Question4='George Washington was the 85th president of the United States'
    Question5='Henry Ford revolutionized factories by creating the assembly line'
    PointsH = 0
    x = 1
    while x == 1:
        print(Question1)
        print(QuestionTF)
        answer = str.upper(input('Your Answer:'))
        if answer == 'FALSE':
            PointsH = PointsH + 1
            x = 0
        elif answer == 'TRUE':
            x = 1
        while x == 1:
            print(Question2)
            print(QuestionTF)
            answer = str.upper(input('Your Answer:'))
            if answer == 'FALSE':
                x = 0
            elif answer == 'TRUE':
                PointsH = PointsH + 1
                x = 0
        x = 1
        while x == 1:
            print(Question3)
            print(QuestionTF)
            answer = str.upper(input('Your Answer:'))
            if answer == 'FALSE':
                x = 0
            elif answer == 'TRUE':
                PointsH = PointsH + 1
                x = 0
        x = 1
        while x == 1:
            print(Question4)
            print(QuestionTF)
            answer = str.upper(input('Your Answer:'))
            if answer == 'TRUE':
                x = 0
            elif answer == 'FALSE':
                PointsH = PointsH + 1
                x = 0
        x = 1
        while x == 1:
            print(Question5)
            print(QuestionTF)
            answer = str.upper(input('Your Answer:'))
            if answer == 'FALSE':
                x = 0
            elif answer == 'TRUE':
                PointsH = PointsH + 1
                x = 0
                
            print('Thank You for Taking the Quiz!')
            print('Your Score is', PointsH,'/5')
            return PointsH


#Trivia
        
def RandomTrivia():
    global answer
    global PointsT
    QuestionTF='True or False'
    Question1='The Author of the book Persepolis is Marjane Satrapi'
    Question2='The 1969 Ford Mustang Mach 1 428 Super Cobra Jet was designed alongside Shelby America'
    Question3='Cody Ko is a famous surpreme court justice'
    Question4='The alphabet has 10 letters'
    Question5='Famous song Hey Julie! is a collab between rapper KYLE and Lil Yachty'
    PointsT = 0
    x = 1
    while x == 1:
        print(Question1)
        print(QuestionTF)
        answer = str.upper(input('Your Answer:'))
        if answer == 'FALSE':
            PointsT = PointsT + 1
            x = 0
        elif answer == 'TRUE':
            x = 1
        while x == 1:
            print(Question2)
            print(QuestionTF)
            answer = str.upper(input('Your Answer:'))
            if answer == 'FALSE':
                x = 0
            elif answer == 'TRUE':
                PointsT = PointsT + 1
                x = 0
        x = 1
        while x == 1:
            print(Question3)
            print(QuestionTF)
            answer = str.upper(input('Your Answer:'))
            if answer == 'TRUE':
                x = 0
            elif answer == 'FALSE':
                PointsT = PointsT + 1
                x = 0
        x = 1
        while x == 1:
            print(Question4)
            print(QuestionTF)
            answer = str.upper(input('Your Answer:'))
            if answer == 'TRUE':
                x = 0
            elif answer == 'FALSE':
                PointsT = PointsT + 1
                x = 0
        x = 1
        while x == 1:
            print(Question5)
            print(QuestionTF)
            answer = str.upper(input('Your Answer:'))
            if answer == 'FALSE':
                x = 0
            elif answer == 'TRUE':
                PointsT = PointsT + 1
                x = 0
                
            print('Thank You for Taking the Quiz!')
            print('Your Score is', PointsT,'/5')
            return PointsT


#Main
Math=0
Science=0
History=0
Trivia=0
response = 'Y'
while response == 'Y':
    x=1
    Display_Menu()
    if ans == 1:
        Math()
    elif ans == 2:
        Science()
    elif ans == 3:
        History()
    elif ans == 4:
        RandomTrivia()
    else:
        print('\nInvalid Input')
    while x == 1:
        response == str.upper(input('\nWould you like to take another quiz? Y or N:'))
        if response == 'Y':
            x=0
        elif response == 'N':
            x=0
        else:
            print('\nInvalid Input')
        if response == 'N':
            output()
            
