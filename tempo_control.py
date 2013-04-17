#!/usr/bin/env python
# DJNSM / @djnsm / djnsm.com -> datamafia.com
# Free to use, please refer to the readme.py file for license , info, and the uncompromised enlightenment

#bitNomad_ohm64.py 
#This is form a midi remote script for the Ohm64 bitNomad @bitnomad  https://github.com/bitnomad
# via bitNomad : it is heavily based on the work of Michael Chenetz from max4live.info
# as well as Kevin Ferguson / http://www.ofrecordings.com/

# Import parameter assignments. All of the parameters are set at parameters.py 
from parameters import *

# The minimum imports and scripts. Always takign suggestions on reducing more
import Live # This allows us (and the Framework methods) to use the Live API on occasion
import time # We will be using time functions for time-stamping our log file outputs
from _Framework.ButtonElement import ButtonElement # Class representing a button a the controller
from _Framework.InputControlElement import * # Base class for all classes representing control elements on a controller || This is where MIDI_NOTE_TYPE is set up
from _Framework.TransportComponent import TransportComponent # Class encapsulating all functions in Live's transport section

class CustomTransportComponent(TransportComponent):#TransportComponent
    """TransportComponent with custom tempo support"""
    
    def __init__(self):
        TransportComponent.__init__(self)
    
    def button(TransportComponent,note_num):
        # Note that the MIDI_NOTE_TYPE constant is defined in the InputControlElement module
        return ButtonElement(True, MIDI_NOTE_TYPE, midi_channel, note_num)

    def _replace_controller(self, attrname, cb, new_control):
        old_control = getattr(self, attrname, None)
        if old_control is not None:
            old_control.remove_value_listener(cb)
        setattr(self, attrname, new_control)
        new_control.add_value_listener(cb)
        self.update()

    def set_tempo_bumpers(self, bump_up_control, bump_down_control):
        self._replace_controller('_tempo_bump_up_control', self._tempo_up_value, bump_up_control)
        self._replace_controller('_tempo_bump_down_control', self._tempo_down_value, bump_down_control)

    def _tempo_shift(self, amount):
        old_tempo = self.song().tempo
        self.song().tempo = max(20, min(999, old_tempo + amount))

    def _tempo_up_value(self, value):
        if value!=0:
            self._tempo_shift(tempo_button_up_interval)
            
    def _tempo_down_value(self, value):
        if value!=0:
            self._tempo_shift(tempo_button_down_interval)