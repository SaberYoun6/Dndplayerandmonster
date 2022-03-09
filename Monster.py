#!/usr/bin/env python3





Class Monster(object):

    def __init__(self,type_of_mon,Health_Points,Armour_Class,Legendary_Actions, Initivitive, Size, strength,dex,cons,wis,intelligence,cha,skills):
        self.type_of_mon = type_of_mon 
        self.Health_Points = Health_Points
        self.Armour_Class = Armour_Class
        self.Legendary_Actions = Legendary_Actions
        self.Initivitive = Initivitive 
        self.Size = Size
        self.strength =strength 
        self.dex = dex
        self.cons = cons
        self.wis = wis
        self.intelligence = intelligence
        self.cha = cha
        self.skills = skills
    #types of monsters
    def type_of_monsters(self):
        mon_type = 0
        if self.type_of_mon.equals("oozes"):
            mon_type = 1
        elif self.type_of_mon.equals("dragon"):
            mon_type  = subtype_of_Dragon()
        elif self.type_of_mon == "gaint":
            mon_type = subtype_of_gaints()
        elif self.type_of_mon == "humanoid":
            mon_type = 4
        elif self.type_of_mon = "undead":
            mon_type = 5
        elif self.type_of_mon = "Aberration":
            mon_type = 6
        elif self.type_of_mon == "Beast":
            mon_type = 7
        elif self.type_of_mon == "celestial":
            mon_type =  subtype_of_Celestail()
        elif self.type_of_mon == "construct":
            mon_type = 9
        elif self.type_of_mon == "elementals":
            mon_type = 10
        elif self.type_of_mon == "fey":
            mon_type = 11
        elif self.type_of_mon = "fiends":
            mon_type = 12
        elif self.type_of_mon = "demons":
            mon_type = 13
        elif self.type_of_mon = "devil":
            mon_type = 14
        elif self.type_of_monf = "Monstrosities":
            mon_type = 15
        elif self.type_of_mon = "plant":
            mon_type = 16
        else:
            mon_type = 17
        return mon_type
    def subtype_of_Dragon():
        mon_type = ()
        if type_of_dragon = input("Black, Blue, Green, Red,White ,Brown, Gray, Purple, Pink, Salt, Yellow ,Brass, Bronze, Copper, Gold, Siliver,Cobalt, Iron,Platinum, Steel,Electrum, Turtles, Drakes, PSeudodragon, Natural, Amber ,Ruby, Sapphire, Amethyst, Crystal, Emerald, Topaz, Pearl, Obsidian, Shadow, Faeire, Astral, Ethereal, Rust, Radient, Mirage, Howling, Lung, ...")
        if type_of_dragon == "Black":
            mon_type = (2,1)
        elif type_of_dragon == "Blue":
            mon_type = (2,2)
        elif type_of_dragon == "Green":
            mon_type = (2,3)
        elif type_of_dragon == "Red":
            mon_type = (2,4)
        elif type_of_dragon =="White":
            mon_type = (2,5)
        elif type_of_dragon =="Brown":
            mon_type = (2,6)
        elif type_of_dragon =="Gray":
            mon_type = (2,7)
        elif type_of_dragon =="Purple":
            mon_type = (2,8)
        elif type_of_dragon =="Pink":
            mon_type = (2,9)
        elif type_of_dragon =="Salt":
            mon_type = (2,10)
        elif type_of_dragon =="Yellow":
            mon_type = (2,11)
        elif type_of_dragon =="Brass":
            mon_type = (2,12)
        elif type_of_dragon =="Bronze":
            mon_type = (2,13)
        elif type_of_dragon =="Copper":
            mon_type = (2,14)
        elif type_of_dragon =="Gold":
            mon_type = (2,15)
        elif type_of_dragon =="Silver":
            mon_type = (2,16)
        elif type_of_dragon =="Cobalt":
            mon_type = (2,17)
        elif type_of_dragon =="Iron":
            mon_type = (2,18)
        elif type_of_dragon =="Platinum":
            mon_type = (2,19)
        elif type_of_dragon =="Steel":
            mon_type = (2,20)
        elif type_of_dragon == "Tutrles":
            mon_type = (2,21)
        elif type_of_dragon == "Drake":
            mon_type = (2,22)
        elif type_of_dragon == "Psudeodragons":
            mon_type = (2,23)
        elif type_of_dragon == "Natural":
            mon_type = (2,24)
        elif type_of_dragon =="Amber":
            mon_type = (2,25)
        elif type_of_dragon =="Ruby":
            mon_type = (2,26)
        elif type_of_dragon =="Amethyst":
            mon_type = (2,27)
        elif type_of_dragon =="Crystal":
            mon_type = (2,28)
        elif type_of_dragon =="Topaz":
            mon_type = (2,29)
        elif type_of_dragon =="Pearl":
            mon_type = (2,30)
        elif type_of_dragon =="Shadow":
            mon_type = (2,31)
        elif type_of_dragon =="Faerie":
            mon_type = (2,32)
        elif type_of_dragon =="Astral":
            mon_type = (2,33)
        elif type_of_dragon =="Etheral":
            mon_type = (2,34)
        elif type_of_dragon =="Rust":
            mon_type = (2,35)
        elif type_of_dragon =="Radiant":
            mon_type = (2,36)
        elif type_of_dragon =="Mirage":
            mon_type = (2,37)
        elif type_of_dragon =="Howling":
            mon_type = (2,38)
        elif type_of_dragon =="Lung":
            mon_type = (2,39)
        else:
            mon_type = (2,40)
        return mon_type
    def subtype_of_gaints():
        mon_type = ()
        gaint_information = input("Cloud, Ettin, Fire, Fog, Frost, Hill, Mountain, Stone, Storm, Titan, Firbolg Formoorain,Ogre, Goliath ,Verbeeg, Voadkyn, Cyclops, Ash, Maur, Craa'ghoran, Phaelin, Desert, Jungle, Reef, Island Orge g, Eldritch, Death ,Sand  gaints")
        if = gaint_information == "Cloud":
            mon_type = (3,1)
        elif gaint_information == "Ettin":
            mon_type = (3,2)
        elif gaint_information == "Fire":
            mon_type = (3,3)
        elif gaint_information == "Fog":
            mon_type =(3,4)
        elif gaint_information == "Frost":
            mon_type = (3,5)
        elif gaint_information == "Hill":
            mon_type = (3,6)
        elif gaint_information == "Mountain":
            mon_type - (3,7)
        elif gaint_information == "Stone":
            mon_type = (3,8)
        elif gaint_information == "Storm":
            mon_type = (3,9)
        elif gaint_information == "Titan":
            mon_type = (3,10)
        elif = gaint_information == "Firbolg":
            mon_type = (3,11)
        elif gaint_information == "Formoorain":
            mon_type = (3,12)
        elif gaint_information == "Ogre":
            mon_type = (3,13)
        elif gaint_information == "Goliath":
            mon_type =(3,14)
        elif gaint_information == "Verbeeg":
            mon_type = (3,15)
        elif gaint_information == "Voadkyn":
            mon_type = (3,16)
        elif gaint_information == "Cycplops":
            mon_type - (3,17)
        elif gaint_information == "Ash":
            mon_type = (3,18)
        elif gaint_information == "Maur":
            mon_type = (3,19)
        elif gaint_information == "Craa'ghoran":
            mon_type = (3,20)
        elif = gaint_information == "Phaelin":
            mon_type = (3,21)
        elif gaint_information == "Desert":
            mon_type = (3,22)
        elif gaint_information == "Jungle":
            mon_type = (3,23)
        elif gaint_information == "Reef":
            mon_type =(3,24)
        elif gaint_information == "Island":
            mon_type = (3,25)
        elif gaint_information == "Orge Gaint":
            mon_type = (3,26)
        elif gaint_information == "Eldritch":
            mon_type - (3,27)
        elif gaint_information == "Sand":
            mon_type = (3,28)
        elif gaint_information == "Death":
            mon_type = (3,29)
        else:
            mon_type = (3,30)
        return mon_type
    def subtype_of_Celestail():
        mon_type = ()
        typing_information=input("Angels, Archons, Guardians, Eladrin")
        if typing_information == "Angels":
            mon_type = (8,1)
        elif typing_information == "Archons":
            mon_type = (8,2)
        elif typing_information == "Guardians":
            mon_type = (8,3)
        elif typing_information == "Eladrin":
            mon_type = (8,4)
        else :
            mon_type = (8,5)
        return mon_type

    def determinedSize(self):
        mon_size =0
        if self.size == "Small":
            mon_size = 1
        elif self.size =="Medium":
            mon_size =2
        elif self.size =="Large":
            mon_size =3
        elif self.size = "Huge":
            mon_size =4
        elif self.size = "Gargantuan":
            mon_size =5:
        return mon_size



    def Create_MOnster(self):

    def skills(self):
