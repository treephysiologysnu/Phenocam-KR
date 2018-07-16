import csv
import os
from django.shortcuts import render
from mysite.settings import BASE_DIR

'''
File Format in metadata files
site_name
lat
long
'''


def read_metadata(site_name):
    result = dict()
    meta_path = os.path.join(BASE_DIR, 'data', site_name, 'metadata')
    f = open(meta_path, 'r', encoding='utf-8')
    reader = csv.reader(f)
    for line in reader:
        result[line[0]] = line[1]
        print(line[0])
        print(line[1])
    f.close()
    return result

def index(request, site_name):
    context = read_metadata(site_name)
    return render(request, 'sites/index.html', context)