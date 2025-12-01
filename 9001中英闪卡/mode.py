import csv
import time
import random

def countdown():
    print("\nAre you ready?")
    time.sleep(1)
    for i in range(3, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    print("Go!\n")
def english_to_chinese(score):
    print("You selected: English to Chinese mode")
    print("\n" + "="*50)
    print("📝 Game Rules:")
    print("• Choose the correct Chinese translation")
    print("• Four options will be provided")
    print("• Select the letter of your answer (A/B/C/D)")
    print("="*50)
    countdown()
    questions = []
    with open('E-C Sport.csv','r',encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            questions.append(row)
    
    selected = random.sample(questions, 5)
    score = 0
    for i,q in enumerate(selected,1):
        print(f"Q{i}: {q['question']}")
        print(f"A.{q['A']}")
        print(f"B.{q['B']}")
        print(f"C.{q['C']}")
        print(f"D.{q['D']}")
        while True:
            answer = input("Your answer (A/B/C/D): ").strip().upper()
            if answer == q['answer']:
                print("Correct!\n")
                score += 1
                break
            elif answer not in ['A','B','C','D']:
                print("Invalid input! Please enter a valid option (A/B/C/D).")
                time.sleep(0.5)
            else:
                print(f"Wrong! The correct answer is {q['answer']}.\n")
                break
            time.sleep(0.5)
        time.sleep(0.5)
    if score == 5:
        print(f"Game finished! Your score: {score}/5")
        print("="*50)
        print("🎉 Congratulations! You got a perfect score!")
        print("="*50)
    elif 3<= score <=4:
        print(f"Game finished! Your score: {score}/5")
        print("="*50)
        print("👍 You got a good score!")
        print("="*50)
    elif 1<=score<3:
        print(f"Game finished! Your score: {score}/5")
        print("="*50)
        print("✊ You need to practice more!")
        print("="*50)
    elif score == 0:
        print(f"Game finished! Your score: {score}/5")
        print("="*50)
        print("😱 W*F are you doing!")
        print("="*50)
    return score
def chinese_to_english(score):
    print("You selected: Chinese to English mode")
    print("\n" + "="*50)
    print("📝 Game Rules:")
    print("• Choose the correct English translation")
    print("• Four options will be provided")
    print("• Select the letter of your answer (A/B/C/D)")
    print("="*50)
    countdown()
    
    questions = []
    with open('C-E Sport.csv','r',encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            questions.append(row)
    
    selected = random.sample(questions, 5)
    score = 0
    for idx, q in enumerate(selected, 1):
        print(f"📖Q{idx}: {q['question(characters+phonetic)']}📖")
        print(f"A. {q['A']}")
        print(f"B. {q['B']}")
        print(f"C. {q['C']}")
        print(f"D. {q['D']}")
        
        while True :
            answer = input("Your answer (A/B/C/D): ").strip().upper()
            if answer == q['answer']:
                print("Correct!\n")
                score += 1
                break
            elif answer not in ['A','B','C','D']:
                print("Invalid input! Please enter a valid option (A/B/C/D).")
                time.sleep(0.5)
            else:
                print(f"Wrong! The correct answer is {q['answer']}.\n")
                break
            time.sleep(0.5)
        time.sleep(0.5)
    if score == 5:
        print(f"Game finished! Your score: {score}/5")
        print("="*50)
        print("🎉 Congratulations! You got a perfect score!")
        print("="*50)
    elif 3<= score <=4:
        print(f"Game finished! Your score: {score}/5")
        print("="*50)
        print("👍 You got a good score!")
        print("="*50)
    elif 1<=score<3:
        print(f"Game finished! Your score: {score}/5")
        print("="*50)
        print("✊ You need to practice more!")
        print("="*50)
    elif score == 0:
        print(f"Game finished! Your score: {score}/5")
        print("="*50)
        print("😱 W*F are you doing!")
        print("="*50)
    return score
if __name__ == "__main__":
    # chinese_to_english()
    english_to_chinese(10)