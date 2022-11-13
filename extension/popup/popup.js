document.addEventListener('DOMContentLoaded', function () {

    var btn = document.getElementById('world_button');
    btn.addEventListener('click', function() {
        console.log("Clicked")
        var newURL = "https://www.geoguessr.com/maps/world/play";
        chrome.tabs.create({ url: newURL });
    });
});