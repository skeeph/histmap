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
    var plg = L.geoJson(c).addTo(map);
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