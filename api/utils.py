import requests, os
from dotenv import load_dotenv

load_dotenv()


def get_additional_data(email):
    headers = {
        'Authorization': 'Bearer {}'.format(os.getenv('CLEARBIT_API_KEY')),
    }
    params = {
        'email': email,
    }
    r = requests.get(url='https://person.clearbit.com/v2/combined/find', headers=headers, params=params)
    result = r.json()
    if 'error' in result:
        return False
    return result['person']['name']['givenName'], result['person']['name']['familyName']


def check_email(email):
    params = {
        'api_key': os.getenv('HUNTER_API_KEY'),
        'email': email,
    }
    r = requests.get(url='https://api.hunter.io/v2/email-verifier', params=params)
    result = r.json()
    if 'errors' in result:
        return False
    return True
