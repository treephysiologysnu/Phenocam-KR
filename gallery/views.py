import os
from django.shortcuts import render
from mysite.settings import BASE_DIR

def read_site_list():
    file_path = os.path.join(BASE_DIR, 'data')
    return os.listdir(file_path)

def read():
    result = dict()
    site_list = read_site_list()
    for site in site_list:
        file_path = os.path.join(BASE_DIR, "data", site)
        try:
            year_list = os.listdir(file_path)
            year_list.remove('metadata')
        except:
            os.mknod(os.path.join(file_path, 'metadata'))
        finally:
            max_year = max(year_list)
        file_path = os.path.join(file_path, max_year)
        max_month = max(os.listdir(file_path))
        file_path = os.path.join(file_path, max_month)
        file_list = os.listdir(file_path)
        file_list.sort()
        result[site] = os.path.join('data', site, max_year, max_month, file_list.pop())
    return result

def index(request):
    site_list = read()
    context = {
        'site_list' : site_list,
    }
    return render(request, 'gallery/index.html', context)