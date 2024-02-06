# xml-parser
XML Parser Utility that takes in an XML file and return structured data. Refer to ```xml_structure.py``` for more details

## Data File
Refer to assets/tasks3.xml

## How-to run it
```python main.py```

## Sample Output
```
Item: 1, Item 1, This is a description with <markup>.
Detail: created, 2024-02-01
Detail: author, Author Name
Item: 2, Item 2, Another item, with CDATA containing <tags> and &entities;.
Detail: created, 2024-02-02
Detail: author, Another Author
Complex:
Nested: 1
Nested: 2, Deeply nested value
```
