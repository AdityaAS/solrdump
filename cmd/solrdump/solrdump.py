# -*- coding: utf-8 -*-
# @Author: AdityaAS
# @Date:   2018-06-21 17:19:21
# @Last Modified by:   AdityaAS
# @Last Modified time: 2018-06-22 01:47:09

import json
import os
import argparse
import requests

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--server', type=str, default="http://10.24.28.113:8983/")
parser.add_argument('--collection', type=str)
parser.add_argument('--fields', type=str, default="*")
parser.add_argument('--query', type=str, default="*:*")
parser.add_argument('--rows', type=int, default=2000)
parser.add_argument('--sort', type=str, default="indexed_at asc, id asc")
parser.add_argument('--output', type=str, default="SolrDump.txt")
parser.add_argument('--verbose', type=bool, default=False)
parser.add_argument('--limit', type=int, default=None)
parser.add_argument('--startCursorMark', type=str, default="*")


args = parser.parse_args()

print(args)

fout = open(args.output, 'w')

startCursorMark = args.startCursorMark
cursorMark = startCursorMark
lastCursorMark = cursorMark
total = 0

limit = args.limit


while True:
	payload = {'q':args.query, 'fl': args.fields, 'rows':args.rows, 'sort':args.sort, 'cursorMark':cursorMark, 'wt':'json'}
	result = requests.get(args.server+'solr/'+args.collection+'/select', params=payload)
	response = result.json()

	total += len(response['response']['docs'])
	
	for doc in response['response']['docs']:
		doc_str = json.dumps(doc)
		# Do Corenlp Stuff here
		# Save Corenlp outputs in ES here
		# Build chunks and do stuff parallely instead of sequentially here
		fout.write(doc_str + '\n')

	print("Fetched %s docs" % str(total))
	lastCursorMark = cursorMark
	cursorMark = response['nextCursorMark']

	if (limit != None and total >= limit) or cursorMark == startCursorMark:
		fout.close()
		print(lastCursorMark)
		break