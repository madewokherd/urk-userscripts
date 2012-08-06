import ui

def onHover(e):
    fr = e.text.rfind('[[',0,e.pos)
    if fr != -1:
        to = e.text.find(']]',e.pos)
        if to != -1:
            target = e.text[fr+2:to]
            if '[[' not in target and ']]' not in target:
                e.tolink.add((fr+2,to))
    
    fr = e.text.rfind('{{',0,e.pos)
    if fr != -1:
        to = e.text.find('}}',e.pos)
        if to != -1:
            target = e.text[fr+2:to]
            if '{{' not in target and '}}' not in target:
                e.tolink.add((fr+2,to))

interwiki = {
    'm':'http://meta.wikipedia.org/wiki/',
    'meta':'http://meta.wikipedia.org/wiki/',
    'commons':'http://commons.wikipedia.org/wiki/',
    'WP':'http://en.wikipedia.org/wiki/WP:', #WP: is not a language
    }

def go_wiki(page):
    #is it a special kind of interwiki link?
    prefix = ''
    if ':' in page:
        prefix, subpage = page.split(':',1)
    page = page.replace(' ','_')
    if prefix in interwiki:
        ui.open_file(interwiki[prefix]+subpage)
    elif len(prefix) in (2,3):
        ui.open_file('http://%s.wikipedia.org/wiki/%s' % (prefix, subpage))
    else:
        ui.open_file('http://en.wikipedia.org/wiki/'+page)

def onClick(e):
    fr = e.text.rfind('[[',0,e.pos)
    if fr != -1:
        to = e.text.find(']]',e.pos)
        if to != -1:
            target = e.text[fr+2:to]
            if '[[' not in target and ']]' not in target:
                go_wiki(target)
    
    fr = e.text.rfind('{{',0,e.pos)
    if fr != -1:
        to = e.text.find('}}',e.pos)
        if to != -1:
            target = e.text[fr+2:to]
            if '{{' not in target and '}}' not in target:
                go_wiki('Template:'+target)
