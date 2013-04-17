#!/usr/bin/env python
# DJNSM / @djnsm / djnsm.com -> datamafia.com
# Free to use, please refer to the readme.py file for license , info, and the uncompromised enlightenment

#NOTE - list and tuple use might be a little loose in the explanation. Please forgive

# Parameter Options 0-127, no collisions!

# ******************************************************************************
# * MAIN CONTROL SURFACE PARAMETERS 
# ******************************************************************************

# midi_channel is offset below. Range begins at 1, not 0. Thus assigning 1 here will send 0 to the machine
midi_channel=1
# Offsetting compensation. Yeah.
midi_channel -= 1  # << Do not remove this unless you understand the consequences

# ******************************************************************************
# * MATRIX PARAMETERS
# *****************************************************************************

# Used to turn code block on/off
# Also triggers volume control in the script. Need Matrix for Volume
enable_matrix = 1 # 1 = yes, 0 or not 1 is no
# matrix off kills a lot of stuff : grid, stops, stop all, volume
# does not impact volume

### NAVIGATION of Control Surface Box ###
### Box navigation. Operates as pairs up/down and left/right

# Up / Down
up_button_note_number = 24 # up navigation
down_button_note_number = 25 # down navigation
# Left / Right
left_button_note_number = 18 # left navigation
right_button_note_number = 19 # right navigation

### CONTROL SURFACE SIZE

## Declare the size of the box in Ableton clip cells.
# This is used to check the launch button count where box_width x box_height = count(launch_button_list)
# used for volume 
box_width = 4 # width of the the "red-box" aka tracks
box_height = 4 #height of the "red-box" aka scenes

### Launch button list *** Required *** Python list format
# Assigned Left to Right, Top to bottom, comma separated
launch_button_list = [
    60,61,62,63,
    52,53,54,55,
    44,45,46,47, 
    36,37,38,39
    ]
# the number of notes in launch_button_list must match box_width * box_height

# Assigned left to right. Use empty list do disable example below.
#stop_track_buttons = [] # Uncomment this line to use no track stop buttons and add comment to next line
# Track stop code block is enabled if variable is not empty via a count
stop_track_buttons = [10,11,12,13]
### (if used) stop_track_buttons must match box_width 

# Assigned top to bottom. Use empty list do disable example below.
# scene_launch_notes = [] # Uncomment this line to use no scene launch buttons and add comment to next line
# Scene launch code block is enabled if variable is not empty via a count
scene_launch_notes = [24,25,26,27,126,127]  
### (if used) scene_launch_notes launch notes must match box_height

### Stop all clips. Disabled by the use of Python None assignment. Example below.
#  stop_all_clips = None # Uncomment this line to use no stop all clips button and add comment to next line
# Stop all clips code block is enabled if variable is set to a valid numeric MIDI value
stop_all_clips = None

# ******************************************************************************
# * TEMPO CONTROL PARAMETERS tempo_control.py Tempo Control via BitNomad - Thx C!
# ******************************************************************************

# Trigger for tempo control enablizationerness
# Used to turn code block on/off
enable_tempo_control = 1 # 1 for yes, 0 for no

# note : tempo_control.py uses session, mixer, midi_channel
# 70 = tempo_button_up     78 = tempo_button_down
tempo_button_up = 22
tempo_button_down = 23

# up and down tempo interval. To go down in bpm use negative
# examples : -1 = down 1 bpm, 3 = up 3 bpm, .02 = increase by .02 bpm (2/100th of a bpm)
# practical range .01 to 10 positive and negative
tempo_button_up_interval = 1.0 
tempo_button_down_interval = -1

# ******************************************************************************
# * VOLUME PARAMETERS : CC values for slider. knob, or fader
# ******************************************************************************

# turns on the various volume stuff
enable_volume_control = 1

# List of CCs for volume control. Reads left to right. Actually a tuple
track_volume = [1,2,3,4]

# enable static volume  / offset volume - will not move w/box overriding track_volume
enable_static_volume = 0 # 1 for yes, 0 for no
track_volume_static = [1, 2, 3, 4] # the CC's
### (if used) the number of track_volume_static values must match box_width 

# Applies only to enable_static_volume = 1
# Track offset 0 has no effect, positive number values will push the audio volume to the right
# skips MIDI tracks.  
volume_offset = 4

# ******************************************************************************
# * Livid Instruments Specific Support
# ******************************************************************************

# LIVID RGB COLOR CODES 
LIVID_OFF = 0
LIVID_RED = 16
LIVID_WHITE = 1
LIVID_CYAN = 4
LIVID_PURPLE = 8
LIVID_BLUE = 32
LIVID_YELLOW = 64
LIVID_GREEN = 127

# ******************************************************************************
# * Velocity Feedback for RGB type units. Not supported by every device.
# ******************************************************************************

# set to true to enable RGB velocity feedback (conditional check)
# Used to turn code block on/off
use_velocity_for_RGB = 1  # 1 for yes, 0 for no

# Use MIDI range per device (0-127). Consult something to tell you what you need to know.
# This is the velocity returned to the following clip states
clip_loaded_stopped = LIVID_BLUE  # clip is in matrix but not playing
clip_currently_playing = LIVID_GREEN  # currently playing clip in matrix
clip_triggered_to_play = LIVID_RED  # clip is triggered to play but not playing yet
