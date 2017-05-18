enemies = ('Troll', 'Goblin', 'Harpy', 'Orc', 'Spider')
bosses = ('Cthulu', 'Dragon', 'Berseker')

def loading():
    print ""
    print "LOADING ZONE......"
    print "LOADING ENEMIES..3/6..."
    print "LOADING LANDSCAPE...6/0..."
    print "LOADING ITEMS..8/13..."
    print "SQUASHING BUGS...0/18..."
    print ""
#starts game
def game_start():
    print "Welcome to THE LAND OF SHADOWBROOK!"
    start = raw_input('Type START to begin or HELP for how to play.')
    while start.strip() != 'START' and start.strip() != 'HELP':
        start = raw_input('Type START to begin or HELP for how to play')
    if start == 'START':
        player = gen_character()
        enter_area(player)
    if start == 'HELP':
        print "HELP MENU"
        print "Every thing should be self explanatory"
        print "All input is case sensitive"
        menu = raw_input('Type START to begin game.')
        if menu == 'START':
            player = gen_character()
            enter_area(player)
        else:
            print "ERROR"
            return

#creates player character
def gen_character():
    player = {}
    player['name'] = raw_input('Type a name: ')
    player['type'] = raw_input('wizard, warrior, or page: ')
    if player['type'] == 'wizard':
        player['health'] = 20
        player['attack'] = 5
    elif player['type'] == 'warrior':
        player['health'] = 5
        player['attack'] = 15
    elif player['type'] == 'page':
        player['health'] = 10
        player['attack'] = 10
    elif player['type'] == 'TEST':
        player['health'] = 50
        player['attack'] = 25
        print "You are holding a section of fence. It's a DE-fence."
        print "You also have an atomizer. It's a weapon of MASS destruction."
    return player

#runs credits
def run_credits(player):
    print ""
    print "Thank you for playing THE LAND OF SHADOWBROOK!"
    print "Created by TIME_LORD STUDIOS"
    print "COPYRIGHT FEBRUARY 2017"
    if player['type'] == 'TEST':
        print "Please help me I am being held hostage by Llamas"
        print "--GAME END--"
        print "This game completed by " + str(player['name'])
    else:
        print "This game is over. Thank you for playing."
        print "This game completed by " + str(player['name'])
    EXIT = raw_input("Do you wish to exit the game? yes or no: ")
    if EXIT == 'yes':
        return
    elif EXIT == 'no':
        print "Narrator: Why not?"
        print "Narrator: There's no reason to still be here."
        leave= raw_input("Just type 'leave' to exit the game.")
        if leave == 'leave':
            return
        else:
            print "Narrator: Just gooooooo!!!"
            print "Narrator: What are you waiting for!?"
            print "Narrator: Are you waiting for some super secret cutscene??"
            print "Narrator: THIS. IS. NOT. A. MARVEL MOVIE!!!"
            stop = raw_input('just type stop to end the game.')
            if stop == 'stop':
                return
            else:
                print "Narrator: Fine..."
                secret_cutscene()
                print "Narrator: Happy now?"
                happines = raw_input('yes or no')
                if happines == 'yes':
                    return
                else:
                    print "Narrator: Fine. Forget you. I don't need your attention."
                    return
        
#used to choose zone
def enter_area(player):
    loading()
    import random
    z = random.randint(1,20)
    if z >= 10:
        y = True
        print "You find yourself in a dungeon"
    else:
        y = False
        print "You find yourself in a forest"
    if y == True:
        print ""
        print "There are two hallways ahead of you"
        print "You hear wispered conversation eminating from the right hallway."
        print "There is a strange glow coming from the hall to the left."
        choose_hall = (raw_input("left or right: "))
        if choose_hall == 'left':
            loading()
            castle_left(player)
        elif choose_hall == 'right':
            loading()
            castle_right(player)
    elif y == False:
        print ""
        print "There are paths through the woods left and right."
        print "The path to the left leads to a clearing."
        print "The right path is lined with bones and has no noticable end."
        choose_path = (raw_input("left or right: "))
        if choose_path == 'left':
            loading()
            forest_left(player)
        elif choose_path == 'right':
            loading()
            forest_right(player)

#left path in dungeon
def castle_left(player):
   print ""
   print "You enter the room to see a large glowing crystal surrounded by monsters."
   print "The monstrs attack you."
   battle(player) 
   if player['health'] > 0:
        print ""
        print 'You defeated the monsters and approched the crystal'
        print 'As you reach out to touch the crystal there is a flash of light'
        print 'When your vision clears you find yourself in a solid stone room with a gold door and a silver door.'
        print 'You walk towards the door a golem emerges from the ground in fornt of you.'
        print "Golem: 'Welcome brave warrior to the hall of choices.'"
        print 'The golem opens its hands to reveal two keys.'
        print "Golem: 'The golden door leads to a great treasure. However, it is gaurded by a powerful enemy.'"
        print "Golem: 'The silver door leads to a great weapon. But to claim it you must pay a price.'"
        key_choice = raw_input("Choose gold or silver key. ")
        if key_choice == 'gold':
            print "You grab the golden key and unlock the golden door."
            print "You hesitate a moment before stepping through the opening."
            loading()
            key_gold(player)
        elif key_choice == 'silver':
            print ""
            print "You grab the silver key and unlock the silver door."
            print "You hesitate a moment before stepping through the opening."
            loading()
            key_silver(player)
   else:
        run_credits(player)

#right path in dungeon    
def castle_right(player):
    print ""
    print "You walk down the right hallway."
    print "The room is rather plain and has another door on the opposite wall."
    print "You look around and see three people chained to the wall and a goblin asleep against the opposite wall."
    print "Prisoner 1: 'Shhh, be quiet if he wakes up he'll call his friends.'"
    print "Prisoner 2: 'Please, get us out of these chains. The key should be over there by the gaurd.'"
    free_prisoners = raw_input("Do you free the prisoners or continue on? yes or no: ")
    if free_prisoners == 'yes':
        print ""
        print "You wallk over to the gaurd. You grab the key."
        print "Prisoner 3: 'Hey buddy. While you're over there why don't you kill the gaurd?'"
        kill_gaurd = raw_input("Kill the gaurd? yes or no: ")
        if kill_gaurd == 'yes':
            print ""
            print "As you draw your sword a second goblin walks in from the other door, sees you and blows a horn."
            print "His horn wakes the first gaurd and brings other monsters"
            battle(player)
            if player['health'] > 0:
                print ""
                print "You kill the gaurd and his friends and free the prisoners."
                print "Prisoner 1: 'Thanks guy. Here take this.'"
                if player['type'] == 'warrior':
                    print "He hands you an amulet."
                    print "BERZEKERS AMULET: +5 health"
                    player['health'] += 5
                elif player['type'] == 'wizard':
                    print "He hands you an ancient tome."
                    print "TOME OF FIRE: +5 attack"
                    player['attack'] += 5
                elif player['type'] == 'page':
                    print "He hands you a cloak"
                    print "CLOAK OF SHADOWS: +5 attack +5 health"
                    player['attack'] += 5
                    player['health'] += 5
                print "After taking the item you exit the room."
                castle_right2a(player);
            else:
                print "The monsters numbers overwealmed you and you were slain."
        elif kill_gaurd == 'no':
            print "You unlock the shackles of the prisoners."
            if player['type'] == 'warrior':
                print "He hands you an amulet."
                print "BERZEKERS AMULET: +5 health"
                player['health'] += 5
            elif player['type'] == 'wizard':
                print "He hands you an ancient tome."
                print "TOME OF FIRE: +5 attack"
                player['attack'] += 5
            elif player['type'] == 'page':
                print "He hands you a cloak"
                print "CLOAK OF SHADOWS: +5 attack +5 health"
                player['attack'] += 5
                player['health'] += 5
            print "After taking the item you exit the room."
            castle_right2a(player);
    elif free_prisoners == 'no':
        print "You walk through the room and ignore the prisoners"
        print "ERROR: Code not found"

#second path in castle
def castle_right2a(player):
    button = False
    key = False
    print "As you leave the room you see a door on either side of the hallway and a larger door at the end."
    inspect = raw_input("Inspect large door? yes or no: ")
    if inspect == 'yes':
        if button == False:
            print "As you walk to open the door the floor opens below you and you fall into a pit of spikes killing you instantly."
        else:
            if key == False:
                print "The door has a large lock preventing you form opening it."
                print "
    elif inspect == 'no':
        doors = raw_input("left or right door: ")
        if doors == 'left':
            print "You enter the left room and find a group of monsters."
            battle(player)
            if player['health'] > 0:
                print "You killed the monsters and a chest appeared in the room's center."
                print "You opened the chest and found a key."
                print "Obtained SMALL KEY!"
                key == True
                print "You leave the room and reenter the hallway."
                inspect2 = raw_input("Inspect large door? yes or no: ")
                if inspect2 == 'yes'
            

#left path in forest
def forest_left(player):
    print "You walk down the left path and enter the clearing."
    print "Apon entering the clearing you find that it is filled with monsters."
    battle(player)
    if player['health'] > 0:
        print "You defeat the monsters."
        print "At the center of the clearing is a pile of weapons."
        grab_weapon = raw_input("Do you take a weapon from the pile? yes or no: ")
        if grab_weapon == 'yes':
            if player['type'] == 'wizard':
                print "You rummage through the pile and find a crystal."
                print "PHILOSEPHERS STONE: +5 attack"
                player['attack'] += 5
            elif player['type'] == 'warrior':
                print "You search the pile and find a crude set of armor."
                print "GOBLIN ARMOR: +5 health"
            elif player['type'] == 'page':
                print "You dig through the pile to find a large sheild."
                print "ROMAN SHEILD: +5 health +5 attack"
                player['health'] += 5
                player['attack'] += 5
    print "You continue on through the clearing and back into the forest."
    print "Error: code not found"
    
def forest_right(player):
    global enemies
    enemies = ('Cannibal')
    print ""
    print "You walk down the path and see a variety of bones. Some are human but some are... not."
    print "You continue to walk down the path. After a while you decide to make camp."
    print "You find and kill a rabbit to eat for dinner. After eating you make a bed of leaves."
    print "You feel a swaying sensation. You open your eyes to find yourself in a brightly lit clearing."
    print "Everything seems to be upside down. You look around to see a camp of cannibals."
    print "The camp is mostly empty and your weapons are on the ground a few feet away."
    struggle = raw_input("Try to break free? yes or no: ")
    if struggle == 'yes':
        print ""
        print "You struggle and manage to free your right arm."
        print "You streach and manage to retrieve your weapon."
        print "You cut yourself free and gather your things just as the tribe returns."
        battle(player)
        if player['health'] > 0:
            print ""
            print "You defeated the cannibals and flee the camp deeper into the forest."
            print "After weeks of stumbling through the forest you come to a town and colapse in the street."
            print "The doctor there treats your wounds and you return home."
            run_credits(player)
        else:
            print "You were killed and eaten by the cannibals."
    elif struggle == 'no':
        print "You did nothing and were roasted by the cannibals."
        run_credits(player)
    global enemies
    enemies = ('Troll', 'Goblin', 'Harpy', 'Orc', 'Spider')

def key_gold(player):
    print ""
    print"You enter the room to see a boss monster gaurding a hoard of gold and jewels."
    boss_fight(player)
    if player['health'] > 0:
        print ""
        print "BAG OF HOLDING: +Infinite Iventory"
        print "You defeated the boss and claimed the treasure."
        print "You exited the dungeon and returned home."
        run_credits(player)
def key_silver(player):
    print ""
    print "You enter the room to see the weapon of legends on a pedestal."
    print "There is a mage standing behind the pedestal."
    print "Mage: 'Welcome " + player['name'] + "'"
    print "Mage: 'Do you wish to claim the weapon?"
    claim_item = raw_input('Claim the weapon? yes or no')
    if claim_item == 'yes':
        print ""
        print "Mage: 'If you really wish to claim this item you must give up what you hold dear.'"
        if player['type'] == 'wizard':
            print "You claim the item and feel your magical ability leave your body."
            print "BOOK OF CREATION"
            run_credits(player)
        elif player['type'] == 'warrior':
            print "You claim the item and feel your courage leave your body."
            print "MEDAL OF UNHARMING"
            run_credits(player)
        elif player['type'] == 'page':
            print "You claim the item and lose the trappings of your proffesion."
            print "CROWN OF SHADOWBROOK"
        elif player['type'] == 'TEST':
            print "You reach out and grab the jar of pickles."
            print "JAR OF PICKLES: -Infinite hunger"
    elif claim_item == 'no':
        print ""
        print "You decide to do nothing and exit the dungeon to return home."
    run_credits(player)

#def castle_right2(player):
    

#used to fight monsters    
def battle(player):
    import random
    fight = 1
    while player['health'] > 0 and fight < 5:
        print random.choice(enemies)
        x = random.randint(0,23)
        print "Enemy attack: " + str(x)
        if player['attack'] > x:
            print "The monster was slayed."
            fight += 1
        elif x > player['health']:
            print "The Monster vanquised the hero."
            player['health'] = 0
            fight += 5
        else:
            print "The battle was long and hard."
            health = player['health'] - x
            if health > 0:
                fight += 1
            else:
                print "You have died"
                fight += 5

def boss_fight(player):
     import random
     fight = 1
     boss = random.choice(bosses)
     boss_health = 50
     x = random.randint(5,30)
     while player['health'] > 0 and fight < 5:
         print boss
         print boss_health
         print "Boss attack: " + str(x)
         if player['attack'] > boss_health:
             print "Boss slain."
         elif x > player['health']:
             print "You were slain by " + boss
             player['health'] = 0
             fight += 5
         else:
             print "The boss landed a solid hit."
             health = player['health'] - x
             if health > 0:
                 fight += 1
             else:
                 print "You have died"
                 fight += 5
def secret_cutscene():
    print ""
    print "Goblin 1: 'Hey guys???'"
    print "Goblin 2: 'Yeah Boris?'"
    print "Goblin 1: 'Where are we?'"
    print "Goblin 2: 'Um... I think we're dead.'"
    print "Death: Welcome to the monser afterlife. Would you like to respawn?"
    print ""
    
game_start()