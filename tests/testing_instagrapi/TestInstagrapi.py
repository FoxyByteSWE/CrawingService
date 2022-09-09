import unittest


from crawler.InstagrapiUtils import InstagrapiUtils
from crawler.media.FoxyByteMedia import FoxyByteMedia
from instagrapi import types


class TestInstagrapi(unittest.TestCase):
    def setUp(self) -> None:
        self.instagrapi = InstagrapiUtils()

    def test_loadCookies(self):
        self.assertEqual(self.instagrapi.loadCookies(),
            {"uuids": {"phone_id": "19fd873a-165b-49ce-8fd7-822571400339", 
                        "uuid": "cb5be7f9-5a34-457e-9fbc-bd8583539415", 
                        "client_session_id": "a5583b19-210a-447d-ba35-c71daa196ad0", 
                        "advertising_id": "ea471400-df95-433c-aeef-5ac48de7b414", 
                        "android_device_id": "android-00e13894c1e74e9a", 
                        "request_id": "ebab8430-0023-485e-bc22-d15e53f924bc", 
                        "tray_session_id": "4393b7fe-129b-480c-89fb-b4054214a0f0"}, 
            "mid": "Ywt9aQABAAHjIUa_3NBvy3tfsv9W", 
            "ig_u_rur": "null", 
            "ig_www_claim": "null", 
            "authorization_data": {"ds_user_id": "53184308084", 
                                    "sessionid": "53184308084%3AvpM1UVQYyVyTxm%3A0%3AAYcpmt0QT2Q2LCVHiJ2-g5u4UwFvwlbz8tku88sEsQ"}, 
            "cookies": {}, 
            "last_login": 1661697456.3865955, 
            "device_settings": {"app_version": "203.0.0.29.118", 
                                "android_version": 26, 
                                "android_release": "8.0.0", 
                                "dpi": "480dpi", 
                                "resolution": "1080x1920", 
                                "manufacturer": "Xiaomi", 
                                "device": "capricorn", 
                                "model": "MI 5s", 
                                "cpu": "qcom", 
                                "version_code": "314665256"}, 
            "user_agent": "Instagram 203.0.0.29.118 Android (26/8.0.0; 480dpi; 1080x1920; Xiaomi; MI 5s; capricorn; qcom; en_US; 314665256)", 
            "country": "US", 
            "country_code": 1, 
            "locale": "en_US", 
            "timezone_offset": -14400})

    def getLocationPkCodeFromName(self):
        self.assertEqual(self.instagrapi.getLocationPkCodeFromName("Farina del mio sacco"),1788391034730029)

    def getMostRecentMediasFromLocation(self):
        self.assertEqual(type(self.instagrapi.getMostRecentMediasFromLocation()), list[types.Media])


