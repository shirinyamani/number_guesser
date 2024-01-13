import random


def input_validation(user_guess):

    if not user_guess.isdigit(): #str
        print("Invalid input! Please enter number between 0-100")
        return False
    
    user_guess= int(user_guess)
    if user_guess > 100 or user_guess<1:
        print("number not in valid range")
        return False

    return True


def main():
    target = random.randint(1,100)
    total_score = 100
    
    while True:
        user_guess = input("Enter a number between 0-100: ")
        
        if user_guess == "q":
            print('we missed you...')
            break

        if not input_validation(user_guess):
            continue

        user_guess = int(user_guess)
        if user_guess > target:
            print('go Lower')
    
        
        elif user_guess < target:
            print('go Upper')

        else:
           print("you won!, your score is 100!")
           wanna_play = input('wanna play again? "y/n" ')
           if wanna_play == 'y':
                
                user_guess = random.randint(1,100)
                total_score = 100
                continue
           else:
                print('Untill next time!')
                break
    
        total_score -= 1
        total_score= max(total_score, 0) #not show -
        print(f' You total score is {total_score}')


                





if __name__=="__main__":
    main()