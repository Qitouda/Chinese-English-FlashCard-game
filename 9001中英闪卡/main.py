
from mode import chinese_to_english,english_to_chinese
from users import User
def set_user():
    print("="*50)
    print(" 🔥🔥🔥 Welcome to the Flashcard Learning Game 🔥🔥🔥 ")
   
    name = input("Please enter your name:")
    user = User(name)
    print("="*50)
    return user

def game_loop():
    user = set_user()
    
    print("="*50)
    print(" 🔥🔥🔥 Flashcard Learning Game 🔥🔥🔥 ")
    print(f"🐼 Welcome back, {user.name}!")
    print(f"Your rank: {user.rank}")
    print(f"Today's playtime: {user.playtimes}")
    print("="*50)
    while True:
        print(user)
        chosen = int(input("<<<|1.Start game|2.Exit game|>>>"))
        if chosen == 1:
            start(user)
        elif chosen ==2:
            end(user)
            break
        else:
            print("Error: Please enter a valid number")
            


def start(user:User):
    
    score = 0
    winstreak=0
    while True:
        print("="*50)
        print("Please select your learning mode:")
        print("1. English to Chinese")
        print("2. Chinese to English")
        print("3. Back")
        chosen = int(input("|Enter your choice (1 or 2 or 3)|"))
        if chosen == 1:
            score = english_to_chinese(score)
            user.update_winstreak(score)
            user.add_playtime()
            user.add_rankscore(score)
            user.change_rank()
            user.update_item()
            print(user)
        elif chosen == 2:
            score = chinese_to_english(score)
            user.update_winstreak(score)
            user.add_playtime()
            user.add_rankscore(score)
            user.change_rank()
            user.update_item()
            print(user)
        elif chosen == 3:
            break
        else:
            print("Error: Please enter a valid number")


def end(user:User):
    width=50
    print("="*60)
    print("🔥"+"Flashcard Learning Game".center(width)+"🔥")
    print("🔥🔥"+user.name.center(width-4)+"🔥🔥")
    print("🔥🔥🔥"+f"Today's playtimes: {user.playtimes}".center(width-8)+"🔥🔥🔥")
    print("🔥🔥🔥"+f"Your rank: {user.rank}".center(width-9)+"🔥🔥🔥")
    print("🔥🔥"+f"Medals: {user.medal}".center(width-4)+"🔥🔥")
    print("🔥"+"See you next time!".center(width)+"🔥")
   
    print("="*60)


if __name__ == "__main__":
    game_loop()