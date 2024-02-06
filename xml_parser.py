import xml.etree.ElementTree as et
from xml_structure import Item, Detail, Complex, Nested

ns = {
    'default': 'http://www.example.com/default',
    'ns': 'http://www.example.com/ns'
}

class XMLParser:
    def __init__(self, xml_file):
        self.xml_file = xml_file
    
    def parse(self):
        '''Parse the XML file and return the structured data, refer to xmL_structure.py for the structured data classes. Logic is simple
        just keep iterating through the XML elements and create the structured data objects. If a complex element is found, create a 
        Complex object'''
        root = et.parse(self.xml_file)

        items = []
        for item_element in root.findall("default:item", namespaces=ns):
            # Get the id, each item has an id, name, description, details and sometimes a complex element
            id = item_element.attrib["id"]
            name = item_element.find("default:name", namespaces=ns).text.strip()
            description = item_element.find("default:description", namespaces=ns).text.strip()
            
            details = []
            # You cannot use finudall here because you are only interested in the direct children of the details element
            for detail_element in item_element.find("default:details", namespaces=ns):
                if 'key' in detail_element.attrib:
                    key = detail_element.attrib['key']
                    value = detail_element.text.strip()
                    details.append(Detail(key, value))
            # the expression .//default:complex is searching for XML elements with the tag name "complex" that are in the given namespace
            complex_element = item_element.find('.//default:complex', namespaces=ns)
            if complex_element is not None:
                nested_elements_lvl1 = complex_element.findall('.//default:nested',namespaces=ns)
                nested_objects = []
                for nested_elem in nested_elements_lvl1:
                    level1 = int(nested_elem.attrib['level'])
                    nested_elements_lvl2 = nested_elem.findall('.//default:nested',namespaces=ns)
                    lvl1 = Nested(level=level1, nested=[])
                    for nested_elem_lvl2 in nested_elements_lvl2:
                        level2 = nested_elem_lvl2.attrib['level']
                        value2 = nested_elem_lvl2.findall('default:value', namespaces=ns)[0].text.strip()
                        lvl1.nested.append(Nested(level2, value=value2))
                    nested_objects.append(lvl1)
                details.append(Complex(nested_objects))
            items.append(Item(id, name, description, details))
        return items
        