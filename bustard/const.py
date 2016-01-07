#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals


# 模板引擎默认支持的内置函数
TEMPLATE_BUILTIN_FUNC_WHITELIST = (
    'all',
    'unicode',
    'isinstance',
    'dict',
    'format',
    'repr',
    'sorted',
    'list',
    'iter',
    'round',
    'cmp',
    'set',
    'bytes',
    'reduce',
    'slice',
    'sum',
    'getattr',
    'abs',
    'hash',
    'len',
    'ord',
    'filter',
    'range',
    'pow',
    'float',
    'divmod',
    'enumerate',
    'basestring',
    'zip',
    'hex',
    'long',
    'next',
    'chr',
    'xrange',
    'type',
    'tuple',
    'reversed',
    'hasattr',
    'delattr',
    'setattr',
    'str',
    'int',
    'unichr',
    'min',
    'any',
    'complex',
    'bool',
    'map',
    'max',
    'object',
    'callable',
)

HTTP_STATUS_CODES = {
    100:    'Continue',
    101:    'Switching Protocols',
    102:    'Processing',
    200:    'OK',
    201:    'Created',
    202:    'Accepted',
    203:    'Non Authoritative Information',
    204:    'No Content',
    205:    'Reset Content',
    206:    'Partial Content',
    207:    'Multi Status',
    226:    'IM Used',              # see RFC 3229
    300:    'Multiple Choices',
    301:    'Moved Permanently',
    302:    'Found',
    303:    'See Other',
    304:    'Not Modified',
    305:    'Use Proxy',
    307:    'Temporary Redirect',
    400:    'Bad Request',
    401:    'Unauthorized',
    402:    'Payment Required',     # unused
    403:    'Forbidden',
    404:    'Not Found',
    405:    'Method Not Allowed',
    406:    'Not Acceptable',
    407:    'Proxy Authentication Required',
    408:    'Request Timeout',
    409:    'Conflict',
    410:    'Gone',
    411:    'Length Required',
    412:    'Precondition Failed',
    413:    'Request Entity Too Large',
    414:    'Request URI Too Long',
    415:    'Unsupported Media Type',
    416:    'Requested Range Not Satisfiable',
    417:    'Expectation Failed',
    418:    'I\'m a teapot',  # see RFC 2324
    422:    'Unprocessable Entity',
    423:    'Locked',
    424:    'Failed Dependency',
    426:    'Upgrade Required',
    428:    'Precondition Required',  # see RFC 6585
    429:    'Too Many Requests',
    431:    'Request Header Fields Too Large',
    449:    'Retry With',  # proprietary MS extension
    451:    'Unavailable For Legal Reasons',
    500:    'Internal Server Error',
    501:    'Not Implemented',
    502:    'Bad Gateway',
    503:    'Service Unavailable',
    504:    'Gateway Timeout',
    505:    'HTTP Version Not Supported',
    507:    'Insufficient Storage',
    510:    'Not Extended'
}
