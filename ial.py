####################
# IAL v2
####################
# IAL stands for Internal Address List. It holds the
# addresses of every user on a channel with you.
## Updates #########
# IAL v2
#  - Small if statement improvements.
#  - Events that add to the IAL are now setupEvent istead
#    of onEvent(Nick not included).
#  - Events that delete from the IAL are now setdownEvent
#    instead of onEvent(Nick included).
## Usage ###########
# e.network._ial is a dictionary with the keys being the
# nicks of every user on a channel with you.
#
# e.network._ial['Nick'] gets the host of Nick in the form
# ident@host.
#
# To get full address of a nick do one of these:
#  '%s!%s' % (nick, e.network._ial[nick])
#  nick+'!'+e.network._ial[nick]
#
# /ialupdate updates the IAL for every channel you are in.
#
# /ialupdate #chan updates the IAL for #chan.
#
# /ialupdate Nick updates the IAL for Nick.
## Author ##########
# uTs was writen by poiuy_qwert. You can contact him on
# irc.gamesurge.net in channels #script, #urk, or #world.
####################
import events
import chaninfo
import windows

def can_see(network,nick):
    for window in chaninfo.channels(network):
        if chaninfo.ison(network, window, nick):
            return True
    return False

def setupJoin(e):
    if e.source == e.network.me:
        if not hasattr(e.network,'_ialwhos'):
            e.network._ialwhos = {}
        e.network._ialwhos[e.target] = True
        events.run('raw WHO '+e.target,e.window,e.network)
    else:
        e.network._ial[e.source] = e.address

def setupRaw(e):
    if e.msg[1] == '352':
        e.network._ial[e.msg[7]] = '%s@%s' % (e.msg[4],e.msg[5])
        e.quiet = True
    elif e.msg[1] == '352' and (e.network._ialwhos.get(e.msg[3]) or e.network._ialwhos.get(e.msg[7])):
        e.quiet = True
    elif e.msg[1] == '315' and e.network._ialwhos.get(e.msg[3]):
        e.quiet = True
        del e.network._ialwhos[e.msg[3]]

def setdownPart(e):
    if not can_see(e.network,e.source) and e.network._ial.get(e.source):
        del e.network._ial[e.source]

def setdownQuit(e):
    if e.network._ial.get(e.source):
        del e.network._ial[e.source]

def setdownNick(e):
    e.network._ial[e.target] = e.address
    if e.network._ial.get(e.source):
        del e.network._ial[e.source]

def onCommandIalupdate(e):
    e.network._ial = {}
    e.network._ialwhos = {}
    if e.args:
        who = e.args[0]
        if who.startswith('#'):
            if who in chaninfo.channels(e.network):
                e.window.write('* Updating IAL for channel %s.' % who)
                e.network._ialwhos[who] = True
                events.run('raw WHO '+who,e.window,e.network)
            else:
                e.window.write('* You are not on channel %s.' % who)
        elif can_see(who):
            e.window.write('* Updating IAL for %s.' % who)
            e.network._ialwhos[who] = True
            events.run('raw WHO '+who,e.window,e.network)
        else:
            e.window.write('* %s is not a valid nick/channel.' % who)
    else:
        e.window.write('* Updating IAL for every channel.')
        for window in chaninfo.channels(e.network):
            e.network._ialwhos[window] = True
            events.run('raw WHO '+window,e.window,e.network)

def setupConnect(e):
    e.network._ial = {}
    e.network._ialwhos = {}

def setdownDisconnect(e):
    if hasattr(e.network,'_ial'):
        del e.network._ial
    if hasattr(e.network,'_ialwhos'):
        del e.network._ialwhos
