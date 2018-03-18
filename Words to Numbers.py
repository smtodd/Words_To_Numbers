# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 21:15:35 2018

@author: steve
"""

#%%
def words_to_numbers(word_input):
    """This is a function to convert a number written in words
    to an actual number"""
    
    #Set up data dictionaries
    #these dictionaries are based on the common 3 digit grouping and naming 
    #conventions used in the United States
    min_length={'hundred': 3, 'thousand': 4, 'million': 7, 'billion':10,
                'trillion':13, 'quadrillion':16, 'quintillion':19,
                'sextillion':22, 'septillion':25, 'octillion':28,
                'nonillion':31, 'decillion':34} 

    power_of_ten={'thousand':3, 'million':6, 'billion':9, 'trillion':12,
               'quadrillion':15, 'quintillion':18, 'sextillion':21,
               'septillion':24, 'octillion':27, 'nonillion':30, 'decillion':33}
    
    single_digits={'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6,
               'seven':7, 'eight':8, 'nine':9}
    
    teens_digits={'ten':10, 'eleven':11, 'twelve':12, 'thirteen':13, 
                  'fourteen':14, 'fifteen':15, 'sixteen':16, 'seventeen':17, 
                  'eighteen':18, 'nineteen':19}
    
    ten_numbers={'twenty':20, 'thirty':30, 'forty':40, 'fifty':50, 'sixty':60,
                 'seventy':70, 'eighty':80, 'ninety':90}
    
    #Split the string of words into an array of words so we can work throug them
    word_list = word_input.split()
    
    #Figure out the minimum and maximum number of digits our final number can
    #have
    CurrMinLen = 0
    for word in word_list:
        if word in min_length:
            if CurrMinLen < min_length[word]:
                CurrMinLen = min_length[word]
                CurrMaxLen = CurrMinLen + 2
    #print(CurrMinLen)
    #print(CurrMaxLen)

    #Set initial variables to 0
    NewStart = 0
    threes_group = 0
    basenum = 1
    
    #Loop through the list of words
    for subword in word_list:
        
        #Group words into lists by the three digit groups common in the USA
        if subword in power_of_ten:
            CommaIndex = word_list.index(subword) + 1
            #print(CommaIndex)
            CommaGroup = word_list[NewStart:CommaIndex]
            print(CommaGroup)
            NewStart = CommaIndex
            
            #Loop through the list of words in the three digit group
            for myword in CommaGroup:
                print(myword)
                
                #Is it the defining word of the three digit group 
                if myword in power_of_ten:
                    threes_group = threes_group + power_of_ten[subword]
                    #print(type(threes_group))
                    #print(threes_group)
                #If is is one hundred, we add two digits onto the length
                elif myword == "hundred":
                    threes_group = threes_group + 2
                    print(threes_group)
                elif "hundred" not in CommaGroup and myword in ten_numbers:
                    threes_group = threes_group + 1                   
                elif "hundred" not in CommaGroup and myword in teens_digits:
                    threes_group = threes_group + 1
                    basenum = teens_digits[myword]
                    basenum = basenum / 10
                elif myword in single_digits:   
                    basenum = single_digits[myword]
                    print(basenum)
    print("final threes_group:", int(basenum*(10**threes_group)))
        #print(lengthdigit)