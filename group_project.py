#dollar store oregon trail by Emma and Cooper and Nate 

#text that says you are in the dollar store oregon trail, you have a wife and a kid, and a wagon hauled by an ox with little supplies. Your goal is to get from minnesota to oregon. - cooper
print("Welcome to the dollar store Oregon trail! You are trying to get from Minesota to Oregon. You have a spouse and a kid, and a wagon hauled by an ox with little supplies.\n")

#You have to pass through five states, there is a challenge in each state - emma
print("You have to pass through five states, each state has a challenge\n")

#create a user input function that asks your name, your spouse name, your kids name, and the ox's name - nate
usersname = input("What is your name?:\n")
def usernames(Rname):
    names = input(f"What is your {Rname}'s name?:\n")
    return names
spouse = usernames("spouse")
child = usernames("child")
ox=usernames("ox")

#assign loop variables for each question that will be used to tell the loop at the end that the question was right or wrong. This allows t a score to be made, and will print your score after winning, or when you answer wrong - Cooper and cooper's dad

q1 = ("")
q2 = ("")
q3 = ("")
q4 = ("")
q5 = ("")
score=0

#create a function that states you died because you were stupid. This will be called later whenever you make a wrong descicion- cooper


def youdied(spouse, child, ox):
    
    Death = (f"You, {spouse}, {child}  and  {ox}  died because you are stupid. please refresh if you want to try again")
    
    return Death
deathmessage = youdied(spouse,child,ox)



#if statement that asks if you want to travel over the mountains or through the plains - nate
MtnsOrPlns = input("How will you continue? will you travel over the mountains? or to the plains?(answer with 'plains' or 'mountains')\n")
if MtnsOrPlns == "mountains":
    #IF YOU CHOSE OVER THE MOUNTAINS, THIS SECTION OF CODE WILL START
    
    #First challenge is in north dakota, your family is starving, will you hunt or eat your supplies question 1/5, your in minnesota - cooper
    challenge1mtn = input("You start journeying through Minnesota, your family is starving, do you go hunt or use supplies? (type 'hunt' or 'supplies')\n")
    
    #if you chose to eat your supplies you didnt have enough and you died - emma
    if challenge1mtn == ("supplies"):
        q1 = "wrong"
        print("you didnt have enough supplies, so", deathmessage)
       
        #if you chose too go hunt, are you hunting deer or a bear question 2/5 your in north dakota - nate
        
    if challenge1mtn == ("hunt"):
        q1 = ("right")
        print("Great! lets go hunting")
        challenge2mtn = input("you cross into north dakota looking for game, should you hunt 'deer' or 'bear?':\n")
        
        #if you chose bear, you get eaten and die - cooper
        if challenge2mtn == ("bear"):
            q2 = ("wrong")
            print("you got mauled and chewed on,", deathmessage)
        
        #if you chose deer, you live and feed your family, but it wasnt a whole lot - emma 
        if challenge2mtn == ("deer"):
            q2 = ("right") 
            print("Good choice, bears are very dangerous! you hunt a deer and feed your family")
            challenge3mtn = input("you get to montana, the family is very hungry. Use supplies or go fishing? ('supplies' or 'fishing'\n")
            
            #if you use supplies, not enough and ya die - cooper
            if challenge3mtn == ("supplies"):
                q3 = ("wrong")
                print("did you not learn? you dont have enough.", deathmessage)
            
            #if you fish, you get a lucky massive trout, and feed your family - emma
            if challenge3mtn == ("fishing"):
                q3 = ("right")
                print("whoah! after a few hours you got a huge bass and fed your family plenty. Good choice\n")
                
                #you arrive in idaho, set up camp in the cold winter, or stay in someones cabin question 4/5 - nate
                challenge4mtn = input("you arrive in the frigid north idaho. Should you set up camp or stay in someones cabin? ('camp' or 'cabin')\n")
                
                #if you decide to sleep in cabin, you sleep in a man named thomas creech's cabin. you get murdered - cooper
                if challenge4mtn == ("cabin"):
                    q4 = ("wrong")
                    print("you find a man named Thomas Creech, he lets you sleep in his cabin, but jokes on you, hes a wanted serial killer.", deathmessage,)
                
                #if you set up camp, its cold, but your family endures. - emma
                if challenge4mtn == ("camp"):
                    q4 = ("right")
                    print("safe choice! stranger danger after all. You set up camp and hudle together until the next mornin'\n")
                    
                    #you get to the final stretch in oregon, do you set up camp again or push through - nate
                    challenge5mtn = input("you finally get to the final stretch in oregon! should you set up camp again to sooth your aching feet? or push through and risk injury? ('camp' or 'push')\n ")
                    
                    #if you set up camp, you get bit by a rattlesnake and die in your sleep - cooper
                    if challenge5mtn == ("camp"):
                        q5 = ("wrong")
                        print("Oh no! as luck would have it, as you were sleeping, you got bit by a rattlesnake!",deathmessage)
                    
                    #if you push through, you make is and win with your family - emma
                    if challenge5mtn == ("push"):
                        q5 = ("right")
                        print("interesting choice, you made a risky desicion but you made it! Congratulations, you win. Refres to play again")

                    


if MtnsOrPlns == "plains":
        
        #IF YOU DECIDED TO GO THROUGH THE PLAINS, THIS SECTION ACTIVATES
        challenge1pln = input("you and your family are halfway through minesota,and get hungry. Shall you hunt or use your supplies? ('hunt' or 'supplies')\n")
        if challenge1pln == ("supplies"):
            q1 = ("wrong")
            print("are you dumb? your supplies were laced with e-coli for some reason. your whole family got dysentery.", deathmessage)
        if challenge1pln == ("hunt"):
            q1 = ("right")
            
            #If you chose to hunt, you can either hunt bison or a bunch of prarie dogs in south dakota question 2/5 - nate
            challenge2pln = input("good choice. As you arrive in south dakota you ask the question, should you hunt bison or a bunch of prairie dogs? ('bison' or 'prairie dogs'. be carful of spelling)\n")
            
            #if you hunt bison, you get trampled and die - cooper
            if challenge2pln == ("bison"):
                q2 = ("wrong")
                print("you tried to get a lone bison, but the herd was near, and trampled you.", deathmessage)
            
            #if you hunt prarie dogs, you get a bunch and they last you and your family - emma 
            if challenge2pln == ("prairie dogs"):
                q2 = ("right")
                print("interesting choice. nonetheless you rack up a dozen of these rodents and feed your family\n")
                
                #you arrive in wyoming, unbeknownst to you the prarie dogs had Tuberculosis, and your whole family is infected. Thug it out or ge a witch doctor to to a magic dance around your fire - nate
                challenge3pln = input("as you step into wyoming, you make a discovery. The prairie dogs had tuberculosis!! Now your whole family is infected. Should you try to thug it out? or find a witch doctor?('thug' or 'witch')\n")
                
                #if you thug it out, you die - cooper
                if challenge3pln == ("thug"):
                    q3 = ("wrong")
                    print("Are you actually dumb? its tuberculosis.", deathmessage)
                
                #if you chose the witch doctor, your family is completely cured. - emma
                if challenge3pln == ("witch"):
                    q3 = ("right")
                    print("wierd choice, but you find a witch doctor off the side of the trail, and ask him to cure your family. he agrees, and does a wierd tribal ritual dance around your campfire that resembles the cha cha slide mixed with the nae nae. This seems to cure you and your family.")
                    
                    #you arrive in idaho, your kid wants to take a break and play. do you be a good father and play tag or shrug him off - nate
                    challenge4pln = input("once in idaho, your kid wants to take a break and play tag. be a good parent and play tag? or shrug him off? ('play' or 'shrug')\n")
                    
                    #if you play with little jimmy, he sprains his ankle and dies. - cooper
                    if challenge4pln == ("play"):
                        q4 = ("wrong")
                        print("Oh no! as you and your kid were running on rough terrain, he breaks his anke and dies. you lost the game" )
                    
                    #if you shrug him off, you avoid catrastrophe and move on. - emma 
                    if challenge4pln == ("shrug"):
                        q4 = ("right")
                        print("you avoid the rough terrain and move on with the journey, allbeit your kid is grouchy now\n")
                        
                        #your in oregon, the final stretch, your family is impatient. do you pick up the pace or play it safe - nate
                        challenge5pln = input("on the last leg of the journey in oregon, your family is getting impatient. Do you pick up the pace? or keep slowing down the fun? ('faster' or 'slow')\n")
                        
                        #if you pick up the pace, you trip, break your arm, sever your carotid artery, and die - cooper
                        if challenge5pln == ("faster"):
                            q5 = ("wrong")
                            print("You tripped over an atom sized pebble, fall and slice your carotid artery open and", deathmessage)
                        
                        #if you play it safe, your family makes it safe and sound and you win - emma 
                        if challenge5pln == ("slow"):
                            q5 = ("right")
                            print("CONGRATULATIONS! You made it safe and sound to your final destination and won the game. Refresh to play again.")
#loop that counts a score based on users questions answered correctly - cooper and coopers dad
right_wrong = [q1,q2,q3,q4,q5] 
score_check = "right"
for item  in  right_wrong:
    if item == score_check: score+=1
    else: score+=0

print("you got",score,"out of 5 questions correctly")
