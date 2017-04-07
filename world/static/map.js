function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++ ) {
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

function getCountriesList() {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", API("countries"), true);
    xhr.send();
    xhr.onload = function () {
        var countries = JSON.parse(xhr.responseText);
        handleCountries(countries);
    }
}

function drawBorders(c) {
    var plg = L.geoJson(c,{style: style}).addTo(map);
    plg.bindPopup(c.properties.name);
}


function handleCountries(countries) {
    for (var i = 0; i < countries.features.length; i++) {
        var c = countries.features[i];
        drawBorders(c);
    }

}

/**
 * @return {string}
 */
function API(query) {
    var api_domain = 'http://localhost:8000/api/';
    return api_domain + query;
}

getCountriesList();