# Copyright 2017 Steve 'Ashcrow' Milner
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
"""
Consul registry specific code.
"""

import requests
import random

from micro_client.common import _Registry, _Service


class Registry(_Registry):

    def __init__(self, endpoint='http://127.0.0.1:8500/v1', session=None):
        self.svcs_endpoint = '{}/catalog/services'.format(endpoint)
        self.service_endpoint = '{}/catalog/service/'.format(endpoint)
        self._session = session or requests.Session()

    def connect(self):
        assert self._session.get(self.svcs_endpoint)

    def resolve(self, name):
        registered = self._session.get(
            '{}{}'.format(self.service_endpoint, name))
        svc_info = random.choice(registered.json())
        return Service(svc_info)


class Service(_Service):

    def __init__(self, data):
        self._data = data

    @property
    def name(self):
        return self._data['ServiceName']

    @property
    def version(self):
        return ''

    @property
    def metadata(self):
        return self._data

    @property
    def id(self):
        return self._data['ServiceID']

    @property
    def address(self):
        return self._data['ServiceAddress']

    @property
    def port(self):
        return self._data['ServicePort']

    @property
    def node_metadata(self):
        return self._data['NodeMeta']
