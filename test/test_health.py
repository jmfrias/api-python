import unittest
from http import HTTPStatus
from flask import json

from settings import app
from controller.generics import readJsonFiles

messages = readJsonFiles('messages', 'health')
operations = readJsonFiles('operations', 'health')
results = readJsonFiles('results')

class TestHealth(unittest.TestCase):
    def test_1_health_content(self):
        print("\nTest for content_type JSON")
        tester = app.test_client(self)
        response = tester.get("/health")

        self.assertEqual(response.content_type, "application/json")

    def test_2_health (self):
        print("\nTest for code 200")
        tester = app.test_client(self)
        response = tester.get("/health")
        status = response.status_code

        self.assertEqual(status, HTTPStatus.OK)

    def test_3_health (self):
        print("\nTest for version 1.0")
        tester = app.test_client(self)
        response = tester.get("/health")
        response = json.loads(response.get_data(as_text=True))
        version = response['meta']['version']

        self.assertEqual(version, "1.0")

if __name__ == "__main__":
    unittest.main()