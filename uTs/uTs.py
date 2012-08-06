#######################
# uTs uTs uTs uTs uTs #
# TTTTTTTTTTTTTTTTTTT #
# TTTTTTTTTTTTTTTTTTT #
# uuu  uuuTTTssssssss #
# uuu  uuuTTTssssssss #
# uuu  uuuTTTsss      #
# uuu  uuuTTTssssssss #
# uuu  uuuTTTssssssss #
# uuu  uuuTTT     sss #
# uuuuuuuuTTTssssssss #
# uuuuuuuuTTTssssssss #
# uTs uTs uTs uTs uTs #
#      Version 7      #
## uTs ################
# uTs stands for urk Theme system. It is used to create themes by
# specifying the text of the event, and in that text having some
# key words wrapped in %( and )s that are replaced by the information
# of that event. It also changes the colors of the nicklist, the tab
# colors, foreground, background, font, and font size. To make this
# work, place this file into the scripts folder where your urk.conf
# file is then it should take priority over the normal theme.py in the
# scripts folder where urk.py is located. The default theme is as close
# as i could get to the default urk theme, and some code has also been
# used from the default theme.py (the hilight code, duration, and a few
# other little things).
## Updates ############
# uTs v7
#  1) Changed the way it updates nicklist.
#  2) Escapes chars in nicks when coloring.
#  3) Themes cleared before new ones loaded.
#  4) Mode-Other now works.
#  5) Fixed %(p)s returning nick when there is no mode.
#  6) Fixed HiText for default theme.
#  7) If you are missing a HiEvent it now trys Event, then HiEvent in
#     defualt, then Event in default.
#  8) Some events now check if there is a channel correctly.
# uTs v6
#  1) Added hostmask coloring in nicklist.
#  2) Hilight is now HiText.
#  3) Some events now have HiEvent.
#  4) Added HiExtra to themes.
# uTs v5
#  1) Added nicklist color support.
# uTs v4
#  1) Strips leading whitespaces and trailing \r and \n's.
#  2) Added %(chan)s to onMode.
#  3) Added %(p)s to events with %(pnick)s to get the nick prefix only.
# uTs v3
#  1) Added %(pnick)s to some events.
#  2) Added Indent to themes.
#  3) Fixed anything broken with new urk version changes.
# uTs v2
#  1) Replacements are now %(name)s instead of <name>.
#  2) Added WhoisStart, WhoisIrcop, WhoisActually, and WhoisEnd events.
## Themes #############
# There are two ways to make your own theme:
#  1) Edit the default theme defined below
#  2) Use /theme to load a .uts file from the same directory as this
#     file.
# Note: Type '/theme file' where file is the name of the theme without
#       the .uts extention. You can also do '/theme' to use the default
#       theme. Theme files MUST have the extention .uts!
#
# If you do not load a theme or it cant find the theme it will use the
# default. Also, if there is something missing from your theme, it
# will take that from the default theme. /themeinfo will also give
# information on the currently loaded theme.
#
# To write a theme take a look at the commenting around the default
# theme for each event on some usefull information about them, then
# write a .uts file and put it in the folder with this file. The file
# format is Event Text, like this:
#  TimeStamp [%H:%M:%S]
#  Prefix *
#  Error Error: %(text)s
# And so on. I have included a theme file named poiuy_qwert.uts for
# your reference too.
# Note: Events are case sensitive so they must be exactly the same
#       as what is shown in the default theme.
#
# WARNING: Do not delete any lines out of the default theme unless
#          the comments in the defualt theme say you can.
#          NOTE: There are dynamic entries like Nick-* and Mode-?
#                which can be in your theme but dont have to. They
#                are defined in the list others just bellow the
#                default theme.
## Author #############
# uTs was writen by poiuy_qwert. You can contact him on
# irc.gamesurge.net in channels #script, #urk, or #world.
#######################

import events
import widgets
import time
from conf import conf
import os
import windows
import chaninfo
import irc

# This is the default theme.
default = {
    # Author is the authors name/nick. Version is the theme version. Contact is contact information. Description is a theme description. (Note: You can remove these. They will default to unknown, vX, None, and None.)
    'Author':'poiuy_qwert',
    'Version':'v1.2',
    'Contact':'irc.gamesurge.net - #script, #urk, #world',
    'Description':'The default urk theme as close as I could replecate it.',
    # TimeStamp is the text replacing %(timestamp)s, use http://docs.python.org/lib/module-time.html#l2h-1955 for more info. (Note: You can remove this. Defaults to nothing.)
    'TimeStamp':'[%H:%M:%S]',
    # Prefix is what replaces %(pre)s. (Note: You can remove this. Defaults to nothing.)
    'Prefix':'*',
    # HiExtra can be True or False if you want to highlight the tab on events other than just HiText. (Defaults to False.)
    'HiExtra':False,
    # Text is when someone sends a message, OwnText is when you send a message. (Replaces: %(timestamp)s, %(pre)s, %(nick)s, %(pnick)s, %(p), %(p), %(text)s.)
    'Text':'%(timestamp)s \x02\x040000CC<\x0F%(nick)s\x02\x040000CC>\x0F %(text)s',
    'OwnText':'%(timestamp)s \x02\x04FF00FF<\x0F%(nick)s\x02\x04FF00FF>\x0F %(text)s',
    # HiText is when someone sends a message with your nick or something from the highlight_words conf entry in it. (Replaces: %(timestamp)s, %(pre)s, %(nick)s, %(pnick)s, %(p), %(text)s). (Note: You can remove this. Defaults to theme Text, then default Hilight, then default Text.)
    'HiText':'%(timestamp)s \x02\x040000CC<\x04FFFF00%(nick)s\x02\x040000CC>\x0F %(text)s',
    # Action is when someone sends an action, OwnAction is when you do. (Replaces: %(timestamp)s, %(pre)s, %(nick)s, %(pnick)s, %(p), %(text)s)
    'Action':'%(timestamp)s \x02\x040000CC%(pre)s \x0F%(nick)s %(text)s',
    'OwnAction':'%(timestamp)s \x02\x04FF00FF%(pre)s \x0F%(nick)s %(text)s',
    # HiAction is when someone sends an action with your nick or something from the highlight_words conf entry in it. (Replaces: %(timestamp)s, %(pre)s, %(nick)s, %(pnick)s, %(p), %(text)s). (Note: You can remove this. Defaults to theme Text, then default Hilight, then default Text.)
    'HiAction':'%(timestamp)s \x02\x040000CC%(pre)s \x0F\x04FFFF00%(nick)s\x0F %(text)s',
    # Notice is when someone notices you, OwnNotice is when you notice someone. (Replaces: %(timestamp)s, %(pre)s, %(nick)s, %(text)s). (Note: If you notice a channel %(nick)s will be the channel.)
    'Notice':'%(timestamp)s \x02\x040000CC-\x0F%(nick)s\x02\x040000CC-\x0F %(text)s',
    'OwnNotice':'%(timestamp)s \x02\x04FF00FF-> -\x0F%(nick)s\x02\x04FF00FF-\x0F %(text)s',
    # HiNotice is when someone sends a notice with your nick or something from the highlight_words conf entry in it. (Replaces: %(timestamp)s, %(pre)s, %(nick)s, %(pnick)s, %(p), %(text)s). (Note: You can remove this. Defaults to theme Text, then default Hilight, then default Text.)
    'HiNotice':'%(timestamp)s \x02\x040000CC-\x04FFFF00%(nick)s\x02\x040000CC-\x0F %(text)s',
    # ChanNotice is when someone notices a channel. (Replaces: %(timestamp)s, %(pre)s, %(nick)s, %(pnick)s, %(p), %(text)s, %(chan)s). (Note: You can remove this. Defaults to Notice.)
    'ChanNotice':'%(timestamp)s \x02\x040000CC-\x0F%(chan)s:%(nick)s\x02\x040000CC-\x0F %(text)s',
    # HiChanNotice is when someone sends a channel notice with your nick or something from the highlight_words conf entry in it. (Replaces: %(timestamp)s, %(pre)s, %(nick)s, %(pnick)s, %(p), %(text)s). (Note: You can remove this. Defaults to theme Text, then default Hilight, then default Text.)
    'HiChanNotice':'%(timestamp)s \x02\x040000CC-\x04FFFF00%(chan)s:%(nick)s\x02\x040000CC-\x0F %(text)s',
    # Ctcp is when someone ctcp's you. (Replaces: %(timestamp)s, %(pre)s, %(nick)s, %(text)s)
    'Ctcp':'%(timestamp)s \x02\x040000CC[\x0F%(nick)s\x02\x040000CC]\x0F %(text)s',
    # HiCtcp is when someone sends a ctcp with your nick or something from the highlight_words conf entry in it. (Replaces: %(timestamp)s, %(pre)s, %(nick)s, %(pnick)s, %(p), %(text)s). (Note: You can remove this. Defaults to theme Text, then default Hilight, then default Text.)
    'HiCtcp':'%(timestamp)s \x02\x040000CC[\x04FFFF00%(nick)s\x02\x040000CC]\x0F %(text)s',
    # ChanCtcp is when someone Ctcp's a channel. (Replaces: %(timestamp)s, %(pre)s, %(nick)s, %(pnick)s, %(p), %(text)s, %(chan)s). (Note: You can remove this. Defaults to Ctcp.)
    'ChanCtcp':'%(timestamp)s \x02\x040000CC[\x0F%(chan)s:%(nick)s\x02\x040000CC]\x0F %(text)s',
    # HiChanCtcp is when someone sends a channel ctcp with your nick or something from the highlight_words conf entry in it. (Replaces: %(timestamp)s, %(pre)s, %(nick)s, %(pnick)s, %(p), %(text)s). (Note: You can remove this. Defaults to theme Text, then default Hilight, then default Text.)
    'HiChanCtcp':'%(timestamp)s \x02\x040000CC[\x04FFFF00%(chan)s:%(nick)s\x02\x040000CC]\x0F %(text)s',
    # CtcpReply is when someone replies to a ctcp. (Replaces: %(timestamp)s, %(pre)s, %(nick)s, %(text)s, %(ctcp)s)
    'CtcpReply':'%(timestamp)s--- %(ctcp)s reply from %(nick)s: %(text)s',
    # HiCtcpReply is when a ctcp repy has your nick or something from the highlight_words conf entry in it. (Replaces: %(timestamp)s, %(pre)s, %(nick)s, %(pnick)s, %(p), %(text)s). (Note: You can remove this. Defaults to theme Text, then default Hilight, then default Text.)
    'HiCtcpReply':'%(timestamp)s\x04FFFF00--- %(ctcp)s reply from %(nick)s: %(text)s',
    # Join is when someone joins a channel. (Replaces: %(timestamp)s, %(pre)s, %(nick)s, %(address)s, %(chan)s)
    'Join':'%(timestamp)s \x02%(nick)s\x02 \x04777777(\x0400CCCC%(address)s\x04777777)\x0F joined %(chan)s',
    # Part is when someone parts a channel. (Replaces: %(timestamp)s, %(pre)s, %(nick)s, %(pnick)s, %(p), %(address)s, %(chan)s)
    'Part':'%(timestamp)s \x02%(nick)s\x02 left %(chan)s \x04777777(\x0400CCCC%(text)s\x04777777)\x0F',
    # Kick is when someone is kicked from a channel. (Replaces: %(timestamp)s, %(pre)s, %(nick)s,  %(pnick)s, %(address)s, %(knick)s, %(pknick)s, %(pk)s, %(chan)s, %(text)s)
    'Kick':'%(timestamp)s \x02%(knick)s\x02 kicked %(nick)s \x04777777(\x0400CCCC%(text)s\x04777777)\x0F',
    # Mode is when either you set a mode on yourself or someone sets a channel mode. (Replaces: %(timestamp)s, %(pre)s, %(nick)s, %(pnick)s, %(p), %(address)s, %(text)s)
    'Mode':'%(timestamp)s \x02%(nick)s\x02 set mode: %(text)s',
    # Quit is when someone quits IRC. (Replaces: %(timestamp)s, %(pre)s, %(nick)s, %(address)s, %(chan)s, %(text)s)
    'Quit':'%(timestamp)s \x02%(nick)s\x02 quit \x04777777(\x0400CCCC%(text)s\x04777777)\x0F',
    # Nick is when someone changes their nick. (Replaces: %(timestamp)s, %(pre)s, %(nick)s, %(address)s, %(newnick)s)
    'Nick':'%(timestamp)s%(nick)s is now known as \x02%(newnick)s\x02',
    # Disconnect is when you disconnect from a server. (Replaces: %(timestamp)s, %(pre)s, %(text)s)
    'Disconnect':'%(timestamp)s%(pre)sDisconnected (%(text)s)',
    # TopicSet is when someone sets the topic of a channel. (Replaces: %(timestamp)s, %(pre)s, %(nick)s, %(address)s, %(chan)s, %(text)s)
    'TopicSet':'%(timestamp)s \x02%(nick)s\x02 set topic on %(chan)s: %(text)s',
    # Topic is when you see the channel topic on join. (Replaces: %(timestamp)s, %(pre)s, %(chan)s, %(text)s)
    'Topic':'%(timestamp)sTopic on %(chan)s is: %(text)s',
    # TopicSetBy is the message telling you who set the topic and when. (Replaces: %(timestamp)s, %(pre)s, %(nick)s, %(pnick)s, %(p), %(chan)s, %(text)s)
    'TopicSetBy':'%(timestamp)sTopic %(chan)s set by %(nick)s at time %(text)s',
    # CreationTime is the message telling you when the channel was created. (Replaces: %(timestamp)s, %(pre)s, %(chan)s, %(text)s)
    'CreationTime':'%(timestamp)sChannel created on %(text)s',
    # WhoisStart is triggered when you whois. (Replaces: %(timestamp)s, %(pre)s, %(nick)s)
    'WhoisStart':'%(timestamp)s  /WHOIS %(nick)s:',
    # WhoisUser is the userline of a whois. (Replaces: %(timestamp)s, %(pre)s, %(nick)s, %(address)s, %(text)s)
    'WhoisUser':'%(timestamp)s%(nick)s is %(address)s * %(text)s',
    # WhoisServer is the server line of a whois event. (Replaces: %(timestamp)s, %(pre)s, %(nick)s, %(network)s, %(text)s)
    'WhoisServer':'%(timestamp)s%(nick)s on %(network)s (%(text)s)',
    # WhoisIdle is the idle line of a whois event. (Replaces: %(timestamp)s, %(pre)s, %(nick)s, %(text)s)
    'WhoisIdle':'%(timestamp)s%(nick)s has been idle for %(text)s',
    # WhoisIrcop is the ircop line of a whois event. (Replaces: %(timestamp)s, %(pre)s, %(nick)s)
    'WhoisIrcop':'%(timestamp)s%(nick)s is an IRC Operator',
    # WhoisActually is the actual host of a user containing their IP. (Replaces: %(timestamp)s, %(pre)s, %(nick)s, %(address)s)
    'WhoisActually':'%(timestamp)s%(nick)s is actually %(address)s',
    # WhoisSignon is the signon line of a whois event. (Replaces: %(timestamp)s, %(pre)s, %(nick)s, %(text)s)
    'WhoisSignon':'%(timestamp)s%(nick)s signed on %(text)s',
    # WhoisChannels is the channels line of a whois event. (Replaces: %(timestamp)s, %(pre)s, %(nick)s, %(text)s)
    'WhoisChannels':'%(timestamp)s%(nick)s on channels: %(text)s',
    # WhoisAccount is the account line of a whois event. (Replaces: %(timestamp)s, %(pre)s, %(nick)s, %(text)s)
    'WhoisAccount':'%(timestamp)s%(nick)s is logged in as %(text)s',
    # WhoisEnd is triggered at the end of a whois. (Replaces: %(timestamp)s, %(pre)s, %(nick)s)
    'WhoisEnd':'%(timestamp)s  End of /WHOIS list.',
    # Error is what is returned when you use an invallid /command. (Replaces: %(timestamp)s, %(pre)s, %(text)s)
    'Error':'Error: %(text)s',
    # Background is the background color of windows and the nicklist. (Note: You can remove this. Defaults to #2E3D49. Only changes on urk startup.)
    'Background':'#2E3D49',
    # Foreground is the foreground color of windows and the nicklist. (Note: You can remove this. Defaults to #DEDEDE. Only changes on urk startup.)
    'Foreground':'#DEDEDE',
    # Font is the font of windows and the nicklist. (Note: You can remove this. Defaults to the conf font entry then sans 8. The form of the line is Font Size. Only changes on urk startup.)
    'Font':'sans 8',
    # TabHilight, TabText, and TabEvent are the tab colors. (Note: You can remove these. Defaults to #00F, #F00, and #363.)
    'TabHilight':'#00F',
    'TabText':'#F00',
    'TabEvent':'#363',
    # Indent is the indent of text wrapped in a window measured in pixels. (Note: You can remove this. Defaults to 20. Must be a nonnegative integer(0,1,2,3..N). Resize window or nicklist to update indents.)
    'Indent':'20',
    # Mode-? is the color of mode ? on the nicklist. ? should be the letter you use to set the mode, I.E. /mode #chan +o nick, you would use Mode-o(Case Sensitive!).
    'Mode-o':'red',
    'Mode-v':'#00007F',
    # This is the color of people with no modes set. (Defaults to Foreground then #FFF).
    'Mode-':'#DEDEDE',
    # This is a list of colors sepereated by spaces for the modes you do not have set. The first unkown mode gets the first color, the second unkown gets the second, so on, then loop back to the begining of the list.
    'Mode-Other':'#009300 #9C009C',
    # This is color for your own nick in the nicklist.
    'MyNick':'#FF7F00',
    # Masks is a list of host masks to color on the nicklist. (You must have IAL.py for this to work! When you connect to a network and autojoin the IAL hasn't filled yet so Masks won't work. Use /colornicks command to update the nicklist colors anytime.)
    'Masks':'*@*Services*',
    # Mask-Colors is a list of colors to color the matching host masks. The first mask gets the first color, the second mask gets the second, so on, then loop back to the begining of the list.
    'Mask-Colors':'red',
    # Nick-* is the color of nick * on the nicklist. * should be the nick of the user who you want to color.
    'Nick-poiuy_qwert':'#FF0'
    # The order the nicklist is colored is: MyNick, Masks, Nick-*, Mode-?, Mode-Other, Mode-
}

theme = {}

other_colored = {}

# This is where the dynamic entries like Mode-? and Nick-* go to make sure they are loaded even if they arn't in the defualt theme.
others = [
    'Mode-',
    'Nick-'
]

def pnick(network,channel,nick,p=False):
    if p:
        channel = chaninfo.getchan(network,channel)
        if channel:
            return chaninfo._justprefix(network,channel,nick)
        else:
            return ''
    elif channel:
        return chaninfo.prefix(network,channel,nick)
    else:
        return nick

def duration(secs):
    times = (
        ("years", "year", 31556952),
        ("weeks", "week", 604800),
        ("days", "day", 86400),
        ("hours", "hour", 3600),
        ("minutes", "minute", 60),
        ("seconds", "second", 1),
    )
    if secs == 0:
        return "0 seconds"
    result = ""
    for plural, singular, amount in times:
        n, secs = divmod(secs, amount)
        if n == 1:
            result = result + " %s %s" % (n, singular)
        elif n:
            result = result + " %s %s" % (n, plural)
    return result[1:]

def is_other(entry):
    for begin in others:
        if entry.startswith(begin):
            return True
    return False

def mask_match(network,nick):
    if hasattr(network,'_ial') and network._ial.get(nick):
        masks = theme.get('Masks',default.get('Masks'))
        if masks:
            masks = masks.split(' ')
            num = 1
            for mask in masks:
                if irc.match_glob(nick+'!'+network._ial[nick],mask):
                    return num
                num += 1
    return False

def color_nick(network,channel,colornick):
    if type(channel).__name__ == 'ChannelWindow':
        parse = network.isupport["PREFIX"][1:].split(')')
        modes = {}
        for l, c in zip(parse[0],parse[1]):
            modes[c] = l
        escape = {'&':'&amp;','<':'&lt;','>':'&gt;'}
        for num, nick in enumerate(channel.nicklist):
            if nick == colornick:
                mode = chaninfo._justprefix(network, chaninfo.getchan(network,channel.id), nick)
                esc_mode = escape.get(mode,mode)
                sortkey = chaninfo.sortkey(network, channel.id, nick)
                col = theme.get('MyNick',default.get('MyNick',''))
                if nick == network.me and col:
                    channel.nicklist[num] = nick, '<span color="%s">%s%s</span>' % (col, esc_mode, nick), sortkey
                elif hasattr(network,'_ial') and mask_match(network,nick):
                    col = theme.get('Mask-Colors',default.get('Mask-Colors'))
                    if col:
                        col = col.split(' ')
                        channel.nicklist[num] = nick, '<span color="%s">%s%s</span>' % (col[mask_match(network,nick) - 1], esc_mode, nick), sortkey
                else:
                    col = theme.get('Nick-'+nick,default.get('Nick-'+nick))
                    if col:
                        channel.nicklist[num] = nick, '<span color="%s">%s%s</span>' % (col, esc_mode, nick), sortkey
                    else:
                        col = theme.get('Mode-'+modes.get(mode,''),default.get('Mode-'+modes.get(mode,''),''))
                        if col:
                            channel.nicklist[num] = nick, '<span color="%s">%s%s</span>' % (col, esc_mode, nick), sortkey
                        else:
                            col = theme.get('Mode-Other',default.get('Mode-Other'))
                            if col:
                                if not mode in other_colored:
                                    col = col.split(' ')
                                    other_colored[mode] = col[len(other_colored) % len(col)]
                                channel.nicklist[num] = nick, '<span color="%s">%s%s</span>' % (other_colored[mode], esc_mode, nick), sortkey
                            else:
                                channel.nicklist[num] = nick, '<span color="%s">%s%s</span>' % (theme['Mode-'], esc_mode, nick), sortkey
                return

def color_nicklist(network,channel):
    if type(channel).__name__ == 'ChannelWindow':
        for nick in channel.nicklist:
            color_nick(network,channel,nick)

def color_nicklists(network):
    for window in windows.get_with(network=network):
        if type(window).__name__ == 'ChannelWindow':
            color_nicklist(network,window)

def output(event,hilight,window,replace,activity=None):
    backup = event
    if hilight:
        event = 'Hi'+event
        if event == 'HiText' or theme.get('HiExtra',default.get('HiExtra')):
            activity = widgets.HILIT
    output = theme.get(event,theme.get(backup,default.get(event,default.get(backup)))) % replace
    window.write(output,activity)

def check_hilight(e,text):
    if not hasattr(e,'hilight'):
        e.hilight = []
        e.hitext = text
        events.trigger('Hilight',e)

def onHilight(e):
    for word in conf.get('highlight_words', []) + [e.network.me]:
        pos = e.hitext.find(word,0)
        while pos != -1:
            e.hilight.append((pos, pos+len(word)))
            pos = e.hitext.find(word, pos+1)

def onText(e):
    check_hilight(e,e.text)
    reps = {
        'nick':e.source,
        'pnick':pnick(e.network,e.target,e.source),
        'p':pnick(e.network,e.target,e.source,True),
        'text':e.text,
        'timestamp':time.strftime(theme.get('TimeStamp',default.get('TimeStamp'))),
        'pre':theme.get('Prefix',default.get('Prefix'))
    }
    output('Text',e.hilight,e.window,reps,widgets.TEXT)

def onOwnText(e):
    reps = {
        'nick':e.network.me,
        'pnick':pnick(e.network,e.target,e.network.me),
        'p':pnick(e.network,e.target,e.network.me,True),
        'text':e.text,
        'timestamp':time.strftime(theme.get('TimeStamp',default.get('TimeStamp'))),
        'pre':theme.get('Prefix',default.get('Prefix'))
    }
    output('OwnText',None,e.window,reps)

def onAction(e):
    check_hilight(e,e.text)
    reps = {
        'nick':e.source,
        'pnick':pnick(e.network,e.target,e.source),
        'p':pnick(e.network,e.target,e.source,True),
        'text':e.text,
        'timestamp':time.strftime(theme.get('TimeStamp',default.get('TimeStamp'))),
        'pre':theme.get('Prefix',default.get('Prefix'))
    }
    output('Action',e.hilight,e.window,reps,widgets.TEXT)

def onOwnAction(e):
    reps = {
        'nick':e.network.me,
        'pnick':pnick(e.network,e.target,e.network.me),
        'p':pnick(e.network,e.target,e.network.me,True),
        'text':e.text,
        'timestamp':time.strftime(theme.get('TimeStamp',default.get('TimeStamp'))),
        'pre':theme.get('Prefix',default.get('Prefix'))
    }
    output('OwnAction',None,e.window,reps)

def onNotice(e):
    check_hilight(e,e.text)
    reps = {
        'nick':e.source,
        'text':e.text,
        'timestamp':time.strftime(theme.get('TimeStamp',default.get('TimeStamp'))),
        'pre':theme.get('Prefix',default.get('Prefix'))
    }
    if chaninfo.ischan(e.network,e.target):
        reps['chan'] = e.target
        reps['pnick'] = pnick(e.network,e.target,e.source)
        window = windows.get(windows.ChannelWindow, e.network, e.msg[3]) or e.window
        output('ChanNotice',e.hilight,window,reps,widgets.TEXT)
    else:
        output('Notice',e.hilight,e.window,reps,widgets.TEXT)

def onOwnNotice(e):
    reps = {
        'nick':e.target,
        'text':e.text,
        'timestamp':time.strftime(theme.get('TimeStamp',default.get('TimeStamp'))),
        'pre':theme.get('Prefix',default.get('Prefix'))
    }
    output('OwnNotice',None,e.window,reps)

def onCtcp(e):
    if not e.quiet and not e.done:
        check_hilight(e,e.text)
        reps = {
            'nick':e.source,
            'text':e.text,
            'timestamp':time.strftime(theme.get('TimeStamp',default.get('TimeStamp'))),
            'pre':theme.get('Prefix',default.get('Prefix'))
        }
        if chaninfo.ischan(e.network,e.target):
            reps['chan'] = e.target
            reps['pnick'] = pnick(e.network,e.target,e.source)
            reps['p'] = pnick(e.network,e.target,e.source,True)
            window = windows.get(windows.ChannelWindow, e.network, e.msg[3]) or e.window
            output('ChanCtcp',e.hilight,window,reps,widgets.TEXT)
        else:
            output('Ctcp',e.hilight,e.window,reps,widgets.TEXT)

def onCtcpReply(e):
    check_hilight(e,e.text)
    reps = {
        'nick':e.source,
        'ctcp':e.name.capitalize(),
        'text':' '.join(e.args),
        'timestamp':time.strftime(theme.get('TimeStamp',default.get('TimeStamp'))),
        'pre':theme.get('Prefix',default.get('Prefix'))
    }
    output('',e.hilight,e.window,reps,widgets.TEXT)

def onJoin(e):
    reps = {
        'nick':e.source,
        'address':e.address,
        'chan':e.target,
        'timestamp':time.strftime(theme.get('TimeStamp',default.get('TimeStamp'))),
        'pre':theme.get('Prefix',default.get('Prefix'))
    }
    output('Join',None,e.window,reps)
    if not e.source == e.network.me:
        color_nick(e.network,e.window,e.source)

def onPart(e):
    reps = {
        'nick':e.source,
        'pnick':pnick(e.network,e.target,e.source),
        'p':pnick(e.network,e.target,e.source,True),
        'address':e.address,
        'chan':e.target,
        'text':e.text,
        'timestamp':time.strftime(theme.get('TimeStamp',default.get('TimeStamp'))),
        'pre':theme.get('Prefix',default.get('Prefix'))
    }
    output('Part',None,e.window,reps,widgets.EVENT)

def onKick(e):
    reps = {
        'nick':e.source,
        'pnick':pnick(e.network,e.channel,e.source),
        'p':pnick(e.network,e.target,e.source,True),
        'knick':e.target,
        'pknick':pnick(e.network,e.channel,e.target),
        'pk':pnick(e.network,e.target,e.target,True),
        'address':e.address,
        'text':e.text,
        'chan':e.channel,
        'timestamp':time.strftime(theme.get('TimeStamp',default.get('TimeStamp'))),
        'pre':theme.get('Prefix',default.get('Prefix'))
    }
    output('Kick',None,e.window,reps,widgets.EVENT)

def onMode(e):
    reps = {
        'nick':e.source,
        'pnick':pnick(e.network,e.target,e.source),
        'p':pnick(e.network,e.target,e.source,True),
        'address':e.address,
        'text':e.text,
        'timestamp':time.strftime(theme.get('TimeStamp',default.get('TimeStamp'))),
        'pre':theme.get('Prefix',default.get('Prefix'))
    }
    if chaninfo.ischan(e.network,e.target):
        reps['chan'] = e.target
        color_nicklist(e.network,e.window)
    output('Mode',None,e.window,reps,widgets.EVENT)

def onQuit(e):
    reps = {
        'nick':e.source,
        'address':e.address,
        'text':e.text,
        'timestamp':time.strftime(theme.get('TimeStamp',default.get('TimeStamp'))),
        'pre':theme.get('Prefix',default.get('Prefix'))
    }
    for window in windows.get_with(network=e.network):
        if chaninfo.ison(e.network, window.id, e.source):
            output('Quit',None,window,reps,widgets.EVENT)

def onNick(e):
    reps = {
        'nick':e.source,
        'newnick':e.target,
        'address':e.address,
        'timestamp':time.strftime(theme.get('TimeStamp',default.get('TimeStamp'))),
        'pre':theme.get('Prefix',default.get('Prefix'))
    }
    for window in windows.get_with(network=e.network):
        if chaninfo.ison(e.network, window.id, e.source):
            color_nick(e.network, window, e.source)
            output('Nick',None,window,reps,widgets.EVENT)

def onDisconnect(e):
    reps = {
        'timestamp':time.strftime(theme.get('TimeStamp',default.get('TimeStamp'))),
        'pre':theme.get('Prefix',default.get('Prefix'))
    }
    if hasattr(e,'error'):
        reps['text'] = e.error
    for window in windows.get_with(network=e.network):
        if isinstance(window, windows.StatusWindow):
            output('Disconnect',None,window,reps,widgets.TEXT)
        else:
            output('Disconnect',None,window,reps,widgets.EVENT)

def onTopic(e):
    reps = {
        'nick':e.source,
        'pnick':pnick(e.network,e.target,e.source),
        'p':pnick(e.network,e.target,e.source,True),
        'address':e.address,
        'chan':e.target,
        'text':e.text,
        'timestamp':time.strftime(theme.get('TimeStamp',default.get('TimeStamp'))),
        'pre':theme.get('Prefix',default.get('Prefix'))
    }
    output('TopicSet',None,e.window,reps,widgets.EVENT)

def onRaw(e):
    if not e.quiet:
        if e.msg[1].isdigit():
            if e.msg[1] == '311':
                reps = {
                    'nick':e.msg[3],
                    'timestamp':time.strftime(theme.get('TimeStamp',default.get('TimeStamp'))),
                    'pre':theme.get('Prefix',default.get('Prefix'))
                }
                output('WhoisStart',None,e.window,reps,widgets.EVENT)
                reps = {
                    'nick':e.msg[3],
                    'address':e.msg[4]+'@'+e.msg[5],
                    'text':e.msg[7],
                    'timestamp':time.strftime(theme.get('TimeStamp',default.get('TimeStamp'))),
                    'pre':theme.get('Prefix',default.get('Prefix'))
                }
                output('WhoisUser',None,e.window,reps,widgets.EVENT)

            elif e.msg[1] == '312':
                reps = {
                    'nick':e.msg[3],
                    'network':e.msg[4],
                    'text':e.msg[5],
                    'timestamp':time.strftime(theme.get('TimeStamp',default.get('TimeStamp'))),
                    'pre':theme.get('Prefix',default.get('Prefix'))
                }
                output('WhoisServer',None,e.window,reps,widgets.EVENT)

            elif e.msg[1] == '313':
                reps = {
                    'nick':e.msg[3],
                    'timestamp':time.strftime(theme.get('TimeStamp',default.get('TimeStamp'))),
                    'pre':theme.get('Prefix',default.get('Prefix'))
                }
                output('WhoisIrcop',None,e.window,reps,widgets.EVENT)

            elif e.msg[1] == '317':
                reps = {
                    'nick':e.msg[3],
                    'text':duration(int(e.msg[4])),
                    'timestamp':time.strftime(theme.get('TimeStamp',default.get('TimeStamp'))),
                    'pre':theme.get('Prefix',default.get('Prefix'))
                }
                output('WhoisIdle',None,e.window,reps,widgets.EVENT)
                if e.msg[5].isdigit():
                    reps['text'] = duration(int(e.msg[5]))
                    output('WhoisSignon',None,e.window,reps)

            elif e.msg[1] == '318':
                reps = {
                    'nick':e.msg[3],
                    'timestamp':time.strftime(theme.get('TimeStamp',default.get('TimeStamp'))),
                    'pre':theme.get('Prefix',default.get('Prefix'))
                }
                output('WhoisEnd',None,e.window,reps,widgets.EVENT)

            elif e.msg[1] == '319':
                reps = {
                    'nick':e.msg[3],
                    'text':e.msg[4],
                    'timestamp':time.strftime(theme.get('TimeStamp',default.get('TimeStamp'))),
                    'pre':theme.get('Prefix',default.get('Prefix'))
                }
                output('WhoisChannels',None,e.window,reps,widgets.EVENT)

            elif e.msg[1] == '329':
                reps = {
                    'chan':e.msg[3],
                    'text':time.ctime(int(e.msg[4])),
                    'timestamp':time.strftime(theme.get('TimeStamp',default.get('TimeStamp'))),
                    'pre':theme.get('Prefix',default.get('Prefix'))
                }
                window = windows.get(windows.ChannelWindow, e.network, e.msg[3]) or e.window
                output('CreationTime',None,window,reps,widgets.EVENT)

            elif e.msg[1] == '330':
                if len(e.msg) == 6 and not e.msg[4].isdigit() and not e.msg[5].isdigit():
                    reps = {
                        'nick':e.msg[3],
                        'text':e.msg[4],
                        'timestamp':time.strftime(theme.get('TimeStamp',default.get('TimeStamp'))),
                        'pre':theme.get('Prefix',default.get('Prefix'))
                    }
                    output('WhoisAccount',None,e.window,reps,widgets.EVENT)
                else:
                    e.window.write(theme.get('Prefix',default.get('Prefix'))+" %s" % ' '.join(e.msg[3:]))

            elif e.msg[1] == '332':
                reps = {
                    'chan':e.msg[3],
                    'text':e.text,
                    'timestamp':time.strftime(theme.get('TimeStamp',default.get('TimeStamp'))),
                    'pre':theme.get('Prefix',default.get('Prefix'))
                }
                window = windows.get(windows.ChannelWindow, e.network, e.msg[3]) or e.window
                output('Topic',None,e.window,reps,widgets.EVENT)

            elif e.msg[1] == '333':
                reps = {
                    'nick':e.msg[4],
                    'chan':e.msg[3],
                    'text':time.ctime(int(e.msg[5])),
                    'timestamp':time.strftime(theme.get('TimeStamp',default.get('TimeStamp'))),
                    'pre':theme.get('Prefix',default.get('Prefix'))
                }
                window = windows.get(windows.ChannelWindow, e.network, e.msg[3]) or e.window
                output('TopicSetBy',None,e.window,reps,widgets.EVENT)

            elif e.msg[1] == '338':
                reps = {
                    'nick':e.msg[3],
                    'address':e.msg[4],
                    'timestamp':time.strftime(theme.get('TimeStamp',default.get('TimeStamp'))),
                    'pre':theme.get('Prefix',default.get('Prefix'))
                }
                output('WhoisActually',None,e.window,reps,widgets.EVENT)

            else:
                e.window.write(theme.get('Prefix',default.get('Prefix'))+" %s" % ' '.join(e.msg[3:]))
    elif e.msg[1] == '366':
        color_nicklist(e.network,e.window)
    elif e.msg[1] == 'ERROR':
        reps = {
            'text':e.msg[4],
            'timestamp':time.strftime(theme.get('TimeStamp',default.get('TimeStamp'))),
            'pre':theme.get('Prefix',default.get('Prefix'))
        }
        output('Error',None,e.window,reps,widgets.EVENT)

def load_theme(e):
    reps = (time.strftime(theme.get('TimeStamp',default.get('TimeStamp'))),theme.get('Prefix',default.get('Prefix')))
    if e and e.args:
        themename = ' '.join(e.args)
        themefile = os.path.join(os.path.split(__file__)[0],themename+'.uts')
        conf['theme'] = themename
    elif conf.get('theme'):
        themename = conf['theme']
        themefile = os.path.join(os.path.split(__file__)[0],themename+'.uts')
    else:
        themename = None
        themefile = None
    try:
        global theme, other_colored
        theme = {}
        other_colored = {}
        read = file(themefile, 'r').readlines()
        for line in read:
            cline = line.lstrip().rstrip('\r\n').split(' ',1)
            if cline[0] and (default.get(cline[0]) or is_other(cline[0])):
                theme[cline[0]] = cline[1].decode("string_escape")
        output = ('%s %s Theme "'+themename+'" loaded.') % (time.strftime(theme.get('TimeStamp',default.get('TimeStamp'))),theme.get('Prefix',default.get('Prefix')))
        try:
            e.window.write(output)
        except:
            print output
    except:
        if themename:
            output = ('%s %s Theme "'+themename+'" could not be found, theme not changed.') % reps
        else:
            output = '%s %s No theme, using default.' % reps
        try:
            e.window.write(output)
        except:
            print output
    widgets.ACTIVITY_MARKUP = {
        widgets.HILIT: "<span foreground='"+theme.get('TabHilight',default.get('TabHilight','#00F'))+"'>%s</span>",
        widgets.TEXT: "<span foreground='"+theme.get('TabText',default.get('TabText','#F00'))+"'>%s</span>",
        widgets.EVENT: "<span foreground='"+theme.get('TabEvent',default.get('TabEvent','#363'))+"'>%s</span>",
    }
    if theme.get('Indent','').isdigit():
        indent = -1 * int(theme['Indent'])
    elif default.get('Indent','').isdigit():
        indent = -1 * int(default['Indent'])
    else:
        indent = -20
    widgets.indent_tag.set_property('indent', indent)
    if not theme.get('Mode-',''):
        theme['Mode-'] = theme.get('Foreground',default.get('Foreground','#DEDEDE'))

def onCommandTheme(e):
    load_theme(e)

def onCommandThemeinfo(e):
    e.window.write('%s %s by %s(Contact information: %s). Description: %s' % (conf.get('theme','Default'), theme.get('Version',default.get('Version','vX')), theme.get('Author',default.get('Author','unknown')), theme.get('Contact',default.get('Contact','None')), theme.get('Description',default.get('Description','None'))))
    info = 'Events Themed: '
    if conf.get('theme'):
        for event in theme:
            info += event+', '
    else:
        for event in default:
            info += event+', '
    e.window.write('%s (Themed/Total: %s/%s)' % (info[:len(info)-2], repr(len(theme)), repr(len(default))))

def onCommandColornicks(e):
    color_nicklists(e.network)

load_theme(None)
textareas = {
    'bg':theme.get('Background',default.get('Background','#2E3D49')),
    'fg':theme.get('Foreground',default.get('Foreground','#DEDEDE')),
    'font':theme.get('Font',default.get('Font',conf.get('font','sans 8'))),
}
widgets.set_style("view", textareas)
widgets.set_style("nicklist", textareas)

