import json
from math import dist
import pandas as pd
from scipy.spatial import distance_matrix
import math
import os


for problem in [ instance.replace('.TXT','') for instance in os.listdir('source') ]:
    instance = dict()
    lines = []
    with open('./source/{}.TXT'.format(problem)) as file:
        index = 0
        for line in file:
            if index == 4:
                max_vehicle_number = int(line.strip().split(None,1)[0])
                vehicle_capacity = int(line.strip().split(None,1)[1])
            if index < 9:
                index = index + 1
                continue
            lines.append(line.strip().split(None , 1)[1].split("       "))
            
    instance['depart'] = {
        "x" : int(lines[0][0].strip()),
            "y" : int(lines[0][1].strip()),
        "demand" : int(lines[0][2].strip()),
        "due_time" : int(lines[0][3].strip()),
        "ready_time" : int(lines[0][4].strip()),
        "service_time" : int(lines[0][5].strip())
    }

    lines.pop(0)

    for i in range(len(lines)):
        instance["customer_{}".format(i + 1)] = {
        "x" : int(lines[i][0].strip()),
        "y" : int(lines[i][1].strip()),
        "demand" : int(lines[i][2].strip()),
        "due_time" : int(lines[i][3].strip()),
        "ready_time" : int(lines[i][4].strip()),
        "service_time" : int(lines[i][5].strip())
    }
    
    df =pd.DataFrame(instance).T
    
    distance_matrix = []

    for i in range(len(df['x'].values)):
        distance_matrix.append([])
        for j in range(len(df['y'].values)):
            distance_matrix[i].append(math.sqrt(math.pow(df['x'].values[i] - df['x'].values[j] , 2) + math.pow(df['x'].values[i] - df['y'].values[j] , 2)))

    instance['distance_matrix'] = distance_matrix

    instance['number_cust'] = len(distance_matrix) - 1
    instance['instance_name'] = problem

    instance['max_vehicle_number'] = max_vehicle_number
    instance['vehicle_capacity'] = vehicle_capacity

    with open('json/{}.json'.format(problem),"w+") as file:
        json.dump(instance,file)