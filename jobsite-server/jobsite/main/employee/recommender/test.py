import sys
import pickle
import time
# sys.path.append(r'C:\Users\huynhhao\Desktop\job_recommender')
# sys.path.append(r'C:\Users\huynhhao\Desktop\job_recommender\recommender\core')

import pandas as pd
import numpy as np

import job_recommender
from network_builder import *
import latent_semantic_analysis

def load_recommender():
    graphpath =  '../../data/network_data/graph.pkl'
    lsapath = '../../data/network_data/lsa.pkl'
    with open(graphpath, 'rb') as f:
        G = pickle.load(f)

    with open(lsapath, 'rb') as f:
        lsa = pickle.load(f)

    jrec = job_recommender.JobRecommender(G, lsa)

    return jrec

all_expertises = ['Java Developer', 'Testing', 'DevOps Engineer', 'Python Developer',
       'Web Designing', 'Hadoop', 'Blockchain', 'ETL Developer',
       'Operations Manager', 'Data Science', 'Mechanical Engineer',
        'Database', 
        'Business Analyst', 'DotNet Developer', 'Automation Testing',
       'Network Security Engineer', 'SAP Developer', 'Civil Engineer',
       ]
       

jrec = load_recommender()
user_data = {}

def test():
    num_recommend = 30
    personalized_results = jrec.rank_nodes(False, jrec.target_node, 'job', 0.85)
    personalized_results = {key:item for i, (key,item) in enumerate(personalized_results.items()) if i < num_recommend}     
    
    for key, value in personalized_results.items():
        job_node = jrec.G.nodes[key]
        company_id = job_node['company_id']
        logo = jrec.G.nodes[company_id]['logo_link']
        
        print(job_node['job_name'])
        
        
test()