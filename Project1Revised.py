#Defining quiz title variables
m_question = 'Math Question Test'
h_question = 'History Question Test'
s_question = 'Science Question Test'
g_question = 'Geography Question Test'

questions = [m_question, h_question, s_question, g_question]

#Developing the quiz topics with questions for user to answer
quiz = {
	
	m_question: [

	("2 + 2 = 4", True),
	("5 x 5 = 20", False),
	("10 / 2 = 5", True),
	("10 + 15 = 25", True),
	("50 - 30 = 30", False)

	],

	h_question: [

	("There were 13 colonies that originally made up the United States of America.", True),
	("The United States Constitution was signed in 1776.", False),
	("The United States Declaration of Independence was created in 1776", True),
	("The Second Amendment is the right to bear arms.", True),
	("The Boston Tea Party occured because the American Colonists hated tea.", False)

	],

	s_question: [

	("The powerhouse of the cell is the Mitochondria.", True),
	("The Sun is known as a yellow dwarf.", True),
	("The 13th element in the Periodic Table is Oxygen.", False),
	("The 1st element in the Periodic Table is Hydrogen.", True),
	("The smallest particle known to mankind is the Atom.", False)

	],

	g_question: [

	("Asia is Earth's largest continent.", True),
	("Australia is the flattest continent.", True),
	("Columbia is the largest country in South America.", False),
	("There are 42 countries in Africa.", False),
	("The captial of Costa Rica is Buernos Aires.", False)

	]
}
#Variable to keep track of how many Correct and Incorrect answers are submitted
result = {"Correct": 0, "Incorrect": 0}

#while loop to ask the user which quiz they would like to take
def quiz_option():
	while True:
		try:
			quiz_num = int(input('Please select the quiz you would like to take:\n1 for {}\n2 for {}\n3 for {}\n4 for {}\nYour Choice: '.format(m_question, h_question, s_question, g_question)))
#Setting up exceptions incase user enters something not expected
		except ValueError:
			print("Your input is not a number, please try again!\n")

		else:
			if 0 >= quiz_num or quiz_num > len(quiz):
				print("Invalid value, please re-enter your option\n")

			else:
				return quiz_num
#while loop to provide questions to user
def get_ans(question, correct_ans):
	while True:
		try:
			print('Question: {}'.format(question))
			ans = int(input("Please type:\n1 for True\n0 for False.\nYour Given Answer: "))
#Exceptions to catch something not expected
		except ValueError:
			print("That is not a number, please try again\n")

		else:
			if ans is not 0 and ans is not 1:
				print("That is an invalid value, please try again\n")
#Function to keep running tab of both Correct and Incorrect answers
			elif bool(ans) is correct_ans:
				result["Correct"] += 1
				return 'Correct'
			else:
				result["Incorrect"] +=1
				return 'Incorrect'

option = quiz_option()
quiz_name = questions[option - 1]

print("\nYou chose to take the {}\n".format(quiz_name))

quiz_q = quiz[quiz_name]
#Shows what answer you chose and whether it is right or wrong
for a in (quiz_q):
	print("Your answer is: {}\n".format(str(get_ans(a[0], a[1]))))
#Prints out your correct and incorrect number of answers
print("\nYou have completed the test with the score of:\nCorrect: " + str(result["Correct"]) + "\nIncorrect: " + str(result["Incorrect"]))

