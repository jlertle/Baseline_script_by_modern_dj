#!/usr/bin/env python

# Welcome to the legendary readme.py file. We have been waiting for you!

# used in log
baseline_script_version_major = 1
baseline_script_version_minor = 0
baseline_script_version_patch = 0
baseline_script_version_note = 'Initial Build'

"""

-----
----
---
--
-
THIS SCRIPT IS FOR ABLETON LIVE 9 ONLY! 
-
--
---
----
-----

Table of contents :

i. Preface
1. License Information
2. Credit and Contact
3. Preamble
4. Usage and Manual
    A. Rules and Operational Guidelines for Control Surface Scripts with Ableton
    B. Comments and Inline Documentation of the Baseline Script
    C. About the Compiler
    D. How to change the name of a control surface.
    E. Why do I only see .pyc files?
    F. Assigning Values to the parameters.py File
5. Meta
    A. Version Information
    B. Change Log
    C. To Do List
    D. Road Map
6. Reference
    A. Ableton Note to MIDI Note Number Value
    B. Support

--------------------------------------------------------------------------------
i. Preface
--------------------------------------------------------------------------------

This script is for Ableton Live 9 generic control needs.  Features include :

1. "Red Box" Relative control and navigation for clips in Session View
2. Navigation, including up, down, left, and right for navigation
3. Single MIDI channel use.
4. Mapping of Stop buttons, including Stop All
5. Scene Launch for the session view
6. Tempo control via button (note) events
    a. Definable increments (floating and non floating)
    b. Increments for add and remove are not required to match
7. Support for RGB LED feedback, especially Livid Instruments
8. Volume support in 2 forms
    a. "Red Box" control surface volume where the control moves with the navigation
    b. Static volume control with offsetting. This is for advanced control surface control where volume should not
    move with the box and often needs to be offset (okay, I really needed this, so you get it too! --M)

Of course features are left as "opt in" via the parameters file when possible, detailed here an and on the parameters.py file

More features are coming. Look at the Road Map

Don't be shy, contribute!

--------------------------------------------------------------------------------
Section 1 : License Information
--------------------------------------------------------------------------------

Copyright (c) 2011, 2012, 2013+ Data Mafia
All rights reserved, as applicable, with respect.

Actually I expect people to do what ever the hell they want, like I can stop
any of this behavior?

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice, this
list of conditions and the following disclaimer in the documentation and/or
other materials provided with the distribution.

* Neither the name of the Data Mafia nor the names of its contributors may be
used to endorse or promote products derived from this software without
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

This work is dual licensed under the BSD3 or Creative Commons, for more
information on this topic please refer to the maintainers information available
via the following addresses and information:

BSD 3 Clause License
http://www.opensource.org/licenses/BSD-3-Clause This license is included below

and/or

Creative Commons Attribution-ShareAlike 3.0 Unported License.
http://creativecommons.org/licenses/by-sa/3.0/

If these licenses are not compatible with a specific use case, please
contact Data Mafia directly to discuss your situation.

--------------------------------------------------------------------------------
Section 2 : Credit and Contact
--------------------------------------------------------------------------------

This body of work represents thousands of hours of work by hundreds of people. 
Not everyone can be listed here directly, but we should mention some names,
companies, and organizations.

Before we mention anyone, a general statement is required :

Ableton is a wonderful software package and I appreciate how the stakeholders,
developers, and creators have not closed the "back door" to the API.  Ideally
this interface and code-set should be documented and supported officially for the
betterment of mankind and music. Until that day, I, as well as others, will
continue to work diligently to provide a general purpose, well written script
for all to use, share, and expand towards greater heights of music and sound
control. I do this FOR THE USERS and this work is presented as a statement of
good faith for others to follow and find inspiration. Included in this notion of
good faith is the formal declaration that Ableton in particular needs to find
a means to balance the business model with the need to provide the tools and
knowledge to continue to enable or contribute to a musical renaissance that is
beyond their control or ownership. Should I become martyr (metaphorically) so
be it. Let an era of change begin at the closing of this paragraph.

--Marc

Managing programmer for this work is Marc / Data Mafia. http://datamafia.com

http://modern.dj and http://moderndotdj.com re-authorized to represent this
script in the form of a web app for all to use, free of charge.

Special thanks to my good friend BitNomad (http://github.com/bitnomad) who is
a great teacher and inspiration to get this script tight. Your code and
contributions are very welcome, anytime.

The earliest versions of this script came via information and code by
Michael Chenetz. Permission has been granted for free distribution from
Michael Chenetz via http://maxforlive.info

Aumhaa and his website (http://www.aumhaa.com) has helped us kick this script
over the line to working condition more than one time. Please keep up your
good work and occasional blog posts. We do read them!

Hanz Petrov, whoever you are, thank you for the initial posts (parts 1-4) that
served as a critical reference for our work in Live 8.
http://hanzoffsystems.tech.officelive.com

Additional thanks to Livid Instruments, my friends, who have continued to
make solid and higher quality controllers. I found what I was looking for
in your hardware and this has been a huge source of inspiration.  I wish
to thank all people who work at Livid. Never stop listening.
http://lividinstruments.com

Ill Gates (http://illgates.com) was the first person to make me realize that
I was doing it wrong.  The painful lesson you provided has guided me in my
in many steps towards full dominion over sound. I am delighted to count you
as a friend and collaborator.

Moldover (http://moldover.com) requires mention. His vision, insight, and
sacrifice has not gone unnoticed. You have my support and friendship no
matter where you may need to travel.

Julien Bayle released the Live 9 _Framework scripts via Github. I don't know
how you did this as a Certified Trainer, regardless, you made it to the finish
line first (https://github.com/gluon) and you deserve credit. Be sure to pass
my sentiments along to Ableton and continue to contribute back to the users.

Considerable help in creating this script was provided by deconstructing the 
QuNeo control surface script created by [credit pending].

To the testers and many people who made our work so great, thank you.  You
know who you are, you know why you are so important, I am in your debt.
Special thanks to sources claiming Ableton status.

Finally, I would like to thank my family, especially my wife Heidi. She is
more than a partner, more than a wife, she is inspiration, motivation, and
serenity required to complete this work and continue to give back and become
a better person.

--------------------------------------------------------------------------------
Section 3 : Preamble
--------------------------------------------------------------------------------

This is a baseline midi remote script for any controller not requiring a
"handshake" or similar serialization. Any controller requiring a proprietary
data exchange to operate is counterproductive, foolish, and insulting. This
feature set should be eliminated or documented.  The legacy business practices
that clearly led to these decisions are hereby officially suspect. I declare
shenanigan on you!   

Any controller that requires a "handshake" will not work with this script.
Support for these shenanigan style scripts is available via the internet and
other sources.

This particular script operates in a very specific manner.  As is the case with
most programming, there is more than one way to do things.  Before any judgement
is cast on my style and (lack of) knowledge of Python please digest these points
first:

1. This script is intended, in the most simple manner, to be accessible
by people who are NOT programmers. As a result, certain needs and
requirements force a certain stylistic divergence from most other
control surface scripts

2. The script is intended to operate, from a configuration standpoint,
via the parameters.py file. This in turn makes the parameters.py file
a configuration beyond integer and list assignment and creates a
means to turn code (blocks) on and off. This allows users to select
functionality they desire. This idea is key.

3. Via the code style mentioned above in #2, additional checks,
configuration, logging, and logic is in use.

4. This script, in style, function, and intent, ultimately has been
created for use in a (web) app scenario.  This is a critical departure
from nearly all, if not all, other control surface scripts. The intent,
again, is to provide a tool and resource that the stakeholders and
various corporate vampires and self-interested parties are not
providing back to the community.

5. Readability, documentation, and comments are an ever-present goal
and desire.  This script should be a resource for control as well
as learning. Those of us who "wrote" this script are not perfect, so feedback,
suggestions, rewrites, and help is always welcome.

6. This work was NOT created for profit or personal gain. In fact this
whole project was originally Marc tying to build the control surface
stuck in his brain.  The first version only took 2000 hours (thousand).
Once complete it was clear that more support was needed, especially for
the non-programmer.  If you would like to donate to the cause, please
do not let me stop you from giving me money. 

The Paypal account to donate for this project is marc@creativeelectronica.com

------------------------------------------------------	--------------------------
Section 4 : Usage and Manual

     A. Rules and Operational Guidelines for Control Surface Scripts with Ableton
     B. Comments and Inline Documentation of the Baseline Script
     C. About the Compiler
     D. Assigning Values in the parameters.py File
     E. Why do I only see .pyc files?
     F. How to change the name of a control surface.
--------------------------------------------------------------------------------

This MIDI Remote Script for Ableton Live 9 is loosely coupled to the
parameters.py file. In non-programmer speak, let me tell you that this file is the only file where a
user should modify anything.  The writing of this Usage and Manual is intended for the
person(s) who have NO programming experience and want to make modifications
to the way the script interacts with Ableton and the API for control surfaces.

A. Rules and Operational Guidelines for Control Surface Scripts with Ableton

The control surface scripts are written in Python (http://python.org) and are compiled as needed
with the launching of Ableton. Python is an exacting language where indentation (usually tab
spacing) defines code and the hierarchy syntax in the script. This is where many errors can occur.
Pay close attention to this aspect of the syntax when making any changes. It is recommended to
get an IDE (integrated development environment) program with Python syntax checking. Personally
I use Active State's Komodo IDE (http://activestate.com) where there are trial and free versions
available. There are other programs available, some for free. If you intend on working on the Python
code beyond a few tweaks of the parameters.py file consider using a program with Python syntax
checking.

B. Comments and Inline Documentation of the Baseline Script

Comments are ubiquitous in scripts and code. They serve many purposes including documentation,
warnings, road-mapping or todo lists, and other inter-programmer or self serving communication.
There are copious amounts of comments in the Baseline script. In fact, this manual is actually a
Python file containing nothing more than a huge comment block (and one variable declaration).

Comments in this work come in 2 formats, inline and multiline.
Inline comments are preceded by the hash (#) symbol. The rule for these comments are 2 fold. First,
comments are limited to one line per hash. Second, all text to the right of the hash is a comment
and totally inert. Comments take on the appearance like these examples :

# This is a comment

or

def special_method(self) : # This is another comment

or possibly

# This comment was broken onto another line to improve
# the readability for the programmer

Multiline comments are encapsulated by triple single quotes ('''), exceptions notwithstanding. A
multiline comment will look like this :

'''
This is a
Multiline
Comment
'''

In the Baseline script I have included a near foolish amount of comments and commentary. Some
humorous (for non-German people), some functional, and many explaining how the script works and
interacts with the Ableton _Framework. The goal is to increase the understanding of the control
surface API and encourage others to do the same. There may be mistakes in my understanding of
the control surface API, Python, or other areas. In the event of a mistake please contact me directly.
Refer to the "Credit and Contact" section to suggest changes or clarification. This includes better
methods and similar programming advice.

In the previous paragraph the term "valid" was used in discussion the compiler. The term valid refers
to a file that can be compiled.  The file can still have errors. Errors after the compiler has
successfully run is in the log.txt file. The log.txt file is where all actions are logged and is important
for debugging and diagnosis of problems in the script.

When working with the compiler and Ableton changes are slow moving as a few things need to
happen in the development cycle.  If a change to a .py file is made the .pyc files should be cleared
(deleted) to force the compiler to run again. This is best practice but may not be necessary. As of
the time of writing this document I can not deliver a set of guidelines as to when or why the
compiler runs.  For every change that is made to the Python files, clear out all of the .pyc files for
that control surface script.

To test changes, save edits to the .py files in the correct directory and open Ableton. This will
compile the files (if valid) on start up making them available once the program is completely open.

C. About the Compiler

Ableton uses Python (a scripting language) to communicate with the API via the included
_Framework. When Ableton launches all valid Python files are compiled into .pyc files. Consider
.pyc files as immutable digital objects resulting from the .py files (instruction sets). These .pyc files
are static and unchanging for all intensive purposes. These files are faster and part of a clean running
system in the context of higher level programming.

D. Why do I only see .pyc files?

If you only see ".pyc" files and NOT ".py" files don't freak out, yet. These are compiled files (think of
them as generally immutable).  I highly encourage all programmers to include the .py files in
distributions. If you only see .pyc files one of 2 things probably happened. First, you deleted the .py
files instead of the .pyc files in building or modifying the control surface script. Look in your trash
bin for these files. Alternatively, you are working with another person's script and they did not
include the native file. Now you should freak out. These files can be decompiled, but this is very far
outside the discussion, scope and instructions of this manual.

E. Assigning Values in the parameters.py File

As mentioned, this script is loosely coupled to the parameters.py file. All changes should be isolated
to this script with the exception of changing the script name (advanced). There are 2 types of
variables in use. They are integers and tuples (lists).

Integers are numbers assigned to a keyword. The format looks like this :

keyword_integer = 99

Where keyword_integer is the keyword "holding" the variable 99.

If the assignment is not in use the word "None" is used in a case-sensitive manner as such :

keyword_integer = None

Tuples and lists are used in a loose manner and may be considered interchangeable to the
nonprogrammer reading this manual. A tuple is a collection of integer values in the context of the
Baseline script. These collections are comma delimited and look like this :

my_tuple = [1,2,3,4,5,6]

The collection is encapsulated by square brackets ([]). The collection may be broken down into
multiple lines as this next example shows :

my_tuple = [
     1,2,3,
     4,5,6
     ]

This is often done for human readability.

Should a tuple not be used an empty set of square brackets is required :

my_tuple = []

These practices will keep the script functional where elements are not in use (disabled).

The parameters.py file has considerable comments inline (please read the "Comments and Inline
Documentation of the Baseline Script" section above). These comments explain the use and
functionality as well as dependencies in control surface script.

In use are many enabling parameters that trigger larger code blocks allowing this script to quickly
change functionality, be automated an a web app, and expanded over time. These parameters
usually have the word "enable" in the name. These enabling parameters should only be assigned 1
or 0 for yes and no respectively. Do not use "None" to disable.

In section 6 "Reference" is a translation of all Ableton note values to integers used in this script.
Use this reference for translation purposes as there are multiple schemas in use for the conversion
of MIDI notes to numeric values.

From here refer to the comments and inline documentation on the parameters.py file in editing
values.

F. How to change the name of a control surface. 

The __init__.py file is where the whole control surface kicks off. This file bootstraps the entire
process, fires off the master control center, places the man behind the curtain, and should be
though of as the point of entry and beginning.  There are some rules for this file and operation.

Rule : This file expects certain arguments beyond the scope of this manual. Do not change anything
other than the control surface script name instances. Commonly there are 3 name instances in
the __init__.py file as written for the Baseline script.

Rule : There are conventions in place regarding naming that must be followed. Rather than discuss
the rules and details we will instead create a strict naming convention that should suffice for all
renaming requirements. Use only English A-Z characters in a case-sensitive manner. Use of
numbers is acceptable, but no name can begin with any character other than A-Z (uppercase or
lowercase). No punctuation should be used except for the underscore (_). The underscore should be
used inside a text block. The following example is considered valid :

Name_of_my_script_version1_2

When selecting a new name for a script there are MANY reserved names that are strictly unavailable.
Refer to the Python documentation for this list (http://python.org). To avoid naming collisions I
recommend prefixing all scripts in a safe manner. Consider your initials followed by an underscore
as a prefix like this :

aa_

creating a script named

aa_my_script_v1

Use of consistent prefixing will keep all scripts grouped together in the Ableton control surface
drop-down menu.

Rule : All script names must be unique.

To change the name of the control surface script all name instances must be changed and
consistent in all appearances.  For the sake of demonstration, all name instances will be referred to
explicitly as name_instance and new_name_instance in code examples. The name_instance and
new_name_instance must be exactly the same in all changes, both in characters on Python file as
well as directory changes and file name changes. All of this is detailed next.

The changes on the __init__.py file are three fold. The first 2 changes are:

from name_instance import name_instance

to this result

from new_name_instance import new_name_instance

The final change on the __init__.py file is to the right of the word "return". It looks like this :

return name_instance(c_instance)

To this result

return new_name_instance(c_instance)

That concludes changes to the __init__.py file.

The new name_instance, as mentioned previously, must be consistent. For the sake of our example
our new name_instance is new_name_instance. The changes to the __init__.py file need to be carried
over to a few more places.

Next change the name of the class on the file named name_instance.py (or whatever the previous
control surface was named). On this file change name_instance to new_name_instance after the
import statements where the code looks like :

class name_instance(ControlSurface):

To this result

class new_name_instance(ControlSurface):

This file needs to have the name changed to reflect the name changes. The file name_instance.py
should be changed to new_name_instance.py.

The final change is a directory folder. As you might suspect, the directory folder should match the
new control surface name. Change the directory previously named name_instance to
new_name_instance.

That concludes the name change instructions for the control surface. To review, here is a brief
outline of the expected file structure for Ableton in compiling Python files for interaction with the
API.

Inside the Ableton app, via the directions specific for your operating system is a folder containing
the MIDI remote scripts, in the form of Python code (native and/or compiled). This folder should
contain a folder called _Framework. The _Framework folder is the Ableton "code" to interact with
the API on a control surface level. Also in this folder is the native (for lack of a better word) scripts
for various controllers and YOUR new script. Your new script may now have a name like
"new_name_instance" where directly inside this folder is a number of Python files ending with ".py"
and possibly ".pyc". For more information on the ".pyc" files please see the section titled "About the
Compiler". All of the files inside the new_name_instance folder should be on the same level meaning
there is no files nested in additional folders. This may change as the script grows or others add new
functionality. There should be a number of other files, but we specifically should see files named
"__init__.py" and "new_name_instance.py" (or the name selected other than new_name_instance).

If for some reason you only see ".pyc" files, please refer to the section titled "Why do I only see .pyc
files?".

--------------------------------------------------------------------------------
Section 5 : Meta

    A. Version Information
    B. Change Log
    C. To Do List
    D. Road Map
--------------------------------------------------------------------------------

A. Version Information
The version of this script is listed at the top of this file using the variable "baseline_script_version"
following the major.minor.patch format. The version number is part of a module schema for the web
app and eventual open source release of all work (including the web app).

B. Change Log

Version 1.0.0 :

Initial release of the Baseline script for Ableton Live9

C. To Do List

Add sends.
Decide if sends should be unlimited or not.
Add track enable control.
Add device control and navigation.
Add proprietary handshakes (APC, MPD, Launchpad)
Livid Base via channel change using "Program Change" method is not refreshing correct.

D. Road Map

Build web app in the most basic sense.
Once the web app is built continue adding features to the script.
Test more before adding to the web app.
Release the web app open source when appropriate.

Please contact us regarding reatures andthe rooadmap.

-----------------------------------------------------------
Section 6 : Reference Information
    A. Ableton Note to MIDI Note Number Value
    B. Support
-----------------------------------------------------------

I love you so much I actually typed out all of the MIDI note translations. You are welcome!

C-2=0
C#-2=1
D-2=2
D#-2=3
E-2=4
F-2=5
F#-2=6
G-2=7
G#-2=8
A-2=9
A#-2=10
B-2=11

C-1=12
C#-1=13
D-1=14
D#-1=15
E-1=16
F-1=17
F#-1=18
G-1=19
G#-1=20
A-1=21
A#-1=22
B-1=23

C0=24
C#0=25
D0=26
D#0=27
E0=28
F0=29
F#0=30
G0=31
G#0=32
A0=33
A#0=34
B0=35

C1=36
C#1=37
D1=38
D#1=39
E1=40
F1=41
F#1=42
G1=43
G#1=44
A1=45
A#1=46
B1=47

C2=48
C#2=49
D2=50
D#2=51
E2=52
F2=53
F#2=54
G2=55
G#2=56
A2=57
A#2=58
B2=59

C3=60
C#3=61
D3=62
D#3=63
E3=64
F3=65
F#3=66
G3=67
G#3=68
A3=69
A#3=70
B3=71

C4=72
C#4=73
D4=74
D#4=75
E4=76
F4=77
F#4=78
G4=79
G#4=80
A4=81
A#4=82
B4=83

C5=84
C#5=85
D5=86
D#5=87
E5=88
F5=89
F#5=90
G5=91
G#5=92
A5=93
A#5=94
B5=95

C6=96
C#6=97
D6=98
D#6=99
E6=100
F6=101
F#6=102
G6=103
G#6=104
A6=105
A#6=106
B6=107

C7=108
C#7=109
D7=110
D#7=111
E7=112
F7=113
F#7=114
G7=115
G#7=116
A7=117
A#7=118
B7=119

C8=120
C#8=121
D8=122
D#8=123
E8=124
F8=125
F#8=126
G8=127

B. Support

We offer no support in any manner.

"""