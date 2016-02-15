# -*- coding: utf-8 -*-

"""
Determines which Stadtbezirksteile in munich intersect with which postal codes and appends them to a django settings file.
More precisely, it adds 3 new variables, by default to a file named settings/preconfig.py
  - `PLZ`: A list of all postal codes in munich as strings
  - `BEZIRKSTEILE`: A list of names of all bezirksteile in munich
  - `PLZ_MAPPING`: A dict that maps every postal code as string to a list of all bezirksteile that the postal code area intersects with

Requirements:
  - python 3.3+
  - osmtogeojson (install with `npm install osmtogeojson`)
  - shapely (install with `sudo pip install shapely`)
"""

import csv
import json
import os
import shutil
import subprocess
import sys

from collections import defaultdict, OrderedDict
from urllib.parse import quote_plus
from urllib.request import URLopener
from shapely.geometry import shape

from django.core.management.base import BaseCommand

def download_data(admin_level, plz_regex_string, filename):
    bbox = '48.07303233901773,11.348190307617188,48.25028349849019,11.73614501953125'
    query = 'rel(' +bbox + ')[boundary=administrative][admin_level={}]; out geom;'.format(admin_level) + \
            'rel(' +bbox + ')[boundary=postal_code][postal_code~"{}"]; out geom;'.format(plz_regex_string)

    file = URLopener()
    file.retrieve('http://overpass-api.de/api/interpreter?data=' + quote_plus(query), filename)

def convert_to_geojson(infile, outfile):
    if shutil.which("osmtogeojson"):
        executable = "osmtogeojson"
    elif os.path.isfile("node_modules/osmtogeojson/osmtogeojson"):
        executable = "node_modules/osmtogeojson/osmtogeojson"
    else:
        raise FileNotFoundError("You need to install osmtogeojson with `npm install osmtogeojson`")

    with open(outfile, 'w') as out:
        subprocess.call([executable, infile], stdout=out)

def parse_file(filename):
    with open('bezirksteile-plz.geojson', encoding='utf-8') as data_file:
        data = json.load(data_file)

    plz = {}
    for plz_boundary in data['features']:
        if 'boundary' in plz_boundary['properties'] and plz_boundary['properties']['boundary']  == 'postal_code':
            name = plz_boundary['properties']['postal_code']
            plz[name] = shape(plz_boundary['geometry'])

    bezirksteile = {}
    for bezirksteil_boundary in data['features']:
        if 'boundary' in bezirksteil_boundary['properties'] and bezirksteil_boundary['properties']['boundary']  == 'administrative':
            name = bezirksteil_boundary['properties']['name'].replace('Bezirksteil ', '')
            bezirksteile[name] = shape(bezirksteil_boundary['geometry'])

    return plz, bezirksteile

def get_intersections(plz, bezirksteile):
    intersections = []
    for plz_name, plz_shape in plz.items():
        for bezirksteil_name, bezirksteil_shape in bezirksteile.items():
            # calculate the percentage of this postal code are covered by this bezirksteil
            percentage = plz_shape.intersection(bezirksteil_shape).area / plz_shape.area
            if percentage > 0:
                intersections.append([plz_name, bezirksteil_name, percentage])

    return intersections

def write_to_python_file(intersections, plz, bezirksteile, filename):
    
    mapping = defaultdict(list)
    for plz_, bezirksteil_, _ in intersections:
        mapping[plz_].append(bezirksteil_)

    # sort the stadtbezirke alphabetically
    for _, i in mapping.items():
        i.sort()

    # sort the postal codes
    mapping = OrderedDict(sorted(mapping.items(), key=lambda t: t[0]))
    
    # append the result to a django settings file, by default preconfig.py
    with open(filename, 'w') as python_file:
        python_file.write("\n")
        python_file.write("# The following entries are generated by `./manage.py create_plz_mapping`\n")
        python_file.write("PLZ = " + str(list(sorted(plz.keys()))) + "\n")
        python_file.write("BEZIRKSTEILE = " + str(list(sorted(bezirksteile.keys()))) + "\n")

        python_file.write("PLZ_MAPPING = {\n")
        python_file.write("\n".join("    {}: {},".format(k, v) for k, v in mapping.items()) + "\n")
        python_file.write("}\n\n");


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--python-filename', default="settings/plz_mapping.py", help='The file where the mapping should be written to so django can use it for its settings')
        parser.add_argument('--overpass-filename', default="bezirksteile-plz.osm", help='The file to save the result of the overpass query')
        parser.add_argument('--geojson-filename', default="bezirksteile-plz.geojson", help='The filename for the overpass answr converted to geojson')

    def handle(self, *args, **options):
        download_data(10, "8[01].+", options['overpass_filename'])
        convert_to_geojson(options['overpass_filename'], options['geojson_filename'])
        plz, bezirksteile = parse_file(options['geojson_filename'])
        intersections = get_intersections(plz, bezirksteile)
        write_to_python_file(intersections, plz, bezirksteile, options['python_filename'])

        print("Done: {} intersections found".format(len(intersections)))