####################
# Color Select v1
####################
# Color Select is the brother(or sister) to
# Color Index. It makes it easy to select
# colors and have them put in your editbox
# as a hex string.
## Usage ###########
# Type '/colsel on/off' to turn Color Select
# on or off.
#
# Config entrie colsel be True or False to
# show On and Off.
#
# Ctrl+L will open the Color Index if it's
# enabled.
#
# There is no support for when creating a
# background color, just hit Ctrl+L again
# and remove it after.
#
# When you press Ok in the window it puts
# the color into the editbox of the window
# Ctrl+L was pressed in.
#
# If you Cancle or Close the window nothing
# happens.
## Author #############
# Color Index was writen by poiuy_qwert. You
# can contact him on irc.gamesurge.net in
# channels #script, #urk, or #world.
#######################
import events
import parse_mirc
import gtk
import windows
from conf import conf

color_select = None

class ColorSelect:
    def __init__(self, win):
        colordialog = gtk.ColorSelectionDialog('Color Select')
        winx = windows.manager.get_position()[0] + win.output.get_allocation().x + 5
        winy = windows.manager.get_position()[1] + win.output.get_allocation().y + 24
        colordialog.move(winx,winy)
        colorwidget = colordialog.colorsel
        colorwidget.set_has_palette(True)
        response = colordialog.run()
        if response == gtk.RESPONSE_OK:
            color = colorwidget.get_current_color()
            win.input.insert(conv_col(color))
        colordialog.hide()
        global color_select
        color_select = None

def conv_col(color):
    ret = ''
    for col in (color.red,color.green,color.blue):
        ret += str(hex(col/256)[2:4]).upper().zfill(2)
    return ret

def onKeyPress(e):
    if conf.get('colsel'):
        global color_select
        if e.key == '^l' and not color_select:
            color_select = ColorSelect(e.window)

def onCommandColsel(e):
    if e.args:
        if e.args[0] == 'on':
            conf['colsel'] = True
            e.window.write('* Color Select enabled.')
        elif e.args[0] == 'off':
            conf['colsel'] = False
            e.window.write('* Color Select disabled.')
