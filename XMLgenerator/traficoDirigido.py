import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString
import csv
from random import randint

def openXML():
    # create the file structure
    customFile = ET.Element("routes")
    customFile.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
    customFile.set("xsi:noNamespaceSchemaLocation", "http://sumo.dlr.de/xsd/routes_file.xsd")

    ET.SubElement(customFile, "vType", id="veh_passenger", vClass="passenger")

    return customFile


def traficoReal(fileCSV, customFile, direcciones):

    #<trip id="veh0" type="veh_passenger" depart="0.00" departLane="best" from="54388038#0-AddedOffRampEdge" to="-251153461"/>

    valores = []

    with open(fileCSV, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            try:
                valores.append([int(row[0]),int(row[1])])
            except:pass

    valores[0][0]=7


    tiempos = []

    for i in range(0,len(valores)):
        for j in range(0,valores[i][1]):
            tiempos.append(int(randint(i*3600, (i+1)*3600)))

    tiempos.sort()

    cont = 0
    for tiempo in tiempos:
        trip = ET.SubElement(customFile, "trip")
        trip.set("id","veh"+str(cont))
        trip.set("type","veh_passenger")
        trip.set("depart",str(tiempo))
        trip.set("departLane","best")
        trip.set("from",direcciones[0])
        trip.set("to",direcciones[1])
        cont+=1
        trip = ET.SubElement(customFile, "trip")
        trip.set("id","veh"+str(cont))
        trip.set("type","veh_passenger")
        trip.set("depart",str(tiempo))
        trip.set("departLane","best")
        trip.set("from",direcciones[2])
        trip.set("to",direcciones[3])
        cont+=1

def closeXML(customFile):

    # create a new XML file with the results
    mydata = ET.tostring(customFile,encoding='unicode')

    data = parseString(mydata) # your string

    with open('resultados/directed.osm.passenger.trips.xml', 'w') as file:
        data.writexml(file, indent='\n', addindent=' ')



customFile = openXML()
fichero = 'dependencias/nCoches.csv'
#origen destino carril ida, origen destino carril vuelta
direcciones = ["54388038#0","-288761327","288761327","54388033"]
traficoReal(fichero, customFile, direcciones)
closeXML(customFile)
