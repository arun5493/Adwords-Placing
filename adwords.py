import numpy as np
import pandas as pd
import sys
import csv
import random
import math

# The path to the data folder should be given as input
if len(sys.argv) != 2:
    print('Please enter in the form python adwords.py greedy/msvv/balance')
    sys.exit(1)
method = sys.argv[1]

if(method != "greedy" and method!='msvv' and method!='balance'):
	print('Please choose from greedy or msvv or balance')

# Reading the vectors from the given csv files
bidder_dataset = pd.read_csv('bidder_dataset.csv' ,names=['advertiser', 'keyword', 'bid_value', 'budget'])

advertiser_budget = {}
query_list = []
query_bid = {}

f = open('queries.txt','r')
reader = csv.reader(f)
for row in reader:
	query_list.append(row[0])
#print len(query_list)

f = open('bidder_dataset.csv','rb')
reader = csv.reader(f)
next(reader,None)

for row in reader:
	#if row[0] not in advertiser_budget:
	#	advertiser_budget[row[0]]=0
	if row[3] !='':
		advertiser_budget[row[0]]=float(row[3])
#print advertiser_budget

f = open('bidder_dataset.csv','rb')
reader = csv.reader(f)
next(reader,None)

for row in reader:
	tmp = []
	if row[1] not in query_bid:
		query_bid[row[1]]=[]
	tmp = [row[0],float(row[2])]	
	query_bid[row[1]].append(tmp)	
#print len(query_bid)


def greedy(query_list,advertiser_budget,query_bid):
	revenue = 0
	for query in query_list:
		#revenue= 0 
		max_bidder = ''
		max_bid = -5.0
		
		for lst in query_bid[query]:
				
			if max_bid < float(lst[1]):
				if float(advertiser_budget[lst[0]]) >= float(lst[1]): 
					max_bid = float(lst[1])
					max_bidder = lst[0]

		if max_bidder!='':
			advertiser_budget[max_bidder] = float(advertiser_budget[max_bidder]) - float(max_bid)	
			revenue =  revenue + max_bid
	#print count
	return revenue

def balance(query_list,advertiser_budget,query_bid):
	
	revenue = 0
	for query in query_list:
		max_bidder = ''
		max_budget = -5.0
		
		for lst in query_bid[query]:
			if ((advertiser_budget[lst[0]] >= lst[1]) and (max_budget < advertiser_budget[lst[0]])): 
				max_budget = advertiser_budget[lst[0]]
				max_bid = lst[1]
				max_bidder = lst[0]

		if max_bidder!='' :
			advertiser_budget[max_bidder] = advertiser_budget[max_bidder] - max_bid	
			revenue =  revenue + max_bid

	return revenue


def msvv(query_list,advertiser_budget_unmodified,query_bid,advertiser_budget_modified):
	
	revenue = 0
	for query in query_list:
		max_bidder = ''
		winner_value = -5.0
		
		for lst in query_bid[query]:

			if ( advertiser_budget_modified[lst[0]] >= lst[1] ) :
			 	tmp = advertiser_budget_unmodified[lst[0]] - advertiser_budget_modified[lst[0]]
			 	fraction = tmp/advertiser_budget_unmodified[lst[0]]
			 	intermediate_val = 1- math.exp(fraction-1)
			 	
			 	if winner_value <= (lst[1]*intermediate_val) :  
					max_bid = lst[1]
					max_bidder = lst[0]
					winner_value =  lst[1]*intermediate_val

		if max_bidder!='' :
			advertiser_budget_modified[max_bidder] = advertiser_budget_modified[max_bidder] - max_bid	
			revenue =  revenue + max_bid

	return revenue

random.seed(0)

if method=='greedy':
	print greedy(query_list,advertiser_budget.copy(),query_bid.copy())
	revenue = 0
	for i in range(0, 100) :
		random.shuffle(query_list)
		revenue += greedy(query_list, advertiser_budget.copy(), query_bid.copy())
	revenue = revenue / 100
	optimal = 0
	for keys in advertiser_budget:
		optimal+=advertiser_budget[keys]
	print float(revenue) / float(optimal)

elif method == 'balance':
	print balance(query_list,advertiser_budget.copy(),query_bid.copy())
	revenue = 0
	for i in range(0, 100) :
		random.shuffle(query_list)
		revenue += balance(query_list, advertiser_budget.copy(), query_bid.copy())
	revenue = revenue / 100
	optimal = 0
	for keys in advertiser_budget:
		optimal+=advertiser_budget[keys]

	print float(revenue) / float(optimal)

elif method == 'msvv':	
	print msvv(query_list,advertiser_budget.copy(),query_bid.copy(),advertiser_budget.copy())
	revenue = 0
	for i in range(0, 100) :
		random.shuffle(query_list)
		revenue += msvv(query_list, advertiser_budget.copy(), query_bid.copy(),advertiser_budget.copy())
	revenue = revenue / 100
	optimal = 0
	for keys in advertiser_budget:
		optimal+=advertiser_budget[keys]

	print float(revenue) / float(optimal)
