import random
from collections import defaultdict
from vocab.after_mids_vocab import after_vocabulary
from vocab.before_mids_vocab import before_vocabulary

vocabulary = before_vocabulary # change this to b4 or after

def display_flashcards(mode):
    items = list(vocabulary.items()) 
    random.shuffle(items)
    i = 0

    for english, data in items:
        pinyin = data["pinyin"]
        char = data["char"]
        
        if mode == 1 and char is not None:  # Character -> Pinyin/English
            print(f"[{i + 1}/{len([item for item in items if item[1]['char'] is not None])}]")
            input(f"Character: {char}\nPress Enter to see translation...")
            print(f"Pinyin: {pinyin}\nEnglish: {english}\n")
            input("Press Enter to continue...")
            print("\n" + "="*50 + "\n")
        elif mode == 2:  # English -> Pinyin/Character
            print(f"[{i + 1}/{len(items)}]")
            input(f"English: {english}\nPress Enter to see translation...")
            print(f"Pinyin: {pinyin}")
            if char is not None:
                print(f"Character: {char}")
            else:
                print("(Character not included in syllabus.)")
            input("\nPress Enter to continue...")
            print("\n" + "="*50 + "\n")
        elif mode == 3:  # Pinyin -> English/Character
            print(f"[{i + 1}/{len(items)}]")
            input(f"Pinyin: {pinyin}\nPress Enter to see translation...")
            print(f"English: {english}")
            if char is not None:
                print(f"Character: {char}")
            else:
                print("(Character not included in syllabus.)")
            input("\nPress Enter to continue...")
            print("\n" + "="*50 + "\n")
        
        i += 1

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