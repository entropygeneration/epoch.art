import requests
import json
import datetime

# cet price of ADA
def get_quote(base_url, currency):
	url = f'{base_url}/quotes/{currency}' # currency = 'ADA'
	r = requests.get(url)
	if r.status_code == 200:
		return json.loads(r.text)
	else:
		print(r.status_code)
		print(r.text)
	
# get individual asset for a collection
def get_assets(base_url, asset_id):
	url = f'{base_url}/assets/{asset_id}'
	r = requests.get(url)
	
	if r.status_code == 200:
		return json.loads(r.text)
	else:
		print(r.status_code)
		print(r.text)

# get base collection info & traits
def get_base_collection(base_url, policy_id):
	url = f'{base_url}/asset-collections/{policy_id}'
	r = requests.get(url)
	
	if r.status_code == 200:
		return json.loads(r.text)
	else:
		print(r.status_code)
		print(r.text)

# get assets from a collection
# sort = recent, cheapest, expensive
# onlyVerified=1
# &traits=Eyes.Heartbreaker%2CPhase.Waxing+Crescent+Moon
def get_collection(base_url, policy_id, page, page_count, query, sort, show_offers):
	url = f'{base_url}/asset-collections/{policy_id}/assets'
	params = {
		'page': str(page),
		'pageCount': str(page_count),
		'query': query,
		'sort': sort,
		'showOffersFirst': str(show_offers)
	}
	r = requests.get(url, params=params)
	
	if r.status_code == 200:
		return json.loads(r.text)
	else:
		print(r.status_code)
		print(r.text)

# get optimized images in webp format
def get_image(policy_id, asset_id):
	url = f'https://assets.epoch.art/{policy_id}/{asset_id}.webp'
	r = requests.get(url)
	
	if r.status_code == 200:
		return r.content
	else:
		print(r.status_code)
		print(r.text)

# https://api.epoch.art/ext/offers?status=sold
# from=03/20/2022
def get_sales(status, policy_id, date):
	url = f'{base_url}/ext/offers'
	params = {
		'status': status,
		'policyId': policy_id,
		'from': date
	}
	r = requests.get(url, params=params)
	
	if r.status_code == 200:
		return json.loads(r.text)
	else:
		print(r.status_code)
		print(r.text)

base_url = 'https://api.epoch.art'
policy_id = 'd0112837f8f856b2ca14f69b375bc394e73d146fdadcc993bb993779'
asset_id = 'd0112837f8f856b2ca14f69b375bc394e73d146fdadcc993bb993779446973636f536f6c6172697330383335'
yesterday = (datetime.date.today() - datetime.timedelta(days = 1)).strftime("%m/%d/%Y")

#r = get_quote(base_url, 'ADA')
#r = get_assets(base_url, policy_id)
#r = get_base_collection(base_url, policy_id)
#r = get_collection(base_url, policy_id, 1, 100, '', 'recent', 1)
#r = get_image(policy_id, asset_id)

#r = get_sales('sold', policy_id, yesterday)
r = get_sales('sold', policy_id, '')
#print(r)

for item in r:
	print(item['_id'])
	print(item['sellerStakeAddress'])
	print(item['sellerPaymentAddress'])
	print(item['asset'])
	print(item['assetName'])
	print(item['policyId'])
	print(item['price'])
	print(item['status'])
	print(item['creationDate'])
	if 'buyDate' in item:
		print(item['buyDate'])
	print('')