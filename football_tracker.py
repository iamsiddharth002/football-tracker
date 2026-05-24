#From today i am starting a great journey and i will always be consistent with my brother CLAUDE and build a great business project called football tracker.
# 1.) create a function called add_player()
# that takes these parameters:
# --name
# --goals
# --assists
# --matches

# 2.) for now just print all the details inside the function
# 3.) call the function with your favourite footabller!.

import json #importing a module json so that it saves my data to text and then in file....

#1. A list to store all players
players = []#the first step is to create an empty list so that when we add details in our function it should be here and we will append the function variable into this players variable.

#2. A function that adds a player to that list
#first add variables name in function to set the parameters for players which we are going to add and then proceed to the next method which is appending the dictionary to the list and after that we will add a code for confirmation that the player name has been added successfully and at last we will call the function and add the players details which we want to add.
def save_players():#save concept we created a funnction
    with open("players.json", "w") as file:#(w) stands for write in our block of code..
        json.dump(players, file)#json.dump is a method to save the players list in a file..
    #the with method helps us to close the file which we created automatically. we don't need to hard code it manually simple as that....

def load_players():#load concept we created a function
    global players #global method we can simply explain it as "hey python - i am not making a new variable, i am talking about the one that already exists outside"..
    try:
        with open("players.json", "r") as file:#(r) stands for read in our block of code..
            players = json.load(file)#json.load is a method to read the list of players in our saved file.. and that line of code means that it will read everything from the file and store it back into players list which we created at the top  of very beginning of our football_tracker code...
            print("Players loaded successfully!")

    except FileNotFoundError:
        print("No saved data found, starting fresh!")

def add_player(name, goals, assists, matches):
    player = {
        "Name": name,      #use parametrs here, not hardcoded values!
        "Goals": goals,
        "Assists": assists,
        "Matches": matches
        }
    players.append(player)#append to players list
    save_players()
    print(f"{name} added successfully!")#print comfirmation

#call the function with any players details you want to add
# add_player("Messi", 910, 412, 1153)
# add_player("Ronaldo", 971, 261, 1322)
# add_player("Neymar", 476, 286, 763)
# add_player("Sunil Chhetri", 94, 40, 151)

#function for showing the players to the user in a proper manner or we can say a proper and clean output of players in our list and their info provided.....
def show_player():
    for player in players:
        print("-------------------")
        print(f"Name: {player['Name']}")
        print(f"Goals: {player['Goals']}")
        print(f"Assists: {player['Assists']}")
        print(f"Matches: {player['Matches']}")
        print("-------------------")

# show_player()#for printing all the players in a clean way


#creating a function to find the best scorer present in our list of players.
def find_top_scorer():
    top_scorer = None
    top_goals = 0
    for player in players:#looping through each player one by one
        if player["Goals"] > top_goals:#it says that if player goals are more than the top scorer.
            top_goals = player["Goals"]#updating the players after the loop so we can get the output for the highest scorer in out list of players.
            top_scorer = player["Name"]
    print(f"Top Scorer: {top_scorer} with {top_goals} goals!")#this print statement we wrote for  closing the for loop and printing the top scorer in a single line with the (f-string) method....
# find_top_scorer()#calling the function......

def search_players():
    name = input("Enter player name: ")
    for player in players:
        if player["Name"] == name:
            print(f"Name: {player['Name']}")
            print(f"Goals: {player['Goals']}")
            print(f"Assists: {player['Assists']}")
            print(f"Matches: {player['Matches']}")
            return

    print(f"{name} Player Not Found!")

# search_players()

def top_assister(stat):
    t_stats = 0
    for player in players:
        if player[stat] > t_stats:
            t_stats = player[stat]
            top_player = player
    print(f"Top player: {top_player['Name']} with {t_stats} {stat}")

# top_assister("Goals")
# top_assister("Assists")
# top_assister("Matches")

def player_stats():
    for player in players:
        if player["Matches"] > 0:
            average = (f"{player['Goals'] / player['Matches']:.2f}")
            average_assists = (f"{player['Assists'] / player['Matches']:.2f}")
            print("-------------------")
            print(f"Name: {player['Name']}")
            print(f"Goals per Match: {average}")
            print(f"Assists per Match: {average_assists}")
        else:
            print("NO Matches Played!!")

# player_stats()

def update_player():
    update_baller = input("Enter player Name: ")

    upgraded_stats = input("Enter your stat to upgrade: 1.Goals 2.Assists 3.Matches: ")

    updated_value = int(input("Update Player information: "))

    for player in players:

        if player['Name'] == update_baller:

            if upgraded_stats == "Goals":
                player['Goals'] = updated_value
                print(f"Name: {player['Name']} \nUpdated Goals: {updated_value}")
                save_players()
                return

            elif upgraded_stats == "Assists":
                player['Assists'] = updated_value
                print(f"Name: {player['Name']} \nUpdated Assists: {updated_value}")
                save_players()
                return

            else:
                player['Matches'] = updated_value
                print(f"Name: {player['Name']} \nUpdated Matches: {updated_value}")
                save_players()
                return

    print("Player not found")

# update_player()

def delete_player():
    user_input = input("Enter name of the player to remove: ")
    for player in players:

        if player['Name'] == user_input:
            players.remove(player)
            save_players()
            print(f"{user_input} Removed successfully!")
            return

    print(f"{user_input} not found in your players list!")

# delete_player()

def menu():
    while True:
        print("1. Add Player")
        print("2. Show Players")
        print("3. Find Top Scorer")
        print("4. Search Player")
        print("5. Find Top Assister")
        print("6. Find Player Stats")
        print("7. Update Player Information")
        print("8. Delete Player")
        print("9. Exit")

        choice = input("Enter your preferable choice: ")

        if choice == "1":
            name = input("Enter Player Name: ")
            goals = int(input("Enter Goals: "))
            assists = int(input("Enter Assists: "))
            matches = int(input("Enter Matches played: "))
            add_player(name, goals, assists, matches)

        elif choice == "2":
            show_player()

        elif choice == "3":
            find_top_scorer()

        elif choice == "4":
            search_players()

        elif choice == "5":
            stat = input("Enter Stat (Goals/Assists/Matches): ")
            top_assister(stat)

        elif choice == "6":
            player_stats()

        elif choice == "7":
            update_player()

        elif choice == "8":
            delete_player()
            break

        elif choice == "9":
            print("Goodbye!")
            print("Thanks for using the app!...")
            break
    
        else:
            print("Invalid choice! Please enter a valid choice.")


load_players()
# add_player("Messi", 910, 412, 1153)
# add_player("Ronaldo", 971, 261, 1322)
# add_player("Neymar", 476, 286, 763)
# add_player("Sunil Chhetri", 94, 40, 151)
# save_players()
# show_player()
menu()