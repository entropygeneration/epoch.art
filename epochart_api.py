import requests
import json
import datetime

# get price of ADA
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
