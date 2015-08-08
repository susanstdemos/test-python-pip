# Copyright (c) 2015 Uber Technologies, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:tornado,dynamic,slots,dynexc=VCRThriftError,dynbase=VCRThriftBase,dynimport=from tchannel.testing.vcr.thrift import *
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from tchannel.testing.vcr.thrift import *

class StatusCode(VCRThriftBase):
  SUCCESS = 0
  FAILURE = 1

  _VALUES_TO_NAMES = {
    0: "SUCCESS",
    1: "FAILURE",
  }

  _NAMES_TO_VALUES = {
    "SUCCESS": 0,
    "FAILURE": 1,
  }

class ArgScheme(VCRThriftBase):
  RAW = 0
  JSON = 1
  THRIFT = 2

  _VALUES_TO_NAMES = {
    0: "RAW",
    1: "JSON",
    2: "THRIFT",
  }

  _NAMES_TO_VALUES = {
    "RAW": 0,
    "JSON": 1,
    "THRIFT": 2,
  }


class TransportHeader(VCRThriftBase):
  """
  Attributes:
   - key
   - value
  """

  __slots__ = [ 
    'key',
    'value',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'key', None, None, ), # 1
    (2, TType.STRING, 'value', None, None, ), # 2
  )

  def __init__(self, key=None, value=None,):
    self.key = key
    self.value = value

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.key)
    value = (value * 31) ^ hash(self.value)
    return value


class Request(VCRThriftBase):
  """
  Attributes:
   - serviceName
   - endpoint
   - headers
   - body
   - hostPort
   - argScheme
   - transportHeaders
  """

  __slots__ = [ 
    'serviceName',
    'endpoint',
    'headers',
    'body',
    'hostPort',
    'argScheme',
    'transportHeaders',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'serviceName', None, None, ), # 1
    (2, TType.STRING, 'endpoint', None, None, ), # 2
    (3, TType.STRING, 'headers', None, "", ), # 3
    (4, TType.STRING, 'body', None, None, ), # 4
    (5, TType.STRING, 'hostPort', None, "", ), # 5
    (6, TType.I32, 'argScheme', None,     0, ), # 6
    (7, TType.LIST, 'transportHeaders', (TType.STRUCT,(TransportHeader, TransportHeader.thrift_spec)), [
    ], ), # 7
  )

  def __init__(self, serviceName=None, endpoint=None, headers=thrift_spec[3][4], body=None, hostPort=thrift_spec[5][4], argScheme=thrift_spec[6][4], transportHeaders=thrift_spec[7][4],):
    self.serviceName = serviceName
    self.endpoint = endpoint
    self.headers = headers
    self.body = body
    self.hostPort = hostPort
    self.argScheme = argScheme
    if transportHeaders is self.thrift_spec[7][4]:
      transportHeaders = [
    ]
    self.transportHeaders = transportHeaders

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.serviceName)
    value = (value * 31) ^ hash(self.endpoint)
    value = (value * 31) ^ hash(self.headers)
    value = (value * 31) ^ hash(self.body)
    value = (value * 31) ^ hash(self.hostPort)
    value = (value * 31) ^ hash(self.argScheme)
    value = (value * 31) ^ hash(self.transportHeaders)
    return value


class Response(VCRThriftBase):
  """
  Attributes:
   - code
   - headers
   - body
  """

  __slots__ = [ 
    'code',
    'headers',
    'body',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'code', None, None, ), # 1
    (2, TType.STRING, 'headers', None, "", ), # 2
    (3, TType.STRING, 'body', None, None, ), # 3
  )

  def __init__(self, code=None, headers=thrift_spec[2][4], body=None,):
    self.code = code
    self.headers = headers
    self.body = body

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.code)
    value = (value * 31) ^ hash(self.headers)
    value = (value * 31) ^ hash(self.body)
    return value


class CannotRecordInteractionsError(VCRThriftError):
  """
  Raised when the record mode for a cassette prevents recording new
  interactions for it.

  Attributes:
   - message
  """

  __slots__ = [ 
    'message',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'message', None, None, ), # 1
  )

  def __init__(self, message=None,):
    self.message = message

  def __str__(self):
    return repr(self)

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.message)
    return value


class RemoteServiceError(VCRThriftError):
  """
  Raised when the remote service throws a protocol error.

  Attributes:
   - code
   - message
  """

  __slots__ = [ 
    'code',
    'message',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.BYTE, 'code', None, None, ), # 1
    (2, TType.STRING, 'message', None, None, ), # 2
  )

  def __init__(self, code=None, message=None,):
    self.code = code
    self.message = message

  def __str__(self):
    return repr(self)

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.code)
    value = (value * 31) ^ hash(self.message)
    return value


class VCRServiceError(VCRThriftError):
  """
  A generic error for VCR exceptions not covered elsewhere.

  Attributes:
   - message
  """

  __slots__ = [ 
    'message',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'message', None, None, ), # 1
  )

  def __init__(self, message=None,):
    self.message = message

  def __str__(self):
    return repr(self)

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.message)
    return value
