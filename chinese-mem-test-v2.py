import random
from collections import defaultdict

# Vocabulary data
vocabulary = {
    # Greetings
    "Hello (singular)": {"pinyin": "nǐ hǎo", "char": None},
    "Hello (plural)": {"pinyin": "nǐ men hǎo", "char": None},
    "See you again": {"pinyin": "zài jiàn", "char": None},
    "To thank": {"pinyin": "xiè xie", "char": None},
    "Thank you": {"pinyin": "xiè xie nǐ", "char": None},
    "No thanks": {"pinyin": "bù xiè", "char": None},
    "You're welcome": {"pinyin": "bù kè qi", "char": None},
    "I'm sorry": {"pinyin": "duì bu qǐ", "char": None},
    "Does not matter (as a reply to I'm sorry)": {"pinyin": "méi guān xi", "char": None},
    
    # Pronouns
    "I (s)": {"pinyin": "wǒ", "char": None},
    "I (p)": {"pinyin": "wǒ men", "char": None},
    "You (s)": {"pinyin": "nǐ", "char": None},
    "You (p)": {"pinyin": "nǐ men", "char": None},
    "He/She/They (s)": {"pinyin": "tā", "char": None},
    "He/She/They (p)": {"pinyin": "tā men", "char": None},
    
    # Numbers
    "0": {"pinyin": "líng", "char": "零"},
    "1": {"pinyin": "yī", "char": "一"},
    "2": {"pinyin": "èr", "char": "二"},
    "3": {"pinyin": "sān", "char": "三"},
    "4": {"pinyin": "sì", "char": "四"},
    "5": {"pinyin": "wǔ", "char": "五"},
    "6": {"pinyin": "liù", "char": "六"},
    "7": {"pinyin": "qī", "char": "七"},
    "8": {"pinyin": "bā", "char": "八"},
    "9": {"pinyin": "jiǔ", "char": "九"},
    "10": {"pinyin": "shí", "char": "十"},
    "100": {"pinyin": "yībǎi", "char": "一百"},
    "1000": {"pinyin": "yīqiān", "char": "一千"},
    
    # Questions
    "What": {"pinyin": "shén me", "char": "什么"},
    "Which": {"pinyin": "nǎ ge", "char": None},
    "Who": {"pinyin": "shéi", "char": None},
    "Follow-up Question": {"pinyin": "ne", "char": None},
    "How much / How many (<10)": {"pinyin": "jǐ", "char": "几"},
    "How old": {"pinyin": "duō dà", "char": None},
    "How to / Ask for instructions": {"pinyin": "zěn me", "char": None},
    
    # People & Professions
    "Teacher": {"pinyin": "lǎo shī", "char": "老师"},
    "Student": {"pinyin": "xué shēng", "char": None},
    "People/person/human": {"pinyin": "rén", "char": "人"},
    "Friend": {"pinyin": "péng you", "char": "朋友"},
    "Study partner / classmate": {"pinyin": "tóng xué", "char": None},
    
    # Language and learning
    "To study": {"pinyin": "xué", "char": None},
    "Chinese language (spoken)": {"pinyin": "hàn yǔ", "char": "汉 --"},
    "Chinese character": {"pinyin": "hàn zì", "char": "汉字"},
    "To write": {"pinyin": "xiě", "char": "写"},
    "To speak (a language)": {"pinyin": "shuō", "char": None},
    "To read aloud": {"pinyin": "dú", "char": None},
    "To read aloud (in reference to a book)": {"pinyin": "dú shū", "char": "-- 书"},
    "Can/Be able to (ability)": {"pinyin": "huì", "char": "会"},
    
    # Identity
    "To call": {"pinyin": "jiào", "char": "叫"},
    "Name": {"pinyin": "míng zi", "char": None},
    "Country": {"pinyin": "guó", "char": "国"},
    
    # Family
    "Have/Has": {"pinyin": "yǒu", "char": "有"},
    "Family": {"pinyin": "jiā", "char": None},
    "Daughter": {"pinyin": "nǚ ér", "char": "女儿"},
    
    # Food
    "Tasty": {"pinyin": "hǎo chī", "char": "好吃"},
    "Eat well": {"pinyin": "chī hǎo", "char": "吃好"},
    "Dish/Cuisine": {"pinyin": "cài", "char": None},
    "To cook/make/produce/do": {"pinyin": "zuò", "char": None},
    "To eat": {"pinyin": "chī", "char": "吃"},
    
    # Dates
    "day (formal)": {"pinyin": "rì", "char": "日"},
    "day (informal)": {"pinyin": "tiān", "char": "天"},
    "date": {"pinyin": "hào", "char": None},
    "Today": {"pinyin": "jīn tiān", "char": "今天"},
    "Tomorrow": {"pinyin": "míng tiān", "char": "明天"},
    "Yesterday": {"pinyin": "zuó tiān", "char": "昨天"},
    "This year": {"pinyin": "jīn nián", "char": "今年"},
    "Month": {"pinyin": "yuè", "char": "月"},
    "Year": {"pinyin": "nián", "char": "年"},
    "Years Old": {"pinyin": "suì", "char": None},
    "Week": {"pinyin": "xīng qī", "char": None},
    
    # Misc
    "This": {"pinyin": "zhè ge", "char": None},
    "That": {"pinyin": "nà ge", "char": None},
    "Very": {"pinyin": "hěn", "char": None},
    "Is/am/are": {"pinyin": "shì", "char": "是"},
    "Good/Agreement/OK": {"pinyin": "hǎo", "char": "好"},
    "No": {"pinyin": "bù", "char": "不"},
    "Book": {"pinyin": "shū", "char": "书"},
    "To go": {"pinyin": "qù", "char": "去"},
    "MW for teacher/student/classmate/etc.": {"pinyin": "gè", "char": "个"},
    "MW for for counting family members": {"pinyin": "kǒu", "char": "口"},
    "China": {"pinyin": "zhōng guó", "char": "中国"},
    
    # New
    "School": {"pinyin": "xué xiào", "char": None},
    "Look/Read/Watch": {"pinyin": "kàn", "char": None},
    "Study a book": {"pinyin": "kàn shū", "char": None},
    "Would like/want to": {"pinyin": "xiǎng", "char": None},
    "To drink": {"pinyin": "hē", "char": None},
    "Tea": {"pinyin": "chá", "char": None},
    "Cooked rice": {"pinyin": "mǐ fàn", "char": None},
    "Shop": {"pinyin": "shāng diàn", "char": None},
    "Buy": {"pinyin": "mǎi", "char": None},
    "Sell": {"pinyin": "mài", "char": None},
    "Cup": {"pinyin": "bēi zi", "char": None},
    "Money": {"pinyin": "qián", "char": None},
    "How much (>10)": {"pinyin": "duō shǎo", "char": None},
    "Units of money (MW)": {"pinyin": "kuài", "char": None},
    "That": {"pinyin": "nà ge", "char": None},
    "Yes/no question": {"pinyin": "ma", "char": None}
}

def display_flashcards(mode):
    items = list(vocabulary.items())
    random.shuffle(items)
    
    for english, data in items:
        pinyin = data["pinyin"]
        char = data["char"]
        
        if mode == 1 and char is not None:  # Character -> Pinyin/English
            input(f"Character: {char}\nPress Enter to see translation...")
            print(f"Pinyin: {pinyin}\nEnglish: {english}\n")
            input("Press Enter to continue...")
            print("\n" + "="*50 + "\n")
        elif mode == 2:  # English -> Pinyin/Character
            input(f"English: {english}\nPress Enter to see translation...")
            print(f"Pinyin: {pinyin}")
            if char is not None:
                print(f"Character: {char}")
            else:
                print("(Character not included in syllabus.)")
            input("\nPress Enter to continue...")
            print("\n" + "="*50 + "\n")
        elif mode == 3:  # Pinyin -> English/Character
            input(f"Pinyin: {pinyin}\nPress Enter to see translation...")
            print(f"English: {english}")
            if char is not None:
                print(f"Character: {char}")
            else:
                print("(Character not included in syllabus.)")
            input("\nPress Enter to continue...")
            print("\n" + "="*50 + "\n")

def quiz():
    print("Chinese Vocabulary Flashcards")
    print("Choose a mode:")
    print("1. Chinese character -> pinyin/English")
    print("2. English -> pinyin/Chinese character")
    print("3. Pinyin -> Chinese character/English")
    print("4. Exit")
    
    while True:
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            print("\nMode: Chinese character -> pinyin/English")
            print("You will see a Chinese character. Press Enter to see its pinyin and English meaning.")
            print("Press Enter again to move to the next character.\n")
            display_flashcards(1)
        elif choice == "2":
            print("\nMode: English -> pinyin/Chinese character")
            print("You will see an English word. Press Enter to see its pinyin and Chinese character.")
            print("Press Enter again to move to the next word.\n")
            display_flashcards(2)
        elif choice == "3":
            print("\nMode: Pinyin -> Chinese character/English")
            print("You will see pinyin. Press Enter to see its English meaning and Chinese character.")
            print("Press Enter again to move to the next word.\n")
            display_flashcards(3)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    quiz()