import random
import requests
from utils.builder import Builder


class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def _request(self, method, location, headers=None, params=None, json=None):
        url = location
        response = self.session.request(method=method, url=url, headers=headers, json=json, params=params)
        return response

    def get_status(self):
        url = 'http://petstore.swagger.io/v2'
        res = self._request("GET", location=url)
        return res

    def rand_pet_pattern(self, id="0", category_id="0", category_name=Builder.fake_username(), name=Builder.fake_name(),
                         tags_id="0", tags_name=Builder.fake_username(), status=random.choice(['available', 'pending',
                                                                                               'sold'])):
        json_pattern_pet = {
            "id": id,
            "category": {
                "id": category_id,
                "name": f"{category_name}"
            },
            "name": f"{name}",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": tags_id,
                    "name": f"{tags_name}"
                }
            ],
            "status": f"{status}"
        }

        return json_pattern_pet

    def create_pet(self, id="0", category_id="0", category_name=Builder.fake_username(), name=Builder.fake_name(),
                   tags_id="0", tags_name=Builder.fake_username(), status=random.choice(['available', 'pending',
                                                                                         'sold'])):
        url = "https://petstore.swagger.io/v2/pet"
        json = ApiClient.rand_pet_pattern(self, id=id, category_id=category_id, category_name=category_name, name=name,
                                          tags_id=tags_id, tags_name=tags_name, status=status)
        result = self._request('POST', location=url, json=json)
        return result

    def delete_pet(self, id_pet):
        url = f'https://petstore.swagger.io/v2/pet/{id_pet}'
        json = {'id': f'{id_pet}'}
        result = self._request('DELETE', location=url, json=json)
        return result

    def create_user(self, username=Builder.fake_username(), firstName=Builder.fake_name(), lastName=Builder.fake_name(),
                    email=Builder.fake_email(), password=Builder.fake_name(), phone=Builder.fake_phone_number()):
        url = 'https://petstore.swagger.io/v2/user'
        json = {
            "username": f"{username}",
            "firstName": f"{firstName}",
            "lastName": f"{lastName}",
            "email": f"{email}",
            "password": f"{password}",
            "phone": f"{phone}",
            "userStatus": 0
        }
        result = self._request('POST', location=url, json=json)
        return result

    def find_pet_by_id(self, id):
        url = f'https://petstore.swagger.io/v2/pet/{id}'
        result = self._request('GET', location=url)
        return result

    def update_existing_pet(self, id="0", category_id="0", category_name=Builder.fake_username(), name=Builder.fake_name(),
                   tags_id="0", tags_name=Builder.fake_username(), status=random.choice(['available', 'pending',
                                                                                         'sold'])):
        url = 'https://petstore.swagger.io/v2/pet'
        json = ApiClient.rand_pet_pattern(self, id=id, category_id=category_id, category_name=category_name, name=name,
                                          tags_id=tags_id, tags_name=tags_name, status=status)
        result = self._request('PUT', location=url, json=json)
        return result
