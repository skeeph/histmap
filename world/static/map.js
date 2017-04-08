var map;
var ajaxRequest;
var plotlist;
var layers = [];

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

/**
 * Удаляет все объекты с карты
 */
function clearMap() {
    for (var i = 0; i < layers.length; i++) {
        layers[i].remove();
    }
    layers = [];
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

function getCountriesList(url, year) {
    if (!url) {
        url = API("countries_geo",year);
    }
    console.log(url);
    var xhr = new XMLHttpRequest();
    xhr.open("GET", url, true);
    xhr.send();
    xhr.onload = function () {
        var countries = JSON.parse(xhr.responseText);
        handleCountries(countries);
    }
}


/**
 * Отрисовка полученного массива стран и вызов функции получения следующий стран
 * @param {object} countries Geojson объекст стран
 */
function handleCountries(countries) {
    var c = L.geoJson(countries, {
        style: style,
        onEachFeature: onEachFeature
    }).addTo(map);
    layers.push(c);
    if (countries.next) {
        getCountriesList(countries.next);
    }
}


/**
 * Функция формирует адрес API
 * @param {string} query Что нужно от API
 * @param {int} year За какой год нужно получить данные
 * @return {string}
 */
function API(query, year) {
    var url = "http://localhost:8000/api/" + query + "/";
    if (year) {
        url = url + "?year=" + year;
    }
    return url;
}

var yearInput = document.querySelector("#year");
yearInput.addEventListener('change', function (e) {
    clearMap();
    getCountriesList(null, yearInput.value);
});

initmap();
getCountriesList(null,yearInput.value);