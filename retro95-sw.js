const PREFIX = 'retro95-workstation:' + self.registration.scope + ':';
const CACHE = PREFIX + 'hardened-v2';
const FILES = ['./', './index.html', './windows95.html', './retro95-manifest.json', './retro95-icon.png', './retro95-icon-512.png'];
const ALLOWED = new Set(FILES.map(path => new URL(path, self.registration.scope).href));
self.addEventListener('install', e => e.waitUntil(caches.open(CACHE).then(c => c.addAll(FILES)).then(() => self.skipWaiting())));
self.addEventListener('activate', e => e.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k.startsWith(PREFIX) && k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim())));
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET' || !ALLOWED.has(e.request.url)) return;
  e.respondWith((async () => {
    const cache = await caches.open(CACHE);
    try {
      const response = await fetch(e.request, {redirect:'error'});
      if (response.ok && response.type === 'basic') await cache.put(e.request, response.clone()).catch(() => {});
      return response;
    } catch {
      return (await cache.match(e.request)) || Response.error();
    }
  })());
});
