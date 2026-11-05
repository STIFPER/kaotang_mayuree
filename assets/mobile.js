/* A compact, accessible mobile navigation, independent of the desktop mega menu. */
(() => {
 const mobile=matchMedia('(max-width:700px)');
 const compactNav=matchMedia('(max-width:1100px)');
 const header=document.querySelector('#header');
 const panel=document.querySelector('#mega-shop');
 const toggle=document.querySelector('#menuBtn');
 if(header&&panel&&toggle){
  const nav=document.createElement('nav');nav.className='mobile-nav';nav.dataset.i18nSkip='';
  const pages=[['index.html','หน้าแรก','Home'],['shop.html','เมนูและสินค้า','Shop'],['gift.html','ชุดของขวัญ','Gift sets'],['story.html','เรื่องของเรา','Our story'],['craft.html','วิธีทำข้าวตัง','Our craft'],['corporate.html','ของขวัญองค์กร','Corporate gifts'],['visit.html','หน้าร้านและติดต่อ','Visit us']];
  const active=location.pathname.split('/').pop()||'index.html';
  const render=()=>{
   const en=document.documentElement.lang==='en';
   nav.setAttribute('aria-label',en?'Main navigation':'เมนูหลัก');
   nav.innerHTML='<p class="mobile-nav-label">'+(en?'EXPLORE MAYUREE':'สำรวจมยุรี')+'</p>'+pages.map(([href,th,eng])=>'<a class="mobile-page-link" href="'+href+'"'+(active===href?' aria-current="page"':'')+'>'+(en?eng:th)+'</a>').join('')+'<div class="mobile-contact"><a href="https://lin.ee/xAbIkYZn" target="_blank" rel="noopener">'+(en?'Order on LINE':'สั่งทาง LINE')+'</a><a href="tel:0896666665">'+(en?'Call us':'โทรหาเรา')+'</a></div>';
  };
  panel.append(nav);render();toggle.setAttribute('aria-controls','mega-shop');
  const sync=()=>{
   const open=compactNav.matches&&panel.classList.contains('open');
   document.documentElement.classList.toggle('mobile-menu-open',open);
   toggle.setAttribute('aria-expanded',String(open));
   toggle.textContent=open?(document.documentElement.lang==='en'?'Close':'ปิด'):(document.documentElement.lang==='en'?'Menu':'เมนู');
   document.querySelectorAll('main,footer,.dock').forEach(el=>{el.inert=open});
  };
  new MutationObserver(sync).observe(panel,{attributes:true,attributeFilter:['class']});
  new MutationObserver(()=>{render();sync()}).observe(document.documentElement,{attributes:true,attributeFilter:['lang']});
  compactNav.addEventListener('change',()=>{if(!compactNav.matches&&panel.classList.contains('open'))toggle.click();sync()});sync();
  nav.addEventListener('click',e=>{if(e.target.closest('a')&&panel.classList.contains('open'))toggle.click()});
  addEventListener('keydown',e=>{
   if(!compactNav.matches||!panel.classList.contains('open'))return;
   if(e.key==='Escape'){e.preventDefault();toggle.click();toggle.focus()}
   if(e.key==='Tab'){
    const links=[...header.querySelectorAll('button,a')].filter(el=>el.getClientRects().length&&getComputedStyle(el).visibility!=='hidden'&&el.closest('.prod')===null);
    const first=links[0],last=links[links.length-1];
    if(e.shiftKey&&document.activeElement===first){e.preventDefault();last.focus()}
    else if(!e.shiftKey&&document.activeElement===last){e.preventDefault();first.focus()}
   }
  });
 }
 document.querySelectorAll('footer .links>div:not(:last-child) h5').forEach((heading,i)=>{
  const group=heading.parentElement,list=group.querySelector('ul');
  if(!list)return;list.id='footer-links-'+i;
  const sync=()=>{if(mobile.matches){heading.setAttribute('role','button');heading.tabIndex=0;heading.setAttribute('aria-controls',list.id);heading.setAttribute('aria-expanded',String(group.classList.contains('open')))}else{['role','tabindex','aria-controls','aria-expanded'].forEach(a=>heading.removeAttribute(a))}};
  heading.addEventListener('keydown',e=>{if(mobile.matches&&(e.key==='Enter'||e.key===' ')){e.preventDefault();heading.click()}});
  new MutationObserver(sync).observe(group,{attributes:true,attributeFilter:['class']});mobile.addEventListener('change',sync);sync();
 });
 document.querySelectorAll('.hm-qual-grid').forEach(grid=>{
  const controls=document.createElement('div');controls.className='photo-carousel-controls';controls.dataset.i18nSkip='';
  controls.innerHTML='<button type="button" aria-label="รูปก่อนหน้า">←</button><span aria-live="polite"></span><button type="button" aria-label="รูปถัดไป">→</button>';grid.after(controls);
  const [prev,next]=controls.querySelectorAll('button'),cards=[...grid.children];
  const step=()=>cards[0].getBoundingClientRect().width+parseFloat(getComputedStyle(grid).gap||0);
  const at=()=>Math.min(cards.length-1,Math.max(0,Math.round(grid.scrollLeft/step())));
  const update=()=>{prev.disabled=at()===0;next.disabled=at()===cards.length-1;controls.querySelector('span').textContent=(at()+1)+' / '+cards.length};
  const go=delta=>grid.scrollTo({left:step()*(at()+delta),behavior:matchMedia('(prefers-reduced-motion:reduce)').matches?'auto':'smooth'});
  prev.addEventListener('click',()=>go(-1));next.addEventListener('click',()=>go(1));grid.addEventListener('scroll',update,{passive:true});new ResizeObserver(update).observe(grid);update();
 });
 // Only the visible side determines the card height on phones.
 document.querySelectorAll('[data-product-deck]').forEach(deck=>{
  const track=deck.querySelector('.deck-track'),pages=[...deck.querySelectorAll('.deck-page')];
  const fit=()=>{if(compactNav.matches){const page=pages.find(p=>p.getAttribute('aria-hidden')!=='true')||pages[0];track.style.height=page.scrollHeight+'px'}else track.style.height=''};
  const resize=new ResizeObserver(fit);pages.forEach(page=>resize.observe(page));
  pages.forEach(page=>new MutationObserver(fit).observe(page,{attributes:true,attributeFilter:['aria-hidden']}));
  compactNav.addEventListener('change',fit);fit();
 });
 // Do not place a duplicate floating purchase button over the visible main action.
 const order=document.querySelector('#addBtn:not([hidden])');
 if(order&&order.tagName==='A')new IntersectionObserver(entries=>document.body.classList.toggle('primary-order-visible',entries[0].isIntersecting),{threshold:.15}).observe(order);
})();
