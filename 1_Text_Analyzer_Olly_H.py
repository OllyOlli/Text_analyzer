"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Olga H.
email: Olcah@email.cz
discord: Olly#1959

Zadání:
Vyžádá si od uživatele přihlašovací jméno a heslo,
zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů,
pokud je registrovaný, pozdrav jej a umožni mu analyzovat texty,
pokud není registrovaný, upozorni jej a ukonči program.**
Registrováni jsou následující uživatelé:

+------+-------------+
| user |   password  |
+------+-------------+
| bob  |     123     |
| ann  |   pass123   |
| mike | password123 |
| liz  |   pass123   |
+------+-------------+

Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS:
Pokud uživatel vybere takové číslo textu, které není v zadání,
program jej upozorní a skončí,
pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí.

Pro vybraný text spočítá následující statistiky:
počet slov,
počet slov začínajících velkým písmenem,
počet slov psaných velkými písmeny,
počet slov psaných malými písmeny,
počet čísel (ne cifer),
sumu všech čísel (ne cifer) v textu.
Program zobrazí jednoduchý sloupcový graf, 
který bude reprezentovat četnost různých délek slov v textu.
 Například takto:
# ...
 7| * 1
 8| *********** 11
 9| *************** 15
10| ********* 9
11| ********** 10

Po spuštění by měl průběh vypadat následovně:

----------------------------------------
There are 54 words in the selected text.
There are 12 titlecase words.
There are 1 uppercase words.
There are 38 lowercase words.
There are 3 numeric strings.
The sum of all the numbers 8510
----------------------------------------
LEN|  OCCURENCES  |NR.
----------------------------------------
  1|*             |1
  2|*********     |9
  3|******        |6
  4|***********   |11
  5|************  |12
  6|***           |3
  7|****          |4
  8|*****         |5
  9|*             |1
 10|*             |1
 11|*             |1

 Postup:
1) Vytvoříme slovník registrovaných uživatelů s přihlašovacím jménem 
jako klíčem a heslem jako hodnotou.
2) Požádáme uživatele o zadání přihlašovacích údajů a ověříme,
 zda jsou správné.
3) Pokud jsou přihlašovací údaje správné, necháme uživatele vybrat text a 
provést statistiky na tomto textu.
3) Spočítáme počet slov, slov začínajících velkým písmenem, slov psaných 
velkými/malými písmeny a číselné řetězce.
4) Spočítáme sumu všech čísel v textu.
5) Vytvoříme sloupcový graf pro délku slov v textu a zobrazíme výsledky.

"""

TEXTS = ['''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.''']

text_count = len(TEXTS)
delimiter = '-' * 40

# Usernames and passwords dictionary
registered_users = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}

# Login
user_name = input('Enter your username: ').lower()

# check if the user is registered
if user_name not in registered_users:
    print('unregistered user, terminating the program..')
    quit()
else:
    # get user input for password and check if it matches
    password = input('password: ')
    p = registered_users.get(user_name)
    if password != p:
        print('wrong password, terminating the program..')
        quit()
    else:
        # welcome message
        print(delimiter)
        print(f'Welcome to the app, {user_name}')
        print(f'We have 3 texts to be analyzed.')
        print(delimiter)

# get user input for which text to analyze
    try:
        choice = int(input("Enter a number btw. 1 and 3 to select: "))
        selected_text = TEXTS[choice - 1]
    except ValueError():
        print('Enter a number, not a letter!')      
    except IndexError:
        print('Invalid selection!')
    else:
        print('Wrong number entered')

# Statistics
selected_text_split = selected_text.split()
clean_text = []

for word in selected_text_split:  # Simplified the loop
    words = word.strip('.,:/;')
    if words:
        clean_text.append(words)

# analyze the text and count various features
words = len(clean_text)
title_words = 0
upper_words = 0
lower_words = 0
numeric_words = 0
numeric_sum = 0


for word in clean_text:
    if word.istitle():
        title_words += 1
    elif word.isupper():
        upper_words += 1
    elif word.islower():
        lower_words += 1
    elif word.isnumeric():
        numeric_words += 1
        numeric_sum += float(word)

# print the results
print(f"There are {(words)} words in the selected text.")
print(f"There are {(title_words)} titlecase words.")
print(f"There are {(upper_words)} uppercase words.")
print(f"There are {(lower_words)} lowercase words.")
print(f"There are {(numeric_words)} numeric strings.")
print(f"The sum of the numbers {(numeric_sum)}.")
print(delimiter)

# Table with results
counts = {}
for word in clean_text:
    word_length = len(word)
    if word_length not in counts:
        counts[word_length] = 1
    else:
        counts[word_length] += 1

sorted_counts = sorted(counts.items())
for length, count in sorted_counts:
    print(f"{length:<6} {count * '*':<18} {count}")