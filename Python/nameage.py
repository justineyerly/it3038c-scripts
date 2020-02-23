import time
start_time = time.time()
print('What is your name?')
myName = input()
while myName != 'Justin':
    if myName == 'Austin':
        print('Ha Ha Ha, very funy. Seriously, who are you?')
        myName = input()
    else:
        print('That is not your name. Please, tell me your real name.')
        myName = input()
print('Hello, ' + myName + '. This is a great name. How old are you?')
myAge = int(input())
if myAge < 13:
        print("You are a minor?")
elif myAge == 13:
        print("You're a teenager now ... that's cool, I guess")
elif myAge > 13 and myAge < 30:
        print("You're young and dumb")
elif myAge >= 30 and myAge < 65:
        print("You're adulting.")
else:
        print(".... and you're not dead yet?")
programAge = int(time.time() - start_time)
print('%s? Thats funny, im only %s seconds older.' % (myAge, programAge))