# TK-TraficSimulator

Programa basado en Python

En el presente proyecto se realizará una pequeña funcionalidad para correr una demo del software de simulación de tráfico realizado con Eclipse Sumo y Python 3.6 o posterior.

Proyecto realizado con por Eneko Eguiguren y Oier Mentxaka con la supervisión de Antonio Raez y Javier Torres

# XMLGenerator

* Dependencias: <br />
  |__ nCoches.csv - Documento CSV con la frecuencia por tramos horarios de los vehiculos que circulan por la vía en ciertas horas del día <br />
  |__ osm.net.xml - Fichero con los datos de la red de carreteras compatible con el formato de Sumo descargado con la herramienta WebWizard proporcionada por Eclipse Sumo <br />
  
* Resultados:   <br />
  |__ directed.osm.passenger.trips.xml - Fichero con los datos de trafico reales de la vía compatible con el fomato de Sumo <br />
  |__ rdm.osm.passenger.trips.xml - Fichero con los datos de trafico aleatorio que consideramos que hay por las vías adyacentes a la que se pretende estudiar compatible con el formato de Sumo <br />
  |__ osm.passengertrips.xml - Fichero resultante con el trafico tanto aleatorio como dirigido compatible con el formato de Sumo <br />

* mergeXML.py - Fichero encargado de juntar los dos tipos de trafico generados en uno solo para la correcta lectura por Sumo
    - Dependencias: <br />
       - Fichero resultados/directed.osm.passenger.trips.xml <br />
       - Fichero resultados/rdm.osm.passenger.trips.xml <br />
    - Resultados: <br />
       - Fichero resultados/rdm.osm.passenger.trips.xml con el trafico aleatorio generado compatible con Sumo <br />
* rdmCarGenerator.bat - Fichero encargado de generar un fichero con el trafico aleatorio estimado por las carreteras adyacentes <br />
    - Dependencias: <br />
       - Necesita el mapa en formato Sumo <br />
       - Valores P y E, los cuales por defecto cogen valor 1 y 100 respectivamente, generando un coche nuevo en la via por cada segundo de ejecución <br />
    - Resultados: <br />
       - Fichero resultados/rdm.osm.passenger.trips.xml con el trafico aleatorio generado compatible con Sumo <br />
* traficoDirigido.py - Fichero encargado de generar el trafico que ha de fluir por la carretera a estudiar compatible con Sumo<br />
    - Dependencias:<br />
       - Fichero en la carpeta "Dependencias" nCoches.csv con los datos de los tramos horarios y la frecuencia de vehiculos por hora <br />
       - Array con 4 valores en cuyas posiciones aparecen coordenada X de origen, coordenada Y de origen, coordenada X de destino y Y de destino direcciones = ["XO","YO","XD","YD"] <br />
    - Resultados: <br />
       - Fichero resultados/directed.osm.passenger.trips.xml con el trafico dirigido generado compatible con Sumo <br />
       

