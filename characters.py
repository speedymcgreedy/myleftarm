# characters module

import random, time
import character
import interactions, altercations, introoutro

# Global constants for the list of items the player can find.
ITEM=['Lamp', 'Broom', 'Pocket knife', 'Machete', 'Alcohol', 'Medicine', 'Oil', 'Lock','Leather clothing',\
          'Brass knuckles', 'Book', 'Spellbook', 'Flashlight', 'Old gun', 'Street clothes']

# Member of the Theives Guild.
def thief(player, status):
    win=True
    if 'Thief necklace' in player.get_hardInventory() and status!='triple':
        print('A thief rushes you!')
        input()
        print('He notices your Thief Necklace and greets you as a friend!')
        print('He shares his latest spoils with you was well.')
        input()
        item=random.choice(ITEM)
        print('He gives you a ', item, '.', sep='')
        interactions.evaluateItem(item, player)
        input()
        return win
    if status=='single' or status=='double': # Thief will steal a random item.
        win=True
        if status=='single':
            print('A Thief rushes you!')
        else:
            print('While you were watching the fight, a Thief rushed you!')
        input()
        if 'Lock' in player.get_inventory(): # 'Lock' beats the thief.
            print('The Thief is fast, but was unable to break your lock.')
            print('He runs away empty-handed.')
        else: # no 'Lock' gets an item stolen
            if len(player.get_inventory())!=0:
                print('The Thief is too fast for you, and your stuff is not secured.')
                stolenItem=player.lose_random_item()
                print('He runs off with your', stolenItem, 'laughing.')
            else: # You have nothing to steal. Lose health
                print('You have nothing to steal. \nThe Thief stabs you in anger.')
                input()
                player.lose_health()
                time.sleep(0.5)
                win=False
    else:
        if 'Thief necklace' in player.get_hardInventory():
            print("The victim was a Thief. \nHe sees your Thief necklace and gives you an item as thanks!")
            input()
            item=random.choice(ITEM)
            print('He gives you a ', item, '.', sep='')
            input()
            interactions.evaluateItem(item, player)
        else:
            print("The victim was a Thief. He agrees to initiate you into the Thieve's Guild!")
            input()
            print('He teaches you to steal, but you are very bad at it.')
            print('You can only use his techniques on defeated enemies.')
            player.gain_hard_item('Thief necklace')
    input()
    return win

# Expelled from the Thieves Guild for harming victims.    
def bandit(player, status):
    win=True
    if status=='single' or status=='double': # Bandit will fight you for your item. Attack=5
        if status=='single':
            print('A Bandit greets you.')
        else:
            print('While you were distracted, a Bandit appears beside you.')
        input()
        fight=random.randint(1,3)
        if fight==1: # no fight, 33%
            print('He seems too tired to bother with you.')
        else:        # fight, 66%
            print('He looks like he is wants your stuff!')
            print('The Bandit ATTACKS!')
            input()
            if player.get_attack()>=5: # Need Machete to win.
                print('You fight off the Bandit. He runs away!')
                if 'Thief necklace' in player.get_hardInventory():
                    print('He disregards the Code of Thieves so you chase him down!')
                    print("You end his violent ways for the sake of the Guild's reputation.")
                    input()
                    interactions.loot(player)
            else:
                if 'Old gun' in player.get_inventory():
                    print('The Old gun misfired!')
                    input()
                print('Your weapon is no match for the Bandit.\nHe beat you up!')
                input()
                if len(player.get_inventory())!=0:
                    stolenItem=player.lose_random_item()
                    print('He walks off with your', stolenItem, 'smiling.')
                else: # You have nothing to steal, lose health.
                    print('You had nothing to steal. \nHe starts kicking you in anger.')
                    kicks=random.randint(1,3) # kicked 1-3 times.
                    input()
                    for x in range(kicks):
                        print('***kick***')
                        player.lose_health()
                        time.sleep(0.5)
                        
                win=False
    else:
        print('The victim was a Bandit. \nHe gives you the last thing he stole as a reward.')
        item=random.choice(ITEM)
        input()
        print('He gives you a ', item, '.', sep='')
        interactions.evaluateItem(item, player)
        if 'Thief necklace' in player.get_hardInventory():
            print('He disregards the Code of Thieves so you put him down anyway!')
            print("You end his violent ways for the sake of the Guild's reputation.")
            input()
            interactions.loot(player)
    input()
    return win

def brawler(player, status):
    win=True
    if status=='single' or status=='double': # Brawler will fight you for 1 life. Attack=4
        if status=='single':
            print('A Brawler is standing over a knocked-out person.')
        else:
            print('A beat-up Brawler is also there.\nHe appears like he was in the fight as well.')
        fight=random.randint(1,3)
        input()
        if fight==1: # no fight, 33%
            print('He seems too tired to fight with you.')
        else:        # fight, 66%
            print('He looks like he is ready for round two!')
            print('The Brawler ATTACKS!')
            input()
            if player.get_attack()>=4: # Need Brass knuckles or better to win.
                print('You knock out the Brawler. He is out cold!')
                if 'Thief necklace' in player.get_hardInventory():
                    interactions.loot(player)
            else:
                if 'Old gun' in player.get_inventory():
                    print('The Old gun misfired!')
                print('Your weapon is no match for the Brawler.\nHe beat you up!')
                input()
                player.lose_health()
                time.sleep(0.5)
                print('The Brawler goes to sleep, preparing for his next fight.')
                win=False
    else:
        print('The victim was a Brawler. \nHe is mad you stopped his fight and attacks your!')
        input()
        if player.get_attack()>=4: # Need Brass knuckles or better to win.
            print('You knock out the Brawler. He is out cold!')
            if 'Thief necklace' in player.get_hardInventory():
                interactions.loot(player)
        else:
            if 'Old gun' in player.get_inventory():
                print('The Old gun misfired!')
            print('Your weapon is no match for the Brawler.\nHe beat you up!')
            input()
            player.lose_health()
            time.sleep(0.5)
            print('The Brawler goes to sleep, preparing for his next fight.')
            win=False
    input()
    return win

def mutant(player, status):
    win=True
    if status=='single' or status=='double': # Mutant will fight you for 1 life. Attack=5
        print('A Mutant emerges from the shadows.')
        fight=random.randint(1,2)
        input()
        if fight==1: # no fight, 50%
            print('He seems to be peaceful.')
        else:        # fight, 50%
            print('He hates all humans!')
            print('The Mutant ATTACKS!')
            input()
            if player.get_attack()>=5: # Need Machete or better to win.
                print('You showed the Mutant that humans are '+\
                      'superior with your stronger weapon!')
                if 'Thief necklace' in player.get_hardInventory():
                    input()
                    interactions.loot(player)
            else:
                if 'Old gun' in player.get_inventory():
                    print('The Old gun misfired!')
                print('Your weapon is no match for the Mutant.\nHe tore you up!')
                input()
                player.lose_health()
                time.sleep(0.5)
                print('The Mutant slinks back into the darkness.')
                win=False
    else:
        print('The victim was a Mutant, you restore his faith in humanity!')
        print('He gives you a Spellbook and Lamp he found earlier that day as thanks.')
        input()
        interactions.evaluateItem('Spellbook', player)
        input()
        interactions.evaluateItem('Lamp', player)
    input()
    return win

def murderer(player, status):
    win=True
    if status=='single' or status=='double': # Murderer will fight you for 2 life. Attack=6
        if status=='single':
            print('A Murderer is standing over his last victim.')
        else:
            print('A Murderer is also in the room, cleaning his blood-soaked knife.')
        fight=random.randint(1,2)
        input()
        if fight==1: # no fight, 50%
            print('He seems to be content with his recent kill.')
            input()
        else:        # fight, 50%
            print('He is filled with bloodlust!')
            print('The Murderer ATTACKS!')
            input()
            if player.get_attack()>=6: # Need Old gun to win.
                print('You shot the Murderer! His reign of terror ends.')
                if 'Thief necklace' in player.get_hardInventory():
                    input()
                    interactions.loot(player)
            else:
                if 'Old gun' in player.get_inventory():
                    print('The Old gun misfired!')
                print('Your weapon is no match for the Murderer.\nHe attempts to kill you!')
                input()
                for x in range(2):
                    player.lose_health()
                    time.sleep(0.5)
                print('The Murderer gets tired of stabbing you and leaves.')
                win=False
    else:
        print('The victim was a known Murderer. He gives you his Machete as thanks!')
        input()
        interactions.evaluateItem('Machete', player)
    input()
    return win

def nurse(player, status):
    win=True
    if status=='single' or status=='double': # Nurse may heal for 2 life or remove Infection. Attack=3
        if status=='single':
            print('A Nurse is in the room with her medicine bag.')
        else:
            print('A Nurse is standing on the outskirts of the fight.')
            print('She sees you and quickly comes closer to you.')
        heal=random.randint(1,2)
        input()
        if heal==1: # heal, 50%
            if 'Infection' in player.get_hardInventory(): # remove infection.
                print('She can tell you are almost blind and heals your Infection.')
                player.lose_hard_item('Infection')
            else: # heal
                print('She sees your wounds and helps to heal you.')
                for x in range(2):
                    time.sleep(0.5)
                    player.gain_health()
            input()
        else: # no heal, 50%
            print('She tells you she does not heal evil people and starts to leave.')
            input()
            print('Enter "yes" to force her to heal you: ', end='')
            forceHeal=input()
            if forceHeal.lower()=='yes' or forceHeal.lower()=='y':
                if player.get_attack()>=3: # Need Machete or better to win.
                    print('You threaten her with your weapon and get healed.')
                    print('Maybe you are evil?')
                    input()
                    for x in range(2):
                        player.gain_health()
                        time.sleep(0.5)
                    if 'Thief necklace' in player.get_hardInventory():
                        print('You already threatened her, so you rob her too!')
                        input()
                        interactions.loot(player)
                        print('You are definitely evil!')
                else:
                    if 'Old gun' in player.get_inventory():
                        print('The Old gun misfired!')
                    print("Your weapon doesn't scare the Nurse.\nShe stabs you with a syringe!")
                    input()
                    for x in range(2):
                        player.lose_health()
                        time.sleep(0.5)
                    print('Your skin burns and your muscles are twitching.')
                    print('She leaves you to your misery.')
                    win=False
            else:
                print('\nYou watch your chance at healing walk away.')
    else:
        print('The victim was a Nurse. She agrees to heal you as thanks!')
        input()
        if 'Infection' in player.get_hardInventory(): # remove infection.
            print('She can tell you are almost blind and heals your Infection.')
            player.lose_hard_item('Infection')
        print('She sees your wounds and helps to heal you.')
        for x in range(2):
            time.sleep(0.5)
            player.gain_health()
    input()
    return win

def alcoholic(player, status):
    win=True
    if status=='single' or status=='double': # Alcoholic might get you drunk.
        print('A drunk man is staggering around the place.')
        input()
        drink=random.randint(1,4)
        if drink==1: # no action, 25%
            print('The man falls over and passes out.')
            input()
            if 'Thief necklace' in player.get_hardInventory():
                print('"Sleeping people are easy targets!" goes through your mind.')
                interactions.loot(player)
        elif drink==2: # infection, 25%
            print('The man thinks you want his precious alcohol for yourself.')
            print('He throws a foul smelling liquid at your face. It burns!')
            input()
            print('As a result, your vision has decreased from an Infection.')
            interactions.infection(player)
            print('Try to locate something to clean your eyes with!')
        else:
            print('The Alcoholic is happy there is another survivor!')
            if status=='single':
                print('He wants to celebrate and you take a drink with him.')
                input()
                for x in range(3):
                    print('And another...\n')
                    time.sleep(0.5)
                print('You get wasted and pass out.')
                input()
                interactions.sleeping(player)
            else:
                input()
                print("You don't have time for his ramblings with a fight occuring in the room!")
                print('You quickly leave the room')
    else:
        reward=random.randint(1,2)
        if reward==1:
            print('The victim was an Alcoholic. \nHe confused you with his real attacker.')
            input()
            print('He throws a foul smelling liquid at your face. It burns!')
            print('As a result, your vision has decreased from an Infection.')
            interactions.infection(player)
            print('Try to locate something to clean your eyes with!')
        else:
            print('The victim was an Alcoholic. He gets you drunk as your reward!')
            input()
            print('You get wasted and pass out.')
            interactions.sleeping(player)
    input()
    return win

def magician(player, status):
    win=True
    if status=='single' or status=='double': # Magician, takes books or attacks
        if status=='single':
            print('A Magician is performing magic on people in the room.')
            print('She seems angry you interupted her ritual.')
            input()
            if 'Spellbook' in player.get_inventory() and 'Handless' in player.get_hardInventory(): # Spellbook wins, remove 'Handless'
                player.lose_item('Spellbook')
                print('You give the Magician your Spellbook. She is very happy now!')
                print('The Magician uses her magic to regrow your hands!')
                player.lose_hard_item('Handless')
                input()
                print('You leave her to practice her new spells from the Spellbook.')
                if 'Thief necklace' in player.get_hardInventory():
                    input()
                    print('Before you left, you notice she is distracted with the Spellbook.')
                    interactions.loot(player)
            elif 'Spellbook' in player.get_inventory(): # Spellbook wins, get 'Wand'
                player.lose_item('Spellbook')
                print('You give the Magician your Spellbook. She is very happy now!')
                print('The Magician gives you a Wand full of magic!')
                input()
                player.gain_item('Wand')
                print('You leave her to practice her new spells from the Spellbook.')
                if 'Thief necklace' in player.get_hardInventory():
                    input()
                    print('Before you left, you notice she is distracted with the Spellbook.')
                    interactions.loot(player)
            elif 'Book' in player.get_inventory(): # Book ties
                player.lose_item('Book')
                print('You give the Magician a Book, telling her it has spells in it.')
                print('You run away while she is distracted by your lie.')
                input()
                win=False
            else: # No book loses
                print('You try to attack, but nothing can beat magic!')
                print('She practices magic on you until she gets bored.')
                input()
                attacks=random.randint(2,5) # 2-5 attacks
                for x in range(attacks):
                    print('***zap***zap***zap***')
                    player.lose_health()
                    time.sleep(0.5)
                print('\nShe finally gets bored and you stagger off.')
                win=False
        elif status=='double':
            print('A magician is also in the room. \nShe is hiding behind a Magical Barrier from the fighters.')
            input()
            print('You decided there is too much action going on and leave the room.')
    else:
        print('The victim was a Magician, and is thankful for your help.')
        print('She gives you a mysterious Amulent!')
        input()
        interactions.evaluateItem('Amulent', player)
    input()
    return win

def groupOfMice(player, status):  # Mice hurt if naked.
    win=True
    if status=='single':
        print('A Group of Mice attacks you!')
    elif status=='double':
        print('The fight has stirred up some mice.\nThey attack you!')
    else:
        print('You help the stranger to get the mice off of them!')
    input()
    if player.get_armor()>0: # Clothing wins.
        print('They are unable to bite through your clothing.')
        print('You swat them off and they scatter away.')
        input()
        player.lose_armor()
    else: # naked will take 2 damage
        win=False
        print('You have no clothes on. \nThe mice easily bite you.')
        input()
        for x in range(2): # 2 dmg
            print('***bite***bite***')
            player.lose_health()
            time.sleep(0.5)
            
    input()
    return win

def wolfpack(player, status): # Wolfpack attacks if no light.
    win=True
    if status=='single':
        print('A Pack of Wolves are running towards you!')
    elif status=='double':
        print('A Pack of Wolves was about to join the frey, but they just noticed you!')
    else:
        print('You kick one of the wolves to stop their attack!')
    input()
    if player.get_vision()>2: # A light source wins.
        print('The wolves get scared off by your light source.')
    else: # No light, 1 damage per wolf
        win=False
        print('There are too many wolves to fight them off. \nEach wolf takes a bite from you.')
        input()
        bites=random.randint(2,4) # 2-4 dmg
        for x in range(bites):
            print('***bite***')
            player.lose_health()
            time.sleep(0.5)
            
    input()
    return win

def spider(player, status): # Spider attacks and maybe infection. 2 Atk
    win=True
    if status=='single':
        print('A large spider jumps at you from the ceiling!')
    elif status=='double':
        print('The fight distracts you from the Spider crawling up your leg!')
    else:
        print('You begin to knock the spiders from their victim.')
    input()
    if player.get_attack()>=2: # A broom wins.
        print('Spiders are fairly weak.')
        print('You easily kill it.')
    else: # No weapon, 1 dmg, maybe infection
        win=False
        if 'Old gun' in player.get_inventory():
            print('The Old gun misfired!')
        print('Spiders are weak, but you have no weapon.\nHe bit you when you squished him!')
        input()
        player.lose_health()
        infection=random.randint(1,4)
        if infection==1: # 25% chance of infection.
            input()
            print('The spiders inside fly everywhere!\nYou got poison in your eye.')
            input()
            print('As a result, your vision has decreased from an Infection.')
            interactions.infection(player)
            print('Try to locate something to clean your eyes with!')
    input()
    return win

def bear(player, status): # Bear mauls and maybe handless. 6 Atk
    win=True
    if status=='single':
        print('A large Bear is in the room eating Honey.\nYou look like a better meal.\nThe Bear charges!')
    elif status=='double':
        print('A large Bear is waiting to eat the loser.\nThe Bear then notices you!')
    else:
        print('You kick the Bear to divert his attention to you!')
    input()
    if player.get_attack()>=6: # Only Old gun wins.
        print('Luckily you had a gun on you.')
        print('You shoot the bear!')
        input()
        print('***BOOM***')
        time.sleep(0.5)
        if status=='single':
            print('\nYou decide to eat his Honey too.')
            input()
            print('***nom***nom***nom***')
            player.gain_health()
    else: # No Old gun, mauling and maybe handless
        win=False
        if 'Old gun' in player.get_inventory():
            print('The Old gun misfired!')
        print('With no gun, the Bear easily takes you down.\nHe begins to maul you!')
        input()
        mauling=random.randint(3,6) # attacks 3-6 times
        for x in range(mauling):
            hands=random.randint(1,10) # 10% chance to lose hands
            if hands==1:
                if 'Handless' not in player.get_hardInventory():
                    print('\nYou try to punch the bear in the face.\nHe bites off your hands!')
                    player.gain_hard_item('Handless')
                    input()
                else:
                    print('***swipe***')
                    player.lose_health()
                    time.sleep(0.5)
                    if hands==2: # 10% chance to lose clothing life.
                        player.lose_armor()
            else:
                print('***swipe***')
                player.lose_health()
                time.sleep(0.5)
                if hands==2: # 10% chance to lose clothing life.
                    player.lose_armor()
    input()
    return win

def alien(player, status):  # Alien loses to 'Wand'.
    win=True
    if status=='single':
        print('An alien is in the room.\nHis mission is to cleanse the world of humans!')
    elif status=='double':
        print('An alien is also in the room watching the fight.\nIt senses you telepathically.')
    else:
        print('You engage the Alien to help the stranger.')
    input()
    if 'Wand' in player.get_inventory() and 'Handless' not in player.get_hardInventory(): # Wand wins.
        print('The Alien starts to attack, so you pull out your Wand.')
        print('You zap the Alien, he was weak to magic!')
        input()
        print('You easily thwart his invasion.')
        print('The wand only had one charge unfortunately. It turned to dust!')
        player.lose_item('Wand')
        player.kill_alien()
        if 'Thief necklace' in player.get_hardInventory():
            input()
            print('The Alien had some items it had gathered for experiments!')
            interactions.loot(player)
    else: # No Wand, 5 damage or probe
        win=False
        print("Only magic can defeat the Alien's mind control.")
        input()
        probe=random.randint(1,2) # 50% chance of probe
        if probe==1 and player.get_armor()>0: # probing, lose clothes
            print('The Alien decides to study you instead of kill you.')
            print('You cannot move. The probing begins!')
            input()
            print('You wake up unharmed, but your clothes are gone...')
            if 'Street clothes' in player.get_inventory():
                player.lose_item('Street clothes')
            else:
                player.lose_item('Leather clothing')
        else:
            print('The Alien uses Mind Blast on you.')
            print('It hurt a lot!')
            input()
            print('***bleep***bleep***BOOM!***')
            time.sleep(0.5)
            for x in range(5): # 5 damage
                player.lose_health()
    input()
    return win

def overseer(player):
    print('Bunch of words')
    for x in range(10):
        player.lose_health()
    input()

def finalOverseer(player):
    print('Words')
    if 'Leather clothing' in player.get_inventory() and player.get_attack()>5: # Player lives
        print('The attack destroyed your Leather clothing, but you destroyed the Overseer!')
        player.lose_item('Leather clothing')
    elif 'Leather clothing' not in player.get_inventory() and player.get_attack()>5:
        print('You shot and killed the Overseer, but his attack killed you as well!')
        input()
        introoutro.endgame(player) # Player loses.
    elif 'Leather clothing' in player.get_inventory() and player.get_attack()<=5:
        if 'Old gun' in player.get_inventory():
            print('The Old gun jammed!')
        print('The attack destroyed your Leather clothing but you are still alive!')
        input()
        print('The Overseer attacked again though and you were not so lucky.')
        print('The Overseer killed you!')
        input()
        introoutro.endgame(player) # Player loses.
    else:
        print('Words about getting ass beat.')
        introoutro.endgame(player) # Player loses.


# In production....
def alienOverlord(player):
    print('You find yourself aboard a strange spacecraft.')
    print('You have thwarted too many Aliens, the Alien Overlord has come to eliminate you!')
    print('The Alien Overlord reaches for its phaser!')
    if 'Amulent' in player.get_inventory() and player.get_attack()>5:
        print('***BOOM***')
        print("Your Amulent gave your bullets magical powers and broke through the Overlord's barrier!")
        print('Direct Hit!')
        input()
        print("Before returning to Earth, you notice a healing tank aboard the room.")
        print("You use the tank to heal your wounds!")
        input()
        if "Infection" in player.get_hardInventory():
            print("The tank has healed your vision! The Infection is gone.")
            player.lose_hard_item('Infection')
        for x in range(10):
            player.gain_health()
        print("You feel much better and use the teleported to return."
        input()
    elif player.get_attack()>5:
        print('***BOOM***')
        print("You bullets bounce off of the Overlord's barrier...")
        input()
        print("He smirks and zaps you with his phaser.")
        print('***Zap***')
        print('You are now a pile of dust.')
        introoutro.endgame(player)
    else:
        if 'Old gun' in player.get_inventory():
            print('The Old gun jammed!')
        print("You have no chance against the Overlord with your current weapon!")
        input()
        print('***Zap***')
        print('You are now a pile of dust.')
        introoutro.endgame(player)
