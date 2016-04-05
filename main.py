import sys
from mapreader import MapReader

if len(sys.argv) < 2:
    print("No params")
    sys.exit(1)
 
print("Opening", sys.argv[1])
reader = MapReader(sys.argv[1])
reader.load_map()

reader.normalize()
reader.divide_entities()

for entity in reader.entity_content:
    
    parsed = reader.parse_entity(entity)
    print("-----------------------------")
    print(parsed)
    
    