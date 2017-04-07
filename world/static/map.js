var map = new L.Map('map');
var ajaxRequest;
var plotlist;
var plotlayers = [];

function initmap() {

    // create the tile layer with correct attribution
    var osmUrl = 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
    //var osmAttrib = 'Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors';
    var osm = new L.TileLayer(osmUrl, {minZoom: 1, maxZoom: 100});

    // start the map in South-East England
    map.setView(new L.LatLng(51.3, 0.7), 1);
    map.addLayer(osm);
}

initmap();

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

function getCountriesList() {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", API("countries_geo"), true);
    xhr.send();
    xhr.onload = function () {
        var countries = JSON.parse(xhr.responseText);
        handleCountries(countries);
    }
}

// function drawBorders(c) {
//     var plg = L.geoJson(c, {
//         style: style,
//         onEachFeature: onEachFeature
//     }).addTo(map);
//     //plg.bindPopup(c.properties.name);
// }


function handleCountries(countries) {
    L.geoJson(countries, {
        style: style,
        onEachFeature: onEachFeature
    }).addTo(map);

}
getCountriesList();


/**
 * @return {string}
 */
function API(query) {
    var api_domain = 'http://localhost:8000/api/';
    return api_domain + query;
}
