(() => {
  const home = document.body.classList.contains('home-page');
  const header = document.querySelector('#header');
  if (home && header) {
    let pending = false;
    const updateHeader = () => { header.classList.toggle('is-framed', window.scrollY > 32); pending = false; };
    addEventListener('scroll', () => { if (!pending) { pending = true; requestAnimationFrame(updateHeader); } }, {passive:true});
    updateHeader();
  }
  document.querySelectorAll('[data-product-deck]').forEach(deck => {
    const track = deck.querySelector('.deck-track');
    const pages = [...deck.querySelectorAll('.deck-page')];
    const prev = deck.querySelector('[data-deck-prev]');
    const next = deck.querySelector('[data-deck-next]');
    const tabs = [...deck.querySelectorAll('[data-deck-to]')];
    let index = 0;
    const english = () => document.documentElement.lang === 'en';
    const labels = () => english() ? ['Choose products', 'Product details'] : ['เลือกสินค้า', 'รายละเอียดสินค้า'];
    const render = () => {
      const names = labels();
      deck.querySelector('.deck-title').textContent = names[index];
      tabs.forEach((button, i) => { button.textContent = names[i]; button.classList.toggle('on', i === index); button.setAttribute('aria-selected', String(i === index)); });
      pages.forEach((page, i) => { page.inert = i !== index; page.setAttribute('aria-hidden', String(i !== index)); });
      prev.disabled = index === 0; next.disabled = index === pages.length - 1;
      prev.setAttribute('aria-label', english() ? 'Previous page' : 'หน้าก่อนหน้า');
      next.setAttribute('aria-label', english() ? 'Next page' : 'หน้าถัดไป');
    };
    const go = (to, instant=false) => {
      index = Math.max(0, Math.min(pages.length-1, to));
      render();
      track.scrollTo({left:track.clientWidth*index, behavior:instant || matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth'});
    };
    prev.addEventListener('click', () => go(index-1));
    next.addEventListener('click', () => go(index+1));
    tabs.forEach((button, i) => button.addEventListener('click', () => go(i)));
    track.addEventListener('keydown', e => { if (e.key === 'ArrowLeft' || e.key === 'ArrowRight') { e.preventDefault(); go(index+(e.key === 'ArrowRight' ? 1 : -1)); } });
    track.addEventListener('scroll', () => { const value = Math.round(track.scrollLeft/track.clientWidth); if(value !== index) { index=value; render(); } }, {passive:true});
    new ResizeObserver(() => go(index,true)).observe(track);
    new MutationObserver(render).observe(document.documentElement,{attributes:true,attributeFilter:['lang']});
    render();
  });
  document.querySelectorAll('.gift-overview .gift-grid').forEach(grid => {
    const cards = [...grid.querySelectorAll('.gset')];
    const controls = document.createElement('div');
    controls.className = 'gift-carousel-controls';
    controls.innerHTML = '<button type="button" aria-label="ชุดของขวัญก่อนหน้า">←</button><span aria-live="polite"></span><button type="button" aria-label="ชุดของขวัญถัดไป">→</button>';
    grid.insertAdjacentElement('afterend', controls);
    const [prev, next] = controls.querySelectorAll('button');
    const step = () => cards[0].getBoundingClientRect().width + parseFloat(getComputedStyle(grid).gap || 0);
    const current = () => Math.max(0,Math.min(cards.length-1,Math.round(grid.scrollLeft/step())));
    const update = () => { const at=current(); prev.disabled=at===0; next.disabled=at===cards.length-1; controls.querySelector('span').textContent=(at+1)+' / '+cards.length; };
    const go = direction => grid.scrollTo({left:step()*(current()+direction),behavior:matchMedia('(prefers-reduced-motion:reduce)').matches?'auto':'smooth'});
    prev.addEventListener('click',()=>go(-1)); next.addEventListener('click',()=>go(1));
    grid.addEventListener('scroll',update,{passive:true});
    grid.addEventListener('keydown', e => { if (e.key==='ArrowLeft'||e.key==='ArrowRight') {e.preventDefault();go(e.key==='ArrowRight'?1:-1);} });
    new ResizeObserver(update).observe(grid);update();
  });
})();
