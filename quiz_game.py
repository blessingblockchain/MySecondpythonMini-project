print('welcome to my computer quiz!')

playing = input('Do you want to play? ')

if playing != 'yes':
    quit()

print('okay! let play:)')
score = 0

answer = input('what does cpu stand for? ')
if answer == 'central processing unit':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('what does GPU stand for? ')
if answer == 'graphic processing unit':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('what does RAM stand for? ')
if answer == 'random access memory':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('what does  PSU stand for? ')
if answer == 'power supply':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print('You got ' + str(score) + ' questions correct!')
print('You got ' + str((score / 4) * 100) + '%.')