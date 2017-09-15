var map;
var ajaxRequest;
var plotlist;
var layers = [];
var w;


function initmap() {
    map = new L.Map('map');
    // create the tile layer with correct attribution
    var osmUrl = 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
    //var osmAttrib = 'Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors';
    var osm = new L.TileLayer(osmUrl, {minZoom: 1, maxZoom: 100});

    // start the map in South-East England
    map.setView(new L.LatLng(51.3, 0.7), 1);
    map.addLayer(osm);
}

function style(feature) {
    return {
        fillColor: getRandomColor(),
        weight: 2,
        opacity: 1,
        color: 'white',
        dashArray: '3',
        fillOpacity: 0.7
    };
}

function onEachFeature(feature, layer) {
    layer.on({
        'click': function (e) {
            var popup = L.popup()
                .setLatLng([e.latlng.lat, e.latlng.lng])
                .setContent(feature.properties.name)
                .openOn(map);

        }
    });
}

/**
 * Генерирует случайный цвет в формате rgb
 * @return {string} Цвет
 */
function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}


/**
 * Удаляет все объекты с карты
 */
function clearMap() {
    for (var i = 0; i < layers.length; i++) {
        layers[i].remove();
    }
    layers = [];
}

function handleWebWorker(jsonstr) {
    var countries = JSON.parse(jsonstr);
    var c = L.geoJson(countries, {
        style: style,
        onEachFeature: onEachFeature
    }).addTo(map);
    layers.push(c);
}

var yearInput = document.querySelector("#year");
yearInput.addEventListener('change', function (e) {
    clearMap();
    w.terminate();
    w = undefined;
    startWebWorker(yearInput.value);
});

initmap();
function startWebWorker(year){
    w = new Worker('/gstatic/mapWorker.js');
    w.postMessage(year);
    w.onmessage = function (event) {
        handleWebWorker(event.data)
    };
}
startWebWorker(2000);