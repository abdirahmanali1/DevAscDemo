import xmltodict

with open('r1.xml') as file:
    xml_string = file.read()

data = xmltodict.parse(xml_string)

print(data['router']['interface']['interface'][0]['ip'])