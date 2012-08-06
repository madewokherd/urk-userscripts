import thread
import ui

BUG_URLS = {
  'Mozilla': 'https://bugzilla.mozilla.org/show_bug.cgi?id=%s',
  'GIMPNet': 'http://bugzilla.gnome.org/show_bug.cgi?id=%s',
  }

def checkForBug(text, pos, target_to):
    l = text.lower().rfind('b', 0, target_to)

    if text[l:].lower().startswith('bug'):
        r = l + 3
        try:
            if text[r] == ' ':
                r += 1
                while text[r].isdigit():
                    r += 1

        except IndexError:
            pass

        if r > pos and r-l > 4:
            return l, r

    return None, None

def onHover(e):
    l, r = checkForBug(e.text, e.pos, e.target_to)

    if l is not None:
        e.tolink.add((l, r))

def onClick(e):
    l, r = checkForBug(e.text, e.pos, e.target_to)

    if l is not None:
        number = int(e.text[l:r].split(' ')[1])

        try:
            url = BUG_URLS[e.window.network.isupport['NETWORK']] % number
        except KeyError:
            url = BUG_URLS['Mozilla'] % number

        ui.open_file(url)

def onCommandBug(e):
    network = e.window.network.isupport['NETWORK']

    import urllib2

    try:
        print e.args[0]
        number = int(e.args[0])
    except IndexError:
        e.window.write("Usage: /bug #")
    except ValueError:
        e.window.write("Usage: /bug #")

    try:
        url = BUG_URLS[network] % number
    except KeyError:
        url = BUG_URLS['Mozilla'] % number

    def get_title(url):
        for line in urllib2.urlopen(url):
            if '<title>' in line:
                return line.split('>')[1].split('<')[0]

    ui.fork(e.window.write, get_title, url)
