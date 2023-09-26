import sys
#welcome message with username
def welcome():
    print('Welcome to Mini Geography Game.')
    name = input('Please enter your name: ')
    print(f'Hello {name}!')

#ask user if they want to enter the game with yes/no/error handler   
    while True:
        play_game = input("Do you want to play Geography Game today? Please enter yes or no").lower()
        if play_game == 'no':
            print("See you next time!")
            sys.exit()
        elif play_game == 'yes':
            print("Let's go")
            break
        else:
            print("Invalid input. Please enter yes or no only.")
    return name

#define if correct answer, count 1, else count 0
def question_answer(question,correct_answer,more_info = ""):
    print(question)
    user_answer = input("Please enter your answer: ").strip().lower()
    print(user_answer)

    if user_answer in map(str.lower, correct_answer):
        print(f"That's correct! {more_info}")
        return 1
    else:
        print(f"Sorry that is not the right answer. {more_info}")
        return 0

if __name__ == "__main__":
    name = welcome()
    score = 0

#create list of question, correct answer and more info 
    question_list = [
        ("Q1: How many oceans are there on Earth? Please enter the number.",["4","5","four","five"], "There are four oceans on Earth: the Atlantic, Pacific, Indian, and Arctic. However Southern Ocean which surrounds Antarctica, is considered the newst and fifth ocean."),
        ("Q2: How many continents are there on Earth?",["7","seven"], "The continents are, from largest to smallest: Asia, Africa, North America, South America, Antarctica, Europe, and Australia (or Oceania)"),
        ("Q3: What is the total number of recognized countries in the world today?", ["195"], "There are 195 countries in the world today. This total comprises 193 countries that are member states of the United Nations and 2 countries that are non-member observer states: the Holy See and the State of Palestine."),
        ("Q4: What is the largest country in the world by land area?", ["Russia"],""),
        ("Q5: What is the smallest country in the world by land area?", ["Vatican City","Holy See"],"The smallest country in the world by land area is Vatican City or Holy See."),
        ("Q6: Which country has the highest number of time zones?", ["Russia"], "Russia compasses 11 time zones in total."),
        ("Q7: Which ocean is located between Europe and North America?", ["Atlantic Ocean","Atlantic"], "Atlantic Ocean is the second largest Ocean in the world. It also separates South America and Africa"),
        ("Q8: How many countries make up the UK?",["4","four"],"Those countries are England, Scotland, Wales and Northern Ireland."),
        ("Q9: How many states are there in the US?",["50","fifty"],"There're 50 States and the District of Columbia."),
        ("Q10: Which country is known as the Land of a Thousand Lakes?",["Finland"],"Finland has over 188,000 lakes")
        ]
#checking user_answer matches correct_answer in the question_list:
    for question, answer, more_info in question_list:
        score += question_answer(question,answer,more_info)
#calculate the final score
total_questions = len(question_list)
score_percentage = score / total_questions * 100 if score >0 else 0

#print final result

print(f'Thank you for playing with us, {name}.')
print(f"Your total score is {str(score)} which is {str(score_percentage)} %.")