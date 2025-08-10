while True:
    print("MAIN MENU")
    print("---- ----")
    print("1. Math Module \n2. Games Module\n3. Exit")
    a = int(input("\nEnter the Choice: "))
    print("\t")
    if a == 1:
        while True:
            print("MATHS MENU")
            print("---- ----")
            print("""1.1) Average of the numbers\n1.2) Temperature Conversion\n1.3) BMI Calculation\n1.4) Statistical Calculation\n1.5) Human Development Index Calculation""")
            b = float(input("\nEnter the Choice: "))
            
            if b == 1.1:
                Calculate_Again = "yes"
                while Calculate_Again == "yes" or Calculate_Again == "y":
                    # Code for Average Calculation
                    numbers = eval(input("Enter the list of numbers separated by space: "))
                    avg = sum(numbers) / len(numbers)
                    print("The average of numbers is", avg)
                    Calculate_Again = input("Want to Calculate Again? (yes/no): ")
                print("To go back to MAIN MENU Enter A\nTo go back to MATHS MENU Enter B")
                back=input("Enter the Choice:")
                if back.lower() == 'a':
                    break
            elif b == 1.2:
                Calculate_Again = "yes"
                while Calculate_Again == "yes" or Calculate_Again == "y":
                    # Code for Temperature Conversion
                    print("To convert Temperature from Celsius to Fahrenheit Enter 1 \nTo convert Temperature from Fahrenheit to Celsius Enter 2")
                    c=int(input("\nEnter the Choice"))
                    if c==1:
                        c=float(input("Enter the Temperature in Celsius"))
                        f=c*9/5+32
                        print("The Temperature in Fahrenheit is",f)
                    elif c==2:
                        f=float(input("Enter the Temperature in Fahrenheit"))
                        c=f-32*5/9
                        print("The Temperature in Celsius is",c)
                    Calculate_Again = input("Want to Calculate Again? (yes/no): ")
                print("To go back to MAIN MENU Enter A\nTo go back to MATHS MENU Enter B")
                back=input("Enter the Choice:")
                if back.lower() == 'a':
                    break
            elif b == 1.3:
                Calculate_Again = "yes"
                while Calculate_Again == "yes" or Calculate_Again == "y":
                    # Code for BMI Calculation
                    print("\t")
                    h=float(input("Enter your height in metre"))
                    m=float(input("Enter your mass in kilogram"))
                    bmi=m/h**2
                    print("Your BMI is",bmi)
                    if bmi<20:
                        print("You are undernourished,Eat more :(")
                    elif 20<bmi<25:
                        print("You are normal :)")
                    else:
                        print("You are overweight,You should loose your weight :(")
                    Calculate_Again = input("Want to Calculate Again? (yes/no): ")
                print("To go back to MAIN MENU Enter A\nTo go back to MATHS MENU Enter B")
                back=input("Enter the Choice:")
                if back.lower() == 'a':
                    break
            elif b == 1.4:
                Calculate_Again = "yes"
                while Calculate_Again == "yes" or Calculate_Again == "y":
                    # Code for Statistical Calculation
                    print("\t")
                    seq=eval(input("Enter the list of values"))
                    import statistics
                    print("Mean=",statistics.mean(seq))
                    print("median=",statistics.median(seq))
                    print("Mode=",statistics.mode(seq))
                    Calculate_Again = input("Want to Calculate Again? (yes/no): ")
                print("To go back to MAIN MENU Enter A\nTo go back to MATHS MENU Enter B")
                back=input("Enter the Choice:")
                if back.lower() == 'a':
                    break
            elif b == 1.5:
                Calculate_Again = "yes"
                while Calculate_Again == "yes" or Calculate_Again == "y":
                    # Code for Human Development Index Calculation
                    print("\t")
                    print("All values to be under 0.00 to 1.00")
                    Life_Expectancy=float(input("Enter the value of Life Expectancy"))
                    Education_Index=float(input("Enter the value of Education Index"))
                    Income_Index=float(input("Enter the value of Income Index"))
                    HDI=Life_Expectancy* Education_Index*Income_Index
                    print("The calculated Human Development Index is",HDI)            
                    Calculate_Again = input("Want to Calculate Again? (yes/no): ")
                print("To go back to MAIN MENU Enter A\nTo go back to MATHS MENU Enter B")
                back=input("Enter the Choice:")
                if back.lower() == 'a':
                    break
            else:
                print("Enter the Correct Choice\nHeading Back to Maths Menu")
    elif a == 2:
        while True:
            print("GAMES MENU")
            print("----- ----")
            print("2.1) Guess the Word\n2.2) Quiz\n2.3) Guess the Number\n2.4) Rock Paper Scissors\n2.5) Escape the Room")
            b = float(input("\nEnter the Choice: "))
            
            if b == 2.1:
                # Code for Guess the Word
                Play_Again="yes"
                while Play_Again=="yes" or Play_Again=="y":
                    import random
                    
                    word=random.choice(["Zipper","Xylophone","Whizzing","Vapourisation","Syndrome","Rhythm","Buzzing","Dictionaries","Oak"]).lower()
                    Guessed="_"*len(word)
                    attempts=6
                    while attempts > 0 and "_" in Guessed:
                        print(Guessed)
                        letter=input("Guess the letter")
                        if letter in word:
                            new_Guessed=""
                            for i in range(len(word)):
                                if word[i]==letter:
                                    new_Guessed += letter
                                else:
                                    new_Guessed += Guessed[i]
                            Guessed=new_Guessed
                        else:
                            attempts-=1
                            print("Incorrect! Attempts left:",attempts)
                    if "_" not in Guessed:
                        print("Congratulations! You guessed the word:",word)
                    else:
                        print("Out of attempts! The word was:",word)
                    Play_Again=input("Want to Play Again?")
                print("To go back to MAIN MENU Enter A\nTo go back to GAMES MENU Enter B")
                back=input("Enter the Choice:")
                if back.lower() == 'a':
                    break
            elif b == 2.2:
                # Code for Quiz
                print("\t")
                print('Welcome to GK Quiz')
                print("All answers to be answered in True or False as an Abbreviation use t or f")
                answer=input('Are you ready to play the Quiz ? (yes/no) :')
                score=0
                attempts=0
                total_questions=5
                         
                if answer.lower()=='yes':
                    answer=input('Question 1: Blue eyes are newer to human race than pottery?')
                    if answer.lower()=='t':
                        score += 1
                        attempts += 1
                        print('correct')
                    elif answer.lower()=='f':
                        attempts += 1
                        print('Wrong Answer :(')
                    else:
                        print('Not Attempted')
                         
                    answer=input('Question 2: Trees existed before sharks? ')
                    if answer.lower()=='f':
                        score += 1
                        attempts += 1
                        print('correct')
                    elif answer.lower()=='t':
                        attempts += 1
                        print('Wrong Answer :(')
                    else:
                        print('Not Attempted')
                    
                    answer=input('Question 3: There are 14 bones in a human foot?')
                    if answer.lower()=='f':
                        score += 1
                        attempts += 1
                        print('correct')
                    elif answer.lower()=='t':
                        attempts += 1
                        print('Wrong Answer :(')
                    else:
                        print('Not Attempted')
                    answer=input('Question 4: Matches were invented before lighters?')
                    if answer.lower()=='f':
                        attempts += 1
                        score += 1
                        print('correct')
                    elif answer.lower()=='t':
                        attempts += 1
                        print('Wrong Answer :(')
                    else:
                        print('Not Attempted')
                    

                    answer=input('Question 5: The population of California is larger than the entire population of Canada?')
                    if answer.lower()=='t':
                        score += 1
                        attempts += 1
                        print('correct')
                    elif answer.lower()=='f':
                        print('Wrong Answer :(')
                    else:
                        print('Not Attempted')
                    print('Thankyou for Playing this small quiz game, you attempted',attempts,"questions out of ",total_questions)
                    mark=(score/total_questions)*100
                    print('Marks obtained:',mark)
                                    
                print("To go back to MAIN MENU Enter A\nTo go back to GAMES MENU Enter B")
                back=input("Enter the Choice:")
                if back.lower() == 'a':
                    break
            elif b == 2.3:
                # Code for Guess the Number
                import random
                
                print("\t")
                Play_Again="yes"
                while Play_Again=="yes" or Play_Again=="y":
                    n = random.randrange(1,10)
                    guess = int(input("Enter the Number: "))
                    while n!= guess:
                        if guess < n:
                            print("Too low")
                            guess = int(input("Enter the Number: "))

                        elif guess > n:
                            print("Too high!")
                            guess = int(input("Enter the Number: "))
                    else:
                        print("you guessed it right!!")
                        Play_Again = input("Want to Play Again")
                print("To go back to MAIN MENU Enter A\nTo go back to GAMES MENU Enter B")
                back=input("Enter the Choice:")
                if back.lower() == 'a':
                    break
            elif b == 2.4:
                # Code for Rock Paper Scissors
                import random
                Play_Again="yes"
                while Play_Again=="yes" or Play_Again=="y":
                    print("\t")
                    player1 = input("Select Rock, Paper, or Scissor :").lower()
                    player2 = random.choice(["Rock", "Paper", "Scissor"]).lower()
                    print("Bot selected: ", player2)
                    
                    if player1 == "rock" and player2 == "paper":
                        print("Bot Won")
                    elif player1 == "paper" and player2 == "scissor":
                        print("Bot Won")
                    elif player1 == "scissor" and player2 == "rock":
                        print("Bot Won")
                    

                    elif player1 == player2:
                        print("Tie")
                    else:
                        print("You Won")
                    Play_Again=input("Want to Play Again")
                print("To go back to MAIN MENU Enter A\nTo go back to GAMES MENU Enter B")
                back=input("Enter the Choice:")
                if back.lower() == 'a':
                    break
            elif b == 2.5:
                # Code for Escape the Room
                print("\t")
                print("Welcome to Escape the Room")
                print("You find yourself in a dark room.")
                print("There are two doors in front of you. Which one do you choose? (1 or 2)")
                choice = input("> ")
                if choice == "1":
                    print("You entered room one.")
                    print("There is a table with a key on it.")
                    print("Do you take the key? (yes/no)")
                    
                    choice = input("> ")
                    
                    if choice.lower() == "yes":
                        print("You took the key and move to the next room.")
                        print("You entered room two.")
                        print("There's a locked door in front of you.")
                        print("Use the key? (yes/no)")
                        
                        choice = input("> ")
                        if choice.lower() == "yes":
                            print("You unlocked the door and escaped! Congratulations!")
                        elif choice.lower() == "no":
                            print("You stay in the room. The end.")
                        else:
                            print("Invalid choice. Game over.")
                    else:
                        print("Invalid choice. Game over.")
                elif choice == "2":
                    print("You entered room two.")
                    print("There's a locked door in front of you.")
                    print("Use the key? (yes/no)")
                    choice = input("> ")
                    if choice.lower() == "yes":
                        print("You unlocked the door and escaped! Congratulations!")
                    elif choice.lower() == "no":
                        print("You stay in the room. The end.")
                    else:
                        print("Invalid choice. Game over.")
                else:
                    print("Invalid choice. Game over.")
                print("To go back to MAIN MENU Enter A\nTo go back to GAMES MENU Enter B")
                back=input("Enter the Choice:")
                if back.lower() == 'a':
                    break
            else:
                print("Enter the Correct Choice\nHeading Back to Games Menu")
    elif a == 3:
        exit()

