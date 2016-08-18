name = raw_input('What is your name?')
print'\n'
print 'Hello '+name+', lets see how big of a Friends fan are you.'
print '\n'

easy_quiz = "__1__ Green finds her dream job at Bloomingdales and later at Polo Ralph Lauren. __2__ Tribiani became a series regular in Days of our lives. __3__ Buffey becomes famous with her new single Smelly Cats. Finally, __4__ Geller and Chandler Bing move out of the city to raise their twins."

medium_quiz = "When __1__ says Rachel’s name at the altar, Emily is heart broken. Everybody is in shock, including Phoebe who was not able to travel to __2__ because she was pregnant with her brother's __3__ .That same night, Monica and __4__ end up sleeping together."

hard_quiz = "The famous Friends apartment is supposedly located in the __1__ in NYC. Chandler decides to quit his job in statistical analysis to become a __2__. When Phoebe gives birth to the triplets, she names the boy __3__ . Monica dates Richard, a man that is __4__ years older than her."

easy_answers = ["Rachel", "Joey", "Phoebe", "Monica"]
medium_answers = ["Ross","London","triplets","Chandler"]
hard_answers = ["West Village", "copywriter", "Frank Jr. Jr.", "21"]

blanks = ["__1__","__2__","__3__","__4__"]

level = raw_input('Please select level of difficulty (easy, medium, hard):')

def difficulty(level):
	'''This function asks the user to choose a level of difficulty (easy, medium or hard). Based on the level chosen, it will return a quiz'''
	if level == 'easy':
		return easy_quiz
	elif level == 'medium':
		return medium_quiz
	elif level == 'hard':
		return hard_quiz
	else:
		print 'Invalid level of difficulty'
		
print '\n'
print difficulty(level) 

print '\n'
print "Fill in the blank the missing word(s) (case sensitive):"
print '\n'



'''This function tells the following functions what level of difficulty the user chose so that they know which answer list to use '''
def answer_set(level):
    if difficulty(level)==easy_quiz:
        return easy_answers
    elif difficulty(level)==medium_quiz:
        return medium_answers
    elif difficulty(level)==hard_quiz:
        return hard_answers
        
'''This function checks if the user's response was correct by comparing the user's input with the answer on the answer list '''         
def answer_correction(response, answers, answer_index): 
     if response==answers[answer_index]:        
         return "Correct"
     else:
     	return "Wrong"        

'''This function is the quiz. It asks the user to fill in the blank. If the user's answer is correct, then it will print Correct, print the prompt with the blank filled, and continue to ask the next blank. If the answer is not correct, it will ask the user to try again. When all blanks are filled, it will say you win, you are a true fan.'''
def fill_blanks():
    chosen_difficulty=difficulty(level)
    answers=answer_set(level)   
    answer_index=0
    blanks_index=0
    while blanks_index<len(blanks):
        response=raw_input("What word goes in " + blanks[blanks_index]+ "?")
        print '\n'
        if answer_correction(response, answers, answer_index)=="Wrong": 
                response=raw_input("Nope! Try again! What word goes in " + blanks[blanks_index] + "?")
        if answer_correction(response, answers, answer_index)=="Correct":
            print "Correct!"
            chosen_difficulty=chosen_difficulty.replace(blanks[blanks_index], response) 
            blanks_index = blanks_index + 1 
            answer_index = answer_index + 1
            
   
	print '\n'
	print chosen_difficulty
	print '\n'
    print "You win!! You are a true Friends Fan!"
            
 
print fill_blanks()

