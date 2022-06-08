import Character
import Monster
class player__character__():
    def __init__(self, name,level, player_character_class,inHertiable_traits, sub_inHertiable_traits, sub_character_class):
        self.name = name
        self.level =level
        self.player_character_class=player_character_class
        self.inHertiable_traits = inHertiable_traits 
        self.sub_inHertiable_traits =sub_inHertiable_traits
        self.sub_character_class = sub_character_class
        self.background_character = background_character

    def player_characters_setup0():

    def player_character_class(self,inputs)
    if self.player_character_class == "Bard":
          num = 1
      elif self.player_character_class == "Barbarian":
          num = 2
      elif self.player_character_class == "Cleric":
          num = 3
      elif self.player_character_class == "Artificer":
          num = 4
      elif self.player_character_class == "Monk":
          num = 5 
      elif self.player_character_class == "Rogue":
          num = 6
      elif self.player_character_class == "Psonic":
          num = 7
      elif self.player_character_class == "Fighter":
          num = 8
      elif self.player_character_class == "Paladin":
          num = 9
      elif self.player_character_class == "Druid":
          num = 10
      elif self.player_character_class == "Wizard":
          num = 11
      elif self.player_character_class == "Warlock":
          num = 12
      elif self.player_character_class == "Sorcerer":
          num = 13
      elif self.player_character_class == "Ranger":
          num = 14
      elif self.player_character_class == "Dragonknight":
          num = 15
      elif self.player_character_class == "Mystic":
          num = 16
      elif self.player_character_class == "Gun Smith":
          num = 17
      else :
          num =18

    def inHertiable_traits(self):
        if self.inHertiable_traits =="Elf":
            num = self.sub_traits_elf()
        elif self.inHertiable_traits =="Half-Elf":
            num = 2 
        elif self.inHertiable_traits =="Half-Orc":
            num = 3
        elif self.inHertiable_traits =="Dragoborne":
            num =self.sub_traits_dragonborne()
        elif self.inHertiable_traits =="Teifling":
            num =self.sub_traits_teifling()
        elif self.inHertiable_traits =="Human":
            num =6
        elif self.inHertiable_traits =="Drawf":
            num = self.sub_traits_drawf()
        elif self.inHertiable_traits =="Gnome":
            num =self.sub_tratis_gnome()
        elif self.inHertiable_traits =="Halfling":
            num = self.sub_traits_halfing()
        elif self.inHertiable_traits =="Fairy":
            num = 10
        elif self.inHertiable_traits =="Minotaur":
            num = 11
        elif self.inHertiable_traits == "Satyr":
            num = 12
        elif self.inHertiable_traits =="Golbin":
            num = 13
        elif self.inHertiable_traits =="3 Golbins in a trench coat":
            num = 14
        elif self.inHertiable_traits =="3 Gnomes in a trench coat":
            num = 15
        elif self.inHertiable_traits =="Orc":
            num = 16
        elif self.inHertiable_traits =="Hobogoblin":
            num = 17
        elif self.inHertiable_traits =="Dragon":
            num = self.sub_traits_dragon()
        elif self.inHertiable_traits =="Aasimar":
            num = 19
        elif self.inHertiable_traits =="Firbolg":
            num = 20
        elif self.inHertiable_traits =="Goliath":
            num = 21
        elif self.inHertiable_traits =="Kenku":
            num = 22
        elif self.inHertiable_traits =="Lizardfolk":
            num = 23
        elif self.inHertiable_traits =="Tabaxi":
            num = 24
        elif self.inHertiable_traits =='Triton':
            num = 25
        elif self.inHertiable_traits =='Bugbear':
            num = 26
        elif self.inHertiable_traits =='Kobold':
            num = 27
        elif self.inHertiable_traits =='Yuan-ti':
            num = 28
        elif self.inHertiable_traits =="Gith":
            num = self.sub_traits_gith()
        elif self.inHertiable_traits =='Changelings':
            num = 30
        elif self.inHertiable_traits =="Kalashtar":
            num = 31
        elif self.inHertiable_traits =="Shifters":
            num = self.sub_traits_shifter()
        elif self.inHertiable_traits =="Warforged":
            num = 33
        elif self.inHertiable_traits == "Dhampir":
            num = 34
        elif self.inHertiable_traits == 'Hexblood':
            num = 35
        elif self.inHertiable_traits == 'Reborn':
            num = 36
        elif self.inHertiable_traits == 'Leonin':
            num = 37
        elif self.inHertiable_traits == 'Centaur':
            num = 38
        elif self.inHertiable_traits == 'harengon':
            num = 39
        elif self.inHertiable_traits == 'Aarakocra':
            num = 40
        elif self.inHertiable_traits == 'Genasi':
            num = sub_traits_genasi()
        else:
            num = race_not_mention(self.inHertiable_traits):
                
        return num 
    def sub_traits_elf(self,subrace_elf):
        if self.sub_inHertiable_traits == "Drow":
            num = [1,1]
        elif self.sub_inHertiable_traits =="High Elf":
            num = [1,2]
        elif self.sub_inHertiable_traits == "Wood Elf":
            num = [1,3]
        elif self.sub_inHertiable_traits == "Autumn Elf": 
            num = [1,4]
        elif self.sub_inHertiable_traits == "Spring Elf":
            num = [1,5]
        elif self.sub_inHertiable_traits == "Summer Elf":
            num = [1,6]
        elif self.sub_inHertiable_traits == "Shadar-Kai":
            num = [1,7]
        elif self.sub_inHertiable_traits == "Winter Elf":
            num = [1,8]
        elif self.sub_inHertiable_traits == 'Sea Elf':
            num = [1,9]
        else: 
            num = [1,elf_not_mention(self.inHertiable_traits)]
    def sub_traits_drawf(self,subrace_drawfs):
        if self.sub_inHertiable_traits == "Duegar" and inHertiable_traits == "Drawf":
            num = [7,1]
        elif self.sub_inHertiable_traits == "Mountain Drawf":
            num = [7,2]
        elif self.sub_inHertiable_traits == "Hill Drawf":
            num = [7,3]
        else:
            num == [7,Drawf_not_mention(self.inHertiable_traits]:
    def sub_traits_dragon(self,subtype):
    tuplesfordragonborne = (2,0)
    tuplesfordragon = (16,0)
    if self.sub_inHertiable_traits == Monster.subtype_of_Dragon(subtype) and inHertiable_traits == 'Dragon':
    num = list(map(lambda i,j : i+j,tuplesfordragon,Monster.subtype_of_Dragon))
    elif inHertiable_traits == 'Dragonborne' and self.sub_inHertiable_trait == subtype:
    num = list(map(lambda i ,j i+j,Monster.subtype_of_Dragon(subtype),tuplesfordragonborne))
    else:




