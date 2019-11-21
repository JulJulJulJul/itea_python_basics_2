from random import randint

total = randint(2,11)
print(total, 'It\'s your first card')
card = randint(2,11)
print(card, 'It\'s your second card')
total = total + card  # score of user's two cards

print('If you want to pick more card, press c. If you want to pas, print pas')
answer = input()  # user need to input valid answer
c = str('c')  # user need to press c if he/she wants to pick one more card
pas = str('pas')  # user need to press pas if he/she wants to quit the game
while answer != c and answer != pas:  # check if user input valid answer
    print('Hey. Smth wrong.If you want to pick more card, press c. If you want to pas, print pas')
    answer = input()
while answer == c:  # if user choose to continue the game he pick one more card
    print('Pick a card')
    new_card = randint(2,11)
    print('Your new card is', new_card)
    total = total + new_card  # user score for this turn
    print('Now your score is ', total)
    if total > 21:
        break
    else:
        print('If you want to pick more card, press c. If you want to pas, print pas')
        answer = input()
        while answer != c and answer != pas:  # check user unswer for case if it is not valid
            print('Hey. Smth wrong.If you want to pick more card, press c. If you want to pas, print pas')
            answer = input()
    
print('Game is over')    
print('Your score is ', total)  
        
user_points = total  # user final score
if user_points > 21:
    print('User lost.User score is ', user_points)  # user loose if his score is more than 21. Bot wins anyway
else:
    bot_card = randint(2,11)  # bot pics first card
    bot_total = randint(2,11)  # bot pics second card
    bot_total = bot_total + bot_card  # bot score for this turn
    print('Bot score ', bot_total)

    bot_choise = randint(0,1)  # bot randomly choose to pick one more card or quit the game
    while bot_choise == 1:
        print('Bot picks a card')
        new_card = randint(2,11)
        bot_total = bot_total + new_card  # bot score for this turn
        if bot_total > 21:  # if bot's score is more than 21 user wins
            print('User win')
            break
    print('Game is over. Bot score is ', bot_total)

    if user_points <= bot_total and bot_total < 21:  # check if bot wins
        print('Bot win')
    elif user_points > bot_total:  # check if user wins
        print('User win')
        
