from string import *
runes_picked = input("Enter the runes picked by Hermione ").lower()
word ={'l':0,'u':0,'m':0,'o':0,'s':0}
# what we do:
'''
IITERATION 1:
    1)  make list lower case to avoid case sensitivity 
    2)  check for edge cases and return -1 
    3)  itterate over only the alphabet charecters to find the letter ( L U M O S ) no order specification neccesary 
''' 
def check_spell(runes_picked,word):
    #check for edge cases
    word = word.copy()
    if not runes_picked.isalpha or len(runes_picked) < 5:
        return -1
    else:
        i=0
        for index,rune in enumerate(runes_picked):
            if rune in word:
                if word[rune] == 0:
                    word[rune] +=1
                    i+=1
                if i==5:
                    return index+1
                
        return -1
    return -1
            
print(check_spell(runes_picked,word) )
            
"""
for generic version :
spell = input("enter spell")
word = {ch: 0 for ch in spell}
"""