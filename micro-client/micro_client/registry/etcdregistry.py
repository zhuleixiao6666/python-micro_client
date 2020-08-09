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
Etcd registry specific code.
"""
import json
import random

from micro_client.common import _Registry, _Service


class Registry(_Registry):

    def __init__(self, etcd_client, prefix='/micro/registry/'):
        self.etcd_client = etcd_client
        self.prefix = prefix

    def connect(self):
        assert self.etcd_client.status()

    def resolve(self, name):
        registered = self.etcd_client.get_prefix(f'{self.prefix}{name}')
        svc_info = json.loads(random.choice(
            [x for x in registered])[0])
        return Service(svc_info)


class Service(_Service):

    def __init__(self, data):
        self._data = data

    @property
    def name(self):
        return self._data['name']

    @property
    def version(self):
        return self._data['version']

    @property
    def metadata(self):
        return self._data['metadata']

    @property
    def _node(self):
        return random.choice(self._data['nodes'])

    @property
    def id(self):
        return self._node['id']

    @property
    def address(self):
        return self._node['address']

    @property
    def node_metadata(self):
        return self._node['metadata']
