#All numbers below 100 are bouncy
counter = 100

#Make sure the proportion is below 100
proportion_is_valid = False
while proportion_is_valid == False:
    proportion = int(input('Proportion of bouncy numbers (%): '))
    if proportion >= 100:
        print('Please enter a number below 100')
    else:
        proportion_is_valid = True

def isBouncy(x):
    lst = []
    for i in str(x):
        lst.append(int(i))
    a = sorted(lst)
    if a == lst:
        return False
    elif lst == list(reversed(a)):
        return False
    else:
        return True

#initialize counters
bounce = 0
nonbounce = 0
testing = True

#Iterate through natural number until desired number is reached
while testing == True:
    counter += 1
    if isBouncy(counter) == True:
        bounce += 1
    if bounce/counter == proportion/100:
        testing  = False

print(str(proportion) +  '% of numbers below ' + str(counter) + ' are bouncy')
