import copy
import random

import characters

gameDev = "Gregory J Coates"
website = "www.gregoryjcoates.com"
playerCharacter = characters.theHero
gameOver = False
gameWon = False

numRooms = 0
killedBy = "empty"
roomDict = {"Direction": {"Empty, Chest, Enemy", "new directions"}}

playerName = "The Hero"

directions = ["north", "east", "south", "west", "secret door"]

chestItems = ["Mimic", "Bomb", "Questionable Potion", " Potion", "Elixir of Life"]

commands = directions

gregList = ["greg", "gregory", "coates", "gregory coates", "gregory j coates"]

chestMessage = ["You see a glint down the hall to the ",
                "Something shinny catches your eye toward the "]

monsterMessage = ["You saw something move down ",
                  "There was something shinny toward the "]

emptyMessage = ["It looks empty down ",
                "You see nothing towards the "]


def welcomemessage(pName, numrooms):
    return "Welcome {} to my dungeon!\n" \
           "There is no going back now if you can make it through {} rooms you will find me!\n" \
           "but beware while all paths lead here some are deadlier than others.".format(pName.capitalize(),
                                                                                        numRooms)


def altWelcomeMessage(pName, numrooms):
    return "Welcome {} to my dungeon!\n" \
           "There is no going back now if you can make it through {} rooms you will find me!\n" \
           "but beware while all paths lead here some are deadlier than others.\n" \
           "Wait... you are me? Well I have been trapped down here against my will" \
           "so you must break free from the dungeon".format(pName.capitalize(), numRooms)


enemies = {"slime": characters.slime,
           "minotaur": characters.minotaur,
           "white rabbit": characters.whiteRabbit,
           "golem": characters.golem,
           "hero": characters.hero,
           "dragon": characters.dragon}

specialEnemies = {"dungeon master": characters.greg,
                  "mimic": characters.mimic,
                  "true slime": characters.rimuru}


def openchest(luck):
    # uses the players luck and rolls for the item in the chest
    chance = (luck * random.randrange(0, 3)) + random.randrange(0, 50)

    while input("You found a chest, enter 'open chest' to continue:").lower() != "open chest":
        pass
    if chance > 10:
        roll = random.randrange(2,4)
        item = chestItems[roll]
    else:
        if chance < 5:
            item = chestItems[0]
        else:
            item = chestItems[1]

    if item == chestItems[0]:
        print('The chest is a mimic! Haha!\n')
        battle(mimic=True)
    elif item == chestItems[1]:
        print("The chest contains a bomb\n")
        healthLost = random.randrange(0, 3)
        playerCharacter.health -= healthLost
        print("The bomb exploed and you lost {} health".format(healthLost))
    elif item == chestItems[2]:
        print("You drink a {}".format(chestItems[2]))
        healthChange = random.randrange(-3, 3)
        if healthChange > 0:
            print("You gained {} health".format(healthChange))
        elif healthChange < 0:
            print("You lost {} health".format(healthChange))
        else:
            print("It did nothing")
        playerCharacter.health += healthChange
    elif item == chestItems[3]:
        healthGained = random.randrange(2, 5)
        playerCharacter.health += healthGained
        print("You gained {} health".format(healthGained))
    elif item == chestItems[4]:
        healthGained = random.randrange(5, 10)
        playerCharacter.health += healthGained
        print("You gained {} health".format(healthGained))


def ui():
    print("\ncommands are:", end=" ")
    for command in commands:
        print(command + ",", end=" ")
    print()
    print("You have {} health and {} rooms left\n".format(playerCharacter.health, numRooms))


def playername():
    global playerName
    global playerCharacter

    playerName = input("What is your name?:").lower()
    print("You entered {} as your name.\n".format(playerName.capitalize()))
    if playerName in gregList:
        playerCharacter = copy.copy(characters.greg)
    elif playerName == "bell":
        playerCharacter = copy.copy(characters.bell)
    elif playerName == "zelda":
        playerCharacter = copy.copy(characters.zelda)
    elif playerName == "rimuru":
        playerCharacter = copy.copy(characters.rimuru)
    elif playerName == "":
        playerCharacter = copy.copy(characters.theHero)
        playerName = "The Hero"
    else:
        playerCharacter = characters.theHero


def room(direction="empty"):
    # Creates exits, rooms, and what is in them
    exits = []
    rooms = {}
    item = "empty"
    while len(rooms) == 0:
        for x in range(0, len(directions)):
            if random.randrange(0, 10) > 5:
                exits.append(directions[x])
        if direction in exits:
            exits.remove(direction)

        for x in range(0, len(exits)):
            if random.randrange(0, 10) > 6:
                item = "chest"
            else:
                if random.randrange(0, 1000) > 300:
                    item = "monster"
            rooms[exits[x]] = [item]

        for key in rooms:
            if rooms[key][0] == "chest":
                rooms[key].append(chestMessage[random.randrange(0, len(chestMessage))])
            elif rooms[key][0] == "monster":
                rooms[key].append(monsterMessage[random.randrange(0, len(monsterMessage))])
            else:
                rooms[key].append(emptyMessage[random.randrange(0, len(emptyMessage))])

    if gameWon == False and gameOver == False:
        for key in rooms:
            print(rooms[key][1] + key)
    print()
    return rooms


def checkinput(pInput, rooms):
    cFail = False
    while cFail == False:
        if pInput in commands:
            if pInput in rooms:
                if rooms[pInput][0] == "monster":
                    # move rooms, start battle
                    battle()
                    cFail == True
                    return pInput
                if rooms[pInput][0] == "chest":
                    openchest(playerCharacter.luck)
                    cFail == True
                    return pInput
                else:
                    cFail == True
                    return pInput
            else:
                print("Command valid but not for this room")
                pInput = input("Enter command:").lower()
        else:
            print("Not a valid command")
            pInput = input("Enter command:").lower()


def battle(boss=False, mimic=False):
    if boss == True:
        enemy = copy.copy(characters.greg)
    elif mimic == True:
        enemy = copy.copy(characters.mimic)
    else:
        enemy = copy.copy(random.choice(list(enemies.values())))

    enemyCopy = copy.copy(enemy)
    print("You have run into", enemy.name, "\n")
    print(playerCharacter)

    print("VS\n")
    print(enemy.enemy())
    while input("Enter 'fight' to continue:") == False:
        pass
    while (playerCharacter.health >= 0) or (enemy.health >= 0):
        # Player attacks
        if dodge(enemy) == True:
            print("Enemy dodged attack")
        else:
            healthLost = playerCharacter.muscle + random.randrange(- int(playerCharacter.muscle / 2), 5)
            enemy.health -= healthLost
            print("You did {} damage".format(healthLost))
        if enemy.health <= 0:
            break
        # Enemy attack
        if dodge(playerCharacter) == True:
            print("You dodged")
        else:
            healthLost = enemy.muscle - int(enemy.muscle / playerCharacter.muscle) + random.randrange(-5, 0)
            playerCharacter.health -= healthLost
            print("You lose {} health".format(healthLost))

    if playerCharacter.health <= 0:
        global gameOver
        global killedBy
        print("you died\n")
        killedBy = enemyCopy
        gameOver = True
    elif enemy.health <= 0 and boss == True:
        global gameWon
        gameWon = True
    elif enemy.health <= 0:
        print(" You won the fight")
        print("Stats are: health, strength, dodge, and luck")
        if boss == False:
            while not getstats(input("Enter the stat you want gain:").lower()):
                pass


def getstats(pInput):
    if pInput == "dodge":
        playerCharacter.dodge += 1
        print("You chose dodge\n")
        return True
    elif pInput == "strength":
        playerCharacter.muscle += 1
        print("You chose strength\n")
        return True
    elif pInput == "health":
        playerCharacter.health += 1
        playerCharacter.maxHealth += 1
        print("You chose health\n")
        return True
    elif pInput == "luck":
        playerCharacter.luck += 1
        print("You chose luck\n")
        return True
    else:
        return False


def moveroom(pInput):
    global numRooms
    print("You have moved through the {} door and it closes behind you.\n".format(pInput))
    ui()
    numRooms -= 1
    if numRooms == 0:
        endRoom()

    return room(pInput)


def dodge(character):
    if character.dodge >= 10:
        if character.dodge * random.randrange(0, 4) > 35:
            print("attack dodged")
            return True
        else:
            return False
    else:
        if character.dodge * random.randrange(0, 5) > 16:
            print("attack dodged")
            return True
        else:
            return False


def endRoom():
    if playerCharacter.name == characters.greg:
        print("Which one of is the real dungeon master?")
        battle(True)
    else:
        print("Mwahahaha I am the dungeon master")
        battle(True)


def gameloop():
    # The main game loop
    if playerCharacter == characters.whiteRabbit:
        enemies["hero"] = characters.bell

    global numRooms
    numRooms = random.randrange(5, 20)

    if playerCharacter.name == characters.greg.name:
        print(altWelcomeMessage(playerName, numRooms))
    else:
        print(welcomemessage(playerName, numRooms))

    ui()
    rooms = room()

    while gameOver == False:

        playerI = checkinput(input("Enter command:").lower(), rooms)

        if (gameOver == False) or (gameWon == False):
            rooms = moveroom(playerI)

        if gameWon == True:
            break
        if gameOver == True:
            break


playername()
gameloop()
if gameOver == True:
    print(" You thought you could get out that way?")
    print("Mwahaha!\n")
    gameOver = False
    playerCharacter = killedBy
    gameloop()
if gameWon == True:
    print("You won {}".format(playerName))
    print("made by {}".format(gameDev))
    print("Visit my website {}".format(website))
