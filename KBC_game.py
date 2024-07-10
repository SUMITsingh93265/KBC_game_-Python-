# Making KBC project

questions = [
    [
        "Besides Sachin Tendulkar, who is the only other Indian cricketer to have scored over 13,000 runs in test cricket?",
        "Virat Kohli", "Sunil Gavaskar", "VVS laxman", "Rahul Dravid", 4
    ],
    [
        "Ranthambore, Sariska and Keoladeo Ghana are all names of what? ",
        "National Parks", "Goosebumps", "Mountains", "Rivers", 1
    ],
    [
        "India’s official entry to Oscars 2021, ” Jallikattu” is, a film in which language?",
        "Hindi", "Punjabi", "Kannada", "Malayalam", 4
    ],
    [
        "In terms of production, which of these is the largest train coach manufacturing unit in the world?",
        "Integral Coach Factory, Bangalore", "Integral Coach Factory, Mumbai",
        "Integral Coach Factory, Chennai", "Integral Coach Factory, Kolkata", 3
    ],
    [
        "In 2020, Louise Gluck won the Nobel Prize in which category?", "Music",
        "Sports", "Literature", "Dance", 3
    ],
    [
        "Which of the following companies was originally started as a loom manufacturing unit in 1909?",
        "Suzuki", "CEAT", "Honda", "Mercedes", 1
    ],
    [
        "In 1994, who became the winner of the first-ever Filmfare R D Burman Award for New Music Talent?",
        "Udit Narayan", "A. R. Rahman", "Lata Mangeshkar", "Raj Burman", 2
    ],
    [
        "What colour did Lord Shiva’s throat turn into when he drank the deadly poison during Samudra Manthan?",
        "Red", "Yellow", "Blue", "Black", 3
    ],
    [
        "What is the profession of Kabir in the film Kabir Singh?", "Engineer",
        "Cricketor", "Athlete", "Doctor", 4
    ],
    [
        "Which of these national parks is named after the river that flows through the park?",
        "Pench", "Tadoba", "Vrindavan", "Wildera", 1
    ],
    [
        "Which state is the largest producer of sugarcane in India?",
        "Maharashtra", "Karnataka", "Madhya Pradesh", "Uttar Pradesh", 4
    ],
    [
        "Which of these colors when mixed with red will produce the color orange?",
        "Violet", "Green", "Orange", "Yellow", 4
    ],
    [
        "Which of these is an ashram set up by Gandhiji set up near Wardha in Maharashtra?",
        "Sri Aurobindo Ashram", "Parmarth Niketan Ashram", "Sevagram",
        "Sivananda Ashram", 3
    ],
    [
        "Who of the following personalities is not married to a sports person?",
        "Anushka Sharma", "Sakshi Singh Rawat", "Mahesh Bhupathi",
        "Sharmila Tagore", 3
    ],
    [
        "Which part of the plant absorbs water and nutrients from the soil?",
        "Stem", "Buds", "Leafs", "Root", 4
    ],
]

level = [
    1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000,
    1250000, 2500000, 5000000, 10000000
]
money = 0
for i in range(0, len(questions)):
    question = questions[i]
    print()
    print("*************************************")
    print(question[0])
    print("*************************************")
    print(f"a. {question[1]}       b. {question[2]}")
    print(f"c. {question[3]}       d. {question[4]}")
    print()
    print("*************************************")
    reply = int(
        input("Apna jawab chune 1 to 4, 0 daba kar game chord sakte hai? "))
    print("*************************************")

    if (reply == 0):
        money = level[i - 1]
        break

    if (reply == question[-1]):
        print(f"Sahi Jawab aap jit chuke hai {level[i]}")
        if (i == 4):
            money = 10000
        elif (i == 9):
            money = 320000
        elif (i == 14):
            money = 10000000
            print("Aap ban chuke hai crorepati")
    else:
        print("Shree maan ji ye galat jawab hai")
        break

print()
print(f"Aap ne kul dhan rashi jiti hai {money}")
