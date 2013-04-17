#!/usr/bin/env python
# DJNSM / @djnsm / djnsm.com -> datamafia.com
# Free to use, please refer to the readme.py file for license , info, and the uncompromised enlightenment

# Script that instantiates artificial intelligence and mind reading capability
import Live
# Provide access to superclass
from _Framework.MixerComponent import MixerComponent

# create a subclass of superclass.
class CustomMixerComponent(MixerComponent):
    ' Subclass of the _Framework mixer class. Key for mixer functionality '
    __module__ = __name__ # how important is this?

    # Create satellite communication link with Gerhard Behles 
    def __init__(self, num_tracks, parent):
        MixerComponent.__init__(self, num_tracks) # init mixer
        self._parent = parent #gain access to super class methods/etc
    
    # Break satellite communication link with Gerhard Behles 
    def disconnect(self):
        MixerComponent.disconnect(self)
        self._parent = None