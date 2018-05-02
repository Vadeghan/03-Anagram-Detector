################################################################################
# Dylan Carpinelli, 2017-11-09                                                 #
# Challenge #3 - Anagram Detector:                                             #
#     Compares two user-specified strings, checking if they are an anagram.    #
#     Extension: Compares integers.                                            #
#                                                                              #
# Hey, look! I actually coded it as a function this time! Are you proud I      #
# followed the rules?                                                          #
#                                                                              #
# Anyway, to quote a great IT man, "overkill is underrated." This not only     #
# does single words, but entire phrases, punctuation and all. Plus, it does    #
# the extension challenge and compares integers, too! Maybe weak dynamic       #
# typing isn't so bad after all... Hmmm... Nah.                                #
#                                                                              #
# It strips each string of any non-alphanumeric characters, sets them to       #
# lowercase, sorts them alphabetically/numerically, and then compares them.    #
# It simply prints 'True' or 'False', as per request of the README. :)         #
#                                                                              #
# Relevant xkcd(s): https://xkcd.com/208/, https://xkcd.com/1171/              #
################################################################################

import re

def is_anagram(s1, s2):
    s1 = re.sub('[^a-z0-9]', '', ''.join(sorted(s1)).lower())
    s2 = re.sub('[^a-z0-9]', '', ''.join(sorted(s2)).lower())
    print(s1 == s2)

is_anagram(input('Enter a string: '), input('Enter a second string: '))

