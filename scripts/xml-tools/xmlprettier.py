import xml.dom.minidom

dom = xml.dom.minidom.parse('C:\\temp\\test.xml') # or xml.dom.minidom.parseString(xml_string)
pretty_xml_as_string = dom.toprettyxml()


with open("C:/temp/pretty.xml", "w", encoding="utf-8") as f:
    f.write(pretty_xml_as_string)