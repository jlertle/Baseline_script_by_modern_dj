#!/usr/bin/env python
# DJNSM / @djnsm / djnsm.com -> datamafia.com
# Free to use, please refer to the readme.py file for license , info, and the uncompromised enlightenment

# live9 / Py support. Needs to be up front
from __future__ import with_statement
# we assign all parameters for all files / modeuls on the Python parameters.py file
from parameters import *
from readme import * #license, credit, and other information - script is free/open source
import Live # Script that instantiates artificial intelligence and mind reading capability
import time # Required for error logging
# what we need from _Framework o a general sense
from _Framework.ButtonElement import ButtonElement # button elemtns
from _Framework.ButtonMatrixElement import ButtonMatrixElement # martix/grd/box
from _Framework.ClipSlotComponent import ClipSlotComponent  #hold buttons
from _Framework.CompoundComponent import CompoundComponent # Bueller?
from _Framework.ControlElement import ControlElement # Element/obj for control?
from _Framework.ControlSurface import ControlSurface # obj fed to __init__
from _Framework.ControlSurfaceComponent import ControlSurfaceComponent 
from _Framework.InputControlElement import * # take contorl and ...? Needs *?
from _Framework.SceneComponent import SceneComponent # New in Live9
from _Framework.SessionComponent import SessionComponent # Session obj

#required as we are subclassing the Sesion Component
from CustomSessionComponent import CustomSessionComponent

# import what is required  for tempo control
if enable_tempo_control == 1:
    from tempo_control import CustomTransportComponent # I subclass there for I am
    from _Framework.TransportComponent import TransportComponent # tempo+?
    
# import what is required for  standard volume control
if enable_volume_control == 1:
    from _Framework.SliderElement import SliderElement #  required for knob/slider element
    # Required, subclass of the Live Mixer
    from CustomMixerComponent import CustomMixerComponent 

# static volume / offset volume
if enable_static_volume == 1:
    from _Framework.MixerComponent import MixerComponent

# Main class
class Baseline_script_by_modern_dj(ControlSurface):
    __module__ = __name__ # Edie Brickell song
    __doc__ = " modern.dj baseline MRS controller script  for live 9 http://modern.dj/app" #shamless self promotion
    
    # bootstrap method
    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance) # bootstrap into the API/_Framework
        with self.component_guard(): # live9 / new requirement
            self.log_message(" - ")
            self.log_message("**************************************************")
            self.version_information() # log information from the readme.py file
            self.log_message(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime()) + "..::|| Modern.DJ LIVE9 baseline MRS opened ||::..")
            self._suppress_session_highlight = True # stop the "Red box" for a second
            self._suppress_send_midi = True # sounds like a good idea
            #self.set_suppress_rebuild_requests(True) #deprecated for 9 !! Legacy note keep here for repository ref, remove later!!
            # Look for matrix option
            if enable_matrix == 1: # yes, matrix aka "red box"
                self.log_message("[matrix enabled]")
                self.volume_offset = volume_offset # see param info / offset for volume
                self.box_width = box_width # track width 
                self.box_height = box_height # track height aka scene count
                self.session = None # local session object
                self._setup_session_control() # init the session via subclass pattern
                # Turn on volume is needed. Nested as Volume has session / matrix dependencies
                if enable_volume_control == 1:
                    self.log_message("[volume control enabled]")
                    self.volume_control = None # param container inside the obj
                    self.mixer = None # holds the obj mixer object
                    # should volume be static or not?
                    if enable_static_volume == 1 :
                        self.track_volume_static = track_volume_static # localize tuple of CCs for volume control
                        self.mixer_custom = None
                        self.custom_offset_mixer() 
                    else :
                        self.track_volume = track_volume # localize tuple of CCs for volume control
                        self._setup_mixer_control()
                    self.session.set_mixer(self.mixer) # for the red box to move left/right w/session
                else:
                    self.log_message("[volume control not enabled")
            else:
                self.log_message("[matrix not enabled]")        
            # Check for tempo control option
            if enable_tempo_control == 1: 
                self.log_message("[tempo enabled]")
                self._setup_transport_control()
            else:
                self.log_message("[tempo not enabled]")
            # turn on "red box" again --  drops mic, walks off stage
            self._suppress_session_highlight = False

    ## tempo via  @bitNomad  / http://github.com/bitnomad 
    # @todo : Move this off and pass the object along newer subclassing patterns
    def _setup_transport_control(self):
        transport = CustomTransportComponent() #Instantiate a Transport Component
        transport.set_tempo_bumpers(transport.button(tempo_button_up), transport.button(tempo_button_down)) # yells "DO IT!!" at tempo code

    # pass session component through a bunch of subclassing
    def _setup_session_control(self):
        self.session = CustomSessionComponent(self.box_width, self.box_height, self) # subclass from _Framework
        is_momentary = True # what exactly does this do in the _Framework?
        if up_button_note_number >= 0 and down_button_note_number >= 0: # opt in enable UP/DOWN nav
            up_button = ButtonElement(is_momentary, MIDI_NOTE_TYPE, midi_channel, up_button_note_number) 
            up_button.name = 'Bank_Select_Up_Button' # sure, why not
            down_button = ButtonElement(is_momentary, MIDI_NOTE_TYPE, midi_channel, down_button_note_number)
            down_button.name = 'Bank_Select_Down_Button' #sure, why not
            self.session.set_scene_bank_buttons(down_button, up_button)
        if right_button_note_number >= 0 and left_button_note_number >= 0: # opt in enable LEFT/RIGHT nav
            right_button = ButtonElement(is_momentary, MIDI_NOTE_TYPE, midi_channel, right_button_note_number)
            right_button.name = 'Bank_Select_Right_Button' #sure, why not
            left_button = ButtonElement(is_momentary, MIDI_NOTE_TYPE, midi_channel, left_button_note_number)
            left_button.name = 'Bank_Select_Left_Button' #sure, why not
            self.session.set_track_bank_buttons(right_button, left_button)
        self.session.name = 'Session_Control' #sure, why not
        matrix = ButtonMatrixElement() # @todo subclass this via established new patterns
        matrix.name = 'Button_Matrix' #sure, why not
        # I loop a little different. The goal is readbility, flexibility, and the web app...incase you did not notice yet
        if len(scene_launch_notes) > 0 and len(scene_launch_notes) == self.box_height: # logic check have launch notes and scene = box height
            for index in range(self.box_height): 
                self.session.scene(index).set_launch_button(ButtonElement(is_momentary, MIDI_NOTE_TYPE, midi_channel, scene_launch_notes[index])) 
        else :
            self.log_message("..::|| Scene launch not in use or error on case of use. Modern.DJ ||::..")
        if len(stop_track_buttons) >0 and len(stop_track_buttons) == self.box_width: #logic check have track stop assignments and 
            track_stop_buttons = [ ButtonElement(is_momentary, MIDI_NOTE_TYPE, midi_channel, stop_track_buttons[index]) for index in range(len(stop_track_buttons))]
            for index in range(len(track_stop_buttons)):
                track_stop_buttons[index].name = 'Track_' + str(index) + '_Stop_Button' # sure, why not
            self.session.set_stop_track_clip_buttons(tuple(track_stop_buttons))
        else :
            self.log_message("..::|| Stop notes not in use or error found Modern.DJ ||::..")
        # Check for stop all clips option
        if stop_all_clips >=0 : 
            self.session.set_stop_all_clips_button(ButtonElement(is_momentary, MIDI_NOTE_TYPE, midi_channel, stop_all_clips))
        # creating the matrix of buttons from the launch_button_list (tuple)
        launch_button_list_len = len(launch_button_list) # var used multiple times. This is a performance modification
        if (self.box_height*self.box_width) ==  launch_button_list_len : # check box size against number of button vars sent
            launch_ctr = launch_button_list_len -1 # decrement for zero offset in list/tuple
            launch_button_list.reverse() #reverse list from human readable for decrement use (performance tweak)
            ## check for use of RGB
            if use_velocity_for_RGB != 1: # if not enabled use these defaults
                self.log_message("..::|| RGB not in effect assigning defaults ||::..")
                self.clip_loaded_stopped = 1
                self.clip_currently_playing = 127
                self.clip_triggered_to_play = 64
            else: # yes RGB in effect...assign per the parameters script
                self.clip_loaded_stopped = clip_loaded_stopped
                self.clip_currently_playing = clip_currently_playing
                self.clip_triggered_to_play = clip_triggered_to_play

            for scene_index in range(self.box_height): # loop on the notes matrix
                scene = self.session.scene(scene_index) # part of the martix built, think rows
                scene.name = 'Scene_' + str(scene_index) # sure, why not
                button_row = [] # create recepticle
                # loop across the tracks
                for track_index in range(self.box_width): 
                    button = ButtonElement(is_momentary, MIDI_NOTE_TYPE, midi_channel, launch_button_list[launch_ctr]) # button instance for _Framework
                    launch_ctr = launch_ctr -1# decrement is faster than increment
                    button.name = str(track_index) + '_Clip_' + str(scene_index) + '_Button' # sure, why not
                    button_row.append(button) # add to our growing list
                    clip_slot = scene.clip_slot(track_index) # clips slot and buttons are not the same thing, this aligns these ideas in the red box
                    clip_slot.name = str(track_index) + '_Clip_Slot_' + str(scene_index) # sure, why not
                    # assign the button and and status in th refrech update
                    clip_slot.set_stopped_value(self.clip_loaded_stopped ) # this number is sent back to the machine allowing diff colors for stopped
                    clip_slot.set_started_value(self.clip_currently_playing) # this number is sent back to the machine allowing diff colors for started/is-playing
                    clip_slot.set_triggered_to_play_value(self.clip_triggered_to_play) # this number is sent back to the machine allowing diff colors for cued, will play next                   
                    clip_slot.set_launch_button(button) # part of the slit+button = go time paradigm
                matrix.add_row(tuple(button_row)) # close out the matrix build. @todo - possible subclass here?
        else : # log message
            self.log_message("..::|| Number of notes defined does not match box height and width Modern.DJ ||::..")
        self.set_highlighting_session_component(self.session) # new for live9 -- this is for the box. via aumhaa/bitnomad
        return None
    
    # Volume control specific
    # Creation of a slider for volume. Not a small burger
    def slider(self, channel, value):
        if (value != -1): 
            return SliderElement(MIDI_CC_TYPE, channel, value) # assign data to slider object
        else:
            return None

    # Static volume control offset via volume_offset param
    def custom_offset_mixer(self):
        # skipped the subclass
        # for some reason this pattern will allow the offset and static volume control.
        # looking for explaination and insight on this...Bueller?
        self.mixer_custom = MixerComponent(self.box_width) # get a local mixer object ready
        self.mixer_custom.name = 'Mixer Custom' # name
        self.mixer_custom.set_track_offset(self.volume_offset)  # the offset
        # compare width with track vol count to qualify -- put somewhere else 
        for index in range(self.box_width): # @marwei must kill this style and count
            self.mixer_custom.channel_strip(index).set_volume_control(self.slider(midi_channel, self.track_volume_static[index]))
    
    # volume control specific, will move with red box
    # Set up mixer locally / object
    def _setup_mixer_control(self):
       self.mixer = CustomMixerComponent(self.box_width, self)  # essentially grab the super class
       self.mixer.name = 'Mixer' # sure, why not
       self.mixer.set_track_offset(0)  # not sure if needed, seems not to hurt.
       # check box width and tuple size. Forward compatibility
       if len(self.track_volume) == self.box_width:  # error checking per established app standard
           # loop on the CCs and create strip/volume control
           for index in range(self.box_width): #  @todo kill this and count in reverse via decrement (performance)
               self.mixer.channel_strip(index).set_volume_control(self.slider(midi_channel, self.track_volume[index]))
       else: # bad math, error messAge, fail
           self.log_message(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime()) + "..::|| volume param bad math message. box_width != len(track_volume) ||::..")
    
    def disconnect(self):
        self.log_message(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime()) + "..::|| Modern.DJ LIVE9 baseline MRS  closed ||::..")
        self.log_message("**************************************************")
        self.log_message(" - ")
        ControlSurface.disconnect(self)
        return None
    
    def version_information(self):
        baseline_version = str(baseline_script_version_major)
        baseline_version += '.'+str(baseline_script_version_minor)
        baseline_version += '.'+str(baseline_script_version_patch)
        self.log_message('Modern.Dj Baseline Script Version '+baseline_version)
        self.log_message('Modern.Dj Baseline Script Release Note : '+baseline_script_version_note)
 
'''
# integer debug copy+paste
someInt = ' %i ' % SOME_NUM
self.log_message(" Seacrh4This "+someInt)
'''