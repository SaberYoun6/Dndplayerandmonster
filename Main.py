#!/usr/bin/env python3

import Character

__author__ = "Saberina Young"
__copyright__ = "Players and monsters 2022, Squid Mtyhos Hammer Industries"
__name__of__file__ = "Main.py"
__credits__ = ["Saberina Young"]
__license__ = "GPL 3.0"
__email__ ="saberina.young.103@gmail.com"
__stauts__ = "Aplha"

class Main(object):
   #def __init__():

    #def initial_game_setup():

    def main():
        object = Character.Characters("Ventus",18,14,4,16,12,11,15,13,17)
        ventus_init = object.initivative()
        ventus_str= object.define_modifitifer("str")
        ventus_spell_dc = object.spell_class_dc("cha")
        ventus_pro = object.proficent
        ventus_cha = object.define_modifitifer("cha")
        vetnus_decpt = object.character_skillS("cha")
        alth_pro_str = object.althelic_proficent("str",True)
        alth_pro_dex = object.althelic_proficent("dex",True)
        alth_pro_con = object.althelic_proficent("con",True)
        aor_pro_str = object.arobitics_proficents("str",False)
        aor_pro_Dex = object.arobitics_proficents("dex",False)
        aor_pro_con = object.arobitics_proficents("con",False)

        str_dex_con_ventus_skills = object.str_dex_con_skills("str","dex","con",True,False,False,False,True)

        int_wis_ventus_skills = object.int_wis_skills("wis","int",True,True,False,False,False,False,False,True,False,False,False)

        cha_ventus_skills = object.cha_skills("cha",False,True,False,False,True)


        print("Ventus initivative : %d \n Ventus strength modfiter : %d \n Ventus spell dc : %d" %(ventus_init,ventus_str,ventus_spell_dc))
        print("Ventus proficent %d\n Ventus christma %d\n Ventus deception %d " %(ventus_pro,ventus_cha,vetnus_decpt))
        print("if ventus was proficent in althelics for strenght %d\n althelic proficent in dex %d\n althelic proficent in con %d" % (alth_pro_str,alth_pro_dex,alth_pro_con))
        print("if ventus is not proficent in aorbatics using strength  %d\n aorbatic using dex %d\n aorbatic con %d" %(aor_pro_str, aor_pro_Dex,aor_pro_con))
        print("Althetics  |  Arobatics | Sleath | Sleight of Hand  ")
        for skill in str_dex_con_ventus_skills:
            print(skill)
        for skill in int_wis_ventus_skills:
            print(skill)
        for skill in cha_ventus_skills:
            print(skill)


Main.main()

