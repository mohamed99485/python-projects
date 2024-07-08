def chat_bot():
    print ("welcome gang!")
    response = input ("what can i help you with?")
    if (response == "calculate\n"):

       func = input("what do you wanna calculate\n")
       num1 = int(input("what's your first number?\n"))
       num2 = int(input("what's your second number?\n"))

       if (func == "add"):
        result == num1 + num2
       elif (func == "mult"):
        result == num1 * num2
       elif (func == "div"):
        result == num1 / num2
       elif (func == "sub"):
        result == num1 - num2
       elif (func == "power"):
        result == num1 ** num2

  
       print("your result is ",result)

chat_bot()