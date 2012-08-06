import windows
def highlight(e):
    windows.manager.set_title("*** ACTIVITY ON %s! ***" % e.window.id)

def onText(e):
    if e.target == e.network.me and not windows.manager.is_active():
        highlight(e)

def setdownHighlight(e):
    if e.Highlight and not windows.manager.is_active():
        highlight(e)

def onActive(e):
    windows.manager.set_title()
    
onSuperActive = onActive

