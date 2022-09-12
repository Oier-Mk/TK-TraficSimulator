# Tk-TraficSimulator

Programa basado en py

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

* mergeXML.py
* rdmCarGenerator.bat 
    + Necesita el mapa en formato Sumo 
* traficoDirigido.py
