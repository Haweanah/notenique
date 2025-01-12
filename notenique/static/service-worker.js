const cacheName = "notenique-cache-v1";
const assets = [
  "/",
  "/static/css/bootstrap.min.css",
  "/static/js/script.js",
  "/static/icons/icon-192x192.png",
  "/static/icons/icon-512x512.png"
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(cacheName).then((cache) => {
      return cache.addAll(assets);
    })
  );
});

self.addEventListener("fetch", (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request);
    })
  );
});