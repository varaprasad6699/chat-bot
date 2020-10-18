"""
1.greet the person and says function of the bot and asks name of the person.
2.After name given by the person ,it welcomes the person and tells objective of the bot.
3.it shows the different categories to select one among them and then taking input from the person which category they want
4.it shows the output of the popular personalities of the category which they are choosen
5.the information is useful to learn making general knowledge
6.atlast it ends with giving thanks to the person
"""
import random
from datetime import datetime


def greeting_and_introduce_person():
    greeting_person = ["welcome to my world,i am a subbu's bot,i am useful to improve your knowledge to about the famous personalities in different categories.can you type your name",
    "exited to meet you,i am subbu's bot ,i gives you a information about different famous personalities,may i know your name "
    ]
    print(random.choice(greeting_person))
def get_current_time_now():
    current_timing = datetime.now()
    say_to_him = "Good morning"
    if current_timing.hour>12 and current_timing.hour<=17:
        say_to_him = "Good afternoon"
    elif current_timing.hour>17 and current_timing.hour<=21:
        say_to_him = "Good evening"
    elif current_timing.hour>21:
        say_to_him = "Hii ,Its too late"
    return say_to_him
def say_welcome(name):
    messaging = ["Nice to meet you ",
    "have wonderfull time with me "
    ]
    print(f"{get_current_time_now()},{random.choice(messaging)}")
def show_menu():
    print("IT SHOWS FAMOUS PERSONALITIES IN WORLD")
    print("1.famous personality in science")
    print("2.famous personality in sports")
    print("3.famous personality in history")
    print("4.famous personality in kingdoms")
    print("5.famous personality in buisiness")
    print("6.todays date")
    print("7.press -1 to exit")
    try:
        return int(input("choose the category-[1-6]"))
    except:
        print("only 1-6")
        return 0
def get_science():
    science = ["1.ALBERT EINSTEIN : The date was Jan. 8, 1930, and the New York museum was showing a film about Albert Einstein and his general theory of relativity. .",
    "2.MARIE CURIE : BIRTH - Maria Salomea Sklodowska in 1867 in Warsaw, Poland ,In 1903, Curie, her husband and Becquerel won the Nobel Prize in Physics for their work on radioactivity",
    "3. Alain Aspect :	Quantum Theory Aspect made his most crucial breakthroughs in quantum theory. In 2005, he was awarded the CSNR Gold Medal by settling a 70-year-old dispute .",
    "4.Mildred Dresselhaus :	Carbon Science -Known as the queen of carbon science",
    "5.Sydney Brenner	:  Biology—Genetics	Sydney Brenner is a biologist and the winner of the 2002 Nobel Prize in Physiology or Medicine, shared with H. Robert .",
    "6.Timothy Berners- : Lee	Computer Science (WWW) Timothy Berners-Lee is a computer scientist, best known as the inventor of the World Wide Web. He was honored as the Inventor of the World Wide Web during the 2012.",
    "............................................"
    ]
    for i in science:
        print(i)
def get_sports():
    sports =["1. Sachin Tendulkar (1973 – ) (India, cricket): Only player to score 30,000 runs in international cricket. ",
    "2.Serena Williams (1981 – ) (US, tennis) : Most successful female tennis player of all time. She has won 23 single grand slam titles, 16 double titles. ",
    "3.Diego Maradona (1960 – ) (Argentina, football) : Joint FIFA player of Century with Pele. Won 1986 World Cup with Argentina.",
    "4.Diego Maradona (1960 – ) (Argentina, football) : Joint FIFA player of Century with Pele. Won 1986 World Cup with Argentina.",
    "5.Lionel Messi (1987 – ) Argentina, football. : One of the most spectacular footballers of the modern game. ",
    "6.Lin Dan (1983 – ) (China, badminton) : Dan is one of the greatest stars of badminton.",
    "................................................"
    ]
    for i in sports:
        print(i)
def get_history():
    history = ["1.Abraham Lincoln (1809 – 1865) : US President during American civil war",
    "2.Nelson Mandela (1918 – 2013) : South African President anti-apartheid campaigner",
    "3.John F. Kennedy (1917 – 1963): US President 1961 – 1963",
    "4.Martin Luther King (1929 – 1968) : American civil rights campaigner",
    "5.Queen Elizabeth II (1926 – ): British monarch since 1954",
    "6.Mahatma Gandhi (1869 – 1948): Leader of Indian independence movement ,Mother Teresa (1910 – 1997) Macedonian Catholic missionary nun",
    "...................................................",
    ]
    for i in history:
        print(i)
def get_kings():
    kings = ["1.Chandragupta Maurya (340-298 BCE) :Mauryan EmperorChandragupta.",
    "2.Oda Nobunaga :Japanese feudal lord, 16th century Great because",
    "3.Boudica Queen :of the Iceni, first century AD Great becaus",
    "4.Maharaja Ranjit Singh :Ruler of the Sikh empire 1801–39Great ",
    "5.William III King of England:, Scotland and Ireland 1689–1702 Great because… he freed Europe from French hegemony",
    "6.Wu Zetian Emperor of China: 690–705 Great because… she was the most powerful woman in Chinese history ",
    "....................................................."
    ]
    for i in kings:
        print(i)
def get_business():
    business = ["1.BILLGATES : As a co-founder of Microsoft, Bill Gates has undeniably influenced the world we live in today. What’s more, his success with the tech giant has led him to a truly remarkable fortune of $89 billion. Before Gates  ",
    "2.Jack Ma (China) : Ma initially came across the internet and had his first big idea – a listings site for China. Four years later he would found Alibaba, a business-to-business commerce site named by Forbes in 2017.",
    "3.Bernard Arnault (France) : Bernard Arnault was once quoted as saying that “luxury goods are the only area in which it is possible to make luxury margins.” And there may be some truth to that statement, too; after all, LVMH, of which Arnault is the chair, CEO and majority shareholder, recorded revenue of more than $44 billion in 2016. LVMH furthermore incorporates.",
    "4.Mukesh Ambani (India) : Through Ambani’s influence, however, Reliance expanded its textile operations and diversified into petrochemicals, technology and telecoms, leading to it becoming the second biggest company in the whole country, according to Fortune’s 2017 Global 500 list. .",
    "5.Alisher Usmanov (Russia) : Alisher Usmanov’s success in business arguably proves the adage that “it’s not what you know but who you know” that counts",
    "6.Ernesto Bertarelli (Switzerland) : Indeed, he and sister Dona went on to expand Serono and increase its revenues threefold in the ten years following Bertarelli’s installment as CEO. In 2007, moreover, the pair sold the company to pharma giant Merck for $9 billion.",
    "......................................................"
    ]
    for i in business:
        print(i)
def bot():
    greeting_and_introduce_person()
    name = input("enter your name ")
    say_welcome(name)
    category = show_menu
    while category != -1:
        if category == 1:
            get_science()
        elif category == 2:
            get_sports()
        elif category == 3:
            get_history()
        elif category == 4:
            get_kings()
        elif category == 5:
            get_business()
        elif category == 6:
            print(str(datetime.now()))
        category = show_menu()
bot()
            


