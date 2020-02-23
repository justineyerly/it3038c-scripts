import time
start_time = time.time()
print('What is your name?')
myName = input()
print('Hello, ' + myName + '. This is a great name. How old are you?')
myAge = int(input())
programAge = int(time.time() - start_time)
print('%s? Thats funny, im only %s seconds older.' % (myAge, programAge))