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
Common code used through the codebase.
"""

import grpc


class _Registry:

    def __init__(self, args, **kwargs):
        raise NotImplementedError()

    def connect(self):
        raise NotImplementedError()

    def resolve(self, name):
        raise NotImplementedError()


class _Service:

    def __init__(self, data):
        self._data = data

    @property
    def name(self):
        raise NotImplementedError()

    @property
    def version(self):
        raise NotImplementedError()

    @property
    def metadata(self):
        raise NotImplementedError()

    @property
    def id(self):
        raise NotImplementedError()

    @property
    def address(self):
        raise NotImplementedError()

    @property
    def node_metadata(self):
        raise NotImplementedError()


class Services:

    def __init__(self, registry):
        self._registry = registry
        self._registry.connect()

    def resolve(self, name):
        return self._registry.resolve(name)

    def insecure(self, name, stubCls):
        channel = grpc.insecure_channel(self.resolve(name).address)
        return stubCls(channel)
