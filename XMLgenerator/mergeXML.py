from os import read
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString


def readXML(file):
  tree = ET.parse(file)
  data = tree.getroot()
  trips = data[1:]
  return trips

def merge(a1, a2):
    trips = (a1+a2)
    return a1+a2

def bubbleSort(arr):
    for i in range(len(arr)):
    	for j in range(0, len(arr) - i - 1):
            if float(arr[j].get("depart")) > float(arr[j + 1].get("depart")):
            	arr[j], arr[j + 1] = arr[j + 1], arr[j]

def renameVeh(arr):
    for i in range(len(arr)):
        arr[i].set("id","veh" + str(i))

def openXML():
    # create the file structure
    customFile = ET.Element("routes")
    customFile.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
    customFile.set("xsi:noNamespaceSchemaLocation", "http://sumo.dlr.de/xsd/routes_file.xsd")

    ET.SubElement(customFile, "vType", id="veh_passenger", vClass="passenger")

    return customFile

def appendTrips(customFile):
    for trip in trips:
        customFile.append(trip)
    return customFile

def closeXML(customFile):
    # create a new XML file with the results
    mydata = ET.tostring(customFile)

    data = parseString(mydata) # your string

    with open('osm.passenger.trips.xml', 'w') as file:
        data.writexml(file, indent='\n', addindent=' ')


file1 = "resultados/rdm.osm.passenger.trips.xml"
file2 = "resultados/directed.osm.passenger.trips.xml"
file1 = readXML(file1)
file2 = readXML(file2)
trips = merge(file1, file2)
bubbleSort(trips)
renameVeh(trips)
tree = openXML()
tree = appendTrips(tree)
closeXML(tree)

print("Sorted array is:")
for i in range(len(trips)):
	print(trips[i].attrib)

