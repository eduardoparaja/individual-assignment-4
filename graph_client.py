# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 15:40:18 2018

@author: edup_
"""
import requests 

graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["d"],
    "d": ["e"],
    "e": [],
    "f": []
    }

def upload_graph(graph): 
    data = graph
    request = requests.post("http://127.0.0.1:5000/upload-graph", json=data)
    return request.json()

def get_degrees_of_separation(origin, destination): 
    data = graph
    request = requests.get('http://127.0.0.1:5000/degrees-of-separation/{}/{}'.format(origin, destination), json=data)
    
    return request.json()