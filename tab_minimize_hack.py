import ui
import windows

def onActive(e):
    if not hasattr(e.window, '_switch_back_f'):
        windows.manager.tabs.get_tab_label(e.window).connect(
            'button-press-event',
            lambda *a: e.window._switch_back_f(e.window)
            )

    last_window = getattr(windows.manager, 'last_window', None)

    def switch_back_f(window):
        if window == windows.manager.get_active() and last_window:
            ui.register_idle(last_window.activate)
    e.window._switch_back_f = switch_back_f

    windows.manager.last_window = e.window

