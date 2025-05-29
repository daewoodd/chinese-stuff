# Vocabulary data
before_vocabulary = {
    # Greetings
    "Hello (singular)": {"pinyin": "nǐ hǎo", "char": None},
    "Hello (plural)": {"pinyin": "nǐ men hǎo", "char": None},
    "See you again": {"pinyin": "zài jiàn", "char": None},
    "To thank": {"pinyin": "xiè xie", "char": None},
    "Thank you": {"pinyin": "xiè xie nǐ", "char": None},
    "No thanks": {"pinyin": "bù xiè", "char": None},
    "You're welcome": {"pinyin": "bù kè qì", "char": None},
    "I'm sorry": {"pinyin": "duì bù qǐ", "char": None},
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
    "Friend": {"pinyin": "péng yǒu", "char": "朋友"},
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
    "Study a book": {"pinyin": "kàn shū", "char": "-- 书"},
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