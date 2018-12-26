# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 15:43:11 2018

@author: edup_
"""

from flask import Flask, jsonify, request

server = Flask("Graph Server is Running")

@server.route('/upload_graph', methods=['POST'])
def upload_graph():
    graph_body = request.get_json()
    return jsonify(graph_body)

@server.route('/degrees-of-separation/<origin>/<destination>', methods=['GET'])
def find_degrees_of_separation(origin, destination, graph='', path=[]):
        
    graph = request.get_json()
    
    path = path + [origin]
    
    if origin == destination:
        return jsonify(len(path)-1)
    
    if origin not in graph:
        return jsonify(None)
    
    for node in graph[origin]:
        if node not in path:
            newpath = find_degrees_of_separation(node, destination, graph, path)
            if newpath is not None:
                return newpath
  
    return jsonify(None)
                
server.run()