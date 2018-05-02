string_1 = input("Enter first phrase: ") #Taking two phrases from the user
string_2 = input("Enter second phrase: ")

def anogram_check(string_1,string_2):
    no_punc_str1 = string_1.lower() #creating variables with lower cased phrase inside
    no_punc_str2 = string_2.lower()
    for i in (""".,?!'":;-–—(){}[] """): #removing punctutation from new variables
        no_punc_str1 = no_punc_str1.replace(i, "")
        no_punc_str2 = no_punc_str2.replace(i,"")
    for i in no_punc_str1: #for statements goes through each letter in first phrase
        if i in no_punc_str2: #if letter is in first phrase and second phrase
            no_punc_str2 = no_punc_str2.replace(i,"",1)#delete first instance of letter in both phrases
            no_punc_str1 = no_punc_str1.replace(i,"",1)
        #print(no_punc_str1, end = " ") checking everything is working
        #print(no_punc_str2)
    if no_punc_str1 == no_punc_str2: #if both phrase are equal to each other(they are also equal to nothing)
        print(string_1, 'and', string_2, 'are anograms') #tell user phrases are anograms
    else:
        print(string_1, 'and', string_2, 'are not anograms') #otherwise tell user they are not

anogram_check(string_1,string_2) #run function
        

    
