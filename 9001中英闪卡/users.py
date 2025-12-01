class User:
    def __init__(self, name):
        
        self.name = name
        self.playtimes = 0
        self.rank = "🐰"
        self.rankscore = 0
        self.item=[]
        self.winstreak=0
        self.medal=[]
    def add_playtime(self):
        self.playtimes +=1
    
    def add_rankscore(self,score):
        if score == 0:
            self.rankscore -=1
        elif 0<score<3:
            self.rankscore = self.rankscore
        elif 3<score<5:
            self.rankscore +=1
        elif score == 5 and self.winstreak == 1:
            self.rankscore +=3
        elif score == 5 and self.winstreak == 2:
            self.rankscore +=4
        elif score == 5 and self.winstreak == 3:
            self.rankscore +=5
    def change_rank(self):
        if -10<self.rankscore<=3:
            self.rank = "🐭"
        elif 4<=self.rankscore <=6:
            self.rank = "🐰"
        elif 6<=self.rankscore <=9:
            self.rank = "🐻"
        elif 10<=self.rankscore <=12:
            self.rank = "🦁"
        elif self.rankscore >=13:
            self.rank = "🐼"
    def update_winstreak(self,score):
        if score == 5:
            self.winstreak +=1
        else:
            self.winstreak = 0

    def update_item(self):
        if self.rank == "🐼" and "🏆 The Ultimate Champion" not in self.item:
            self.item.append("🏆 The Ultimate Champion")
            self.medal.append("🏆")
            print("🏆 You have won an achievement: The Ultimate Champion")
        if self.playtimes == 5 and "🥇 Practice Maniac" not in self.item:
            self.item.append("🥇Practice Maniac")
            self.medal.append("🥇")
            print("🥇 You have won an achievement: Practice Maniac")
        if self.winstreak == 3 and "🎖️ Eye fast chips" not in self.item:
            self.item.append("🎖️ Eye fast chips")
            self.medal.append("🎖️")
            print("🎖️ You have won an achievement: Eye fast chips")
        
        
    def __str__(self):
        return (
            f"{self.rank}"+f"{self.name}".center(15)+f"{self.rank}\n"
            f"{self.rank}"+f"Playtimes: {self.playtimes}".center(15)+f"{self.rank}\n"
            f"{self.rank}"+f"Rankscore: {self.rankscore}".center(15)+f"{self.rank}\n"
            f"{self.rank}"+f"Medals: {'| '.join(self.medal) if self.medal else 'None'}".center(15)+f"{self.rank}"
        )
        
    