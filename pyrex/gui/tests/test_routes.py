from ..views import web_frontend
import unittest
import webtest


test_app = webtest.TestApp(web_frontend)


routes = {
    'index': '/',
    'contract_list': '/contracts',
    'contract_details': '/contract/1230123',
    'contract_trade_details': '/contract/1230123/trade/1230123',
}


class RoutesTest(unittest.TestCase):
    pass


def route_test_wrapper(route):
    def fixture(self):
        resp = test_app.get(route)
        assert resp.status_int == 200
        assert resp.content_type == 'text/html'
        assert resp.content_length > 0
    return fixture


for route_name, route in routes.items():
    setattr(RoutesTest, f'test_{route_name}', route_test_wrapper(route))


if __name__ == '__main__':
    unittest.main()
