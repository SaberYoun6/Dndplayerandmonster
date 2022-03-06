#!/usr/bin/env  ptyhon3


__author__ = "Saberina Young"
__copyright__ = "OGL"
__credits__ = ["Saberina Young",]
__license__ = "GPL 3.0"
__maintianer__ = "Saberina Young"
__email__ = "saberina.young.103@gmail.com"
__status__ = "Aplha"

### depedencies ####


class Characters():
    def setting_up_character():
        charater_Name = input("Please put your character name")
        character_attribute = []
"""character_Attributes = [hit_points, armor_class, initivate
, str, dex, con,
int, wid, cha]""" 
        for status in character_attributes:
            try:
                all_status= input("hitpoints, armor_class, initivate,str,dex,con,int,wid,cha ")
                a_status=all_status.split(", ")
                hitpoints=int(a_status[0])
                armour_class  = int(a_status[1])
                initivative = int(a_status[2])
                strength = int(a_status[3])
                dexitery = int(a_status[4])
                constution = int(a_status[5])
                intelligence = int(a_status[6])
                wisdom = int(a_status[7])
                charistma = int(a_status[8])
                break:
            except:
                print("Oops!", sys.exc_info()[0],"occurred.")
                print("Next entry.")
                print()
        character_attribute.append(hitpoint)
        character_attribute.append(armour_class)
        character_attribute.append(initivative)
        character_attribute.append(strength)
        character_attribute.append(dexitery)
        character_attribute.append(constution)
        character_attribute.append(intelligence)
        character_attribute.append(wisdom)
        character_attribute.append(charistma)
        return dict(charater_Name,character_attribute)


    
"""




