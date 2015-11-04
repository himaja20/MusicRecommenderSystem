
from pyechonest import catalog, config
config.ECHO_NEST_API_KEY="KO5QUBGMUVJZA0PFA"

cat = catalog.Catalog('CACNYVZ1332EB0BA9D')
print(cat.get_item_dicts())
