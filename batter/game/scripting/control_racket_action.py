from constants import *
from game.scripting.action import Action


class ControlRacketAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        racket1 = cast.get_first_actor(RACKET_GROUP1)
        if self._keyboard_service.is_key_down(UP1): 
            racket1.swing_left()
        elif self._keyboard_service.is_key_down(DOWN1): 
            racket1.swing_right()  
        else: 
            racket1.stop_moving()        

        racket2 = cast.get_first_actor(RACKET_GROUP2)
        if self._keyboard_service.is_key_down(UP2): 
            racket2.swing_left()
        elif self._keyboard_service.is_key_down(DOWN2): 
            racket2.swing_right()  
        else: 
            racket2.stop_moving()  