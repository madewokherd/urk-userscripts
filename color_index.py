####################
# Color Index v1.5
####################
# Color Index is a script to create a color
# index window like mIRC.
## Updates #########
# v1.5
#   - Fixed glitch with range
## Usage ###########
# Type '/colind on/off' to turn Color Index
# on or off.
#
# Type '/colind -t on/off' to turn Color
# Index title off.
#
# Config entries colind and colind-title can
# be True or False to show On and Off.
#
# Ctrl+K will open the Color Index if it's
# enabled.
#
# When making a background color the comma
# will open the Color Index if it's enabled.
#
# Clicking a color on the Color Index will
# place it in the editbox and close the
# window.
#
# Clicking the X on the title if its enabled
# will close the window with no color added.
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

color_index = None

class ColorIndex:
    def select(self, widget=None, event=None, data=None):
        global color_index
        if data:
            self.win.input.insert(data)
        color_index.window.hide_all()
        color_index = None

    def __init__(self, win):
        if conf.get('colind-title'):
            height = 67
        else:
            height = 46
        self.win = win
        self.window = gtk.Window(gtk.WINDOW_POPUP)
        winx = windows.manager.get_position()[0] + win.input.get_allocation().x + 5
        winy = windows.manager.get_position()[1] + win.input.get_allocation().y - height + 22
        self.window.move(winx,winy)
        self.window.set_title('Color Index')
        self.window.set_size_request(174,height)
        self.window.set_border_width(3)

        all = gtk.VBox(True, 2)
        self.window.add(all)

        if conf.get('colind-title'):
            toolbar = gtk.HBox(False)
            all.pack_start(toolbar)
            tool_lab = gtk.Label('Color Index')
            tool_lab.set_size_request(149,19)
            tool_event = gtk.EventBox()
            toolbar.pack_start(tool_lab)
            toolbar.pack_start(tool_event)
            tool_but = gtk.Label('X')
            tool_event.add(tool_but)
            tool_event.set_events(gtk.gdk.BUTTON_PRESS_MASK)
            tool_event.connect('button_press_event', self.select)

        top_row = gtk.HBox(True, 2)
        bot_row = gtk.HBox(True, 2)
        all.pack_start(top_row)
        all.pack_start(bot_row)

        event_box = []
        color_lab = []
        for col in range(16):
            event_box.append(gtk.EventBox())
            if col < 8:
                top_row.pack_start(event_box[col])
            else:
                bot_row.pack_start(event_box[col])
            color_lab.append(gtk.Label(str(col).zfill(2)))
            event_box[col].add(color_lab[col])
            event_box[col].set_events(gtk.gdk.BUTTON_PRESS_MASK)
            event_box[col].connect('button_press_event', self.select, str(col).zfill(2))
            event_box[col].modify_bg(gtk.STATE_NORMAL,event_box[col].get_colormap().alloc_color(parse_mirc.colors[col]))
        self.window.show_all()
        self.window.window.set_keep_above(True)

def is_color(text,cursor):
    for num in range(1,4):
        offset = cursor-num
        if offset > 0:
            if text[offset] == '\x03' and not offset == 1:
                return True
            elif not text[offset].isdigit():
                return False
    return False

def onKeyPress(e):
    if conf.get('colind'):
        global color_index
        if color_index:
            color_index.select()
        else:
            if e.key == 'comma' and is_color(e.window.input.get_text(),e.window.input.get_property('cursor-position')):
                color_index = ColorIndex(e.window)
            elif e.key == '^k':
                color_index = ColorIndex(e.window)

def onActive(e):
    global color_index
    if color_index:
        color_index.select()

def onCommandColind(e):
    if e.args:
        if e.args[0] == 'on' and 't' in e.switches:
            conf['colind-title'] = True
            e.window.write('* Color Index Title enabled.')
        elif e.args[0] == 'on':
            conf['colind'] = True
            e.window.write('* Color Index enabled.')
        elif e.args[0] == 'off' and 't' in e.switches:
            conf['colind-title'] = False
            e.window.write('* Color Index Title disabled.')
        elif e.args[0] == 'off':
            conf['colind'] = False
            e.window.write('* Color Index disabled.')
