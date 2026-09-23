/* Psyclopédia — service worker minimal.
   Il rend le site installable et affiche les alertes de cours.
   Il ne met pas les pages en cache : le contenu reste celui du serveur. */
self.addEventListener("install", function (event) {
  event.waitUntil(self.skipWaiting());
});

self.addEventListener("activate", function (event) {
  event.waitUntil(self.clients.claim());
});

self.addEventListener("notificationclick", function (event) {
  event.notification.close();
  var href = (event.notification.data && event.notification.data.href) || "./index.html";
  event.waitUntil(
    self.clients.matchAll({ type: "window", includeUncontrolled: true }).then(function (list) {
      for (var i = 0; i < list.length; i++) {
        if ("focus" in list[i]) {
          if (typeof list[i].navigate === "function") list[i].navigate(href);
          return list[i].focus();
        }
      }
      if (self.clients.openWindow) return self.clients.openWindow(href);
      return null;
    })
  );
});
