import sys
import random
from rich.table import Table
from rich.console import Console
from rich.prompt import Prompt

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

console = Console()

# Vocabulary list
vocab_list = [
    # Pronouns
    ("I (s/p)", "wǒ", "我"),
    ("You (s/p)", "nǐ / nǐmen", "你 / 你们"),
    ("He/She/It (s/p)", "tā / tāmen", "他 / 她 / 它 / 他们"),

    # Numbers
    ("1", "yī", "一"), ("2", "èr", "二"), ("3", "sān", "三"),
    ("4", "sì", "四"), ("5", "wǔ", "五"), ("6", "liù", "六"),
    ("7", "qī", "七"), ("8", "bā", "八"), ("9", "jiǔ", "九"),

    # Questions
    ("What C", "shénme", "什么"),
    ("Which", "nǎ", "哪"),
    ("Who", "shéi", "谁"),
    ("Follow-up Q", "ne", "呢"),
    ("How much/ How many C", "duōshǎo", "多少"),
    ("how old", "duō dà", "多大"),
    ("how to/instructions", "zěnme", "怎么"),

    # People & Professions
    ("Teacher C", "lǎoshī", "老师"),
    ("Student", "xuéshēng", "学生"),
    ("People/person C", "rén", "人"),
    ("Friend C", "péngyǒu", "朋友"),
    ("Study partner / classmate", "tóngxué", "同学"),

    # Languages & Learning
    ("To study", "xué", "学"),
    ("chinese lang (spoken)", "hànyǔ", "汉语"),
    ("chinese lang (written)", "zhōngwén", "中文"),
    ("chinese char C", "hànzì", "汉字"),
    ("to write C", "xiě", "写"),
    ("to speak", "shuō", "说"),
    ("to read aloud", "niàn", "念"),
    ("can (ability)", "huì", "会"),

    # Identity
    ("To Call (verb) C", "jiào", "叫"),
    ("Name", "míngzi", "名字"),
    ("Country C", "guó", "国"),

    # Family
    ("Have/Has C", "yǒu", "有"),
    ("Family", "jiā", "家"),
    ("daughter C", "nǚ'ér", "女儿"),

    # Food
    ("to eat C", "chī", "吃"),
    ("tasty", "hǎochī", "好吃"),
    ("eat well", "chī hǎo", "吃好"),
    ("dish", "cài", "菜"),
    ("to cook/make/produce/do", "zuò", "做"),

    # Time & Date
    ("day C", "rì", "日"),
    ("today C", "jīntiān", "今天"),
    ("tomorrow C", "míngtiān", "明天"),
    ("yesterday C", "zuótiān", "昨天"),
    ("this year C", "jīnnián", "今年"),
    ("years old", "suì", "岁"),

    # Miscellaneous
    ("this/that", "zhè / nà", "这 / 那"),
    ("very", "hěn", "很"),
    ("good C", "hǎo", "好"),
    ("No C", "bù", "不"),
    ("book C", "shū", "书"),
    ("to go C", "qù", "去"),
    ("MW for ren if no family", "gè", "个"),

    # Newly added
    ("school", "xué xiào", ""),
    ("look/read/watch", "kàn", ""),
    ("to read aloud", "dù", ""),
    ("read book aloud", "dú shū", ""),
    ("study book (silently)", "kàn shū", ""),
    ("would like/want", "xiǎng", ""),
    ("to drink", "hē", ""),
    ("tea", "chá", ""),
    ("cooked rice", "mǐ fàn", ""),
    ("shop", "shàng diàn", ""),
    ("buy", "mǎi", ""),
    ("sell", "mài", ""),
    ("cup", "bēi zi", ""),
    ("money", "qián", ""),
    ("how much (>10)", "duō shǎo", ""),
    ("unit of money", "kuài", ""),
    ("that", "nà", ""),
    ("what", "nǎ", "")
]

def quiz_pinyin_english(vocab):
    console.print("\n[bold blue]Pinyin ↔ English Quiz[/bold blue]\n")
    random.shuffle(vocab)
    for english, pinyin, _ in vocab:
        show_pinyin = random.choice([True, False])
        if show_pinyin:
            console.print(f"[green]Pinyin:[/green] {pinyin}")
            Prompt.ask("Press Enter to show English", default="", show_default=False)
            console.print(f"[magenta]English:[/magenta] {english}\n")
        else:
            console.print(f"[magenta]English:[/magenta] {english}")
            Prompt.ask("Press Enter to show Pinyin", default="", show_default=False)
            console.print(f"[green]Pinyin:[/green] {pinyin}\n")

def quiz_to_chinese(vocab):
    console.print("\n[bold yellow]Pinyin/English → Chinese Character Quiz[/bold yellow]\n")
    chinese_vocab = [entry for entry in vocab if entry[2].strip()]
    random.shuffle(chinese_vocab)
    for english, pinyin, chinese in chinese_vocab:
        console.print(f"[green]Pinyin:[/green] {pinyin} | [magenta]English:[/magenta] {english}")
        Prompt.ask("Press Enter to show Chinese", default="", show_default=False)
        console.print(f"[yellow]Chinese Character:[/yellow] {chinese}\n")

def main():
    console.print("[bold cyan]Choose a quiz mode:[/bold cyan]")
    console.print("1. Pinyin ↔ English")
    console.print("2. Pinyin/English → Chinese Characters")

    choice = Prompt.ask("Enter 1 or 2", choices=["1", "2"])
    if choice == "1":
        quiz_pinyin_english(vocab_list)
    else:
        quiz_to_chinese(vocab_list)

main()
