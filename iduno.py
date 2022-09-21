human_turn = input('input human turn:')
computer_turn = input('input computer turns:')

if human_turn == computer_turn:
 print('DRAW')
elif human_turn == 'rock' and computer_turn == 'scissors' :
 print('human wins!')
elif human_turn == 'paper' and computer_turn == 'rock' :
 print('human wins!')
elif human_turn == 'scissors' and computer_turn == 'paper' :
 print('human wins!')
else:
 print("computer wins!")
