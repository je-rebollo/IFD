{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/je-rebollo/IFD/blob/main/ifd004.js\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "KFx7ra6A2EGw"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "const fullImageContainer = document.querySelector('.full-image-container');\n",
        "\n",
        "async function cargarLeafletYMapa() {\n",
        "  await cargarLeaflet(); // Suponiendo que esta función carga Leaflet de forma asíncrona\n",
        "  // Ahora que Leaflet está cargado, inicializamos el mapa\n",
        "  var map = L.map('map').setView([lat, lon], zoom);\n",
        "  // Añadir la capa de tiles y otros elementos del mapa aquí\n",
        "}\n",
        "\n",
        "cargarLeafletYMapa();\n",
        "\n",
        "var tileLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {\n",
        "  maxZoom: 19,\n",
        "  attribution: '© OpenStreetMap contributors'\n",
        "}).addTo(map);\n",
        "\n",
        "tileLayer.on('load', function inicializarMapa(lat, lon, zoom) {\n",
        "  var map = L.map('map').setView([lat, lon], zoom);\n",
        "  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {\n",
        "      maxZoom: 19,\n",
        "      attribution: '© OpenStreetMap contributors'\n",
        "  }).addTo(map);\n",
        "  return map;\n",
        "  console.log('Todas las losetas visibles han sido cargadas');\n",
        "});\n",
        "\n",
        "\n",
        "function inicializarMapa(lat, lon, zoom) {\n",
        "  var map = L.map('map').setView([lat, lon], zoom);\n",
        "  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {\n",
        "      maxZoom: 19,\n",
        "      attribution: '© OpenStreetMap contributors'\n",
        "  }).addTo(map);\n",
        "  return map;\n",
        "}\n",
        "\n",
        "// Manejador de eventos para cargar el menú\n",
        "document.addEventListener('DOMContentLoaded', function() {\n",
        "  fetch('index3.html')\n",
        "      .then(response => response.text())\n",
        "      .then(data => {\n",
        "          document.getElementById('menu').innerHTML = data;\n",
        "      });\n",
        "\n",
        "  // Inicializar el mapa con la ubicación por defecto\n",
        "  var map = inicializarMapa(0, 0, 13);\n",
        "\n",
        "  // Geolocalización y manejo de miniaturas aquí...\n",
        "});\n",
        "\n",
        "// Función para abrir nuevas ventanas\n",
        "function abrirNuevaVentana(url) {\n",
        "  window.open(url, \"_blank\");\n",
        "}\n",
        "\n",
        "// Función para manejar clics en miniaturas\n",
        "function manejarClicMiniatura(thumbnail) {\n",
        "  thumbnail.addEventListener('click', function() {\n",
        "      document.getElementById('full-image').src = this.src;\n",
        "      document.getElementById('imageModal').style.display = 'flex';\n",
        "  });\n",
        "}\n",
        "\n",
        "// Agregar manejadores de eventos a las categorías\n",
        "const categorias = [document.getElementById(\"categoria1\"), document.getElementById(\"categoria2\"), document.getElementById(\"categoria3\")];\n",
        "categorias.forEach((categoria, index) => {\n",
        "  categoria.addEventListener(\"click\", function() {\n",
        "      abrirNuevaVentana(`https://ejemplo.com/servicio${index + 1}`);\n",
        "  });\n",
        "});\n",
        "\n",
        "// Agregar manejadores de eventos a las miniaturas\n",
        "const thumbnails = document.querySelectorAll('.thumbnails img');\n",
        "thumbnails.forEach(manejarClicMiniatura);\n",
        "\n",
        "// Manejador para cerrar el modal de imagen completa\n",
        "document.getElementById('closeModal').addEventListener('click', function() {\n",
        "  document.getElementById('imageModal').style.display = 'none';\n",
        "});"
      ],
      "metadata": {
        "id": "bnRF3dYW2bya"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}