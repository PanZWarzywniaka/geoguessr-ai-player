window.addEventListener("load", main, false);

function main (evt) {

    console.log("Page was loaded ");

    function hide (class_name) {
        var els = document.getElementsByClassName(class_name);
        for(var i=0; i<els.length; i++) {
            console.log("Hiding: ",els[i])
            els[i].style.display = 'none';
        }
        
    }

    hide("game-layout__controls");
    hide("game-layout__status");
    hide("gmnoprint");
    hide("gm-style-cc");
    hide("guess-map guess-map--size-3");
    hide("guess-map__canvas-container");
    hide("guess-map__guess-button");
    hide("game-layout__guess-map");
    hide("guess-map");
    hide("guess-map__canvas-container");

}
