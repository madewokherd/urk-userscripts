####################
# Debug by poiuy_qwert
#  v2
## Debug ###########
# Debug is a script to create debug windows
# that show all incoming and outgoing raws
# for certain networks. Place the file in
# your profiles script folder and type:
#  /load filename
## Updates #########
# v2
#  - Fixed for newest update(no longer needs
#     unnoficial irc.py fix)
## Usage ###########
# Typing in a debug window will send the
# text to the network as a raw.
#
# To create a debug window for a network,
# you just type '/debug' in any window
# that is a part of that network.
#
# To stop debugging on a network just type
# '/debug off' in any window that is a part
# of that network.
#
# You can type '/pingpong on/off' to turn
# display of PING and PONG raws on/off.
#
# You can add the 'pingpong' config entry
# to True or False to set if PING and PONG
# raws are displayed.
#
# You can add the 'debug' config entry to
# open a debug window on every network
# when you connect to it.
#
# To change the output format change what
# is returned in the procedure debug_output.
## Author #############
# Debug was writen by poiuy_qwert. You can
# contact him on irc.gamesurge.net in
# channels #script, #urk, or #world.
#######################

import events
import windows
import time
import irc
from conf import conf

class DebugWindow(windows.SimpleWindow):
    def __init__(self, network, id):
        windows.SimpleWindow.__init__(self, network, id)

def get_debug(network):
    for window in windows.manager:
        if type(window).__name__ == 'DebugWindow' and window.network == network:
            return window

def not_debug(id):
    for window in windows.manager:
        if window.id == id:
            return False
    return True

def debug_output(text,own):
    if own:
        return '\x0314%s[\x0303SENT\x0314] %s \x0302%s\x0314 %s' % (time.strftime(conf.get('timestamp','%H:%M:%S ')),text[0],text[1],' '.join(text[2:]))
    else:
        return '\x0314%s[\x0304RCVD\x0314] %s \x0302%s\x0314 %s' % (time.strftime(conf.get('timestamp','%H:%M:%S ')),text[0],text[1],' '.join(text[2:]))

def onRaw(e):
    debug = get_debug(e.network)
    if debug:
        msg = irc.parse_irc(e.raw, e.network.server)
        if not msg[1] == 'PING' or conf.get('pingpong',True):
            debug.write(debug_output(msg,False))

def onOwnRaw(e):
    debug = get_debug(e.network)
    if debug:
        msg = irc.parse_irc(e.raw, e.network.server)
        if not msg[1] == 'PONG' or conf.get('pingpong',True):
            debug.write(debug_output(msg,True))

def onCommandSay(e):
    if isinstance(e.window, DebugWindow):
        events.run('raw '+' '.join(e.args), e.window, e.network)

def onCommandDebug(e):
    window = get_debug(e.network)
    if e.args and e.args[0] == 'off':
        if window:
            window.close()
        else:
            e.window.write('* There is no debug window for this network.')
    elif not window:
        debug = 1
        while not not_debug('debug '+str(debug)):
            debug += 1
        windows.new(DebugWindow, e.network, 'debug '+str(debug))
    else:
        e.window.write('* There is already a debug window for this network.')

def onCommandPingpong(e):
    if e.args:
        if e.args[0] == 'on':
            conf['pingpong'] = True
            e.window.write('* Ping Pongs being displayed.')
        else:
            conf['pingpong'] = False
            e.window.write('* Ping Pongs not being displayed displayed.')

def onConnect(e):
    if conf.get('debug'):
        debug = get_debug(e.network)
        if debug:
            windows.mutate(DebugWindow, e.network, debug.id)
        else:
            events.run('debug', e.window, e.network)
