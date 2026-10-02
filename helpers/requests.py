import json
import time

import requests
from os.path import dirname, join

from gql import Client
from jsonschema.validators import validate

from helpers.configuration import Configuration
import allure

class APIRequests:
    rest_uri = Configuration.base_url

    def __init__(self):
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        self._token = None

    def _get_result(self, response):
        try:
            data = response.json()
        except ValueError:
            data = response.text
        return {
            'data': data,
            'status_code': response.status_code
        }

    def _load_json_schema(self, filename):
        relative_path = join('../test_data/schemas', filename)
        absolute_path = join(dirname(__file__), relative_path)

        with open(absolute_path) as schema_file:
            return json.loads(schema_file.read())

    @allure.step("Get Request")
    def get(self, resource_path, params=None):
        response = requests.get(self.rest_uri + resource_path, params=params, headers=self.headers)
        return self._get_result(response)

    @allure.step("Post Request")
    def post(self, resource_path, request):
        response = requests.post(self.rest_uri + resource_path, json=request, headers=self.headers)
        return self._get_result(response)

    @allure.step("Delete Request")
    def delete(self, resource_path):
        self.refresh_token()
        header = {"Cookie": f"token={self._token}"}
        response = requests.delete(self.rest_uri + resource_path, headers=header)
        return response.status_code

    @allure.step("Schema Validation")
    def assert_valid_schema(self, data, schema_file):
        return validate(data, schema_file)

    def refresh_token(self):
        credentials = {
            "username": Configuration.auth_username,
            "password": Configuration.auth_password,
        }
        response = requests.post(self.rest_uri + "/auth", json=credentials, headers=self.headers)
        self._token = response.json()["token"]
