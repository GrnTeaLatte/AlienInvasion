import csv

import pygal
from pygal.style import RotateStyle

from country_codes import get_country_code

# Load the data into a list
filename = 'forestry_data.csv'
with open(filename) as f:
    reader = csv.reader(f)
    try:
        header_row = next(reader)
    except Exception as e:
        print(e)

    # Build a dictionary of population data.
    forests = {}
    for row in reader:
        try:
            country_name = row[0]
            percentage = row[30]
            code = get_country_code(country_name)
            if code:
                forests[code] = int(float(percentage))
        except ValueError:
            print(country_name, 'missing data')

wm_style = RotateStyle('#336699')
wm = pygal.maps.world.World(style = wm_style)
wm.title = 'World Forestry in 2016, by Country'
wm.add('2016', forests)

wm.render_to_file('world_forests.svg')
