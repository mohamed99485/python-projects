def fizz_buzz(num):
    if (num % 3 == 0):
        print("Fizz")
    elif (num % 5 == 0):
        print ("Buzz")
    elif (num % 3 and num % 5):
        print ("Fizz Buzz")
    else:
        print ("not fizz or buzz")

fizz_buzz(3)
fizz_buzz(5)
fizz_buzz(15)
fizz_buzz(4)