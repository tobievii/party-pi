#!/ usr/bin/python
########### Python 2.7 #############

import http.client
import urllib.request, urllib.parse, urllib.error
import base64
import json
import requests


def emotion_api(url_path):

    body = "{'URL':'" + url_path + "'}"

    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '1cc9418279ff4b2683b5050cfa6f3785',
    }

    params = urllib.parse.urlencode({
    })

    try:
        conn = http.client.HTTPSConnection('api.projectoxford.ai')
        conn.request("POST", "/emotion/v1.0/recognize?%s" %
                     params, body, headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
        json_data = json.loads(data)
        return json_data
    except Exception as e:
        print(("[Errno {0}] {1}".format(e.errno, e.strerror)))
if __name__ == '__main__':
    emotion_api(url_path)
