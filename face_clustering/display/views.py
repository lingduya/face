#coding:utf-8
#from django.http import HttpResponse

#def index(request):
    #return HttpResponse(u"图片加载成功！")

from django.shortcuts import render
import os
import numpy as np
'''
def home(request):
    path_thumbnail = "/Users/jinzhenya/Desktop/face_clustering/display/thumbnail/"
    ids = os.listdir(path_thumbnail)
    #ids = list(ids1).sort()
    print(ids)
    #List = map(str, range(100))# 一个长度为100的 List
    return render(request, 'home.html', {'ids1': ids})
'''
'''
def home(request):
    path_thumbnail = "/Users/jinzhenya/Desktop/face_clustering/display/static/images/"
    ids = os.listdir(path_thumbnail)
    print(ids)
    d = {}
    for id in ids:
        d[id] = len(os.listdir(path_thumbnail + id))
    print (d)
    for k,v in d.items():
        print (k,v)
    return render(request, 'home.html', {'d1': d.items()})


def home(request):
    path_thumbnail = "/Users/jinzhenya/Desktop/face_clustering/display/static/images/"
    ids = os.listdir(path_thumbnail)

    d = {}
    for id in ids:
        pictures = os.listdir(path_thumbnail + id)
        d[id] = [len(pictures),np.random.choice(pictures)]
        
    for k,v in d.items():
        print ('id:',k)
        print ('num_pictures:',v[0])
        print ('name_picture:',v[1])
    return render(request, 'home.html', {'d1': d.items()})'''

def home(request):
    path_thumbnail = "display/static/images/"
    ids = os.listdir(path_thumbnail)
    d = {}
    for id in ids:
        pictures = os.listdir(path_thumbnail + id)
        d[id] = [len(pictures), np.random.choice(pictures)]

    parameters = []
    for k, v in d.items():
        parameters.append([k,v[0],v[1]])
    return render(request, 'home.html', {'d1':parameters})

def second(request):
    files = [f for f in os.listdir('./display/static/images/1')]
    print (files)
    return render(request, 'second.html')