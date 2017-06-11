
from django.test import (
    TestCase,
    Client,
)


class MainTest(TestCase):
    def test_main(self):
        client = Client()
        r = client.get("/")
        self.assertTrue(r.is_rendered)
        self.assertEqual(r.status_code, 200)
