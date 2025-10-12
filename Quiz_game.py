
import random
quiz = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "Who wrote the play 'Romeo and Juliet'?", "answer": "William Shakespeare"},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    {"question": "Who developed the theory of relativity?", "answer": "Albert Einstein"},
    {"question": "Which element has the chemical symbol ‘O’?", "answer": "Oxygen"},
    {"question": "What is the fastest land animal?", "answer": "Cheetah"},
    {"question": "In which year did World War II end?", "answer": "1945"},
    {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "What is the hardest natural substance on Earth?", "answer": "Diamond"},
    {"question": "Which is the smallest continent?", "answer": "Australia"},
    {"question": "How many players are there in a cricket team?", "answer": "11"},
    {"question": "What is the national currency of Japan?", "answer": "Yen"},
    {"question": "Who invented the telephone?", "answer": "Alexander Graham Bell"},
    {"question": "Which organ purifies blood in the human body?", "answer": "Kidney"},
    {"question": "What is the boiling point of water in Celsius?", "answer": "100"},
    {"question": "Who was the first person to walk on the moon?", "answer": "Neil Armstrong"},
    {"question": "What gas do plants release during photosynthesis?", "answer": "Oxygen"},
    {"question": "What is the capital of India?", "answer": "New Delhi"},
    {"question": "Which country is known as the Land of the Rising Sun?", "answer": "Japan"},
    {"question": "What is H2O commonly known as?", "answer": "Water"},
    {"question": "Who is known as the Father of Computers?", "answer": "Charles Babbage"},
    {"question": "What is the chemical symbol for gold?", "answer": "Au"},
    {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
    {"question": "What is the largest mammal in the world?", "answer": "Blue Whale"},
    {"question": "Who discovered gravity?", "answer": "Isaac Newton"},
    {"question": "Which sport uses a shuttlecock?", "answer": "Badminton"},
    {"question": "Which is the longest river in the world?", "answer": "Nile"},
    {"question": "What is the square root of 64?", "answer": "8"},
    {"question": "Who was the first President of the United States?", "answer": "George Washington"},
    {"question": "Which planet is closest to the Sun?", "answer": "Mercury"},
    {"question": "Which is the largest ocean on Earth?", "answer": "Pacific Ocean"},
    {"question": "What is the currency of the United Kingdom?", "answer": "Pound Sterling"},
    {"question": "Which festival is known as the Festival of Lights in India?", "answer": "Diwali"},
    {"question": "What is the chemical formula for salt?", "answer": "NaCl"},
    {"question": "Who invented the light bulb?", "answer": "Thomas Edison"},
    {"question": "Which metal is liquid at room temperature?", "answer": "Mercury"},
    {"question": "What is the largest desert in the world?", "answer": "Sahara Desert"},
    {"question": "How many continents are there on Earth?", "answer": "7"},
    {"question": "Who was the first woman to win a Nobel Prize?", "answer": "Marie Curie"},
    {"question": "What is the process by which plants make their food?", "answer": "Photosynthesis"},
    {"question": "Which is the tallest mountain in the world?", "answer": "Mount Everest"},
    {"question": "What is the largest internal organ in the human body?", "answer": "Liver"},
    {"question": "Which planet has rings around it?", "answer": "Saturn"},
    {"question": "Who is known as the Missile Man of India?", "answer": "Dr. A.P.J. Abdul Kalam"},
    {"question": "What is the national animal of India?", "answer": "Bengal Tiger"},
    {"question": "Which instrument measures atmospheric pressure?", "answer": "Barometer"},
    {"question": "What is the chemical symbol for iron?", "answer": "Fe"},
    {"question": "In which country were the Olympic Games invented?", "answer": "Greece"},
    {"question": "Which planet is known as the Morning Star?", "answer": "Venus"},
    {"question": "Which organ in the human body is responsible for pumping blood?", "answer": "Heart"},
    {"question": "Which is the largest bone in the human body?", "answer": "Femur"}
]
print("Welcome to Quiz Game ")
while True:
    user = input("Do You Want to Play  (yes/no): ").strip().lower()
    if(user == "yes"):
        print("\nOkay Let`s Play :)")
        print("There are total '10' questions \n\n ------------Best of luck------------- \n")
        score = 0
        for _ in range(0,10):
            question = random.choice(quiz)
            print(f"Your question : {question["question"]}")
            answer = input("Enter your answer : ").strip().lower()
            if(answer == question["answer"].strip().lower()):
                score += 1
            print(score)
        print(f"Your final score is {score}/10")
        print(f"Your final score is {(score/10)*100}%")
    else:
        break
    