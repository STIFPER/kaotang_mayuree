"""Builds corrected pack graphics from the existing sleeves (the originals flavor-salted*.svg / flavor-jasmine*.svg are NOT modified).
Nutrition numbers are from the SGS nutrition labelling documents (190 g jar):
  Original  (6565751): 900 kcal / sugar 24 g / fat 36 g / sodium 780 mg   (45 / 37 / 55 / 39 %)  ~6 servings
  Lite=Rice (6938561): 900 kcal / sugar 24 g / fat 42 g / sodium 570 mg   (45 / 37 / 65 / 28 %)  ~6 servings
  Salted    (6938562): 900 kcal / sugar  4 g / fat 42 g / sodium 540 mg   (45 /  6 / 65 / 27 %)  ~6 servings
95 g jars (~3 servings): Original 450/12/18/390 (22/18/28/20 %) = the existing flavor-salted-mini.svg;
  Lite 450/12/21/280 (22/18/32/14 %);  Salted 450/2/21/270 (22/3/32/14 %)
Usage (from the site folder):  python3 -I _build/packs/make_pack_graphics.py
Outputs: assets/flavor-original.svg, flavor-lite.svg, flavor-salty-orange.svg (190 g) and flavor-lite-mini.svg, flavor-salty-orange-mini.svg (95 g)"""
from PIL import Image, ImageDraw, ImageFont
import numpy as np, re, base64, io, colorsys
FONT='/Users/stifper/Library/Fonts/NotoSansThai_Condensed-SemiBold.ttf'
SSF=4
def draw_text_c(img,cx,cy,text,size,fill,stroke=0,strokefill=(0,0,0)):
    big=Image.new('RGBA',(img.width*SSF,img.height*SSF),(0,0,0,0));d=ImageDraw.Draw(big)
    ft=ImageFont.truetype(FONT,size*SSF)
    bb=d.textbbox((0,0),text,font=ft,stroke_width=stroke*SSF)
    w=bb[2]-bb[0];h=bb[3]-bb[1]
    d.text((cx*SSF-w/2-bb[0],cy*SSF-h/2-bb[1]),text,font=ft,fill=fill,stroke_width=stroke*SSF,stroke_fill=strokefill)
    big=big.resize(img.size,Image.LANCZOS);base=img.convert('RGBA');base.alpha_composite(big);return base.convert('RGB')
def edit(src_svg,vals,servings,orange=False):
    s=open(src_svg,encoding='utf-8').read()
    im=Image.open(io.BytesIO(base64.b64decode(re.search(r'xlink:href="data:image/png;base64,([^"]+)"',s).group(1)))).convert('RGB')
    bg=im.getpixel((20,744))
    d=ImageDraw.Draw(im)
    for cx,(v,p) in zip([165,267,367,467],vals):
        d.rectangle((cx-46,808,cx+46,825),fill=(255,255,255))
        d.ellipse((cx-44,858,cx+44,888),fill=(255,255,255))
        im=draw_text_c(im,cx,816,v,23,(0,0,0))
        im=draw_text_c(im,cx+1,872,'*'+p+'%',21,(0,0,0))
        d=ImageDraw.Draw(im)
    d.rectangle((526,732,548,756),fill=bg)
    im=draw_text_c(im,537,744,str(servings),25,(255,255,255),stroke=2)
    field='#bc332c' if 'salted' in src_svg else '#f2eede'
    if orange:
        a=np.asarray(im).astype(float)/255
        r,g,b=a[:,:,0],a[:,:,1],a[:,:,2]
        mx=a.max(axis=2);mn=a.min(axis=2);v=mx;sat=np.where(mx>0,(mx-mn)/np.maximum(mx,1e-6),0)
        dlt=np.maximum(mx-mn,1e-6)
        hue=np.where(mx==r,((g-b)/dlt)%6,np.where(mx==g,(b-r)/dlt+2,(r-g)/dlt+4))/6.0
        tb=colorsys.rgb_to_hsv(226/255,98/255,52/255);bgv=colorsys.rgb_to_hsv(188/255,51/255,44/255)
        w=np.clip((sat-0.45)/0.2,0,1)*np.clip((v-0.58)/0.1,0,1)
        newh=(hue+(tb[0]-bgv[0])*w)%1.0
        news=np.clip(sat*(1-w)+(sat*(tb[1]/bgv[1]))*w,0,1);newv=np.clip(v*(1-w)+(v*(tb[2]/bgv[2]))*w,0,1)
        h6=newh*6;i=np.floor(h6).astype(int)%6;f=h6-np.floor(h6)
        p_=newv*(1-news);q=newv*(1-f*news);t=newv*(1-(1-f)*news)
        out=np.zeros_like(a)
        for k,(rr,gg,bb_) in enumerate([(newv,t,p_),(q,newv,p_),(p_,newv,t),(p_,q,newv),(t,p_,newv),(newv,p_,q)]):
            mk=(i==k);out[:,:,0][mk]=rr[mk];out[:,:,1][mk]=gg[mk];out[:,:,2][mk]=bb_[mk]
        im=Image.fromarray((out*255).clip(0,255).astype('uint8'))
        field='#e16233'
    buf=io.BytesIO();im.save(buf,'PNG',optimize=True)
    s=re.sub(r'xlink:href="data:image/png;base64,[^"]+"','xlink:href="data:image/png;base64,'+base64.b64encode(buf.getvalue()).decode()+'"',s,count=1)
    s=s.replace('fill="#bc332c"','fill="%s"'%field) if orange else s
    return s
T=[('assets/flavor-original.svg','assets/flavor-salted.svg',[('900','45'),('24','37'),('36','55'),('780','39')],6,False,'Mayuree original large packaging graphic'),
   ('assets/flavor-lite.svg','assets/flavor-jasmine.svg',[('900','45'),('24','37'),('42','65'),('570','28')],6,False,'Mayuree lite (rice) large packaging graphic'),
   ('assets/flavor-salty-orange.svg','assets/flavor-salted.svg',[('900','45'),('4','6'),('42','65'),('540','27')],6,True,'Mayuree salted (orange) large packaging graphic'),
   ('assets/flavor-lite-mini.svg','assets/flavor-jasmine-mini.svg',[('450','22'),('12','18'),('21','32'),('280','14')],3,False,'Mayuree lite (rice) mini packaging graphic'),
   ('assets/flavor-salty-orange-mini.svg','assets/flavor-salted-mini.svg',[('450','22'),('2','3'),('21','32'),('270','14')],3,True,'Mayuree salted (orange) mini packaging graphic')]
for out,src,vals,serv,orange,title in T:
    s=edit(src,vals,serv,orange)
    s=re.sub(r'<title>[^<]*</title>','<title>'+title+'</title>',s,count=1)
    open(out,'w',encoding='utf-8').write(s);print(out,len(s)//1024,'KB')
