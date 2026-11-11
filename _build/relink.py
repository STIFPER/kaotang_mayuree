import re
PAGE={'about':'story.html','chapters':'story.html','places':'story.html','corp':'corporate.html','partner':'partner.html','faq':'faq.html','shop':'shop.html','menu':'shop.html','flavors':'shop.html','gift':'gift.html','story':'story.html','charcoal':'craft.html','process':'craft.html','why':'story.html','strip':'craft.html','bleed':'craft.html','visit':'visit.html','reviews':'visit.html'}
TOP={'shop','menu','gift','story','visit','corp','partner','faq'}
def relink(html, ids):
    def tag(m):
        t=m.group(0)
        h=re.search(r'href="#(\w+)"',t)
        if not h: return t
        k=h.group(1)
        if k=='top': return t.replace('href="#top"','href="index.html"')
        if k not in PAGE: return t
        if k in TOP and 'data-pick=' not in t:
            pick=re.search(r'data-pick-opt="(\w+)"',t)
            return t.replace(h.group(0),'href="'+PAGE[k]+('?opt='+pick.group(1) if pick and k=='shop' else '')+'"')
        if k in ids: return t
        pick=re.search(r'data-pick-opt="(\w+)"',t)
        dest=PAGE[k]+('?opt='+pick.group(1) if pick and k=='shop' else '')+'#'+k
        return t.replace(h.group(0),'href="'+dest+'"')
    return re.sub(r'<a\b[^>]*>',tag,html)
