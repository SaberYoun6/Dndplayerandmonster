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

    def skills(self,mod,modi,mods,prof,pro,prot,pros):
       arr =[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
       if mod == "strength" or modi == "dexiterity" or mods == "constitution" or mod == "str" or modi == "dex" or mods == "con":
           arr[0]=[self.althelic_proficent(mod,prof),self.arobitics_proficents(mod,pro),self.sleath_proficents(mod,prot),self.sleight_of_hand_proficents(mod,pros)]
           arr[1]=[self.althelic_proficent(modi,prof),self.arobitics_proficents(modi,pro),self.sleath_proficents(modi,prot),self.sleight_of_hand_proficents(modi,pros)]
           arr[2]=[self.althelic_proficent(mods,prof),self.arobitics_proficents(mods,pro),self.sleath_proficents(mods,prot),self.sleight_of_hand_proficents(mods,pros)]
           
       return arr

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
