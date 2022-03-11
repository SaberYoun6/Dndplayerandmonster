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
        print("Ventus initivative : %d \n Ventus strength modfiter : %d \n Ventus spell dc : %d \n" %(ventus_init,ventus_str,ventus_spell_dc))
        print("Ventus proficent %d\n Ventus christma %d\n Ventus deception %d\n " %(ventus_pro,ventus_cha,vetnus_decpt))


Main.main()

