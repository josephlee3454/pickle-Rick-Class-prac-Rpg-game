from arrs import *
from randomMaker import *
from heal import *
class Game:


    

    def __init__(self):
        self.health = 200
        self.enemy_count = 30
        self.enemy_damage = 5
        self.boss_health = 20
        self.boss_attack = 15
        self.total_enemys_killed = 0
        self.heal = 10
        self.attack = get_attack()
        self.start_story_arr = get_story()

     

    def start_game(self):
        for i in self.start_story_arr:
            input(i)

    def pickleRickle(self):
        input("Pickle Rick is on the third floor awaiting to fight the 70 agents that have been sent down you .... press ***enter to continue during story mode ***")
        input("Pickle Rick have a aresenol of weapons that you have built from things around the office")
        input("The way the game works is you will be propmted with options to heal or attack ")
        while self.enemy_count > 0 and self.health > 0:
            dam_attack = randDamAttack()
            if dam_attack != 0:

                gA = input("Agent Director: men attack \n type heal , attack or rick somthing up  ")
                if gA == "attack":
                    rickSays = get_attack()[randomAtttackMaker()]["saying"]+ " "
                    damageAmt = get_attack()[randomAtttackMaker()]["attack"]
                    self.enemy_count = self.enemy_count - damageAmt
                    self.total_enemys_killed += damageAmt
                    print(f'{rickSays}  {damageAmt} enemys killed ')
                    print(f'total enemys killed {self.total_enemys_killed} out of 70')
                if gA == "heal":
                    
                    self.health = self.health + 25
                    healing(self.health)
                
                if gA == "rick somthing up":
                    rickleTime = 3
                    f_string = f'total hp left {self.enemy_count}'
                    if rickleTime == 3:
                        self.enemy_count -= 35
                        print("Pickle Rick uses a sea shell and blows it like a horn and says great now we are both fucked \n a wierd man in tights pops out and says \n Mr.Nimbus: I am mister nimbus taste my waves of destruction \n he says as he pelvic thrusts in the direction of where his waves go" + f_string)
                    elif rickleTime == 12:
                        self.enemy_count -= 40
                    print("pickle rick builds a make shift mr meekes box \n Mr.Meekes: i'm Mr.Meekes how can i help you \n Rick: kill all who gets in my way \n mr.meekes poofs a uzi out of out of no where and tilts it side ways and says \n Mr.Meekes: Im mr.meekes die mother fucker" + f_string)
            else: 
                self.health -= 20
                print("Agent Director: haha solen'a ni gues you arnt immortal we will kill you")
                print("Rick: You are so dumb im not some mythlogical creature that haunts child dreams i haunt every dream im freddie cougar and the boogie man put together now **burp !!!!!!** its time for you to die ")
        if self.health == 0:
            print("Agent Director: silly littel pickle you met your ultimate demise")

        else:
            print("******************************************************************************\n\n\n\n\n\nAgent Director: How ..... How .... did you take them all out .....\n")
            print("Rick : Lemme check my list of powers and weaknesses umm ...  ability to do anything, but only whenever I want. \n")
            print("Agent Director: solena ? ... pickle ... we can work together yeah together we can achieve so much power \n")
            print("Rick: lick lick lick my balls , **burp !!!** im shutting this shit hole down \n \n")
            print("Agent Director: then you you left me with no choice but to send the worlds most dangerous man wanted in seven different countries .................. To be continued \n\n ")
            print("Morty: yeah bro rick won again, if you havnt noticed its a pretty stacked game heavily in favor of rick \n Rick: shut-up morty its because the world is stacked in my favor if you havnt noticed i am god in this bitch  morty !!!! im a pickle god Morty !!!!! Morty im a fucking pickle God !!!!!!! im pickle Rick !!!!!!")
            


    


game1 = Game()
game1.pickleRickle()
# game1.printAttack()
# dict =[{"attack": 1, "saying": "im pickle rick"},{"attack": 4, "saying": "im amazing !!!!"}]

# print(dict[0]["attack"])
# print(dict[1]["saying"])