"""Builds assets/flavor-salty-orange.svg (the single-size orange "เค็ม" pack graphic) from the existing red sleeve in assets/flavor-salted.svg.
The red files are NOT modified. Changes: field colour red->orange, nutrition numbers per the real orange label (900 kcal / 4 g / 42 g / 540 mg), '6 servings'.
Usage: python3 -I _build/packs/make_salty_orange_pack.py  (run from the site folder)"""
from PIL import Image, ImageDraw, ImageFont
import numpy as np, re, base64, io, colorsys
s=open('assets/flavor-salted.svg',encoding='utf-8').read()
m=re.search(r'xlink:href="data:image/png;base64,([^"]+)"',s)
im=Image.open(io.BytesIO(base64.b64decode(m.group(1)))).convert('RGB')
F='/Users/stifper/Library/Fonts/'
SSF=4
def draw_text_c(img,cx,cy,text,size,fill,stroke=0,strokefill=(0,0,0)):
    big=Image.new('RGBA',(img.width*SSF,img.height*SSF),(0,0,0,0));d=ImageDraw.Draw(big)
    ft=ImageFont.truetype(F+'NotoSansThai_Condensed-SemiBold.ttf',size*SSF)
    bb=d.textbbox((0,0),text,font=ft,stroke_width=stroke*SSF)
    w=bb[2]-bb[0];h=bb[3]-bb[1]
    d.text((cx*SSF-w/2-bb[0],cy*SSF-h/2-bb[1]),text,font=ft,fill=fill,stroke_width=stroke*SSF,stroke_fill=strokefill)
    big=big.resize(img.size,Image.LANCZOS);base=img.convert('RGBA');base.alpha_composite(big);return base.convert('RGB')
d=ImageDraw.Draw(im)
for cx,(v,p) in zip([165,267,367,467],[('900','45'),('4','6'),('42','65'),('540','27')]):
    d.rectangle((cx-46,808,cx+46,825),fill=(255,255,255))
    d.ellipse((cx-44,858,cx+44,888),fill=(255,255,255))
    im=draw_text_c(im,cx,816,v,23,(0,0,0))
    im=draw_text_c(im,cx+1,872,'*'+p+'%',21,(0,0,0))
    d=ImageDraw.Draw(im)
d.rectangle((526,732,548,756),fill=(188,51,44))
im=draw_text_c(im,537,744,'6',25,(255,255,255),stroke=2)
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
for k,(rr,gg,bb) in enumerate([(newv,t,p_),(q,newv,p_),(p_,newv,t),(p_,q,newv),(t,p_,newv),(newv,p_,q)]):
    mk=(i==k);out[:,:,0][mk]=rr[mk];out[:,:,1][mk]=gg[mk];out[:,:,2][mk]=bb[mk]
res=Image.fromarray((out*255).clip(0,255).astype('uint8'))
buf=io.BytesIO();res.save(buf,'PNG',optimize=True)
s2=re.sub(r'xlink:href="data:image/png;base64,[^"]+"','xlink:href="data:image/png;base64,'+base64.b64encode(buf.getvalue()).decode()+'"',s,count=1)
s2=s2.replace('fill="#bc332c"','fill="#e16233"').replace('<title>Mayuree salted large packaging graphic</title>','<title>Mayuree salty (orange) large packaging graphic</title>')
open('assets/flavor-salty-orange.svg','w',encoding='utf-8').write(s2)
res.save('/tmp/_salty_sleeve_preview.png') if False else None
print('ok',len(s2)//1024,'KB')
