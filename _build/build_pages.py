import os
HERE=os.path.dirname(os.path.abspath(__file__))
ALTS={'lifestyle-sharing-spoons': 'ช้อนสองคันตักข้าวตังจากชามเดียวกัน', 'lifestyle-pool-reading': 'นั่งอ่านหนังสือริมสระกับข้าวตังทรงเครื่อง', 'lifestyle-picnic-bowl': 'ข้าวตังทรงเครื่องในชามบนผ้าปิกนิกลายสก็อต', 'lifestyle-beach-bag-book': 'กล่องมยุรีในกระเป๋าถักข้างหนังสือ', 'lifestyle-silver-tray-breakfast': 'ข้าวตังทรงเครื่องบนถาดเงินพร้อมมื้อเช้า'}
import re,sys,json
PAGEMETA=json.loads(open(HERE+'/pagemeta.json',encoding='utf-8').read())
sys.path.insert(0,HERE)
from relink import relink
src=open(HERE+'/master.html',encoding='utf-8').read()
head=src[:src.index('<!-- ===== HEADER')]
hdr=src[src.index('<!-- ===== HEADER'):src.index('<main id="top">')]
mainall=src[src.index('<main id="top">')+len('<main id="top">'):src.index('</main>')]
ftr=src[src.index('</main>')+len('</main>'):src.index('<script>')]
scripts=src[src.index('<script>'):]
scripts=scripts.replace('header.classList.toggle("alt", scrollY > hero.offsetTop','header.classList.toggle("alt", hero.offsetHeight > 0 && scrollY > hero.offsetTop')
assert 'hero.offsetHeight > 0' in scripts
# split sections
starts=[m.start() for m in re.finditer(r'<section',mainall)]
secs=[]
for i,s0 in enumerate(starts):
    e=starts[i+1] if i+1<len(starts) else len(mainall)
    blk=mainall[s0:e]
    # attach preceding comment (belongs to this section) - ignore
    cls=re.search(r'<section[^>]*?(?:id="(\w+)")?[^>]*class="([^"]*)"|<section[^>]*class="([^"]*)"[^>]*?(?:id="(\w+)")?',blk)
    tag=re.match(r'<section[^>]*>',blk).group(0)
    key=(re.search(r'id="(\w+)"',tag) or re.search(r'class="(\w+)',tag)).group(1)
    secs.append((key,blk))
print([k for k,_ in secs])
pages={'shop.html':['shop','flavors','menu'],'story.html':['about','story','chapters','places','why'],'craft.html':['charcoal','process','bleed','strip'],'gift.html':['gift'],'visit.html':['visit'],'corporate.html':['corp']}
need=['addBtn','addPrice','barName','bleedPh','chSound','chVideo','chVideoWrap','fda','flGrid','ingr','opts','price','qtys','selName','shop','sizeName','thumbs','title','track']
titles={'shop.html':'เมนูและสินค้า','story.html':'เรื่องของเรา','gift.html':'ชุดของขวัญ','visit.html':'หน้าร้าน'}
for fn,keys in pages.items():
    body=''.join(b for key in keys for k,b in secs if k==key)
    if fn=='visit.html':
        rv='<div class="visit-rv"><div class="rv-left"><p class="label">เสียงจากลูกค้า</p><div class="rv-score"><b>5.0</b><span class="stars">★★★★★</span></div><p class="rv-cap">จาก 54 รีวิวบน Google</p></div><div class="rv-chips"><div class="chip"><b>Google Maps</b><span>5.0 ★ · 54 รีวิว</span></div><div class="chip"><b>Lazada</b><span>คะแนนร้าน 97% · ซื้อซ้ำ 100%</span></div></div><div class="vr-photos">'+''.join('<img src="assets/photos/%s.jpg" alt="%s" loading="lazy">'%(n,ALTS[n]) for n in ('lifestyle-sharing-spoons','lifestyle-pool-reading','lifestyle-picnic-bowl','lifestyle-beach-bag-book','lifestyle-silver-tray-breakfast'))+'</div></div>'
        i=body.rindex('  </div>\n</section>')
        body=body[:i]+'      '+rv+'\n'+body[i:]
    ids=set(re.findall(r'id="(\w+)"',body))|{k for k in keys}
    ids|={'menu'} if 'menu' in keys else set()
    full=body+hdr+ftr
    stubs=''
    for n in need:
        if f'id="{n}"' not in body+hdr:
            stubs+=('<video hidden id="chVideo" muted></video>' if n=='chVideo' else '<div hidden id="title"><small></small></div>' if n=='title' else f'<div hidden id="{n}"></div>')
    if 'data-u=' not in body: stubs+=''.join(f'<i hidden data-u="{u}"></i>' for u in 'dhm')
    h=relink(hdr,ids); f=relink(ftr,ids); b=relink(body,ids)
    out=head+hdr_placeholder if False else None
    page=head+h+'<main id="top">'+b+'</main>'+f+stubs+scripts
    page=page.replace('<title>มยุรี ข้าวตังทรงเครื่อง</title>','<title>'+titles.get(fn,'')+'</title>',1)
    tt,te,dt,de=PAGEMETA[fn]
    page=page.replace('__TITLE_EN__',te).replace('__DESC_EN__',de).replace('__TITLE__',tt).replace('__DESC__',dt)
    page=re.sub(r'<title>[^<]*</title>','<title>'+tt+'</title>',page,count=1)
    page=page.replace('<nav>\n      <a href="'+fn+'"','<nav>\n      <a aria-current="page" href="'+fn+'"',1)
    for a_,href in (('เมนู','shop.html'),('จัดชุดของขวัญ','gift.html'),('เรื่องของเรา','story.html'),('หน้าร้าน','visit.html')):
        if href==fn: page=re.sub(r'<a href="'+href+r'"( data-mega="\w+")?>'+a_+'</a>',lambda m:'<a aria-current="page" href="'+href+'"'+(m.group(1) or '')+'>'+a_+'</a>',page,count=1)
    open(fn,'w',encoding='utf-8').write(page)
    print(fn,len(page),sorted(ids))

# ---- 404 page (same header/footer, friendly message)
fn='404.html'
body='<section class="e404"><div><img src="assets/lineart-couple.png" alt="" role="presentation"><p class="label">404</p><h1 class="display">ไม่พบหน้านี้</h1><p>หน้าที่คุณหาอาจถูกย้ายหรือไม่มีอยู่แล้ว</p><div class="row"><a class="pill" href="index.html">กลับหน้าแรก</a><a class="pill outline" href="shop.html">ดูเมนู</a></div></div></section>'
stubs=''.join(('<video hidden id="chVideo" muted></video>' if n=='chVideo' else '<div hidden id="title"><small></small></div>' if n=='title' else f'<div hidden id="{n}"></div>') for n in need if f'id="{n}"' not in hdr)+''.join(f'<i hidden data-u="{u}"></i>' for u in 'dhm')
page=head+relink(hdr,set())+'<main id="top">'+body+'</main>'+relink(ftr,set())+stubs+scripts
tt,te,dt,de=PAGEMETA[fn]
page=page.replace('__TITLE_EN__',te).replace('__DESC_EN__',de).replace('__TITLE__',tt).replace('__DESC__',dt)
page=re.sub(r'<title>[^<]*</title>','<title>'+tt+'</title>',page,count=1)
page=page.replace('<meta name="viewport"','<meta name="robots" content="noindex">\n<meta name="viewport"',1)
open(fn,'w',encoding='utf-8').write(page)
print(fn,len(page))
