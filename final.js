// Espera a que el documento HTML se haya cargado completamente
document.addEventListener("DOMContentLoaded", function() {
    // Inicializar el mapa y establecer la ubicación y el nivel de zoom
    var map = L.map('map').setView([0, 0], 13); // La ubicación inicial se establece en latitud 0 y longitud 0

    // Añadir una capa de mapa de OpenStreetMap al mapa
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    // Obtener la ubicación del usuario utilizando la API de geolocalización del navegador
    if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition(function(position) {
            // Obtener las coordenadas de latitud y longitud del usuario
            var lat = position.coords.latitude;
            var lon = position.coords.longitude;

            // Centrar el mapa en la ubicación del usuario y añadir un marcador
            map.setView([lat, lon], 13);
            var marker = L.marker([lat, lon]).addTo(map);

            // Añadir un mensaje emergente al marcador
            marker.bindPopup("<b>Aquí Tu ubicación actual</b>").openPopup();
            //alert("Latitud: " + lat + "\nLongitud: " + lon);
            var fixedMarker = L.marker([-30.904860, -55.544553]).addTo(map);
            fixedMarker.bindPopup("<b>Ubicación fija de referencia</b>").openPopup();
        });
    } else {
        // Si la geolocalización no está disponible en el navegador, muestra un mensaje de error
        alert("Geolocalización no disponible en este navegador.");
    }

    // Añadir un marcador fijo en una ubicación específica (por ejemplo, latitud -34.9055 y longitud -56.1915)
    var fixedMarker = L.marker([-30.904860, -55.544553]).addTo(map);
    fixedMarker.bindPopup("<b>Ubicación fija de referencia</b>").openPopup();
});
