
from pyechonest import catalog, config
import json

config.ECHO_NEST_API_KEY="KO5QUBGMUVJZA0PFA"

cat = catalog.Catalog('CACNYVZ1332EB0BA9D')
json_str = cat.get_item_dicts()

##json_str = '{"first_name": "Guido", "last_name":"Rossum"}'
parsed_json = json.loads(str(json_str).encode("utf-8"))

##print(parsed_json)
print (parsed_json)
