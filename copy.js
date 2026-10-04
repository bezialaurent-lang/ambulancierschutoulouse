const fs = require('fs');
fs.copyFileSync(
    "article de presse/Grève des ambulanciers du CHU de Toulouse _ « À l'hôpital ou à Airbus, c'est l'ouvrier qui trinque ! ».pdf",
    "blog/media/Grève des ambulanciers du CHU de Toulouse _ « À l'hôpital ou à Airbus, c'est l'ouvrier qui trinque ! ».pdf"
);
console.log("Copied!");
