import os
HERE=os.path.dirname(os.path.abspath(__file__))
import re
import sys
sys.path.insert(0,HERE)
from relink import relink
src=open(HERE+'/master.html',encoding='utf-8').read()
head=src[:src.index('</style>')]                      # head + all shared CSS
hdr=src[src.index('<!-- ===== HEADER ===== -->'):src.index('<main id="top">')]
ftr=src[src.index('<!-- ===== FOOTER ===== -->'):src.index('<script>')]
js=src[src.index('<script>\n(() => {'):]
# ---- links in header/footer → shop.html
def fix(h):
    h=re.sub(r'data-pick-opt="(\w+)"','',h)
    h=re.sub(r'href="#shop"([^>]*?)\s*>',lambda m:'href="shop.html"'+m.group(1)+'>',h)
    h=re.sub(r'href="#(menu|gift|story|charcoal|why|visit|strip|reviews)"',r'href="shop.html#\1"',h)
    h=h.replace('href="#top"','href="index.html"')
    return h
hdr=relink(hdr,set()); ftr=relink(ftr,set())
# pick-option deep links
hdr=hdr.replace('<a class="mcard" href="shop.html"  style="--bg:#F3B08F">','<a class="mcard" href="shop.html?opt=salted" style="--bg:#F3B08F">')
hdr=hdr.replace('<a href="shop.html" >“เค็ม” Salted</a>','<a href="shop.html?opt=salted">“เค็ม” Salted</a>').replace('<a href="shop.html" >“ข้าว” Jasmine Rice</a>','<a href="shop.html?opt=jasmine">“ข้าว” Jasmine Rice</a>')
hdr=hdr.replace('<a href="shop.html" >Duo Set</a>','<a href="shop.html?opt=duo">Duo Set</a>')
hdr=re.sub(r'<a class="mcard" href="shop.html"\s+style="--bg:#E6DCC0"','<a class="mcard" href="shop.html?opt=jasmine" style="--bg:#E6DCC0"',hdr)
hdr=re.sub(r'<a class="mcard" href="shop.html"\s+style="--bg:#F2C4AE"','<a class="mcard" href="shop.html?opt=duo" style="--bg:#F2C4AE"',hdr)
hdr=re.sub(r'<a class="mcard" href="shop.html"\s+style="--bg:#F3B08F"','<a class="mcard" href="shop.html?opt=salted" style="--bg:#F3B08F"',hdr)

css='''
/* =============== HOME (หน้าแรก) =============== */
.hm-hero{background:var(--red);color:var(--cream);position:relative;overflow:hidden;display:grid;grid-template-rows:auto auto;text-align:center;padding:clamp(40px,7vh,80px) 0 0}
.hm-hero h1{font-family:var(--display);font-size:clamp(2.6rem,7.6vw,7rem);line-height:1.12;max-width:15ch;margin:.25em auto .5em;color:var(--cream)}
.hm-hero h1 em{font-style:normal;color:var(--ochre)}
.hm-hero .label{color:var(--blush)}
.hm-hero .pill{background:var(--cream);color:var(--ink);border-color:var(--cream);box-shadow:0 3px 0 var(--ochre)}
.hm-art{position:relative;display:flex;justify-content:center;align-items:flex-end;gap:clamp(8px,2vw,28px);padding-top:clamp(28px,5vh,64px);overflow:hidden;margin-top:clamp(16px,3vw,40px)}
.hm-art .ph{width:clamp(110px,15vw,240px);aspect-ratio:3/4;margin-bottom:clamp(10px,3vw,40px);border-radius:var(--r-lg)!important;object-fit:cover;border-radius:var(--r-lg) var(--r-lg) 0 0;margin-bottom:-2px}
.hm-art .ph.l{rotate:-4deg;transform-origin:bottom}
.hm-art .ph.r{rotate:4deg;transform-origin:bottom}
.hm-art .packs{position:relative;display:flex;align-items:flex-end;margin-bottom:-6px;z-index:2}
.hm-art .packs .disc{position:absolute;left:50%;bottom:-34%;width:150%;translate:-50% 0;z-index:0;animation:hmspin 70s linear infinite}
.hm-art .packs .pk{position:relative;z-index:1;height:clamp(210px,min(34vw,46vh),480px);width:auto;filter:drop-shadow(0 22px 22px rgba(50,10,5,.4));transition:transform .5s var(--ease)}
.hm-art .packs .pk.a{rotate:-6deg;margin-right:-5%}.hm-art .packs .pk.b{rotate:5deg}
.hm-art .packs:hover .pk.a{transform:translateX(-10px) rotate(-3deg)}.hm-art .packs:hover .pk.b{transform:translateX(10px) rotate(3deg)}
@keyframes hmspin{to{rotate:360deg}}

.hm-promos{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(12px,1.6vw,22px);padding:clamp(48px,7vw,96px) 0 0}
.hm-card{position:relative;display:flex;flex-direction:column;min-height:clamp(420px,42vw,560px);border-radius:var(--r-lg);overflow:hidden;padding:clamp(22px,2.4vw,34px);color:var(--ink);transition:transform .45s var(--ease)}
.hm-card:hover{transform:translateY(-6px)}
.hm-card .k{font-size:.84rem;letter-spacing:.08em}
html[lang="th"] .hm-card .k{letter-spacing:.02em}
.hm-card h3{font-size:clamp(1.7rem,2.6vw,2.4rem);line-height:1.2;margin:.2em 0 .3em}
.hm-card p{font-size:.98rem;max-width:30ch}
.hm-card .go{margin-top:auto;align-self:flex-start}
.hm-card .art{position:absolute;inset:auto 0 0 0;height:52%;display:flex;justify-content:center;align-items:flex-end;pointer-events:none}
.hm-card .art img.cover{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.hm-card.ph-card .art{height:100%;inset:0;z-index:0}
.hm-card.ph-card>*:not(.art){position:relative;z-index:1}
.hm-card.ph-card::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(60,8,10,.82),rgba(60,8,10,.1) 60%,rgba(60,8,10,.55));z-index:0}
.hm-card.ph-card{color:var(--cream)}
.hm-card .art .pk{height:clamp(170px,17vw,250px);width:auto;filter:drop-shadow(0 14px 12px rgba(50,15,5,.3))}
.hm-card .art .pk+.pk{margin-left:-4%;rotate:5deg}
.hm-card .art .pk:first-child{rotate:-5deg}
/* Keep the Duo illustration above the card edge. */
.hm-promos .hm-card:first-child .art{bottom:clamp(42px,4.5vw,64px)}
.hm-card .go{position:relative;z-index:2}

.hm-say{position:relative;text-align:center;padding:clamp(70px,10vw,150px) 0 clamp(40px,6vw,80px)}
.hm-say h2{font-size:clamp(2rem,5.2vw,4.4rem);max-width:18ch;margin:0 auto;color:var(--ink)}
.hm-say .drop{display:block;width:26px;height:36px;margin:28px auto 0;background:var(--red);border-radius:50% 50% 50% 50%/62% 62% 38% 38%;rotate:180deg}
.hm-say .jar{position:absolute;height:clamp(120px,16vw,230px);top:clamp(30px,6vw,90px)}
.hm-say .jar.a{left:4%;rotate:-8deg}.hm-say .jar.b{right:4%;rotate:8deg;scale:-1 1}

.hm-two{display:grid;gap:clamp(40px,7vw,110px);padding:clamp(20px,4vw,60px) 0 clamp(60px,9vw,130px)}
.hm-blurb{display:grid;grid-template-columns:1fr 1fr;gap:clamp(24px,5vw,80px);align-items:center}
.hm-blurb:nth-child(even) .art{order:2}
.hm-blurb .art{position:relative;aspect-ratio:1;display:grid;place-items:center}
.hm-blurb .art .tex{position:absolute;inset:6%;width:88%;height:88%;object-fit:contain}
.hm-blurb .art .jar{position:relative;height:84%}
.hm-blurb .art .round{position:relative;width:64%;aspect-ratio:1;object-fit:cover;border-radius:50%;border:6px solid var(--paper);rotate:-4deg}
.hm-blurb h3{font-size:clamp(1.2rem,1.6vw,1.5rem);text-align:center;margin-bottom:.6em}
.hm-blurb p{font-size:1.05rem;max-width:36ch;margin-inline:auto;text-align:center;color:var(--ink-2)}
.hm-blurb .txt{padding-inline:clamp(0px,3vw,40px)}

.hm-trio{background:var(--cream);padding:clamp(60px,8vw,110px) 0;border-radius:var(--r-lg) var(--r-lg) 0 0}
.hm-trio h2{text-align:center;font-size:clamp(1.9rem,4vw,3.2rem);margin-bottom:clamp(28px,4vw,56px)}
.hm-prods{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(12px,1.6vw,22px)}
.hm-prod{position:relative;display:flex;flex-direction:column;align-items:center;text-align:center;padding:clamp(18px,2vw,28px);border-radius:var(--r-lg);background:var(--paper);transition:transform .45s var(--ease)}
.hm-prod:hover{transform:translateY(-6px)}
.hm-prod .meta{display:flex;justify-content:space-between;width:100%;font-size:.86rem}
.hm-prod .stage{width:100%;aspect-ratio:1;border-radius:var(--r-md);display:flex;align-items:flex-end;justify-content:center;gap:0;margin:14px 0 18px;padding-bottom:6%;overflow:hidden;transition:background .4s}
.hm-prod .stage .pk{height:78%;width:auto;filter:drop-shadow(0 14px 12px rgba(50,15,5,.28));transition:transform .5s var(--ease)}
.hm-prod .stage .pk.mini{height:52%}
.hm-prod:hover .stage .pk{transform:rotate(-5deg) translateY(-6px)}
.hm-prod .tag{font-size:.84rem;letter-spacing:.06em}
.hm-prod h3{font-size:1.5rem;line-height:1.2;margin:.15em 0 .1em}
.hm-prod p{font-size:.96rem;color:var(--ink-2);max-width:26ch;margin-bottom:16px}
.hm-prod .pill{margin-top:auto}
.hm-all{text-align:center;margin-top:clamp(28px,4vw,48px)}

.hm-facts{padding:clamp(60px,8vw,110px) 0 0;overflow:hidden}
.hm-facts .row{display:flex;gap:16px;width:max-content;animation:hmslide 46s linear infinite}
.hm-facts:hover .row{animation-play-state:paused}
.hm-fact{display:flex;flex-direction:column;justify-content:space-between;gap:28px;width:clamp(240px,25vw,340px);min-height:clamp(190px,18vw,240px);padding:24px 26px;border-radius:var(--r-lg);font-size:1.02rem;line-height:1.55;color:var(--ink)}
.hm-fact:nth-child(4n+1){background:var(--ochre)}.hm-fact:nth-child(4n+2){background:var(--blush)}
.hm-fact:nth-child(4n+3){background:var(--red);color:var(--cream)}.hm-fact:nth-child(4n){background:var(--ink);color:var(--cream)}
.hm-fact b{display:block;font-size:clamp(2.4rem,4vw,3.4rem);line-height:1;font-variant-numeric:lining-nums}
.hm-fact:nth-child(4n+3) b{color:var(--ochre)}.hm-fact:nth-child(4n) b{color:var(--blush)}
@keyframes hmslide{to{transform:translateX(calc(-50% - 8px))}}

.hm-ways{padding:clamp(70px,9vw,130px) 0 0;overflow:hidden}
.hm-mq{display:flex;width:max-content;animation:hmslide 38s linear infinite;font-family:var(--display);font-size:clamp(2.4rem,8vw,7rem);line-height:1.2;color:var(--ink);white-space:nowrap}
.hm-mq span{padding-right:.6em}.hm-mq span:nth-child(even){color:var(--red)}
.hm-use{display:grid;grid-template-columns:1fr 1.1fr;gap:clamp(24px,5vw,80px);align-items:center;padding:clamp(36px,6vw,80px) 0}
.hm-use .shot{position:relative;aspect-ratio:4/5;border-radius:var(--r-lg);overflow:hidden}
.hm-use .shot img{width:100%;height:100%;object-fit:cover}
.hm-use ul{list-style:none;display:flex;flex-wrap:wrap;gap:10px;margin:18px 0 26px}
.hm-use li{padding:.5em 1.1em;border:1.5px solid var(--ink);border-radius:999px;font-size:.98rem}
.hm-use h3{font-size:clamp(1.7rem,3vw,2.6rem);line-height:1.2}
.hm-use p{font-size:1.05rem;color:var(--ink-2);max-width:42ch;margin-top:.7em}

.hm-about{text-align:center;padding:clamp(40px,6vw,90px) 0 clamp(60px,8vw,110px)}
.hm-about h2{font-size:clamp(1.8rem,4vw,3.2rem);max-width:20ch;margin:0 auto .6em}

.hm-rail{overflow:hidden;padding:0 0 clamp(60px,8vw,110px)}
.hm-rail .row{display:flex;gap:14px;width:max-content;animation:hmslide 60s linear infinite}
.hm-rail img{height:clamp(220px,26vw,360px);aspect-ratio:2/3;object-fit:cover;border-radius:var(--r-md)}
.hm-rail-head{display:flex;justify-content:space-between;align-items:baseline;flex-wrap:wrap;gap:8px 18px;padding-bottom:20px}

/* HERO = วิดีโอเต็มจอ */
.hm-hero{position:relative;display:block;min-height:min(86svh,780px);padding:0;display:flex;align-items:center;background:var(--ink);overflow:hidden}
.hm-hero .bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.hm-hero .shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(90,14,16,.8) 0%,rgba(90,14,16,.6) 45%,rgba(90,14,16,.2) 72%,rgba(90,14,16,.5) 100%)}
.hm-hero .in{position:relative;z-index:2;padding:clamp(56px,10vh,110px) 0}
.hm-hero .label{color:var(--cream);text-shadow:0 1px 12px rgba(60,8,10,.6)}
.hm-hero h1{text-shadow:0 2px 24px rgba(60,8,10,.45)}
.hm-hero .packs{position:absolute;left:50%;bottom:-3%;translate:-50% 0;z-index:2;display:flex;align-items:flex-end}
.hm-hero .packs .pk{height:clamp(170px,min(26vw,34vh),360px);width:auto;filter:drop-shadow(0 22px 22px rgba(30,5,5,.5));transition:transform .5s var(--ease)}
.hm-hero .packs .pk.a{rotate:-6deg;margin-right:-4%}.hm-hero .packs .pk.b{rotate:5deg}
.hm-hero .packs:hover .pk.a{transform:translateX(-10px) rotate(-3deg)}.hm-hero .packs:hover .pk.b{transform:translateX(10px) rotate(3deg)}

/* ส่วนเล่าเรื่องใต้ข้อความหลัก: จัดใหม่ให้กระชับ อ่านง่าย */
.hm-say{padding:clamp(56px,7vw,100px) 0 clamp(20px,3vw,40px)}
.hm-two{gap:clamp(36px,5vw,72px);padding:clamp(10px,2vw,30px) 0 clamp(60px,8vw,110px)}
.hm-blurb{grid-template-columns:minmax(0,.9fr) minmax(0,1fr);gap:clamp(24px,5vw,72px);max-width:1040px;margin-inline:auto;width:100%}
.hm-blurb .art{max-width:400px;width:100%;justify-self:center}
.hm-blurb .txt{padding:0;text-align:left}
.hm-blurb .txt .label{display:block;margin-bottom:.9em;color:var(--red)}
.hm-blurb h3{font-size:clamp(1.9rem,3.4vw,3rem);text-align:left;line-height:1.2;margin-bottom:.5em;color:var(--ink)}
.hm-blurb p{font-size:clamp(1.05rem,1.4vw,1.25rem);max-width:none;margin:0;text-align:left;line-height:1.75;color:var(--ink)}

/* ลายเส้นกระปุก: วางกระจายหลายจุด คลิกแล้วเด้ง */
.hm-trio .wrap,.hm-use,.hm-say{position:relative}
.jar-fx{position:absolute;z-index:3;cursor:pointer;height:clamp(110px,13vw,190px);width:auto;transform-origin:50% 92%;transition:transform .35s var(--spring);-webkit-tap-highlight-color:transparent;user-select:none}
.jar-fx:hover{transform:rotate(-7deg) translateY(-6px)}
.jar-fx.pop{animation:jarpop .85s var(--ease)}
@keyframes jarpop{0%{transform:none}18%{transform:translateY(-34px) rotate(-16deg)}40%{transform:translateY(0) rotate(10deg)}58%{transform:translateY(-12px) rotate(-6deg)}78%{transform:rotate(3deg)}100%{transform:none}}
.jar-fx.j1{left:clamp(8px,6vw,110px);top:clamp(40px,6vw,90px);rotate:-9deg}
.hm-blurb .art .jar-fx.j2{right:-6%;bottom:-4%;height:clamp(110px,12vw,170px);rotate:13deg}
.jar-fx.j3{right:clamp(0px,3vw,60px);top:-6%;rotate:8deg;scale:-1 1}
.jar-fx.j4{right:clamp(0px,2vw,30px);bottom:2%;height:auto;width:clamp(150px,17vw,250px);rotate:-4deg}
@media (max-width:900px){.jar-fx{height:96px}.jar-fx.j1{left:2%;top:8px}.jar-fx.j3{top:-8px}.jar-fx.j4{right:0;bottom:-10px;width:130px;height:auto}.hm-blurb .art .jar-fx.j2{height:100px;right:-2%}}
@media (prefers-reduced-motion:reduce){.jar-fx.pop{animation:none}}

/* ตัวอย่างขั้นตอนการทำบนหน้า Home */
.hm-proc{padding:clamp(10px,2vw,30px) 0 clamp(60px,8vw,110px)}
.hm-proc-head{display:flex;flex-direction:column;align-items:center;text-align:center;gap:14px;margin-bottom:clamp(28px,4vw,52px)}
.hm-proc-head h2{font-size:clamp(2rem,4.4vw,3.4rem);line-height:1.2}
.hm-proc-head .label{color:var(--red)}
.hm-proc-grid{grid-template-columns:repeat(3,1fr)}
@media (max-width:700px){.hm-proc-grid{grid-template-columns:1fr}}

/* รูปถ่ายสินค้าจริง */
.hm-lineup{margin:0 0 clamp(28px,4vw,52px);border-radius:var(--r-lg);overflow:hidden;aspect-ratio:21/9;background:#E9ECEF}
.hm-lineup img{width:100%;height:100%;object-fit:cover;object-position:50% 55%}
.hm-prod .stage.photo{padding:0;overflow:hidden;background:#EEF0F2}
.hm-prod .stage.photo .pk-ph{width:100%;height:100%;object-fit:cover;transition:transform .6s var(--ease)}
.hm-prod:hover .stage.photo .pk-ph{transform:scale(1.05)}
@media (max-width:700px){.hm-lineup{aspect-ratio:4/3}}

/* ลายเส้นแทนรูปกลมในบล็อกเล่าเรื่อง */
.hm-blurb .art .line{width:auto;max-width:92%;height:auto;max-height:100%;object-fit:contain;transition:transform .5s var(--spring)}
.hm-blurb:hover .art .line{transform:rotate(-3deg) scale(1.03)}

/* ลายเส้นผู้หญิงสวมหมวก (ตัวแทนแบรนด์) เหนือหัวข้อ */
.hm-about{position:relative}
.hm-about .about-lady{position:static;display:block;margin:0 auto 22px;height:clamp(150px,19vw,260px);width:auto;rotate:0deg}

/* กรอบ หอม กลมกล่อม — เน้นภาพ */
.hm-qual{background:#FBEFE6;padding:clamp(48px,7vw,96px) 0 clamp(44px,6vw,80px)}
.hm-qual .wrap{width:calc(100% - clamp(24px,3.4vw,56px));max-width:none}
.hm-qual h2{font-size:clamp(2.6rem,7vw,6rem);line-height:1.1;color:var(--ink);margin-bottom:clamp(22px,3.4vw,44px);letter-spacing:-.005em}
.hm-qual-grid{list-style:none;display:flex;gap:clamp(10px,1.6vw,22px);width:calc(100% - clamp(24px,3.4vw,56px));margin-inline:auto;align-items:stretch}
.hm-qual-grid li{position:relative;flex:var(--ar) 1 0;min-width:0;aspect-ratio:var(--ar);overflow:hidden;border-radius:4px;background:var(--cream)}
.hm-qual-grid picture{display:block;width:100%;height:100%}
.hm-qual-grid img{width:100%;height:100%;object-fit:cover;display:block;transition:transform 1s var(--ease)}
.hm-qual-grid li:hover img{transform:scale(1.05)}
/* QUALITY reference framing: closer subjects, no shooting-paper edges. */
.hm-qual-grid li:nth-child(1){--crop-scale:1.45;--crop-origin:50% 85%}
.hm-qual-grid li:nth-child(2){--crop-scale:1.42;--crop-origin:50% 56%}
.hm-qual-grid li:nth-child(3){--crop-scale:1.50;--crop-origin:25% 15%}
.hm-qual-grid li:nth-child(4){--crop-scale:1.03;--crop-origin:50% 50%}
.hm-qual-grid img{transform:scale(var(--crop-scale));transform-origin:var(--crop-origin)}
.hm-qual-grid li:hover img{transform:scale(calc(var(--crop-scale)*1.025))}
.hm-qual-intro{margin-bottom:clamp(18px,2vw,28px)}



.hm-qual-grid span{position:absolute;left:12px;bottom:12px;padding:.45em 1em;border-radius:999px;background:rgba(251,239,230,.94);color:var(--ink);font-size:.95rem;line-height:1.3}
.hm-qual-foot{display:flex;align-items:center;justify-content:flex-end;flex-wrap:wrap;gap:12px;margin-top:clamp(18px,2.6vw,32px);width:calc(100% - clamp(24px,3.4vw,56px))}
.hm-qual-intro .badge{display:inline-flex;align-items:center;gap:10px;font-size:1rem}
.hm-qual-intro .badge::before{content:"✓";color:var(--red);font-size:1.15em}
@media (max-width:700px){
  .hm-qual .wrap,.hm-qual-foot{width:calc(100% - 24px)}
  .hm-qual h2{font-size:2.6rem}
  .hm-qual-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px;width:calc(100% - 24px)}
  .hm-qual-grid li{aspect-ratio:.7;flex:none}
  .hm-qual-grid span{left:8px;bottom:8px;font-size:.8rem;padding:.4em .85em}
  .hm-qual-foot{flex-direction:column;align-items:stretch;width:calc(100% - 32px)}
  .hm-qual-intro .badge{justify-content:center}
  .hm-qual-foot .pill{width:100%}
}

@media (max-width:900px){
  .hm-promos,.hm-prods{grid-template-columns:1fr}
  .hm-card{min-height:420px}
  .hm-prod .stage{aspect-ratio:1.25}
  .hm-blurb,.hm-use{grid-template-columns:1fr}
  .hm-blurb .art{max-width:300px}
  .hm-blurb:nth-child(even) .art{order:0}
  .hm-say .jar{display:none}
  .hm-art .ph{width:clamp(90px,26vw,160px)}
}
/* MOBILE — home */
/* =========================================================
   MOBILE — จัดใหม่สำหรับมือถือ (ไม่ใช่แค่ย่อจากเดสก์ท็อป)
   ========================================================= */
html{touch-action:manipulation;-webkit-tap-highlight-color:transparent}
input,select,textarea{font-size:16px!important}           /* iOS ไม่ซูมเมื่อแตะช่องกรอก */
html[lang="th"] .nw{white-space:nowrap}                    /* ไม่ตัดคำไทยกลางคำในหัวข้อ */
.dock{display:none}
@media (max-width:700px){
  body{overflow-x:hidden}
  .wrap{width:calc(100% - 32px)}
  /* แถบสั่งซื้อติดล่างจอ */
  .dock{display:flex;gap:8px;position:fixed;left:12px;right:12px;bottom:calc(12px + env(safe-area-inset-bottom));z-index:70;
    padding:8px;border-radius:999px;background:rgba(246,241,227,.94);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);
    box-shadow:0 10px 30px rgba(60,10,10,.18),0 0 0 1.5px var(--ink);transform:translateY(140%);transition:transform .45s var(--ease)}
  body.dock-on .dock{transform:none}
  .dock-btn{flex:1;display:grid;place-items:center;height:44px;border-radius:999px;font-family:var(--display);font-size:.92rem;color:var(--ink)}
  .dock-btn.main{flex:1.5;background:var(--red);color:var(--cream)}
  footer{padding-bottom:calc(96px + env(safe-area-inset-bottom))}
  .toast{bottom:calc(92px + env(safe-area-inset-bottom))!important}

  .hm-card:hover,.hm-prod:hover,.gset:hover{transform:none;translate:none;rotate:none}

  /* Hero */
  .hm-hero{min-height:74svh!important}
  .hm-hero h1{font-size:clamp(2.3rem,10.5vw,3rem)!important;line-height:1.2;max-width:none}
  .hm-hero .label{font-size:.8rem}

  /* หัวข้อ/ข้อความ */
  .hm-say{padding:56px 0 8px!important}
  .hm-say h2{font-size:clamp(1.9rem,8.6vw,2.4rem)!important}
  .hm-two{gap:44px!important;padding-bottom:56px!important}
  .hm-blurb{gap:14px!important}
  .hm-blurb .art{max-width:230px!important;aspect-ratio:auto!important;justify-self:start!important}
  .hm-blurb .art .line{max-height:230px;width:auto;max-width:100%}
  .hm-blurb h3{font-size:1.75rem!important}
  .hm-blurb p{font-size:1rem!important}
  .hm-use{gap:22px!important;padding:24px 0 40px!important}
  .hm-use .shot{aspect-ratio:4/3!important}
  .hm-about .about-lady{height:150px!important}
  .hm-about h2{font-size:1.8rem!important}
  .jar-fx.j3{display:none}

  /* ฟุตเตอร์: กะทัดรัด */
  footer .cols{gap:28px}
  footer .links{grid-template-columns:1fr 1fr!important;padding-left:0;border-left:0;gap:22px 16px}
  footer .links>div:last-child{grid-column:1/-1}
  footer .links>div:last-child ul{display:flex;flex-wrap:wrap;gap:8px}
  footer .links>div:last-child a{display:inline-block;padding:8px 14px;border:1.5px solid var(--ink);border-radius:999px}
  footer form{margin-top:22px}
  footer .legal{flex-direction:column;gap:6px}

  /* หน้าสินค้า */
  .opts{gap:8px}
  .opt{padding:10px 6px!important}
  .opt b{font-size:1.05rem}
  .tabs nav button{padding-inline:6px}
  .menu-card,.fl{border-radius:var(--r-lg)}

  /* หน้าร้าน */
  .visit-media{min-height:420px!important}
  .gal-btn{width:40px;height:40px}
}


/* =========================================================
   MOBILE v2 — เลย์เอาต์เฉพาะมือถือ (แต่ละส่วนจัดคนละแบบตามเนื้อหา)
   ========================================================= */
@media (max-width:700px){
  /* HERO: ภาพเต็มจอ ข้อความชิดล่างซ้าย ปุ่มเต็มความกว้างในระยะนิ้วโป้ง */
  .hm-hero{min-height:calc(100svh - 68px)!important;display:flex!important;align-items:flex-end!important}
  .hm-hero .shade{background:linear-gradient(180deg,rgba(90,14,16,.1) 0%,rgba(90,14,16,.2) 38%,rgba(90,14,16,.88) 100%)!important}
  .hm-hero .in{text-align:left;padding:0 0 calc(26px + env(safe-area-inset-bottom))!important}
  .hm-hero h1{margin:.25em 0 .55em!important;text-align:left}
  .hm-hero .pill{width:100%;height:54px;font-size:1rem}

  /* PROMOS: เบนโต้ — ใบใหญ่ 1 + ใบเล็ก 2 */
  .hm-promos{display:grid!important;grid-template-columns:1fr 1fr!important;gap:10px!important;padding-top:16px!important}
  .hm-promos .hm-card{padding:18px!important}
  .hm-promos .hm-card:first-child{grid-column:1/-1;min-height:340px!important}
  .hm-promos .hm-card:not(:first-child){min-height:0!important;aspect-ratio:3/4;padding:14px!important}
  .hm-promos .hm-card:not(:first-child) p{display:none}
  .hm-promos .hm-card:not(:first-child) h3{font-size:1.12rem!important;line-height:1.25;margin:.25em 0 0!important}
  .hm-promos .hm-card:not(:first-child) h3 br{display:none}
  .hm-promos .hm-card:not(:first-child) .k{font-size:.72rem!important}
  .hm-promos .hm-card:not(:first-child) .go{height:34px;padding:0 12px;font-size:.74rem}
  .hm-promos .hm-card:nth-child(2) .art img.cover{top:50%!important;height:50%!important}
  .hm-promos .hm-card:first-child .art{height:56%}

  /* TAGLINE: ชิดซ้ายแบบนิตยสาร */
  .hm-say{text-align:left!important;padding:52px 0 0!important}
  .hm-say h2{margin:0!important;font-size:2.15rem!important;max-width:none;line-height:1.2}

  /* เล่าเรื่อง: ลายเส้นกับข้อความวางคู่กัน สลับซ้ายขวา */
  .hm-two{gap:34px!important;padding:26px 0 52px!important}
  .hm-blurb{grid-template-columns:40% 1fr!important;gap:16px!important;align-items:center!important}
  .hm-blurb:nth-child(even){grid-template-columns:1fr 40%!important}
  .hm-blurb:nth-child(even) .art{order:2!important}
  .hm-blurb .art{max-width:none!important;width:100%;aspect-ratio:auto!important;justify-self:stretch!important}
  .hm-blurb .art .line{max-height:210px;width:100%!important;max-width:100%!important;height:auto}
  .hm-blurb .txt .label{margin-bottom:.4em!important;font-size:.74rem}
  .hm-blurb h3{font-size:1.28rem!important;margin-bottom:.35em!important}
  .hm-blurb p{font-size:.9rem!important;line-height:1.6!important}

  /* ขั้นตอน: รายการแนวตั้ง รูปเล็กซ้าย ข้อความขวา (อ่านไล่ลงได้เร็ว) */
  .hm-proc-head{align-items:flex-start!important;text-align:left!important;gap:8px!important;margin-bottom:14px!important}
  .hm-proc-head h2{font-size:1.85rem!important}
  .process .sec-head{text-align:left!important;margin-bottom:18px!important}
  .process .sec-head h2{font-size:2rem!important}
  .pr-grid,.hm-proc-grid{display:flex!important;flex-direction:column;gap:0!important}
  .pr-step{display:grid!important;grid-template-columns:96px 1fr;gap:14px!important;align-items:center;padding:12px 0;border-top:1px solid rgba(126,20,22,.16)}
  .pr-step:last-child{border-bottom:1px solid rgba(126,20,22,.16)}
  .pr-img{aspect-ratio:1!important;border-radius:16px!important}
  .pr-n{width:26px!important;height:26px!important;font-size:.8rem!important;left:6px!important;top:6px!important;box-shadow:none!important}
  .pr-step figcaption b{font-size:1.06rem!important}
  .pr-step figcaption span{font-size:.86rem!important;line-height:1.5}

  /* สินค้า: ภาพรวมเต็มขอบ + กริด 2 คอลัมน์ + Mini เป็นการ์ดแนวนอน */
  .hm-trio{border-radius:0!important;padding:44px 0!important}
  .hm-trio h2{text-align:left!important;font-size:1.85rem!important;margin-bottom:18px!important}
  .hm-lineup{margin:0 -16px 22px!important;border-radius:0!important;aspect-ratio:16/10!important}
  .hm-prods{display:grid!important;grid-template-columns:1fr 1fr!important;gap:10px!important}
  .hm-prod{padding:10px 10px 12px!important;border-radius:18px!important}
  .hm-prod .meta,.hm-prod p{display:none!important}
  .hm-prod .stage{margin:0 0 10px!important;aspect-ratio:1!important;border-radius:12px!important}
  .hm-prod .tag{font-size:.7rem!important}
  .hm-prod h3{font-size:1rem!important;line-height:1.3}
  .hm-prod .pill{height:36px;padding:0 8px;font-size:.76rem;width:100%;margin-top:10px}
  .hm-prod:nth-child(3){grid-column:1/-1;display:grid!important;grid-template-columns:42% 1fr;column-gap:14px;text-align:left;align-items:center;
    grid-template-areas:"stage tag" "stage h3" "stage p" "stage pill"}
  .hm-prod:nth-child(3) .stage{grid-area:stage;margin:0!important}
  .hm-prod:nth-child(3) .tag{grid-area:tag;align-self:end}
  .hm-prod:nth-child(3) h3{grid-area:h3}
  .hm-prod:nth-child(3) p{grid-area:p;display:block!important;font-size:.84rem;margin:2px 0 0;max-width:none}
  .hm-prod:nth-child(3) .pill{grid-area:pill;width:auto;justify-self:start;align-self:start}
  .hm-all{text-align:left!important;margin-top:18px!important}
  .hm-all .pill{width:100%}

  /* กินแบบมยุรี: รูปเต็มขอบ ชิปเลื่อนแถวเดียว */
  .hm-use .shot{margin-inline:-16px;border-radius:0!important;aspect-ratio:4/3!important}
  .hm-use>*{min-width:0}
  .hm-use ul{flex-wrap:nowrap!important;overflow-x:auto;margin-inline:-16px!important;padding:0 16px 4px!important;scrollbar-width:none}
  .hm-use ul::-webkit-scrollbar{display:none}
  .hm-use li{flex:0 0 auto;white-space:nowrap}
  .hm-use h3{font-size:1.85rem!important}
  .hm-use .pill{width:100%}

  .hm-about{text-align:left!important}
  .hm-about .about-lady{margin:0 0 18px!important}
  .hm-about .pill{width:100%}

  /* ฟุตเตอร์: หมวดลิงก์พับเก็บได้ */
  footer .links{grid-template-columns:1fr!important;gap:0!important}
  footer .links>div:not(:last-child){border-top:1px solid rgba(126,20,22,.2)}
  footer .links>div:not(:last-child) h5{display:flex;justify-content:space-between;align-items:center;padding:15px 0;margin:0!important;cursor:pointer;font-size:1rem!important}
  footer .links>div:not(:last-child) h5::after{content:"+";font-size:1.4rem;line-height:1;transition:transform .3s var(--ease)}
  footer .links>div.open h5::after{transform:rotate(45deg)}
  footer .links>div:not(:last-child) ul{display:none!important;padding-bottom:14px}
  footer .links>div.open ul{display:grid!important}
  footer .links>div:last-child{padding-top:18px;border-top:1px solid rgba(126,20,22,.2)}

  /* หน้าสินค้า: รูปเต็มขอบ ไม่มีกรอบ */
  .hero .media{aspect-ratio:4/5;min-height:0!important}
  .hero .frame{inset:0!important;border-radius:0!important}
  .hero .info{padding:26px 16px 36px!important}

  /* ชุดของขวัญ: กริด 2 คอลัมน์ กะทัดรัด */
  .gift-grid{display:grid!important;grid-template-columns:1fr 1fr!important;gap:10px!important}
  .gset{padding:10px 10px 14px!important;gap:8px!important;border-radius:18px!important}
  .gset .gset-ph{margin:0!important;border-radius:12px!important;--r:1/1}
  .gset h3{font-size:1rem!important}
  .gset h3 small{font-size:.74rem!important}
  .gset dl{gap:6px!important}
  .gset dt{font-size:.68rem!important}
  .gset dd{font-size:.8rem!important}
  .gset dl b{font-size:1.02rem!important}

  /* หน้าร้าน: รูปขึ้นก่อน ข้อมูลตามมา รีวิวเป็นแถวรูปเล็ก */
  .visit-card{display:flex!important;flex-direction:column}
  .visit-media{order:-1;min-height:360px!important;border-left:0!important;border-bottom:1.5px solid var(--ink)}
  .visit-card dl div{grid-template-columns:86px 1fr!important}
  .visit-cta .pill{flex:1}
  .visit-rv .vr-photos{display:grid!important;grid-template-columns:repeat(5,1fr)!important;gap:6px!important}
  .visit-rv .vr-photos img{border-radius:10px!important}
}

@media (prefers-reduced-motion:reduce){.hm-art .packs .disc{animation:none}.hm-facts .row,.hm-mq,.hm-rail .row{animation:none}}
'''

facts=[("1968","เปิดครัวที่เอกมัย ซ.10 ก่อนส่งต่อถึงรุ่นที่ 3"),("5–7 นาที","ข้าวหอมมะลิบางเฉียบ คั่วบนเตาถ่านจนกรอบเบา"),("0","ผงชูรสและสารกันบูด ในทุกกระปุก"),("6 เดือน","เก็บได้นาน ปิดฝาเกลียวให้แน่นหลังเปิด"),("สุรินทร์","ข้าวหอมมะลิส่งตรงมาจากสุรินทร์"),("ขอนแก่น","หมูหยองรสเข้มจากขอนแก่น ใส่เต็มคำ")]
fact_html=''.join(f'<div class="hm-fact"><b>{a}</b>{b}</div>' for a,b in facts)
fact_html=fact_html*2
ways=["ชาร้อน","กาแฟดำ","ปิกนิก","ของฝาก","ชามเต็ม","ทุกวัน"]
mq=''.join(f'<span>{w}</span>' for w in ways)*2
rail=['mini-box-in-hand','lifestyle-picnic-board','mini-dog-on-cabinet','product-silver-tray-coffee','mini-in-suitcase','lifestyle-pool-snack','mini-jar-iced-drinks','lifestyle-breakfast-table','mini-walking-with-box','product-bowls-stacked','mini-jar-coffee-sandwich','mini-red-suitcase','process-wok-ladle','mini-tote-in-car']
rail_html=''.join(f'<img src="assets/photos/{r}.jpg" alt="" loading="lazy">' for r in rail)*2

main=f'''<main id="top">

<!-- ===== HERO ===== -->
<section class="hm-hero">
  <video class="bg" src="assets/video/hero.mp4" poster="assets/video/hero-poster.jpg" autoplay muted loop playsinline preload="auto" aria-hidden="true"></video>
  <div class="shade"></div>
  <div class="wrap in">
      <h1 class="display"><span class="nw">ข้าวตังทำมือ</span><br><span class="nw">ทำให้ทุกคำ</span> <em class="nw">อร่อยขึ้น</em></h1>
    <a class="pill" href="shop.html">ดูเมนู ›</a>
  </div>
</section>

<!-- ===== PROMO CARDS ===== -->
<section class="wrap hm-promos">
  <a class="hm-card rv-in" href="shop.html?opt=duo" style="background:var(--ochre)">
    <span class="k label">ของใหม่ · 2 รสชาติ</span>
    <h3>“เค็ม” และ “ข้าว”</h3>
    <p>กล่องใหม่ มีถาดแยกชิ้น ของมาไม่แตกสักแผ่น</p>
    <span class="art"><img class="pk" src="assets/flavor-salted.svg" alt=""><img class="pk" src="assets/flavor-jasmine.svg" alt=""></span>
    <span class="pill go">ดู Duo Set</span>
  </a>
  <a class="hm-card rv-in d1" href="gift.html" style="background:var(--blush)">
    <span class="k label">ชุดของขวัญ</span>
    <h3>จัดชุดของขวัญ<br>จากครัวมยุรี</h3>
    <p>ชะลอม กระเป๋า ถุงผ้า — เลือกชุดที่ใช่ แล้วทักไลน์</p>
    <span class="art"><img class="cover" style="top:46%;height:54%;border-radius:var(--r-md) var(--r-md) 0 0;object-position:50% 30%" src="assets/photos/gift-christmas-cloth-set.jpg" alt=""></span>
    <span class="pill go">ดูชุดของขวัญ</span>
  </a>
  <a class="hm-card ph-card rv-in d2" href="craft.html#charcoal" style="background:var(--ink)">
    <span class="art"><img class="cover" src="assets/video/charcoal-poster.jpg" alt=""></span>
    <span class="k label">รู้มั้ย?</span>
    <h3>เรายังใช้เตาถ่าน</h3>
    <p>คั่วทีละแผ่น ไฟนุ่มสม่ำเสมอ จึงกรอบเบาและหอมควันถ่าน</p>
    <span class="pill light go">ดูเตาถ่าน</span>
  </a>
</section>

<!-- ===== TAGLINE ===== -->
<section class="hm-say">
  <div class="wrap">
    <h2 class="display rv-in"><span class="nw">ข้าวตังกรอบสด</span> <span class="nw">หอมไฟถ่าน</span></h2>
  </div>
</section>

<section class="wrap hm-two">
  <div class="hm-blurb rv-in">
    <div class="art"><img class="line" src="assets/lineart-rice.png" alt="" role="presentation"></div>
    <div class="txt"><span class="label">วัตถุดิบ</span><h3 class="display">ข้าวดี ข้าวตังก็ดี</h3><p>ข้าวหอมมะลิจากสุรินทร์ หมูหยองจากขอนแก่น ปรุงตามสูตรคุณยายสมสมร ไม่ใส่ผงชูรส ไม่ใส่สารกันบูด</p></div>
  </div>
  <div class="hm-blurb rv-in">
    <div class="art"><img class="line" src="assets/lineart-pour.png" alt="" role="presentation"></div>
    <div class="txt"><span class="label">ทำมือทุกวัน</span><h3 class="display">ทำสดใหม่ ส่งถึงมือ</h3><p>ทำมือที่ร้านสุขุมวิท 51 ทุกวัน คั่วบนเตาถ่านทีละแผ่น แล้วบรรจุในกระปุกปิดสนิทเพื่อล็อกความกรอบ</p></div>
  </div>
</section>

<!-- ===== QUALITY (กรอบ หอม กลมกล่อม) — เน้นภาพ ===== -->
<section class="hm-qual">
<ul class="hm-qual-grid">
    <li class="rv-in" style="--ar:.749"><picture><source media="(max-width:700px)" srcset="assets/photos/quality-1-rice.jpg"><img src="assets/photos/quality-1-rice.jpg" alt="ข้าวหอมมะลิในชามโลหะ" loading="lazy"></picture></li>
    <li class="rv-in d1" style="--ar:.737"><picture><source media="(max-width:700px)" srcset="assets/photos/quality-2-pork-floss.jpg"><img src="assets/photos/quality-2-pork-floss.jpg" alt="หมูหยองเนื้อเบาฟูและแผ่นข้าวตัง" loading="lazy"></picture></li>
    <li class="rv-in d2" style="--ar:.705"><picture><source media="(max-width:700px)" srcset="assets/photos/quality-3-seasoning.jpg"><img src="assets/photos/quality-3-seasoning.jpg" alt="ร่อนผงปรุงรส" loading="lazy"></picture></li>
    <li class="rv-in d3" style="--ar:.665"><picture><source media="(max-width:700px)" srcset="assets/photos/quality-4-wok.jpg"><img src="assets/photos/quality-4-wok.jpg" alt="ข้าวตังในกระทะใหญ่" loading="lazy"></picture></li>
  </ul>
</section>

<!-- ===== PRODUCTS ===== -->
<section class="hm-trio">
  <div class="wrap">
    <img class="jar-fx j3" src="assets/lineart-jar.png" alt="" role="presentation">
    <figure class="hm-lineup rv-in"><img src="assets/photos/product-packs-trio.jpg" alt="ข้าวตังทรงเครื่องกล่องใหม่ทุกรส" loading="lazy"></figure>
    <h2 class="display">ข้าวตังแบบที่ควรจะเป็น</h2>
    <div class="hm-prods">
      <a class="hm-prod rv-in" href="shop.html?opt=salted">
        <div class="meta"><span class="label">รสเค็ม</span><span class="label">190 g</span></div>
        <div class="stage photo"><img class="pk-ph" src="assets/photos/product-pack-salted.jpg" alt="กล่อง “เค็ม” Salted" loading="lazy"></div>
        <span class="tag label">เค็ม มัน กลมกล่อม</span>
        <h3>“เค็ม” Salted</h3>
        <p>หมูหยองเต็มคำ กลิ่นหอมเตาถ่าน</p>
        <span class="pill outline">฿165 · ดู “เค็ม”</span>
      </a>
      <a class="hm-prod rv-in d1" href="shop.html?opt=jasmine">
        <div class="meta"><span class="label">รสข้าว</span><span class="label">190 g</span></div>
        <div class="stage photo"><img class="pk-ph" src="assets/photos/product-pack-jasmine.jpg" alt="กล่อง “ข้าว” Jasmine Rice" loading="lazy"></div>
        <span class="tag label">หอมข้าว อ่อนละมุน</span>
        <h3>“ข้าว” Jasmine Rice</h3>
        <p>ไม่มีหมูหยอง ทานมังสวิรัติได้</p>
        <span class="pill outline">฿165 · ดู “ข้าว”</span>
      </a>
      <a class="hm-prod rv-in d2" href="shop.html">
        <div class="meta"><span class="label">Mini</span><span class="label">95 g</span></div>
        <div class="stage photo"><img class="pk-ph" src="assets/photos/mini-box-in-hand-square.jpg" alt="กล่อง Mini 95 g" loading="lazy"></div>
        <span class="tag label">ตัวเล็ก พกง่าย</span>
        <h3>Mini 95 g</h3>
        <p>ลองก่อนซื้อใหญ่ หรือเป็นของแจก</p>
        <span class="pill outline">฿99 · ดูเมนู</span>
      </a>
    </div>
    <div class="hm-all"><a class="pill" href="shop.html">ดูเมนูทั้งหมด ›</a></div>
  </div>
</section>

<!-- ===== SO MANY WAYS ===== -->
<section class="hm-ways">
  <div class="wrap hm-use">
    <div class="shot rv-in"><img src="assets/photos/lifestyle-tea-table.jpg" alt="ชาร้อนคู่ข้าวตังทรงเครื่อง"></div>
    <div class="rv-in d1">
      <span class="label">กินแบบมยุรี</span>
      <h3 class="display">กินได้หลายแบบ อร่อยได้ทุกวัน</h3>
      <ul><li>คู่ชาร้อน</li><li>กับกาแฟดำ</li><li>ปิกนิก</li><li>ของฝากผู้ใหญ่</li><li>ชุดของขวัญ</li></ul>
      <p>เปิดฝาแล้วทานได้เลย แบ่งกินได้ประมาณ 3 ครั้งต่อกระปุกใหญ่</p>
      <p style="margin-top:20px"><a class="pill outline" href="shop.html">เลือกรสชาติ ›</a></p>
    </div>
  </div>
</section>

<section class="hm-about wrap">
  <img class="about-lady jar-fx" src="assets/lineart-couple.png" alt="" role="presentation">
  <h2 class="display rv-in"><span class="nw">ทำโดยคนที่จริงจัง</span><span class="nw">กับข้าวตัง</span><span class="nw">มาตั้งแต่ปี 1968</span></h2>
  <a class="pill" href="story.html">เรื่องของเรา ›</a>
</section>

<section class="hm-rail">
  <div class="wrap hm-rail-head"><span class="label">ดูว่ามยุรีกำลังทำอะไรอยู่:</span><a class="ul" href="https://www.instagram.com/kaotang_mayuree" target="_blank" rel="noopener">Instagram</a></div>
  <div class="row">{rail_html}</div>
</section>

</main>

'''

# ---- script
a=js.index('/* ===== ภาษา'); b=js.index('/* ----- hero options')
pre=js[:js.index('  const st =')] if False else ''
prelude=js[js.index('(() => {'):js.index('  /* ----- hero options')]
mega=js[js.index('  /* ----- mega menu'):js.index('  /* การ์ดวิดีโอในเมนู')]
vidcards=js[js.index('  /* การ์ดวิดีโอในเมนู'):js.index('  /* ลิงก์ในเมนูที่เลือกรสให้เลย')]
i18n=js[js.index('  /* =========================================================\n     I18N'):js.index('  function applyLang(){')]
home_en='''
    /* ===== หน้าแรก ===== */
    "ข้าวตังทำมือ":"Handmade crackers","ทำให้ทุกคำ":"make every bite","อร่อยขึ้น":"better","ดูเมนู ›":"See the menu ›",
    "ของใหม่ · 2 รสชาติ":"New · 2 flavors","กล่องใหม่ มีถาดแยกชิ้น ของมาไม่แตกสักแผ่น":"New pack with a separating tray — not a single cracker broken in transit","ดู Duo Set":"See the Duo Set",
    "จัดชุดของขวัญ":"Personalize gifting","จากครัวมยุรี":"from the Mayuree kitchen","ชะลอม กระเป๋า ถุงผ้า — เลือกชุดที่ใช่ แล้วทักไลน์":"Baskets, bags, cloth pouches — pick your set, then message us on LINE","ดูชุดของขวัญ":"See gift sets",
    "รู้มั้ย?":"Did you know?","เรายังใช้เตาถ่าน":"We still cook on charcoal","คั่วทีละแผ่น ไฟนุ่มสม่ำเสมอ จึงกรอบเบาและหอมควันถ่าน":"Roasted one sheet at a time. Soft, even heat makes them light, crisp and smoky-fragrant.","ดูเตาถ่าน":"See the stove",
    "ข้าวตังกรอบสด หอมไฟถ่าน":"Fresh, crisp crackers with a charcoal aroma",
    "ข้าวดี ข้าวตังก็ดี":"Good rice, good crackers","ข้าวหอมมะลิจากสุรินทร์ หมูหยองจากขอนแก่น ปรุงตามสูตรคุณยายสมสมร ไม่ใส่ผงชูรส ไม่ใส่สารกันบูด":"Jasmine rice from Surin, pork floss from Khon Kaen, made to Khun Yai Somsamorn's recipe. No MSG, no preservatives.",
    "ทำสดใหม่ ส่งถึงมือ":"Made fresh, handed to you","วัตถุดิบ":"Ingredients","ข้าวหอมมะลิ":"Jasmine rice","หมูหยองเบาฟู":"Fluffy pork floss","หวาน เค็ม หอมกระเทียม":"Sweet, salty, garlicky","ผัดบนเตาถ่าน":"Charcoal-fried","ดูวิธีทำ ›":"See how ›","ทำไมถึงอร่อย":"Why it tastes so good","กรอบ หอม กลมกล่อม":"Crisp, fragrant, balanced","เนื้อสัมผัสที่แตกต่างจากขนมขบเคี้ยวทั่วไป":"A texture unlike ordinary snacks","“ข้าวตังแต่ละชิ้นผ่านการคัดเลือก เพื่อให้ผู้บริโภคได้รับรสชาติที่สม่ำเสมอและเข้มข้นในทุกคำ”":"“Every piece is selected, so each bite tastes consistent and full of flavor.”","ผลิตจากข้าวหอมมะลิ ให้กลิ่นหอมและเนื้อสัมผัสบางกรอบ":"Made from jasmine rice — fragrant, thin and crisp","คลุกเคล้ากับหมูหยองเนื้อเบาฟู":"Tossed with light, fluffy pork floss","ปรุงรสหวาน เค็ม และหอมกระเทียมอย่างพอดี":"Seasoned sweet, salty and garlicky — just right","ผัดบนเตาถ่าน ให้กลิ่นหอมกระทะเฉพาะตัว":"Wok-fried over charcoal for a signature aroma","ไม่ใส่ผงชูรส และสารกันเสีย":"No MSG, no preservatives","ดูวิธีทำทุกขั้นตอน ›":"See every step ›","ข้าวหอมมะลิในชามโลหะ":"Jasmine rice in a metal bowl","หมูหยองเนื้อเบาฟูและแผ่นข้าวตัง":"Fluffy pork floss and rice crackers","ร่อนผงปรุงรส":"Sifting the seasoning","ผัดข้าวตังในกระทะบนเตาถ่าน":"Stir-frying crackers in a wok over charcoal","กล่อง Mini 95 g":"Mini 95 g pack","ข้ามไปเนื้อหา":"Skip to content","ข้าวตังกรอบสด":"Fresh, crisp crackers","หอมไฟถ่าน":"with a charcoal aroma","ทำโดยคนที่จริงจัง":"Made by people who take ","กับข้าวตัง":"rice crackers seriously ","มาตั้งแต่ปี 1968":"since 1968","ข้าวตังทรงเครื่องกล่องใหม่ทุกรส":"The new Kaotang Songkrueng packs, every flavor","กล่อง “เค็ม” Salted":"“Salted” pack","กล่อง “ข้าว” Jasmine Rice":"“Jasmine Rice” pack","ชาร้อนคู่ข้าวตังทรงเครื่อง":"Hot tea with Kaotang Songkrueng","ทำมือทุกขั้นตอน":"Handmade at every step","ดูขั้นตอนทั้งหมด ›":"See the full process ›","ทำมือทุกวัน":"Handmade daily","ทำมือที่ร้านสุขุมวิท 51 ทุกวัน คั่วบนเตาถ่านทีละแผ่น แล้วบรรจุในกระปุกปิดสนิทเพื่อล็อกความกรอบ":"Handmade daily at our Sukhumvit 51 shop, roasted over charcoal sheet by sheet, then sealed in a tight jar to lock in the crunch.",
    "ข้าวตังแบบที่ควรจะเป็น":"Rice crackers the way they should be","เค็ม มัน กลมกล่อม":"Savory · rich · balanced","หมูหยองเต็มคำ กลิ่นหอมเตาถ่าน":"Generous pork floss, charcoal-fragrant","฿165 · ดู “เค็ม”":"฿165 · View Salted",
    "หอมข้าว อ่อนละมุน":"Fragrant rice · gentle","ไม่มีหมูหยอง ทานมังสวิรัติได้":"No pork floss — vegetarian-friendly","฿165 · ดู “ข้าว”":"฿165 · View Jasmine Rice",
    "ตัวเล็ก พกง่าย":"Small · easy to carry","ลองก่อนซื้อใหญ่ หรือเป็นของแจก":"Try before going large, or share around","฿99 · ดูเมนู":"฿99 · See menu","ดูเมนูทั้งหมด ›":"See the full menu ›",
    "เปิดครัวที่เอกมัย ซ.10 ก่อนส่งต่อถึงรุ่นที่ 3":"Kitchen opens in Ekkamai Soi 10 — now in its third generation","5–7 นาที":"5–7 min",
    "ข้าวหอมมะลิบางเฉียบ คั่วบนเตาถ่านจนกรอบเบา":"Paper-thin jasmine rice, charcoal-roasted until light and crisp","ผงชูรสและสารกันบูด ในทุกกระปุก":"MSG and preservatives in every jar",
    "เก็บได้นาน ปิดฝาเกลียวให้แน่นหลังเปิด":"Keeps well — screw the lid tight after opening","ข้าวหอมมะลิส่งตรงมาจากสุรินทร์":"Jasmine rice straight from Surin","หมูหยองรสเข้มจากขอนแก่น ใส่เต็มคำ":"Richly seasoned pork floss from Khon Kaen, in every bite",
    "สุรินทร์":"Surin","ขอนแก่น":"Khon Kaen","6 เดือน":"6 months",
    "กินแบบมยุรี":"Eat the Mayuree way","กินได้หลายแบบ อร่อยได้ทุกวัน":"So many ways to enjoy, every day",
    "คู่ชาร้อน":"With hot tea","กับกาแฟดำ":"With black coffee","ปิกนิก":"Picnic","ของฝากผู้ใหญ่":"A gift for elders","ชุดของขวัญ":"Gift sets",
    "เปิดฝาแล้วทานได้เลย แบ่งกินได้ประมาณ 3 ครั้งต่อกระปุกใหญ่":"Open and enjoy — a large jar makes about 3 servings","เลือกรสชาติ ›":"Choose a flavor ›",
    "ทำโดยคนที่จริงจังกับข้าวตังมาตั้งแต่ปี 1968":"Made by people who have taken rice crackers seriously since 1968","เรื่องของเรา ›":"Our story ›",
    "ดูว่ามยุรีกำลังทำอะไรอยู่:":"See what Mayuree is up to:","รู้มั้ย":"Did you know",
    "ชาร้อน":"Hot tea","กาแฟดำ":"Black coffee","ของฝาก":"Gifts","ชามเต็ม":"A full bowl","ทุกวัน":"Every day",
'''
i18n=i18n.replace('  const EN = {\n','  const EN = {'+home_en,1)
home_apply='''  function applyLang(){
    document.documentElement.lang = LANG;
    fillPacks();
    translateTree();
    const H = document.documentElement.dataset, md = document.querySelector('meta[name="description"]');
    if (!H.descTh && md) H.descTh = md.getAttribute("content");
    document.title = t(H.titleTh, H.titleEn);
    if (md) md.setAttribute("content", t(H.descTh, H.descEn));
    $$("#langBtn b").forEach(b => b.classList.toggle("on", b.dataset.l === LANG));
    const mb = $("#menuBtn"); mb.textContent = mb.getAttribute("aria-expanded") === "true" ? t("ปิด","Close") : t("เมนู","Menu");
    mb.setAttribute("aria-label", t("เมนู","Menu"));
  }
  $("#langBtn").addEventListener("click", () => {
    LANG = LANG === "en" ? "th" : "en";
    try { localStorage.setItem("lang", LANG); } catch(e){}
    applyLang();
  });
  let tt; window.toast = m => { const el = $("#toast"); el.textContent = m; el.classList.add("show"); clearTimeout(tt); tt = setTimeout(() => el.classList.remove("show"), 2200); };
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting){ e.target.classList.add("in"); io.unobserve(e.target); } }), { threshold:.15 });
  $$(".rv-in").forEach(el => io.observe(el));
  addEventListener("scroll", () => header.classList.toggle("scrolled", scrollY > 10), { passive:true });
  $$(".jar-fx").forEach(j => { j.addEventListener("click", () => { j.classList.remove("pop"); void j.offsetWidth; j.classList.add("pop"); }); j.addEventListener("animationend", () => j.classList.remove("pop")); });
  /* ----- แถบสั่งซื้อมือถือ: โผล่เมื่อเลื่อนผ่านช่วงบน ----- */
  const dockToggle = () => document.body.classList.toggle("dock-on", scrollY > 420 && (innerHeight + scrollY) < document.body.scrollHeight - 120);
  addEventListener("scroll", dockToggle, { passive:true }); dockToggle();
  /* ----- มือถือ: ฟุตเตอร์พับเก็บได้ ----- */
  $$("footer .links>div:not(:last-child) h5").forEach(h => h.addEventListener("click", () => {
    if (matchMedia("(max-width:700px)").matches) h.parentElement.classList.toggle("open");
  }));
  const hv = $(".hm-hero .bg"); if (hv && matchMedia("(prefers-reduced-motion:reduce)").matches) hv.pause();
  applyLang();
})();
'''
script='<script>\n'+prelude+'  const header = $("#header");\n'+mega+vidcards+i18n+home_apply+'</script>\n</body>\n</html>\n'
# home title
head=head.replace('<title>มยุรี ข้าวตังทรงเครื่อง</title>','<title>มยุรี ข้าวตังทรงเครื่อง</title>',1)
out=head+css+'</style>\n</head>\n<body>\n\n'+hdr+main+ftr+'\n'+script
# __TITLE__ fill
out=out.replace('__TITLE_EN__','Mayuree Kaotang Songkrueng — Homemade Thai Rice Crackers since 1968').replace('__DESC_EN__',"Handmade Thai rice crackers roasted over charcoal, Grandma's recipe since 1968 · Sukhumvit 51, Bangkok").replace('__TITLE__','มยุรี ข้าวตังทรงเครื่อง — ข้าวตังทำมือตั้งแต่ปี 1968').replace('__DESC__','ข้าวตังทรงเครื่องทำมือ คั่วบนเตาถ่าน สูตรคุณยายตั้งแต่ปี 1968 · ร้านสุขุมวิท 51 กรุงเทพฯ · สั่งทาง LINE')
out=re.sub(r'<title>[^<]*</title>','<title>'+'มยุรี ข้าวตังทรงเครื่อง — ข้าวตังทำมือตั้งแต่ปี 1968'+'</title>',out,count=1)
out=out.replace('<nav>\n      <a href="index.html"','<nav>\n      <a aria-current="page" href="index.html"',1)
out=out.replace('</head>', '<link rel="stylesheet" href="assets/presentation.css?v=4">\n<link rel="stylesheet" href="assets/mobile.css?v=1">\n</head>', 1)
out=out.replace('<body>', '<body class="home-page">', 1)
out=out.replace('</body>', '<script src="assets/presentation.js?v=5" defer></script>\n<script src="assets/mobile.js?v=1" defer></script>\n</body>', 1)
open('index.html','w',encoding='utf-8').write(out)
print(len(out))
