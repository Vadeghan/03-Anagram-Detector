#Made by Marika Colby (12.10)

QueryEnd = "\n  > "

def is_anagram(first, second, strict):
    #Test strictly or non-strictly if the two strings are anagrams
    if strict == "n":
        first = first.lower()
        second = second.lower()
        
    return sorted(str(first)) == sorted(str(second))

def StringInput(question):
    #Take an input of length greater than zero and return it as a string.
    output = str(input(question + QueryEnd))
    while len(output) == 0:
        print("invalid input\n")
        output = str(input(question + QueryEnd))
    return output

def IntegerInput(text):
    #Ask for an integer above one.
    output = input(text + QueryEnd)
    if not IsInteger(output):
        #If the input is not an integer, repeat.
        print(InputError)
        output = PositiveIntegerInput(text)
        #If the integer is too low, repeat.
    elif int(output) <= 1:
        print(InputError)
        output = PositiveIntegerInput(text)
    #Return the input string as an integer.
    return int(output)

def IsInteger(test):
    #Test to see if the input is an integer.
    try:
        int(test)
        return True
    except:
        return False

#Accept one input from a specified list of inputs.
def CustomInput(question, inputs):
    extension = " ("
    #Display available options as specified, but accept upper and lower case inputs.
    for index, item in enumerate(inputs):
        extension += item + "/"
        inputs[index] = inputs[index].lower()
    #Replace the final '/' of the extension with ')'.
    extension = extension[0:-1] + ")"
        
    output = str(input(question + extension + QueryEnd))
    #Continue asking for input until the input is in the specified list.
    while not output.lower() in inputs:
        print("invalid input\n")
        output = str(input(question + extension + QueryEnd))
    return output

#script
while True:

    FirstString = StringInput("\nWhat is the first string?")
    SecondString = StringInput("\nWhat is the Second string?")

    if is_anagram(FirstString, SecondString, "y") and is_anagram(FirstString, SecondString, "n"):
        #If they are anagrams no matter what, just say so.
        print("\n'%s' and '%s' are absolutely anagrams!" % (FirstString, SecondString))

    elif (not is_anagram(FirstString, SecondString, "y")) and (not is_anagram(FirstString, SecondString, "n")):
        #If they are not anagrams no matter what, just say so.
        print("\n'%s' and '%s' are absolutely not anagrams." % (FirstString, SecondString))

    else:
        #If they could or could no be anagrams, ask for the type of test that should be done on them.
        TestStrictly = CustomInput("\nShould these string be tested strictly?", ["Y","N"])
        #A strict test includes capital letters, a non-scrict test makes them all lower case.
        if is_anagram(FirstString, SecondString, TestStrictly):
            if TestStrictly == "y":
                print("\n'%s' and '%s' are anagrams!" % (FirstString, SecondString))
            else:
                print("\n'%s' and '%s' (ignoring capitalisation) are anagrams!" % (FirstString, SecondString,))
        else:
            if TestStrictly == "y":
                print("\n'%s' and '%s' are not anagrams..." % (FirstString, SecondString))
            else:
                print("\n'%s' and '%s' (ignoring capitalisation) are not anagrams!" % (FirstString, SecondString,))
                
    print("\n------------------------------------------------\n")
