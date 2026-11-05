/* SVG UI icons stay consistent across platforms and never invoke an emoji font. */
(() => {
  const paths = {
    '↗': 'M5 19 19 5M5 5h14v14',
    '›': 'm9 5 7 7-7 7',
    '←': 'M20 12H4m7-7-7 7 7 7',
    '→': 'M4 12h16m-7-7 7 7-7 7',
    '▶': 'm8 5 11 7-11 7Z',
    '★': 'm12 3 2.8 5.8 6.4.9-4.6 4.5 1.1 6.4-5.7-3-5.7 3 1.1-6.4L2.8 9.7l6.4-.9Z',
    '✓': 'm5 12 4 4L19 6',
    '✦': 'm12 2 2.5 7.5L22 12l-7.5 2.5L12 22l-2.5-7.5L2 12l7.5-2.5Z'
  };
  function make(char) {
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.setAttribute('class', 'ui-icon' + ('★▶✦'.includes(char) ? ' ui-icon-solid' : ''));
    svg.setAttribute('viewBox', '0 0 24 24');
    svg.setAttribute('aria-hidden', 'true');
    svg.setAttribute('focusable', 'false');
    svg.dataset.i18nSkip = '';
    const path = document.createElementNS(svg.namespaceURI, 'path');
    path.setAttribute('d', paths[char]);
    svg.append(path);
    return svg;
  }
  function decorate(root) {
    if (!root || root.nodeType !== 1) return;
    const walk = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    const nodes = [];
    while (walk.nextNode()) {
      const node = walk.currentNode;
      if (!node.parentElement.closest('script,style,svg,textarea,input') &&
          [...node.data].some(char => paths[char])) nodes.push(node);
    }
    for (const node of nodes) {
      const fragment = document.createDocumentFragment();
      let text = '';
      for (const char of node.data) {
        if (paths[char]) {
          if (text) { fragment.append(document.createTextNode(text)); text = ''; }
          fragment.append(make(char));
        } else text += char;
      }
      if (text) fragment.append(document.createTextNode(text));
      node.replaceWith(fragment);
    }
  }
  decorate(document.body);
  new MutationObserver(records => {
    const roots = new Set();
    for (const record of records) {
      if (record.type === 'characterData') roots.add(record.target.parentElement);
      else for (const node of record.addedNodes) roots.add(node.nodeType === 1 ? node : node.parentElement);
    }
    roots.forEach(decorate);
  }).observe(document.body, {childList: true, characterData: true, subtree: true});
})();
