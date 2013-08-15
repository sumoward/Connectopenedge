"""
Brian Ward
Principal Systems
13/08/2013
"""

import requests
import xml.etree.ElementTree as ET

URL1 = 'https://www.rollbase.com/rest/api/login?'
USER = 'sumoward'
PASS = 'WildfireSheep'
CUSTid = 75651266


class Progress_Python:

    def api_connect(self):
        payload = {'loginName': USER, 'password': PASS, 'custid': CUSTid}
        #connect with post
        r = requests.post(URL1, data=payload)
        xml = r.text
        return xml

    def parse_xml(self, source_xml):
        root = ET.fromstring(source_xml)
        return root[0].text

    def query(self, sessionId):
        URL_getBuildStatus = 'http://www.rollbase.com/rest/api/getBuildStatus?'
        payload = {'sessionId': sessionId}
        r = requests.get(URL_getBuildStatus, params=payload)
        return r.text

    def api_logout(self, sessionId):
        URL_logout = 'http://www.rollbase.com/rest/api/logout?'
        payload = {'sessionId': sessionId}
        r = requests.get(URL_logout, params=payload)
        return r.text

if __name__ == "__main__":
    print('*' * 40)
    tester1 = Progress_Python()
    source_xml = tester1.api_connect()
    sessionId = tester1.parse_xml(source_xml)
    print(sessionId)
    print('*' * 40)
    build_status = tester1.query(sessionId)
    print(build_status)
    print('*' * 40)
    bye = tester1.api_logout(sessionId)
    print(bye)
