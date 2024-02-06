from xml_parser import XMLParser
from xml_structure import Item, Detail, Complex, Nested

def main():
    xml_parser = XMLParser('assets/tasks3.xml')
    items = xml_parser.parse()
    for item in items:
        print(f'Item: {item.id}, {item.name}, {item.description}')
        for detail in item.details:
            if isinstance(detail, Detail):
                print(f'Detail: {detail.key}, {detail.value}')
            elif isinstance(detail, Complex):
                print('Complex:')
                for nested in detail.nested:
                    print(f'Nested: {nested.level}')
                    for nested2 in nested.nested:
                        print(f'Nested: {nested2.level}, {nested2.value}')

if __name__ == '__main__':
    main()
