#p es el factor de multiplicacion
#e es el numero mayor en el que se generan nuevos vehiculos
#p = 1 y e = 100 genera un coche por segundo
python "%SUMO_HOME%\tools\randomTrips.py" -n dependencias/osm.net.xml -p 8 -e 32351 -o resultados/rdm.osm.passenger.trips.xml  --vehicle-class passenger --vclass passenger --prefix veh --min-distance 300 --trip-attributes "departLane=\"best\"" --fringe-start-attributes "departSpeed=\"max\"" --allow-fringe.min-length 1000 --lanes --validate
