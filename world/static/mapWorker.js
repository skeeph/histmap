/**
 * Функция формирует адрес API
 * @param {string} query Что нужно от API
 * @param {int} year За какой год нужно получить данные
 * @return {string}
 */
function API(query, year) {
    var url = "https://geo.khabib.me/api/" + query + "/";
    if (year) {
        url = url + "?year=" + year;
    }
    return url;
}


/**
 * Отрисовка полученного массива стран и вызов функции получения следующий стран
 * @param {object} countries Geojson объекст стран
 */
function handleCountries(countries) {
    postMessage(JSON.stringify(countries));
    if (countries.next) {
        // FIXME: Убрать лютый костыль. Сделать так чтобы DRF по умолчанию возвращал https
        getCountriesList(countries.next.replace("http://", "https://"));
    } else {
        close();
    }
}

function getCountriesList(url, year) {
    if (!url) {
        url = API("countries_geo", year);
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

onmessage = function (e) {
    year = e.data;
    getCountriesList(null, year)
};

