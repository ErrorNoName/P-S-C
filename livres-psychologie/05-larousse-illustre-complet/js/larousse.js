// Larousse Psychologie — interactions ludiques
document.addEventListener('DOMContentLoaded', () => {
  // Animation d'entrée des cartes
  document.querySelectorAll('.cat-card, .section-card, .dict-item').forEach((el, i) => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(12px)';
    el.style.transition = `opacity 0.4s ${i * 0.05}s, transform 0.4s ${i * 0.05}s`;
    requestAnimationFrame(() => {
      el.style.opacity = '1';
      el.style.transform = 'translateY(0)';
    });
  });

  // Filtrage dictionnaire par lettre (si barre présente)
  const dictItems = document.querySelectorAll('.dict-item');
  if (dictItems.length > 20) {
    const letters = [...new Set([...dictItems].map(d => d.dataset.letter))].sort();
    const bar = document.createElement('div');
    bar.className = 'alpha-bar';
    bar.innerHTML = letters.map(l => `<button data-l="${l}">${l}</button>`).join('') +
      '<button data-l="ALL">Tout</button>';
    bar.style.cssText = 'display:flex;flex-wrap:wrap;gap:0.25rem;margin-bottom:1rem';
    dictItems[0].parentElement.insertBefore(bar, dictItems[0]);
    bar.querySelectorAll('button').forEach(btn => {
      btn.style.cssText = 'padding:0.3rem 0.6rem;border:1px solid #CBD5E0;background:white;border-radius:4px;cursor:pointer';
      btn.onclick = () => {
        const l = btn.dataset.l;
        dictItems.forEach(d => {
          d.style.display = (l === 'ALL' || d.dataset.letter === l) ? '' : 'none';
        });
      };
    });
  }
});
