import zeep
from zeep import Client, Settings
from zeep import xsd
from zeep.transports import Transport


client = Client(wsdl='https://www.w3schools.com/xml/tempconvert.asmx?wsdl')

sonuc=client.service.CelsiusToFahrenheit(12)

print (sonuc)

