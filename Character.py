#!/usr/bin/env  ptyhon3
'''
This class is only used for NPC
'''

__author__ = "Saberina Young"
__copyright__ = "Dnd stats"
__credits__ = ["Saberina Young",]
__license__ = "GPL 3.0"
__maintianer__ = "Saberina Young"
__email__ = "saberina.young.103@gmail.com"
__status__ = "Aplha"

### depedencies ####
import mariadb
import os
import sys
import numpy as np

class Characters(object):
    def __init__(self,charater_name,hitpoint,armour_class, proficent,strength,dexiterity,constitution,intelligence,wisdom, charistma):
        self.character_name = charater_name
        self.hitpoint = hitpoint
        self.armour_class = armour_class
        self.proficent = proficent
        self.strength = strength
        self.dexiterity = dexiterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charistma = charistma

    def define_modifitifer(self,mods):
        mod =0
        if mods == "strength" or mods == "str" :
            mod = np.floor(self.strength /2 -5)
        elif mods == "dexiterity" or mods == "dex":
            mod = np.floor(self.dexiterity /2 -5)
        elif mods == "constitution" or mods == "con":
            mod = np.floor(self.constitution /2 -5)
        elif mods == "intelligence" or mods == "int":
            mod = np.floor(self.intelligence /2 -5)
        elif mods == "wisdom" or mods == "wis":
            mod = np.floor(self.wisdom /2 -5)
        elif mods == "charistma" or mods == "cha":
            mod = np.floor(self.charistma /2 -5)
        else:
            mod =0
        return mod 
    def character_skillS(self,mods):
       mod = self.define_modifitifer(mods)+ self.proficent
       return mod
    def spell_class_dc(self,mods):
       spell_dc = 8 + self.define_modifitifer(mods) + self.proficent 
       return spell_dc
    def  initivative(self):
       inits = (self.dexiterity/2) -5
       return inits
    def character_is_not_proficent(self,mods):
       mod = self.define_modifitifer(mods)
       return mod
    def althelic_proficent(self,mod,prof):
       a=0
       if mod == "strength" or mod == "str" and prof == True:
          a = self.character_skillS(mod)
       elif mod == "dexiterity" or mod == "dex" and  prof == True:
          a = self.character_skillS(mod)
       elif mod == "constitution" or mod == "con" and  prof == True:
          a = self.character_skillS(mod)
       else:
          a = self.character_is_not_proficent(mod)
       return a 
    def arobitics_proficents(self,mod,prof):
       a = 0
       if mod == "strength" or mod == "str" and  prof == True:
           a = self.character_skillS(mod)
       elif mod == "dexiterity" or mod == "dex" and  prof == True:
           a = self.character_skillS(mod)
       elif mod == "constitution" or mod == "con" and  prof == True:
           a = self.character_skillS(mod)
       else:
           a = self.character_is_not_proficent(mod)
       return a
    def sleath_proficents(self,mod,prof):
       s = 0
       if mod == "dexiterity" or mod == "dex" and prof == True:
           s = self.character_skillS(mod)
       else:
           s = self.character_is_not_proficent(mod)
       return s
    def sleight_of_hand_proficents(self,mod,prof): 
       s =0 
       if mod == "dexiterity" or mod == 'dex' and prof == True:
           s = self.character_skillS(mod)
       else:
           s = self.character_is_not_proficent(mod)
       return s
    def animal_handling_skills(self,mod,prof):
       a = 0
       if mod == "wisdom" or mod == "wis" and prof == True:
           a = self.character_skillS(mod)
       elif mod == "intelligence" or mod == "int" and prof == True:
           a = self.character_skillS(mod)
       else:
           a = self.character_is_not_proficent(mod)
       return a
    def arcana_skills(self,mod,prof):
       a = 0
       if mod == "intelligence" or mod == "int" and prof ==True:
           a = self.character_skillS(mod)
       elif mod == "wisdom" or mod == "wis" and prof == True:
           a = self.character_skillS(mod)
       else:
           a = self.character_is_not_proficent(mod)
       return a
    def history_skill(self,mod,prof):
       h = 0
       if mod == 'intelligence' or mod == 'int' and prof == True:
           h = self.character_skillS(mod)
       elif mod == 'wisdom' or mod == 'wis' and prof == True:
           h = self.character_skillS(mod)
       else:
           h = self.character_is_not_proficent(mod)
       return h 
    def insight_skill(self,mod,prof):
       i = 0 
       if mod == 'wisdom' or mod == 'wis' and prof == True:
           i = self.character_skillS(mod)
       elif mod == "intelligence" or mod == "int" and prof == True:
           i = self.character_skillS(mod)
       else:
           i = self.character_is_not_proficent(mod)
       return i
    def investigation_skill(self,mod,prof):
       i = 0
       if mod == "intelligence" or mod == "int" and prof == True: 
           i = self.character_skillS(mod)
       elif mod == "wisdom" or mod == "wis" and prof == True: 
           i = self.character_skillS(mod)
       else:
           i = self.character_is_not_proficent(mod)
       return i 
    def medicine_skill(self,mod,prof):
       m= 0
       if mod == 'wisdom' or mod == 'wis' and prof == True:
           m = self.character_skillS(mod)
       elif mod == "intelligence" or mod == "int" and prof == True:
           m = self.character_skillS(mod)
       else:
           m = self.character_is_not_proficent(mod)
       return m
    def nature_skill(self,mod,prof):
       n = 0
       if mod == "intelligence" or mod == "int" and prof == True: 
           n = self.character_skillS(mod)
       elif mod == "wisdom" or mod == "wis" and prof == True: 
           n = self.character_skillS(mod)
       else:
           n = self.character_is_not_proficent(mod)
       return n
    def perception_skill(self, mod,prof):
       p= 0
       if mod == 'wisdom' or mod == 'wis' and prof == True:
           p = self.character_skillS(mod)
       elif mod == "intelligence" or mod == "int" and prof == True:
           p = self.character_skillS(mod)
       else:
           p = self.character_is_not_proficent(mod)
       return p

    def religon_skill(self, mod , prof): 
       r = 0
       if mod == "intelligence" or mod == "int" and prof == True: 
           r = self.character_skillS(mod)
       elif mod == "wisdom" or mod == "wis" and prof == True: 
           r = self.character_skillS(mod)
       else:
           r = self.character_is_not_proficent(mod)
       return r

    def survival_skill(self, mod ,prof):
       s= 0
       if mod == 'wisdom' or mod == 'wis' and prof == True:
           s = self.character_skillS(mod)
       elif mod == "intelligence" or mod == "int" and prof == True:
           s = self.character_skillS(mod)
       else:
           s = self.character_is_not_proficent(mod)
       return s
    def deception_skill(self,mod,prof):
       d = 0
       if mod == 'charistma' or mod == 'cha' and prof == True:
           d = self.character_skillS(mod)
       elif mod == 'int' or mod == 'intelligence' and prof==True:
           d = self.character_skillS(mod)
       else:
           d = self.character_is_not_proficent(mod)
       return d 

    def intimidation_skill(self,mod,prof):
       i =0
       if mod == "strength" or mod == "str" and prof == True:
           i = self.character_skillS(mod)
       elif mod == "cha" or mod == "charistma" and prof == True:
           i = self.character_skillS(mod)
       else:
           i = self.character_is_not_proficent(mod)
       return i
    def preformace_skill(self,mod,prof):
       p = 0
       if mod == 'charistma' or mod =='cha' and prof == True:
           p = self.character_skillS(mod)
       else:
           p = self.character_is_not_proficent(mod)
       return p
    def persusion_skill(self,mod,prof):
       p =0 
       if mod == 'charistma' or mod == 'cha' and prof == True:
           p = self.character_skillS(mod)
       else:
           p = self.character_is_not_proficent(mod)
       return p 
    def str_dex_con_skills(self,mod,modi,mods,prof,pro,prot,pros,pr0s):
       arr =[[0,0,0,0,0],[0,0,0,0],[0,0,0,0]]
       if mod == "strength" or modi == "dexiterity" or mods == "constitution" or mod == "str" or modi == "dex" or mods == "con":
           arr[0]=[self.althelic_proficent(mod,prof),self.arobitics_proficents(mod,pro),self.sleath_proficents(mod,prot),self.sleight_of_hand_proficents(mod,pros),self.intimidation_skill(mod,pr0s)]
           arr[1]=[self.althelic_proficent(modi,prof),self.arobitics_proficents(modi,pro),self.sleath_proficents(modi,prot),self.sleight_of_hand_proficents(modi,pros)]
           arr[2]=[self.althelic_proficent(mods,prof),self.arobitics_proficents(mods,pro),self.sleath_proficents(mods,prot),self.sleight_of_hand_proficents(mods,pros)]
       elif  mod == "dexiterity" or modi == "constitution" or mods =="strength" or mod == "dex" or modi == 'con' or mods == 'str':
           arr[0]=[self.althelic_proficent(mods,prof),self.arobitics_proficents(mods,pro),self.sleath_proficents(mods,prot),self.sleight_of_hand_proficents(mods,pros),self.intimidation_skill(mods,pr0s)]
           arr[1]=[self.althelic_proficent(mod,prof),self.arobitics_proficents(mod,pro),self.sleath_proficents(mod,prot),self.sleight_of_hand_proficents(mod,pros)]
           arr[2]=[self.althelic_proficent(modi,prof),self.arobitics_proficents(modi,pro),self.sleath_proficents(modi,prot),self.sleight_of_hand_proficents(modi,pros)]
       elif mod == "constitution" or modi == "strength" or mods == "dexiterity" or mod == 'con' or modi == 'str' or mods == 'dex':
           arr[0]=[self.althelic_proficent(modi,prof),self.arobitics_proficents(modi,pro),self.sleath_proficents(modi,prot),self.sleight_of_hand_proficents(modi,pros),self.intimidation_skill(modi,pr0s)]
           arr[1]=[self.althelic_proficent(mods,prof),self.arobitics_proficents(mods,pro),self.sleath_proficents(mods,prot),self.sleight_of_hand_proficents(mods,pros)]
           arr[2]=[self.althelic_proficent(mod,prof),self.arobitics_proficents(mod,pro),self.sleath_proficents(mod,prot),self.sleight_of_hand_proficents(mod,pros)]
       elif mod == "strength" or  modi =="constitution" or mods == "dexiterity" or mod =="str" or modi == "con" or mod == "dex":
           arr[0]=[self.althelic_proficent(mod,prof),self.arobitics_proficents(mod,pro),self.sleath_proficents(mod,prot),self.sleight_of_hand_proficents(mod,pros),self.intimidation_skill(mod,pr0s)]
           arr[1]=[self.althelic_proficent(mods,prof),self.arobitics_proficents(mods,pro),self.sleath_proficents(mods,prot),self.sleight_of_hand_proficents(mods,pros)]
           arr[2]=[self.althelic_proficent(modi,prof),self.arobitics_proficents(modi,pro),self.sleath_proficents(modi,prot),self.sleight_of_hand_proficents(modi,pros)]
       elif mod == 'dexiterity' or modi =="strength" or mods == "constitution" or mod == 'dex' or modi == 'str' or mods == 'con':
           arr[0]=[self.althelic_proficent(modi,prof),self.arobitics_proficents(modi,pro),self.sleath_proficents(modi,prot),self.sleight_of_hand_proficents(modi,pros),self.intimidation_skill(modi,pr0s)]
           arr[1]=[self.althelic_proficent(mod,prof),self.arobitics_proficents(mod,pro),self.sleath_proficents(mod,prot),self.sleight_of_hand_proficents(mod,pros)]
           arr[2]=[self.althelic_proficent(mods,prof),self.arobitics_proficents(mods,pro),self.sleath_proficents(mods,prot),self.sleight_of_hand_proficents(mods,pros)]
       elif mod == 'constitution' or modi == 'dexiterity' or mods =='strength' or mod == 'con' or modi == 'dex' or mods == 'str':
           arr[0]=[self.althelic_proficent(mods,prof),self.arobitics_proficents(mods,pro),self.sleath_proficents(mods,prot),self.sleight_of_hand_proficents(mods,pros),self.intimidation_skill(mods,pros)]
           arr[1]=[self.althelic_proficent(modi,prof),self.arobitics_proficents(modi,pro),self.sleath_proficents(modi,prot),self.sleight_of_hand_proficents(modi,pros)]
           arr[2]=[self.althelic_proficent(mod,prof),self.arobitics_proficents(mod,pro),self.sleath_proficents(mod,prot),self.sleight_of_hand_proficents(mod,pros)]
       else:
           arr
       return arr
    def int_wis_skills(self,mod,mods,pro,prof,prot,pros,profi,profit,prots,proficnt,pr0s,proficent,pr0fs):
       arr=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0]]
       if mod == "wisdom" or mods == "intelligence" or mod == "wis" or mods == "int":
           arr[0] = [self.animal_handling_skills(mod,pro),self.arcana_skills(mod,prof),self.history_skill(mod,prot),self.insight_skill(mod,pros),self.investigation_skill(mod,profi),self.medicine_skill(mod,profit),self.nature_skill(mod,prots),self.perception_skill(mod,proficnt),self.religon_skill(mod,pr0s),self.survival_skill(mod,proficent)]
           arr[1] = [self.animal_handling_skills(mods,pro),self.arcana_skills(mods,prof),self.history_skill(mods,prot),self.insight_skill(mods,pros),self.investigation_skill(mods,profi),self.medicine_skill(mods,profit),self.nature_skill(mods,prots),self.perception_skill(mods,proficnt),self.religon_skill(mods,pr0s),self.survival_skill(mods,proficent),self.deception_skill(mods,pr0fs)]
       elif mod == "intelligence" or mods == "wisdom" or mod == "int" or mods == "wis":
           arr[0] = [self.animal_handling_skills(mods,pro),self.arcana_skills(mods,prof),self.history_skill(mods,prot),self.insight_skill(mods,pros),self.investigation_skill(mods,profi),self.medicine_skill(mods,profit),self.nature_skill(mods,prots),self.perception_skill(mods,proficnt),self.religon_skill(mods,pr0s),self.survival_skill(mods,proficent)]
           arr[1] = [self.animal_handling_skills(mod,pro),self.arcana_skills(mod,prof),self.history_skill(mod,prot),self.insight_skill(mod,pros),self.investigation_skill(mod,profi),self.medicine_skill(mod,profit),self.nature_skill(mod,prots),self.perception_skill(mod,proficnt),self.religon_skill(mod,pr0s),self.survival_skill(mod,proficent),self.deception_skill(mod,pr0fs)]
       else:
           arr
       return arr
    def cha_skills(self,mod,pro,prof,prot,pros):
       arr = [0,0,0,0]
       arr = [self.deception_skill(mod,pro),self.intimidation_skill(mod,prof),self.preformace_skill(mod,prot),self.persusion_skill(mod,pros)]
       return arr

    def characters_damsge(self,damage_taken):
       if self.total_hitpoints() < 0 : 
           self.hitpoint = self.total_hitpoints() - damage_taken
       return self.hitpoint
    def character_healling(self,healing):
       if  healing >= self.total_hitpoints():
           self.hitpoint= self.total_hitpoints() + healing
       return self.hitpoint

    def temp_hp(self,temp_hitpoints):
       self.hitpoint = self.total_hitpoints() + temp_hitpoints
       return self.hitpoint

    def total_hitpoints(self):
       self.hitpoint


'''    def setting_up_character(self):
        charater_Name = input("Please put your character name")
        for status in character_attributes:
            try: con = mariadb.connect(
                    user=os.getenv("DB_USER"),
                    password= os.getenv("DB_PASSWORD"),
                    host=os.getenv("DB_HOST"),
                    port=3306,
                    database=OS.getenv("DB_DATABASE")
                    )

            except mariadb.Error as ex :
                printf("An error occured while connectiong to MariaDB {%s}" % ex)
                sys.exit(1)
            cur = con.cursor()
    def inserting_characters(self):
        Characters.setting_up_character()
            connect.mycursor(""" CREATE TABLE CHARACTERS (Id NOT NULL int, Name varchar(255) NOT NULL, HP int, AC int, Init int,str int,dex int,con int, intell int, wid int, cha int)""")

            query("INSERT INTO CHARACTERS (Id, Name,hp,AC,Init,str,dex,con,intell,wid,cha) VALUES ( %d,'%S',%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d")
            values = ( self.character_name,self.hitpoint,self.armour_class,self.initivative,self.strength,self.dexiterity,self.constitution,self.intelligence,self.wisdom,self.charistma)
            cur.execute(query,values)
            print("{cur.rowCount}, details inserted")
            con.commit()
    def updating_characters(self):
        characters.inserting_characters()
        qurey= f"UPDATE CHARACTERS Set name = %s WHERE %s = %d"
        values = self, self.character_name , dex, self.dexiterity
        conn.commit()
    def delete_character(self):
        query = f"DELETE FROM CHARACTERS WHERE name = %s"
        cur.execute(query)
        con.commit()
        con.close()'''
