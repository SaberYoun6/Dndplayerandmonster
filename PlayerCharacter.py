import Character
class player__character__():
    def __init__(self, name,level, player_character_class,inHertiable_traits, sub_inHertiable_traits, sub_character_class):
        self.name = name
        self.level =level
        self.player_character_class=player_character_class
        self.inHertiable_traits = inHertiable_traits 
        self.sub_inHertiable_traits =sub_inHertiable_traits
        self.sub_character_class = sub_character_class
    def player_characters_setup():

    def player_character_class(self)
      if self.player_character_class == "bard":
          num = 1
      elif self.player_character_class == "barbarian":
          num = 2
      elif self.player_character_class == "cleric":
          num = 3
      elif self.player_character_class == "artificer":
          num = 4
      elif self.player_character_class == "monk":
          num = 5 
      elif self.player_character_class == "Rogue":
          num = 6
      elif self.player_character_class == "psonic":
          num = 7
      elif self.player_character_class == "fighter":
          num = 8
      elif self.player_character_class == "paladin":
          num = 9
      elif self.player_character_class == "druid":
          num = 10
      elif self.player_character_class == "wizard":
          num = 11
      elif self.player_character_class == "warlock":
          num = 12
      elif self.player_character_class == "Sorcerer":
          num = 13
      elif self.player_character_class == "ranger":
          num = 14
      elif self.player_character_class == "dragonknight":
          num = 15
      elif self.player_character_class == "mystic":
          num = 16
      else :
          num =17

    def inHertiable_traits(self):
        if self.inHertiable_traits == "elf":
            num = self.sub_traits_elf()
        elif self.inHertiable_traits == "half-elf":
            num = 2 
        elif self.inHertiable_traits == "half-orc":
            num = 3
        elif self.inHertiable_traits == "dragoborne":
            num =self.sub_traits_dragonborne()
        elif self.inHertiable_traits == "teifling":
            num =self.sub_traits_teifling()
        elif self.inHertiable_traits == "human":
            num =6
        elif self.inHertiable_traits == "drawf":
            num = self.sub_traits_drawf()
        elif self.inHertiable_traits == "gnome":
            num =self.sub_tratis_gnome()
        elif self.inHertiable_traits == " halfling":
            num = self.sub_traits_halfing()
        elif self.inHertiable_traits == "fairy":
            num = 10
        elif self.inHertiable_traits == "Minotaur":
            num = 11
        elif self.inHertiable_traits == "Satyr":
            num = 12
        elif self.inHertiable_traits == "golbin":
            num = 13
        elif self.inHertiable_traits == "3 golbins in a trench coat":
            num = 14
        elif self.inHertiable_traits == "3 gnomes in a trench coat":
            num = 15
        elif self.inHertiable_traits == "Orc":
            num = 16
        elif self.inHertiable_traits == "hobogoblin":
            num = 17
        elif self.inHertiable_traits =="dragon":
            num = 18
        elif self.inHertiable_traits == "aasimar":
            num = 19
        elif self.inHertiable_traits == "firbolg":
            num = 20
        elif self.inHertiable_traits == "goliath":
            num = 21
        elif self.inHertiable_traits =="kenku":
            num = 22
        elif self.inHertiable_traits ==  "Lizardfolk":
            num = 23
        elif self.inHertiable_traits == "tabaxi":
            num = 24
        elif self.inHertiable_traits == 'triton':
            num = 25
        elif self.inHertiable_traits == 'bugbear':
            num = 26
        elif self.inHertiable_traits == 'kobold':
            num = 27
        elif self.inHertiable_traits == 'yuan-ti':
            num = 28
        elif self.inHertiable_traits == "gith":
            num = self.sub_traits_gith()
        elif self.inHertiable_traits == 'Changelings':
            num = 30
        elif self.inHertiable_traits == "kalashtar":
            num = 31
        elif self.inHertiable_traits == "shifters":
            num = self.sub_traits_shifter()
        elif self.inHertiable_traits == "warforged":
            num = 33
        elif self.inHertiable_traits == "":
            num = 34
        else:
            num = race_not_mention():
        return num 
    def sub_traits_elf(self):
        if self.sub_inHertiable_traits == "drow":
            num = [1,1]
        elif self.sub_inHertiable_traits =="high elf":
            num = [1,2]
        elif self.sub_inHertiable_traits == "wood elf":
            num = [1,3]
        elif self.sub_inHertiable_traits == "autumn elf": 
            num = [1,4]
        elif self.sub_inHertiable_traits == "spring elf":
            num = [1,5]
        elif self.sub_inHertiable_traits == "summer elf":
            num = [1,6]
        elif self.sub_inHertiable_traits == "shari-dari":
            num = [1,7]
        elif self.sub_inHertiable_traits == "winter elf":
            num = [1,8]
        elif self.sub_inHertiable_traits == 'Eldrain':
            num = [1,9]

