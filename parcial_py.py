{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMFCpS7vMH9/hxuxvgnAhmO",
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
        "<a href=\"https://colab.research.google.com/github/je-rebollo/IFD/blob/main/parcial_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def error ():\n",
        "  a = input (\"ingrese valor\")\n",
        "  a = int(a)+1\n",
        "\n",
        "try :\n",
        "  error()\n",
        "\n",
        "\n",
        "except Exception as e:\n",
        "  print(mensajes_error.get(str(e)))\n",
        "else:\n",
        "  print(\"no hubo error\")\n",
        "finally:\n",
        "  print(\"siempre se ejecuta\")\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zJuOAF8OsZIy",
        "outputId": "517c26fe-a02a-4dbb-faf1-b1133c21ff0f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "ingrese valory6y6\n",
            "None\n",
            "siempre se ejecuta\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "4Z9S9wfzfEz8",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "eda1b88d-1056-4eaf-aadc-25ceffa2b4b3"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "No se puede dividir un número entre cero. division by zero\n",
            "Execution finished.\n"
          ]
        }
      ],
      "source": [
        "\n",
        "mensajes_error = {\n",
        "    \"division by zero\": \"No se puede dividir un número entre cero.\",\n",
        "    \"invalid literal for int() with base 10: 'abc'\": \"No se puede convertir la cadena 'abc' a un número entero.\",\n",
        "    \"list index out of range\": \"Se intentó acceder a una posición que no existe en la lista.\",\n",
        "    \"'NoneType' object has no attribute 'upper'\": \"Se intentó usar un método en un objeto que es None.\",\n",
        "    \"'dict' object has no attribute 'append'\": \"Se intentó usar un método que no existe para diccionarios.\",\n",
        "    \"'int' object is not iterable\": \"Se intentó iterar sobre un número entero, lo cual no es posible.\",\n",
        "    \"unsupported operand type(s) for +: 'int' and 'str'\": \"No se puede sumar un número y una cadena.\",\n",
        "    \"cannot import name 'x' from 'y'\": \"No se pudo importar un nombre específico desde un módulo.\",\n",
        "    \"No module named 'modulo_inexistente'\": \"El módulo que se intenta importar no existe.\",\n",
        "    \"[Errno 2] No such file or directory: 'archivo.txt'\": \"El archivo especificado no fue encontrado.\",\n",
        "}\n",
        "\n",
        "errores = {\n",
        "    \"SyntaxError\": \"Error de sintaxis: el código no sigue las reglas del lenguaje Python.\",\n",
        "    \"NameError\": \"Error de nombre: se intenta usar una variable que no ha sido definida.\",\n",
        "    \"TypeError\": \"Error de tipo: se realiza una operación con tipos de datos incompatibles.\",\n",
        "    \"ValueError\": \"Error de valor: el tipo de dato es correcto, pero el valor no es apropiado.\",\n",
        "    \"IndexError\": \"Error de índice: se accede a una posición que no existe en una secuencia.\",\n",
        "    \"KeyError\": \"Error de clave: se intenta acceder a una clave inexistente en un diccionario.\",\n",
        "    \"AttributeError\": \"Error de atributo: se intenta usar un atributo o método que no existe para un objeto.\",\n",
        "    \"ZeroDivisionError\": \"Error de división por cero: se intenta dividir un número entre cero.\",\n",
        "    \"ImportError\": \"Error de importación: no se puede importar un módulo o componente.\",\n",
        "    \"ModuleNotFoundError\": \"Módulo no encontrado: el módulo que se intenta importar no existe.\",\n",
        "    \"FileNotFoundError\": \"Archivo no encontrado: se intenta abrir un archivo que no existe.\",\n",
        "    \"IndentationError\": \"Error de indentación: el código no está correctamente indentado.\",\n",
        "    \"RuntimeError\": \"Error de ejecución: ocurre un error genérico durante la ejecución.\",\n",
        "    \"StopIteration\": \"Fin de iteración: un iterador no tiene más elementos.\",\n",
        "    \"MemoryError\": \"Error de memoria: el programa ha agotado la memoria disponible.\",\n",
        "    \"OverflowError\": \"Desbordamiento: un número es demasiado grande para ser representado.\"\n",
        "}\n",
        "def prueba():\n",
        "  valor = 10 / 0\n",
        "  return valor\n",
        "\n",
        "try:\n",
        "    lista=[]\n",
        "    # Code that might raise an exception\n",
        "    prueba()\n",
        "    print(lista[1])\n",
        "    prueba()\n",
        "except Exception as e:    # Code to handle the exception\n",
        "    print(mensajes_error.get(str(e)), e)\n",
        "finally:\n",
        "    # Code that always runs, regardless of whether an exception occurred\n",
        "    print(\"Execution finished.\")\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "genero = (\"ficción\", \"históricas\", \"fantasía\", \"misterio\", \"romance\", \"thrillers\", \"Poesía\")\n",
        "# libro {nombre, autor, genero, copias, sit , espera[])}\n",
        "libros = {}\n",
        "libros[\"l1\"] ={nombre:\"hp\", autor:\"pepe\", genero:\"históricas\", copias:3, prestado:False , espera[]}\n",
        "# CI, Nombre , teléfono , ciudad\n",
        "usuarios = {}\n",
        "usuarios[11] = (\"Juan\", \"098000011\", \"Rivera\")\n",
        "# fecha {dia, mes, año}\n",
        "# fecha prestamos, fecha devolución, estado (t / F) , libros, usuarios\n",
        "prestamo = []\n",
        "prestamos = []\n",
        "prestamo.append({dia:1, mes:12, año:2025})\n",
        "prestamo.append(0)\n",
        "prestamo.append(False)\n",
        "prestamo.append(\"a1\")\n",
        "prestamo.append(11)\n",
        "\n",
        "prestamos.append(prestamo)\n",
        "\n",
        "# pila código del libro\n",
        "pila_reparacion = []\n",
        "cola_reparacion.append(\"a1\")\n"
      ],
      "metadata": {
        "id": "qunoRZmJfVqd",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 106
        },
        "outputId": "24584bdd-de0b-45c8-d7c2-e97e957abfb3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "':' expected after dictionary key (ipython-input-1582029037.py, line 4)",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"/tmp/ipython-input-1582029037.py\"\u001b[0;36m, line \u001b[0;32m4\u001b[0m\n\u001b[0;31m    libros[\"l1\"] ={nombre:\"hp\", autor:\"pepe\", genero:\"históricas\", copias:3, prestado:False , espera[]}\u001b[0m\n\u001b[0m                                                                                                   ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m ':' expected after dictionary key\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "genero = (\"ficción\", \"históricas\", \"fantasía\", \"misterio\", \"romance\", \"thrillers\", \"Poesía\")\n",
        "\n",
        "usuarios = { 101 :  [ \"Ana Pérez\", \"091123456\", \"Montevideo\"],\n",
        "    102:  [\"Luis Gómez\", \"092234567\", \"Rivera\"],\n",
        "    103: [ \"Sofía Rodríguez\",  \"093345678\",  \"Salto\"],\n",
        "    104: [ \"Carlos Díaz\",  \"094456789\",  \"Paysandú\"],\n",
        "    105: [ \"Javier López\",  \"095567890\",  \"Rivera\"],\n",
        "    106: [ \"Marta Fernández\",  \"096678901\",  \"Montevideo\"],\n",
        "    107: [ \"Pedro Benítez\",  \"097789012\",  \"Salto\"],\n",
        "    108: [ \"María Castro\",  \"098890123\",  \"Paysandú\"],\n",
        "    109: [ \"Elena Garcés\",  \"099901234\",  \"Rivera\"],\n",
        "    110: [ \"Jorge Vázquez\",  \"091112345\",  \"Montevideo\"],\n",
        "}\n",
        "\n",
        "libros = {\n",
        "    \"L001\": {\n",
        "        \"nombre\": \"El Código Da Vinci\", \"autor\": \"Dan Brown\", \"genero\": \"thrillers\", \"copias\": 3, \"en_mantenimiento\": False, \"lista_espera\": [107]\n",
        "    },\n",
        "    \"L002\": {\n",
        "        \"nombre\": \"Cien Años de Soledad\", \"autor\": \"Gabriel García Márquez\", \"genero\": \"ficción\", \"copias\": 1, \"en_mantenimiento\": False, \"lista_espera\": [101, 102]\n",
        "    },\n",
        "    \"L003\": {\n",
        "        \"nombre\": \"1984\",\n",
        "        \"autor\": \"George Orwell\",\n",
        "        \"genero\": \"ficción\",\n",
        "        \"copias\": 4,\n",
        "        \"en_mantenimiento\": False,\n",
        "        \"lista_espera\": []\n",
        "    },\n",
        "    \"L000\": {\n",
        "        \"nombre\": \"Crimen y Castigo\",\n",
        "        \"autor\": \"Fiódor Dostoievski\",\n",
        "        \"genero\": \"históricas\",\n",
        "        \"copias\": 2,\n",
        "        \"en_mantenimiento\": True,\n",
        "        \"lista_espera\": []\n",
        "    },\n",
        "    \"L005\": {\n",
        "        \"nombre\": \"Orgullo y Prejuicio\",\n",
        "        \"autor\": \"Jane Austen\",\n",
        "        \"genero\": \"romance\",\n",
        "        \"copias\": 2,\n",
        "        \"en_mantenimiento\": False,\n",
        "        \"lista_espera\": []\n",
        "    },\n",
        "    \"L006\": {\n",
        "        \"nombre\": \"El Señor de los Anillos2\",\n",
        "        \"autor\": \"J.R.R. Tolkien\",\n",
        "        \"genero\": \"fantasía\",\n",
        "        \"copias\": 5,\n",
        "        \"en_mantenimiento\": False,\n",
        "        \"lista_espera\": []\n",
        "    },\n",
        "    \"L106\": {\n",
        "        \"nombre\": \"El Señor de los Anillos2\",\n",
        "        \"autor\": \"J.R.R. Tolkien\",\n",
        "        \"genero\": \"fantasía\",\n",
        "        \"copias\": 5,\n",
        "        \"en_mantenimiento\": False,\n",
        "        \"lista_espera\": []\n",
        "    },\n",
        "    \"L116\": {\n",
        "        \"nombre\": \"El Señor de los Anillos\",\n",
        "        \"autor\": \"J.R.R. Tolkien\",\n",
        "        \"genero\": \"fantasía\",\n",
        "        \"copias\": 5,\n",
        "        \"en_mantenimiento\": False,\n",
        "        \"lista_espera\": []\n",
        "    },\n",
        "    \"L007\": {\n",
        "        \"nombre\": \"Un Mundo Feliz\",\n",
        "        \"autor\": \"Aldous Huxley\",\n",
        "        \"genero\": \"ficción\",\n",
        "        \"copias\": 2,\n",
        "        \"en_mantenimiento\": False,\n",
        "        \"lista_espera\": []\n",
        "    },\n",
        "    \"L008\": {\n",
        "        \"nombre\": \"Don Quijote de la Mancha\",\n",
        "        \"autor\": \"Miguel de Cervantes\",\n",
        "        \"genero\": \"ficción\",\n",
        "        \"copias\": 1,\n",
        "        \"en_mantenimiento\": False,\n",
        "        \"lista_espera\": [103, 101]\n",
        "    },\n",
        "    \"L009\": {\n",
        "        \"nombre\": \"El Hobbit\",\n",
        "        \"autor\": \"J.R.R. Tolkien\",\n",
        "        \"genero\": \"fantasía\",\n",
        "        \"copias\": 3,\n",
        "        \"en_mantenimiento\": False,\n",
        "        \"lista_espera\": []\n",
        "    },\n",
        "    \"L010\": {\n",
        "        \"nombre\": \"Harry Potter y la Piedra Filosofal\",\n",
        "        \"autor\": \"J.K. Rowling\",\n",
        "        \"genero\": \"fantasía\",\n",
        "        \"copias\": 4,\n",
        "        \"en_mantenimiento\": True,\n",
        "        \"lista_espera\": [104, 109]\n",
        "    }\n",
        "}\n",
        "prestamos = [((1, 12, 2025), 0, False , \"L010\", 101 ), ((12, 11, 2025), 0, True , \"L009\", 103 ),\n",
        "             ((1, 3, 2025), 0, False , \"L005\", 101 ),\n",
        "             ((19, 12, 2025), 0, False , \"L005\", 102 )]"
      ],
      "metadata": {
        "id": "EZ-YGk33se5n"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "p1=[\"hola\"]\n",
        "if not p1 :\n",
        "  print(\"lista vacia\")\n",
        "else:\n",
        "  print(\"lista no vacia\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IVTaknxppn7g",
        "outputId": "fb74d23a-5959-4ffa-90c6-4906426ba064"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "lista no vacia\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "mes = 1.0\n",
        "type(mes)\n",
        "if mes in (1,2,3,4,5,6,7,8,9,10,11,12):\n",
        "  print(mes)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dkXlizBDcOhV",
        "outputId": "a0341aa4-16a2-4388-bf34-d08be1b2ab88"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "j = [t for t in usuarios.keys()]\n",
        "print(j)\n",
        "for i in usuarios.keys():\n",
        "  print(i)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FbUvJS2vMDaf",
        "outputId": "5100f8d3-1388-469d-8fd9-fd4616563d62"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[101, 102, 103, 104, 105, 106, 107, 108, 109, 110]\n",
            "101\n",
            "102\n",
            "103\n",
            "104\n",
            "105\n",
            "106\n",
            "107\n",
            "108\n",
            "109\n",
            "110\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# mostrar todos los libros de un genero\n",
        "# entrada colección libros, un género valido\n",
        "def mostrar_libros(l, gen):\n",
        "    for c, v in l.items():\n",
        "        print(c, v.get(\"nombre\"), \"-\", v.get(\"autor\"))\n",
        "\n",
        "# Contar cuántos pedidos de libros están en espera.\n",
        "def contar_esperas (l):\n",
        "    suma = 0\n",
        "    for i in l:\n",
        "      #(código faltante)\n",
        "      None\n",
        "    return suma\n",
        "\n",
        "# Contar cuantos usuarios están esperando libros\n",
        "# Se crea una lista con la suma de todas las listas de espera\n",
        "def contar_usuarios_espera (l):\n",
        "  aux=[]\n",
        "  for i in l:\n",
        "    aux = aux + l[i][\"lista_espera\"]\n",
        "  resultado = set(aux)\n",
        "  print(aux, resultado)\n",
        "\n",
        "  return len(resultado)\n",
        "\n",
        "def contar_usuarios_no_espera (l , us):\n",
        "  aux=[]\n",
        "  for i in l:\n",
        "    aux = aux + l[i][\"lista_espera\"]\n",
        "  espera = set(aux)\n",
        "  ci = set(us.keys())\n",
        "  resultado = ci-espera\n",
        "  return len(resultado)\n",
        "\n",
        "def lista_autores(l):\n",
        "  aux = []\n",
        "  for i in l:\n",
        "    aux.append(l[i][\"autor\"])\n",
        "  return set(aux)\n",
        "\n",
        "def contar_esperas_us (l, us):\n",
        "  suma = 0\n",
        "  for i in l:\n",
        "    for j in l[i][\"lista_espera\"]:\n",
        "      if j == us:\n",
        "        suma = suma + 1\n",
        "  return suma\n",
        "def contar_esperas_lib (l, lib):\n",
        "  return len(l[lib][\"lista_espera\"])\n",
        "\n",
        "def contar_mis_pendientes (l, ci):\n",
        "  suma = 0\n",
        "  for i in l:\n",
        "    for j in l[i][\"lista_espera\"]:\n",
        "      if j == ci:\n",
        "        suma = suma + 1\n",
        "  return suma\n",
        "def solicitud_por_us (lib, us):\n",
        "  aux = {}\n",
        "  for i in us:\n",
        "    aux[i] = contar_mis_pendientes(lib, i)\n",
        "  return aux\n",
        "\n",
        "def solicitud_por_lib (l, c):\n",
        "  aux = {}\n",
        "  for i in l:\n",
        "    for j in l[i][\"lista_espera\"]:\n",
        "      if j == c:\n",
        "        aux[i] = l[i]\n",
        "  return aux\n",
        "solicitud_por_us(libros, usuarios)"
      ],
      "metadata": {
        "id": "mVb-0jnJzNQh",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "b0937de1-5d21-4233-820a-eac0c0b7f7fa"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{101: 2,\n",
              " 102: 1,\n",
              " 103: 1,\n",
              " 104: 1,\n",
              " 105: 0,\n",
              " 106: 0,\n",
              " 107: 1,\n",
              " 108: 0,\n",
              " 109: 1,\n",
              " 110: 0}"
            ]
          },
          "metadata": {},
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "print(\"lista autores\", len(lista_autores(libros)))\n",
        "print(\"libros en espera\", contar_esperas(libros))\n",
        "print(len(libros), \"usuarios en espera\", contar_usuarios_espera(libros))\n",
        "print(\"usuarios en no espera\",contar_usuarios_no_espera(libros, usuarios))\n",
        "print(contar_esperas_lib(libros,\"L010\" ))\n",
        "print(contar_esperas_us(libros, 301))\n",
        "mostrar_libros(libros, \"acción\")"
      ],
      "metadata": {
        "id": "YmAyz-kDzl73",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "cafab2b0-19bd-45d6-9510-b54179002d80"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "lista autores 9\n",
            "libros en espera 0\n",
            "[107, 101, 102, 103, 101, 104, 109] {101, 102, 103, 104, 107, 109}\n",
            "11 usuarios en espera 6\n",
            "usuarios en no espera 4\n",
            "2\n",
            "0\n",
            "L001 El Código Da Vinci - Dan Brown\n",
            "L002 Cien Años de Soledad - Gabriel García Márquez\n",
            "L003 1984 - George Orwell\n",
            "L000 Crimen y Castigo - Fiódor Dostoievski\n",
            "L005 Orgullo y Prejuicio - Jane Austen\n",
            "L006 El Señor de los Anillos2 - J.R.R. Tolkien\n",
            "L106 El Señor de los Anillos - J.R.R. Tolkien\n",
            "L007 Un Mundo Feliz - Aldous Huxley\n",
            "L008 Don Quijote de la Mancha - Miguel de Cervantes\n",
            "L009 El Hobbit - J.R.R. Tolkien\n",
            "L010 Harry Potter y la Piedra Filosofal - J.K. Rowling\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def contar_libros_mes(p , m ):\n",
        "  suma = 0\n",
        "  for i in p:\n",
        "    if i[0][1] == m and not i[2]:\n",
        "      suma = suma + 1\n",
        "  return suma\n",
        "mes = int(input(\"ingrese mes\"))\n",
        "if (mes > 0 and mes < 13):\n",
        "  print(contar_libros_mes(prestamos, mes))\n",
        "mes = float(input(\"ingrese mes\"))\n",
        "if (mes in (1,2,3,4,5,6,7,8,9,10,11,12)):\n",
        "  print(contar_libros_mes(prestamos, mes))\n",
        "mes = input(\"ingrese mes\")\n",
        "if (mes > 0 or mes < 13):\n",
        "  print(contar_libros_mes(prestamos, mes))\n",
        "\n",
        "mes = int(input(\"ingrese mes\"))\n",
        "if (mes in (1:12)):\n",
        "  print(contar_libros_mes(prestamos, mes))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 298
        },
        "id": "nqsiUThpa14_",
        "outputId": "2dc1836c-1ea6-4af3-e84c-92c6cedf99be"
      },
      "execution_count": null,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "ingrese mes12\n",
            "a 2\n",
            "ingrese mes12\n",
            "c 2\n",
            "ingrese mes12\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "TypeError",
          "evalue": "'>' not supported between instances of 'str' and 'int'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipython-input-3993273617.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     12\u001b[0m   \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"c\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcontar_libros_mes\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mprestamos\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmes\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     13\u001b[0m \u001b[0mmes\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"ingrese mes\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 14\u001b[0;31m \u001b[0;32mif\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0mmes\u001b[0m \u001b[0;34m>\u001b[0m \u001b[0;36m0\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0mmes\u001b[0m \u001b[0;34m<\u001b[0m \u001b[0;36m13\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     15\u001b[0m   \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"b\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcontar_libros_mes\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mprestamos\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmes\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     16\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mTypeError\u001b[0m: '>' not supported between instances of 'str' and 'int'"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in prestamos:\n",
        "  if ( i [0] [1] == 12) and not i[2] :\n",
        "    print(i)\n",
        "aut=[]\n",
        "for i in libros:\n",
        "  if libros[i][\"autor\"] not in aut:\n",
        "    aut.append(libros[i][\"autor\"])\n",
        "print(len(aut))\n",
        "\n",
        "aut=[]\n",
        "for i in libros:\n",
        "  aut.append(libros[i][\"autor\"])\n",
        "print(len(set(aut)))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AQlXJU4DdCRM",
        "outputId": "58b2e602-1c93-4ada-f99e-0c5dc003fddc"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "((1, 12, 2025), 0, False, 'L010', 101)\n",
            "((19, 12, 2025), 0, False, 'L005', 102)\n",
            "9\n",
            "9\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "auuto=[]\n",
        "for x in (libros):\n",
        "  if libros[x].get(\"autor\") not in auuto:\n",
        "    auuto.append(libros[x].get(\"autor\"))\n",
        "print(len(auuto))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bV5zsAgZlnVD",
        "outputId": "450be877-3e1b-4d71-a7c0-1d334e75fe37"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "9\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(solicitud_por_us(libros , usuarios))"
      ],
      "metadata": {
        "id": "tZVg7LaTQgfY",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ac294c2a-e705-40c7-cfc9-7cb672302952"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{101: 2, 102: 1, 103: 1, 104: 1, 105: 0, 106: 0, 107: 1, 108: 0, 109: 1, 110: 0}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "codigo libros prestados"
      ],
      "metadata": {
        "id": "ftJVZXyFgjhf"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "CI = set(usuarios.keys())\n",
        "espera = []\n",
        "for i in libros:\n",
        "  espera = espera + libros[i][\"lista_espera\"]\n",
        "espera = set(espera)\n",
        "print(espera)\n",
        "resutlado=0\n",
        "for i in CI :\n",
        "  if i not in espera  :\n",
        "    resutlado += 1\n",
        "    print(resutlado)\n",
        "print(len(CI)-len(espera))\n",
        "for i in enumerate(libros):\n",
        "  print(i)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "S9azvpnk27cL",
        "outputId": "e5028745-d413-40ae-d86f-2cceb77f8e71"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{101, 102, 103, 104, 107, 109}\n",
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "4\n",
            "(0, 'L001')\n",
            "(1, 'L002')\n",
            "(2, 'L003')\n",
            "(3, 'L000')\n",
            "(4, 'L005')\n",
            "(5, 'L006')\n",
            "(6, 'L106')\n",
            "(7, 'L116')\n",
            "(8, 'L007')\n",
            "(9, 'L008')\n",
            "(10, 'L009')\n",
            "(11, 'L010')\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def codigo_libros_prestados (p):\n",
        "    codigos = [prestamo[3] for prestamo in p]\n",
        "    return codigos\n",
        "\n",
        "def codigo_libros_prestados1 (p):\n",
        "    codigos = []\n",
        "    for i in range (len(p)):\n",
        "      codigos[i]=p[i][3]\n",
        "    return codigos\n",
        "\n",
        "\n",
        "def codigo_libros_prestados3 (p):\n",
        "  codigos = []\n",
        "  for i in range (len(p)):\n",
        "    codigos.append(p[i][3])\n",
        "  return codigos\n",
        "\n",
        "def codigo_libros_prestados2 (p):\n",
        "  codigos = []\n",
        "  for i in p:\n",
        "   codigos.append(i[3])\n",
        "  return codigos\n",
        "\n",
        "print(\"libros prestados\" , codigo_libros_prestados(prestamos))\n",
        "#print(\"libros prestados\" , codigo_libros_prestados1(prestamos))\n",
        "print(\"libros prestados2\" , codigo_libros_prestados2(prestamos))\n",
        "print(\"libros prestados3\" , codigo_libros_prestados3(prestamos))\n",
        "\n",
        "\n",
        "\n",
        "#Libro nunca prestado\n",
        "def nunca_prestado(l, p):\n",
        "  aux1 = set(libros.keys())\n",
        "  codigos1 = codigo_libros_prestados (p)\n",
        "  codigos2 = codigo_libros_prestados (p)\n",
        "  codigos = codigo_libros_prestados (p)\n",
        "  aux2 = set(codigos)\n",
        "  print(aux1 , aux2)\n",
        "  return aux1-aux2\n",
        "\n",
        "# Libro menos prestado\n",
        "def libro_menos_prestado(p):\n",
        "  codigos = codigo_libros_prestados (p)\n",
        "  cod = []\n",
        "  if len(codigos) == 0:\n",
        "    return None\n",
        "  minimo = codigos.count(codigos[0])\n",
        "  for i in codigos:\n",
        "    if minimo > codigos.count(i):\n",
        "      minimo = codigos.count(i)\n",
        "  for i in codigos:\n",
        "    if minimo == codigos.count(i):\n",
        "      cod.append(i)\n",
        "      return (cod, minimo)\n",
        "\n",
        "print(\"libro menos \",libro_menos_prestado(prestamos))\n",
        "print(nunca_prestado(libros, prestamos))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ejlQ_8cSJo68",
        "outputId": "c9a4409f-36ff-4af8-b38c-95d4bdedc6b6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "libros prestados ['L010', 'L009', 'L005', 'L005']\n",
            "libros prestados2 ['L010', 'L009', 'L005', 'L005']\n",
            "libros prestados3 ['L010', 'L009', 'L005', 'L005']\n",
            "libro menos  (['L010'], 1)\n",
            "{'L001', 'L006', 'L003', 'L009', 'L002', 'L116', 'L005', 'L000', 'L008', 'L010', 'L007', 'L106'} {'L010', 'L009', 'L005'}\n",
            "{'L001', 'L006', 'L003', 'L002', 'L116', 'L000', 'L007', 'L008', 'L106'}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def sumar_dias (f, dia):\n",
        "  fecha = list(f)\n",
        "  if fecha[1]  in (1,3,5,7,8,10,12) :\n",
        "    if fecha[0]\t+ dia > 31:\n",
        "      dias = dia - (31 - fecha[0])\n",
        "      fecha[0] = dias\n",
        "      fecha[1] = fecha[1] + 1\n",
        "      if fecha[1] == 13:\n",
        "        fecha[2] = fecha[2]+1\n",
        "        fecha[1] = 1\n",
        "\n",
        "    else:\n",
        "      fecha[0] = fecha[0] + dia\n",
        "    return fecha\n",
        "  if fecha[1] in (4,6,9,11):\n",
        "    if fecha[0]\t+ dia > 30:\n",
        "      dia = dia - (30 - fecha[0])\n",
        "      fecha[0] = dia\n",
        "      fecha[1] = fecha[1] + 1\n",
        "    else:\n",
        "      fecha[0] = fecha[0] + dia\n",
        "    return fecha\n",
        "  if fecha[1]==2 and fecha[2] % 4 != 0 :\n",
        "    if fecha[0]\t+ dia > 28:\n",
        "      dia = dia - (28 - fecha[0])\n",
        "      fecha[0] = dia\n",
        "      fecha[1] = fecha[1] + 1\n",
        "    else:\n",
        "      fecha[0] = fecha[0] + dias\n",
        "    return tuple(fecha)\n",
        "  if fecha[1]==2 and fecha[2] % 4 == 0 :\n",
        "    if fecha[0]\t+ dia > 29:\n",
        "      dia = dia - (29 - fecha[0])\n",
        "      fecha[0] = dia\n",
        "      fecha[1] = fecha[1] + 1\n",
        "    else:\n",
        "      fecha[0] = fecha[0] + dia\n",
        "    return tuple(fecha)\n",
        "print(sumar_dias ((10, 12, 2024) , 22))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "q2mAm7o6578d",
        "outputId": "7bc76839-ee82-488e-dfd5-2c9ff39136db"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 1, 2025]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def dar_lugar(plia_reparacion, c_libro):\n",
        "  return plia_reparacion.index(c_libro)\n",
        "\n",
        "def dar_lugar2 (plia_reparacion, c_libro):\n",
        "  aux = 0\n",
        "  for i in range(len(plia_reparacion)):\n",
        "    if plia_reparacion[i] == c_libro:\n",
        "      aux = i\n",
        "  return aux\n",
        "def dar_lugar3 (plia_reparacion, c_libro):\n",
        "  for valor, codigo in enumerate(pila_reparacion):\n",
        "    if codigo == c_libro:\n",
        "      return valor\n",
        "  return None\n",
        "\n",
        "\n",
        "pila_reparacion_urgente = []\n",
        "pila_reparacion = []\n",
        "pila_reparacion.append(\"a1\")\n",
        "pila_reparacion.append(\"L001\")\n",
        "pila_reparacion.append(\"a3\")\n",
        "pila_reparacion.append(\"a4\")\n",
        "pila_reparacion.append(\"a5\")\n",
        "\n",
        "print (dar_lugar3 (pila_reparacion,\"a3\"), dar_lugar2 (pila_reparacion,\"a3\"),dar_lugar (pila_reparacion,\"a3\"))"
      ],
      "metadata": {
        "id": "14_EaWrMJhg1",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "fade197e-3600-4e85-f255-f9fb97c3354d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2 2 2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def control (pr, lib):\n",
        "  a = input (\"ingrese codigo libro\")\n",
        "  if a in lib :\n",
        "    return dar_lugar(pr, a)\n",
        "  else:\n",
        "    return None\n",
        "\n",
        "print ( control (pila_reparacion, libros))"
      ],
      "metadata": {
        "id": "ha_rLJvOQkiB",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "1a6668d0-9fd0-4cc8-b98b-e1015a8cb0d5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "ingrese codigo libroL001\n",
            "1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pila_reparacion_urgente = []\n",
        "pila_reparacion = []\n",
        "pila_reparacion.append(\"L003\")\n",
        "pila_reparacion.append(\"L002\")\n",
        "pila_reparacion.append(\"L006\")\n",
        "pila_reparacion.append(\"L001\")\n",
        "pila_reparacion.append(\"L003\")\n",
        "contador=0\n",
        "def pertenece (Pila, codigo) :\n",
        "  pila = Pila.copy()\n",
        "  global contador\n",
        "  contador = contador + 1\n",
        "  indice = len(pila) - 1\n",
        "  print(contador, indice)\n",
        "  if indice == -1 :\n",
        "    return False\n",
        "  else :\n",
        "    if pila[indice]==codigo:\n",
        "      return True\n",
        "    else:\n",
        "      pila.pop()\n",
        "      return pertenece(pila, codigo)\n",
        "\n",
        "print(pertenece(pila_reparacion, \"a3\"))\n",
        "print(pila_reparacion)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WB1gKv6N6EGs",
        "outputId": "6338acef-140a-4ba8-d65c-8c7fa74e3f7f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 4\n",
            "2 3\n",
            "3 2\n",
            "4 1\n",
            "5 0\n",
            "6 -1\n",
            "False\n",
            "['L003', 'L002', 'L006', 'L001', 'L003']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "Aquí tienes un ejemplo:\n",
        "\n",
        "my_dict = {\n",
        "    \"dic1\": {\"itemA\": 10, \"itemB\": [1, 2]},\n",
        "    \"dic2\": {\"itemA\": 20, \"itemB\": [3, 4]},\n",
        "    \"dic3\": {\"itemA\": 30, \"itemB\": [5, 6]}\n",
        "}\n",
        "\n",
        "# Para obtener una lista de los valores de \"itemA\"\n",
        "list_itemA = [inner_dict[\"itemA\"] for inner_dict in my_dict.values()]\n",
        "print(f\"Lista de itemA: {list_itemA}\")\n",
        "\n",
        "\n",
        "def cont_lib_gen (aux, resultado):\n",
        "  if len(aux)==0:\n",
        "    return resultado\n",
        "\n",
        "  else :\n",
        "    resultado[aux[len(aux)-1][2]] =+ 1\n",
        "    print(aux[len(aux)-1])\n",
        "    aux.pop()\n",
        "    return cont_lib_gen(aux,resultado)\n",
        "\n",
        "gen=dict.fromkeys(genero,0)\n",
        "print(libros, gen)\n",
        "print(cont_lib_gen(libros, gen))\n"
      ],
      "metadata": {
        "id": "6ZqdFmnTuDVZ",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 335
        },
        "outputId": "b2693b7a-f824-4826-ecd7-f334848e23d3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'L001': {'nombre': 'El Código Da Vinci', 'autor': 'Dan Brown', 'genero': 'thrillers', 'copias': 3, 'en_mantenimiento': False, 'lista_espera': [107]}, 'L002': {'nombre': 'Cien Años de Soledad', 'autor': 'Gabriel García Márquez', 'genero': 'ficción', 'copias': 1, 'en_mantenimiento': False, 'lista_espera': [101, 102]}, 'L003': {'nombre': '1984', 'autor': 'George Orwell', 'genero': 'ficción', 'copias': 4, 'en_mantenimiento': False, 'lista_espera': []}, 'L000': {'nombre': 'Crimen y Castigo', 'autor': 'Fiódor Dostoievski', 'genero': 'históricas', 'copias': 2, 'en_mantenimiento': True, 'lista_espera': []}, 'L005': {'nombre': 'Orgullo y Prejuicio', 'autor': 'Jane Austen', 'genero': 'romance', 'copias': 2, 'en_mantenimiento': False, 'lista_espera': []}, 'L006': {'nombre': 'El Señor de los Anillos', 'autor': 'J.R.R. Tolkien', 'genero': 'fantasía', 'copias': 5, 'en_mantenimiento': False, 'lista_espera': []}, 'L007': {'nombre': 'Un Mundo Feliz', 'autor': 'Aldous Huxley', 'genero': 'ficción', 'copias': 2, 'en_mantenimiento': False, 'lista_espera': []}, 'L008': {'nombre': 'Don Quijote de la Mancha', 'autor': 'Miguel de Cervantes', 'genero': 'ficción', 'copias': 1, 'en_mantenimiento': False, 'lista_espera': [103, 101]}, 'L009': {'nombre': 'El Hobbit', 'autor': 'J.R.R. Tolkien', 'genero': 'fantasía', 'copias': 3, 'en_mantenimiento': False, 'lista_espera': []}, 'L010': {'nombre': 'Harry Potter y la Piedra Filosofal', 'autor': 'J.K. Rowling', 'genero': 'fantasía', 'copias': 4, 'en_mantenimiento': True, 'lista_espera': [101, 105]}} {'ficción': 0, 'históricas': 0, 'fantasía': 0, 'misterio': 0, 'romance': 0, 'thrillers': 0, 'Poesía': 0}\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "KeyError",
          "evalue": "9",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipython-input-18-1550898949.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     11\u001b[0m \u001b[0mgen\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mdict\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfromkeys\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mgenero\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     12\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlibros\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mgen\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 13\u001b[0;31m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcont_lib_gen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlibros\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mgen\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m/tmp/ipython-input-18-1550898949.py\u001b[0m in \u001b[0;36mcont_lib_gen\u001b[0;34m(aux, resultado)\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m   \u001b[0;32melse\u001b[0m \u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 6\u001b[0;31m     \u001b[0mresultado\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0maux\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0maux\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m\u001b[0;34m+\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      7\u001b[0m     \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0maux\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0maux\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      8\u001b[0m     \u001b[0maux\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpop\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyError\u001b[0m: 9"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "lista_libros = list(libros.keys())\n",
        "print(lista_libros)\n",
        "\n",
        "cantidad_pedididos = [lp [\"lista_espera\"] for lp in libros.values()]\n",
        "print(cantidad_pedididos)\n",
        "\n",
        "def dar_pedidos_cli (cp , ci):\n",
        "  if len(cp)==0:\n",
        "    return 0\n",
        "  else:\n",
        "    # Check the last element without removing it\n",
        "    if ci in cp[-1]:\n",
        "      # Recurse on the list excluding the last element\n",
        "      return 1 + dar_pedidos_cli(cp[:-1], ci)\n",
        "    else:\n",
        "      # Recurse on the list excluding the last element\n",
        "      return dar_pedidos_cli(cp[:-1], ci)\n",
        "\n",
        "# Corregida para usar un bucle en lugar de recursión con estado compartido\n",
        "def dar_pedidos_cli2 (cp , ci):\n",
        "  count = 0\n",
        "  for lista_espera in cp:\n",
        "    if ci in lista_espera:\n",
        "      count += 1\n",
        "  return count\n",
        "\n",
        "\n",
        "print(dar_pedidos_cli( cantidad_pedididos, 101))\n",
        "print(dar_pedidos_cli2( cantidad_pedididos, 101))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fJBr1H9pn5-h",
        "outputId": "99756d1e-56d7-4151-e4b1-c3c1fb7bce4d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['L001', 'L002', 'L003', 'L000', 'L005', 'L006', 'L106', 'L007', 'L008', 'L009', 'L010']\n",
            "[[107], [101, 102], [], [], [], [], [], [], [103, 101], [], [101, 105]]\n",
            "3\n",
            "3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "cantidad_pedididos = [lp [\"lista_espera\"] for lp in libros.values()]\n",
        "print(cantidad_pedididos)\n",
        "\n",
        "def dar_pedidos_cli (cp , ci):\n",
        "  if len(cp)==0:\n",
        "    return 0\n",
        "  else:\n",
        "    if ci in cp[len(cp)-1]:\n",
        "      cp.pop()\n",
        "      return 1 + dar_pedidos_cli(cp, ci)\n",
        "    else:\n",
        "      cp.pop()\n",
        "      return dar_pedidos_cli(cp, ci)\n",
        "\n",
        "      l[p[indice][3]].get(\"nombre\"))\n",
        "    return prestamos_us( p , us , l , indice+1 )"
      ],
      "metadata": {
        "id": "TBkUohgO3OSm"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def prestamos_us (p, us , l , indice=0):\n",
        "  print(len(p), indice)\n",
        "  if indice == len(p):\n",
        "    return 0\n",
        "  else:\n",
        "    print(p[indice][4], us)\n",
        "    if p[indice][4]==us:\n",
        "      print( l[p[indice][3]].get(\"nombre\"))\n",
        "\n",
        "PASO RECURSIVO --->\n",
        "\n",
        "indice=0\n",
        "prestamos_us(prestamos, 101, libros)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lZ6OpMY7SMPF",
        "outputId": "f4477696-9197-4201-c983-06773df4aba4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4 0\n",
            "101 101\n",
            "Harry Potter y la Piedra Filosofal\n",
            "4 1\n",
            "103 101\n",
            "4 2\n",
            "101 101\n",
            "Orgullo y Prejuicio\n",
            "4 3\n",
            "102 101\n",
            "4 4\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0"
            ]
          },
          "metadata": {},
          "execution_count": 24
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def contar_palabras5(titulo):\n",
        "  palabras=titulo.split()\n",
        "  return len(palabras)\n",
        "\n",
        "def contar_palabras4(titulo):\n",
        "  contador=0\n",
        "  palabras=titulo.split()\n",
        "  for i in range(len(palabras)):\n",
        "    contador += 1\n",
        "  return contador\n",
        "\n",
        "def contar_palabras(titulo):\n",
        "  contador=0\n",
        "  palabras=titulo.split()\n",
        "  for i in palabras:\n",
        "    contador += 1\n",
        "  return contador\n",
        "\n",
        "def contar_palabras2(titulo):\n",
        "  return len(titulo)\n",
        "\n",
        "def contar_palabras3(titulo) :\n",
        "  contador=0\n",
        "  for i in titulo :\n",
        "    contador += 1\n",
        "  return contador\n",
        "\n",
        "codigo=input(\"Ingrese código de libro\")\n",
        "if codigo not in  libros:\n",
        "  print(contar_palabras(codigo))\n",
        "  print(contar_palabras2(codigo))\n",
        "  print(contar_palabras3(codigo))\n",
        "  print(contar_palabras4(codigo))\n",
        "  print(contar_palabras5(codigo))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pJWrs1gH_sYs",
        "outputId": "e2a8f8d6-b05d-4816-cfd1-ef3c3f7123de"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ingrese código de librohola que tal\n",
            "3\n",
            "12\n",
            "12\n",
            "3\n",
            "3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "pA1XDd6rwTPG"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def repetidos (l):\n",
        "  aux = list(l.fromkeys(l, 0))\n",
        "  for i in aux:\n",
        "    aux2 = l[i].get(\"nombre\")\n",
        "    for j in aux:\n",
        "      if l[j].get(\"nombre\")==aux2:\n",
        "        return True\n",
        "      else :\n",
        "        return False\n",
        "\n",
        "def repetidos2 (l):\n",
        "  aux = list(l.fromkeys(l, 0))\n",
        "  for i in aux:\n",
        "    aux2 = l[i].get(\"nombre\")\n",
        "    for j in aux:\n",
        "      if l[j].get(\"nombre\")==aux2:\n",
        "        return True\n",
        "  return False\n",
        "\n",
        "def repetidos1(l):\n",
        "  aux = []\n",
        "  for i in l:\n",
        "    aux.append(l[i].get(\"nombre\"))\n",
        "  aux1=set(l)\n",
        "  aux2=set(aux)\n",
        "  aux3=aux1-aux2\n",
        "  if (aux3)==0:\n",
        "    return True\n",
        "  else:\n",
        "    return False\n",
        "\n",
        "def repetidos4(l):\n",
        "  aux = []\n",
        "  for i in l:\n",
        "    aux.append(l[i].get(\"nombre\"))\n",
        "  aux1=len(set(l))\n",
        "  aux2=len((set(aux)))\n",
        "  print(\"aux\",aux1)\n",
        "  print(\"aux\",aux2)\n",
        "  aux3=aux1-aux2\n",
        "  print(aux3)\n",
        "  if (aux3)==0:\n",
        "    return False\n",
        "  else:\n",
        "    return True\n",
        "\n",
        "print(repetidos (libros), repetidos1 (libros) , repetidos2 (libros), repetidos4 (libros))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4itMC6gZk5LG",
        "outputId": "9ea79b07-5ec6-496f-bfa8-46fd28c86be8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "aux 12\n",
            "aux 11\n",
            "1\n",
            "True False True True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "suma=0\n",
        "for l in libros.values():\n",
        "  if 107 in (l[\"lista_espera\"]):\n",
        "    suma=suma+1\n",
        "print(suma)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zo3ZtjPMwd_h",
        "outputId": "92627186-8da0-48c7-efb0-66d7371b67cb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "00\n",
        "def opinion (libros) :\n",
        "  aux = {}\n",
        "  for l in libros:\n",
        "    total_opinion = contar_opinion(libros[l].get(\"nombre\"))\n",
        "    aux[libros[l].get(\"nombre\")] = total_opinion\n",
        "  print(aux)\n",
        "\n",
        "def contar_opinion( titulo , critico=1):\n",
        "  calificacion = int(input(\"  Ingrese calificación  : \"))\n",
        "  if calificacion == 0 :\n",
        "    return 0\n",
        "  else :\n",
        "    critico = critico + 1\n",
        "    return calificacion + contar_opinion( titulo , critico)\n",
        "opinion(libros)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yv-zNFaDWH-9",
        "outputId": "9856a5be-1991-494e-8756-5a710bed0a53"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "  Ingrese calificación  : 12\n",
            "  Ingrese calificación  : 12\n",
            "  Ingrese calificación  : 0\n",
            "  Ingrese calificación  : 0\n",
            "  Ingrese calificación  : 0\n",
            "  Ingrese calificación  : 0\n",
            "  Ingrese calificación  : 0\n",
            "  Ingrese calificación  : 0\n",
            "  Ingrese calificación  : 0\n",
            "  Ingrese calificación  : 0\n",
            "  Ingrese calificación  : 0\n",
            "  Ingrese calificación  : 0\n",
            "  Ingrese calificación  : 0\n",
            "  Ingrese calificación  : 0\n",
            "{'El Código Da Vinci': 24, 'Cien Años de Soledad': 0, '1984': 0, 'Crimen y Castigo': 0, 'Orgullo y Prejuicio': 0, 'El Señor de los Anillos2': 0, 'El Señor de los Anillos21': 0, 'El Señor de los Anillos': 0, 'Un Mundo Feliz': 0, 'Don Quijote de la Mancha': 0, 'El Hobbit': 0, 'Harry Potter y la Piedra Filosofal': 0}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def rr (us):\n"
      ],
      "metadata": {
        "id": "HM-cXCvWhWnC"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "def reparar_libro(pila):\n",
        "  i= len(pila)-1\n",
        "  reparados=pila.pop()\n",
        "  return reparados\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KoldH8kBfrs_",
        "outputId": "b7de7a99-5904-41fd-813c-18a871aae3c2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "L002\n",
            "['L003']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = tuple(input(\"ingrese lista\"))\n",
        "print(a)\n",
        "b = str(a)+\"hola\"\n",
        "print(type(b))\n",
        "\n",
        "def departamentos (usuarios):\n",
        "  op = []\n",
        "  for us in usuarios :\n",
        "    print(us)\n",
        "    op.append(usuarios[us][2])\n",
        "  op.sort()\n",
        "  return set(op)\n",
        "print(departamentos(usuarios))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BZDs0vUdrdql",
        "outputId": "d83a59fb-281b-4116-8bca-33e4a51e7b64"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "ingrese listasdf\n",
            "('s', 'd', 'f')\n",
            "<class 'str'>\n",
            "101\n",
            "102\n",
            "103\n",
            "104\n",
            "105\n",
            "106\n",
            "107\n",
            "108\n",
            "109\n",
            "110\n",
            "{'Montevideo', 'Salto', 'Rivera', 'Paysandú'}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def us_inactivos(us, pres):\n",
        "  aux_us= set(us)\n",
        "  aux_pre = []\n",
        "  for i in pres :\n",
        "    aux_pre.append(i[4])\n",
        "  aux_pre = set(aux_pre)\n",
        "  print( aux_us - aux_pre)\n",
        "\n",
        "if len(prestamos) == 0:\n",
        "  us_inactivos(usuarios, prestamos)\n",
        "else:\n",
        "  print(\"no 1\")\n",
        "\n",
        "if len(prestamos) != 0 and len(usuarios)!=0:\n",
        "  us_inactivos(usuarios, prestamos)\n",
        "\n",
        "if len(prestamos) != 0:\n",
        "  print(us_inactivos(usuarios, prestamos))\n",
        "\n",
        "if len(prestamos) > 0:\n",
        "  a=us_inactivos(usuarios, prestamos)\n",
        "  print(\"a\",a)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AlZjaA7w9kX2",
        "outputId": "fd32a130-5379-4889-9c33-5018d45b862e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "no 1\n",
            "{104, 105, 106, 107, 108, 109, 110}\n",
            "{104, 105, 106, 107, 108, 109, 110}\n",
            "2 None\n",
            "{104, 105, 106, 107, 108, 109, 110}\n",
            "a None\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "def titulo_repetido(l):\n",
        "  if len(l)!= 0 :\n",
        "    a=l.pop()\n",
        "    if a in l:\n",
        "      return True\n",
        "    else:\n",
        "      return titulo_repetido(aux)\n",
        "  return False\n",
        "\n",
        "\n",
        "aux1 = []\n",
        "for i in libros:\n",
        "  aux1.append(libros[i].get(\"nombre\"))\n",
        "print(titulo_repetido(aux1))\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "s-p4brYTDDcL",
        "outputId": "54d66ddc-3caa-42fe-eeb4-ed1df48afb5d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n"
          ]
        }
      ]
    }
  ]
}