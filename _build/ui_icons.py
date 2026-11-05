"""Replace UI glyphs in HTML text only; never touch scripts, CSS, or artwork."""
from html.parser import HTMLParser
ICONS = {
 '↗':'M5 19 19 5M5 5h14v14', '›':'m9 5 7 7-7 7',
 '←':'M20 12H4m7-7-7 7 7 7', '→':'M4 12h16m-7-7 7 7-7 7',
 '▶':'m8 5 11 7-11 7Z', '★':'m12 3 2.8 5.8 6.4.9-4.6 4.5 1.1 6.4-5.7-3-5.7 3 1.1-6.4L2.8 9.7l6.4-.9Z',
 '✓':'m5 12 4 4L19 6', '✦':'m12 2 2.5 7.5L22 12l-7.5 2.5L12 22l-2.5-7.5L2 12l7.5-2.5Z'
}
def svg(char):
 fill=' ui-icon-solid' if char in '★▶✦' else ''
 return f'<svg class="ui-icon{fill}" viewBox="0 0 24 24" aria-hidden="true" focusable="false" data-i18n-skip><path d="{ICONS[char]}"/></svg>'
class IconHTML(HTMLParser):
 def __init__(self):super().__init__(convert_charrefs=False);self.parts=[];self.raw=None;self.svg_depth=0
 def handle_starttag(self,tag,attrs):
  self.parts.append(self.get_starttag_text())
  if tag in ('script','style'):self.raw=tag
  if tag=='svg':self.svg_depth+=1
 def handle_startendtag(self,tag,attrs):self.parts.append(self.get_starttag_text())
 def handle_endtag(self,tag):
  self.parts.append(f'</{tag}>')
  if tag==self.raw:self.raw=None
  if tag=='svg':self.svg_depth=max(0,self.svg_depth-1)
 def handle_data(self,data):self.parts.append(data if self.raw or self.svg_depth else ''.join(svg(c) if c in ICONS else c for c in data))
 def handle_entityref(self,name):self.parts.append('&'+name+';')
 def handle_charref(self,name):self.parts.append('&#'+name+';')
 def handle_comment(self,data):self.parts.append('<!--'+data+'-->')
 def handle_decl(self,data):self.parts.append('<!'+data+'>')
def iconize(html):
 p=IconHTML();p.feed(html);return ''.join(p.parts)
