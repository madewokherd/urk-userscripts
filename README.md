Scripts for urk that are not included by default.

Unless otherwise indicated, all sources are authored by Vincent Povirk, Marc Liddell, and poiuy_qwert, and are licensed under the GPL version 2 or greater.

== List of user scripts
buglink.py - hotlinking for bugzilla bugs
color_index.py - Color Index window to choose colors like mIRC
color_select.py - Color chooser for hex colors
debug.py - debug window like mIRC(displayes incoming and outgoing raws)
tab_minimize_hack.py - hack to make clicking on the active tab go to the prevously active tab
urgency.py - change main window title on activity
uts/uTs.py - replacement for theme.py with easier customization
wikilink.py - hotlinking for links to wikipedia
ial.py - The Internal Address List holds the addresses of every user on a channel with you. 

== Install instructions

To install a script, copy it into userpath/scripts. To find the value of
userpath, type

    /pyeval urk.userpath

On Linux, this will generally be ~/.urk, in which case you should put scripts in ~/.urk/scripts

All scripts in userpath/scripts will be loaded on startup by default. To load a script immediately, use the /load command. For example, to load wikilink.py, type

    /load wikilink

