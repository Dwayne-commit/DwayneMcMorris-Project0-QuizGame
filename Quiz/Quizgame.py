import click

@click.command()
def too():
    
    print("Mom: Good Morning.")
    print("How do you feel today?")
    ah = input("Enter Well or Not Well:" + " ")
    print("After leaving the house you arrive at school")
    print("Are you ready for your quiz?")

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)
    score = int((correct_guesses/len(questions))*100)
    
    if score >= 50:
        print("Great Job!")
        print("Mom: Here's your allowance plus a tip for the good grades!")
        m = 160.00
        print(str(m) + "$")
        float(m)
        print("Feeling Hungry you decide to grab somthing to eat with your friend")
        print("Waiter Asks: Would you like Breakfast or Lunch")
        cho = str(input("Enter Breakfast or Lunch" + " "))
        cho.upper()
        if cho == "Lunch":
            men1()
            print("Choose from the menu")
            food = input(str("I would like.."))
            print("Your friend ask could you also pay for her to have a meal")
            mP = input(str("Yes or No:"))
            mP.upper()
            if mP == "Yes":
                fc = input(str("Choose which Menu they'll eat from. Breakfast or Lunch:"))
                fc.upper()
                if fc == "Breakfast":
                    breakf()
                    print("Choose from the menu")
                elif fc == "Lunch":
                    men1()
                    print("Choose from the menu")
                else:
                    print("Here's a Shake!")
        
                    
        elif cho == "Breakfast":
            breakf()
            print("Choose from the menu")
            food = input(str("I would like.."))
            print("Your friend ask could you also pay for her to have a meal")
            mP = input(str("Yes or No:"))
            mP.upper()
            if mP == "Yes":
                fc = input(str("Choose which Menu they'll eat from. Breakfast or Lunch:"))
                fc.upper()
                if fc == "Breakfast":
                    breakf()
                    print("Choose from the menu")
                elif fc == "Lunch":
                    men1()
                    print("Choose from the menu")
                else:
                    print("Here's a Shake!")
                    
        else:
            print("Here's a Shake!")
            
        e = input(str("Leave a Tip. Yes or No:"))
        e.upper()
        if e == "Yes":
            print(m - 30.0)
        elif e == "No":
            print(m - 20.0)
        else:
            print(m - 20.0)
        print("After having a bite to eat you see it's getting pretty late")
        print("You decide to head home and end your day")
            
            
    elif score <= 60:
        print("Try better next time!")
        print("Mom: Here's your allowance study harder")
        ml = 110.00
        print(str(ml) + "$")
        float(ml)
        print("You decide to head to the book store to improve your score.")
        b = input(str("Choose a book from the list. Enter C++, Python, or Web:"))
        b.upper()
        book()
        if b == "C++":
            print(ml - 102.0)
            print("May I see Id")
            lisc()
        elif b == "Python":
            print(ml - 47.83)
            print("May I see Id")
            lisc()
        elif b == "Web":
            print(ml - 68.75)
            print("May I see Id?")
            lisc()
            print("Thanks")
        else:
            ("We didn't have anything you liked. Sorry")
        
    else:
        print("Try Again")
    print("After a long day you decide to head home and go to sleep.")
    end_game()
        

# -------------------------
def check_(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")
    

# -------------------------
def end_game():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -------------------------


questions = {"Q1: When did technology the company Apple start?": "A", "Q2: What is the name of Microsoft's Founder?": "B", "Q3: What Operating System does a Samsung phone use?": "A", "Q4: When was Python created?": "C", "Q5: What does OS stand for?": "C", "Q6: How many moons does Saturn have?": "B",  "Q7: What are three types of Big Data?": "A", "Q8: What is an API?": "D", "Q9: What tag creates a button in HTML?" : "A", "Q10: A variable within a local scope is called?" : "C"}

options =  [["A: April 1, 1976", "B: March 29, 1984", "C:April 5, 2019", "D:None are correct"], ["A: Steve Jobs", "B: Bill Gates", "C: Mark Zuckerberg", "D: None are correct"],
    ["A: Android", "B: Windows 10", "C: IOS", "D: None are correct"], ["A: March 30, 2000", "B: May 9, 1990", "C: February 20, 1991", "D: None are Correct"], ["A: On stage", "B: On Display", "C: Operating System", "D: None are correct"], ["A: 12", "B: 82", "C: 45", "D: None are correct"], 
    ["A: Structured, Unstructerd, Semi-Structured", "B: Clean, Un-Clean, Semi-Clean", "C: Volume, Verocity, Velocity", "D: None are Correct"], ["A: App", "B: Text", "C: Document", "D: None are Correct"], ["A: <button>", "B: <center>", "C: <dir>", "D: None are Correct"], ["A: Global variable", "B: Enclosed variable", "C: Local Variable", "D: None are correct"]]




def breakf():
    import json
    import pymongo
    import pprint
    from pymongo import MongoClient
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]

    coll = mydb["menus"]
    list1 = [
        {"title":"buttermilk pancakes", "category":"breakfast", "price": "12.99", "img": "./images/item-1.jpeg"},
        {"title":"country delight", "category":"breakfast", "price": "10.99", "img": "./images/item-4.jpeg"},
        {"title":"bacon overflow", "category":"breakfast", "price": "8.99", "img": "./images/item-7.jpeg"},
        {"title":"quarantine buddy", "category":"shakes", "price": "9.99", "img": "./images/item-9.jpeg"}
        ]
    y = coll.delete_many({})
    x = coll.insert_many(list1)
    #print(x.inserted_ids)

    #print(myclient.list_database_names())
    
    for b in coll.find({},{"title": 1, "price": 1}):
        ppb = pprint.PrettyPrinter(width=41, compact=True)
        ppb.pprint(b)
        
def lisc():
    import random
    key = input("Enter Name:")
    value = input("Enter Address:")

    mydict = {}
    mydict.update({key:value})
    x= random.sample(range(1,10),9)
    print(mydict)
    print("No.")
    for i in x:
        print(i, end = '')



def men1():
    import json
    import pprint
    f1 = open('Lunch.json')
    data1 = json.load(f1)
    for i in data1['Menu']:
        pp = pprint.PrettyPrinter(width=41, compact=True)
        pp.pprint(i)
    f1.close()

def book():
    import json
    import pprint
    f2 = open('Library.json')
    data2 = json.load(f2)
    for i in data2['books']:
        pp1 = pprint.PrettyPrinter(width=41, compact=True)
        pp1.pprint(i)
    f2.close()




if __name__ == '__main__':
    too()
