let link = document.getElementById("link");
if (link)
    link.href = location.href.replaceAll(
        /[^\/]*\.replit\.dev/g,
        "pickaxe.showierdata.xyz"
    );