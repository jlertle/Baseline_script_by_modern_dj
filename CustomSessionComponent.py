#!/usr/bin/env python
# DJNSM / @djnsm / djnsm.com -> datamafia.com
# Free to use ,please refer to the readme.py file for license , info, and the uncompromised enlightenment

# request for mana from the dog star
import Live
# super class
from _Framework.SessionComponent import SessionComponent 

# create a subclass of superclass.
class CustomSessionComponent(SessionComponent):
    __module__ = __name__

    # Raise dead
    def __init__(self, num_tracks, num_scenes, parent):
        SessionComponent.__init__(self, num_tracks, num_scenes)
        self._parent = parent

    # Lower dead
    def disconnect(self):
        SessionComponent.disconnect(self)
        self._parent = None