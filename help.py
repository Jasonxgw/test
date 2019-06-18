#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib.parse import parse_qsl

__author__ = 'Terry'


def print_headers_raw_to_dict(headers_raw_l):
    print("{\n    '" + ",\n    ".join(map(lambda s: "'" +
                                                    "': '".join(s.strip().split(': ')) + "'", headers_raw_l))[
                       1:-1] + "'\n}")


def print_headers_raw_to_dict_space(headers_raw_l):
    print("{\n    '" + ",\n    ".join(map(lambda s: "'" + "': '".join(s.strip().split('\t')) + "'", headers_raw_l))[
                       1:-1] + "'\n}")


def print_dict_from_copy_headers(headers_raw):
    headers_raw = headers_raw.strip()
    headers_raw_l = headers_raw.splitlines()

    if 'HTTP/1.txt.1.txt' in headers_raw_l[0]:
        headers_raw_l.pop(0)
    if headers_raw_l[0].startswith('Host'):
        headers_raw_l.pop(0)
    if headers_raw_l[-1].startswith('Cookie'):
        headers_raw_l.pop(-1)

    if ':' in headers_raw_l[-1]:
        print_headers_raw_to_dict(headers_raw_l)
    else:
        print_headers_raw_to_dict_space(headers_raw_l)


def print_url_params(url_params):
    s = str(parse_qsl(url_params.strip(), 1))
    print("OrderedDict(\n    " + "),\n    ".join(map(lambda s: s.strip(), s.split("),")))[1:-1] + ",\n)")


if __name__ == '__main__':
    text = '''
__user: 100010894030665
__a: 1
__dyn: 7AgNe-4amaAxd2u6aJGeFxqeCwKyWzEy4aheC267Uqzob4q2i5U4e2C3C2mK9xK5WwIKaxeUW3KFUe8HzobrzogU9A69Ukz8nxm3i3a4E9ohwoU8-1rG7EWq6862um1owhFUhKEtxy5UrwFwgElx-bx-2KfwnEszXG48yq1yGdhUix62PK6UylxfwzAx2cGcBKm4U-4K3-5obV8yEqUpxCcAh9ogVFXAy8aElxeaCzUcUjzbxiEmwAwUzFKcxp2Utwwx-2y8woEcEqw
__req: 17
__be: 1
__pc: PHASED:ufi_home_page_pkg
dpr: 1
__rev: 1000577170
__comet_req: false
fb_dtsg: AQGAQRnZdVi3:AQFsJuS5evEy
jazoest: 22112
__spin_r: 1000577170
__spin_b: trunk
__spin_t: 1554706706
    '''

    print_dict_from_copy_headers(text)

    # url_params = 'username=yiexingtest003%40163.com&password=fdfasf&savelogin=1.txt&url=http%3A%2F%2Fcaipiao.163.com%2Fagent%2FloginAgentV2.htm%3Fcallback%3Dlogin143999647097272&url2=http%3A%2F%2Fcaipiao.163.com%2Fagent%2FloginAgentV2.htm%3Fcallback%3Dlogin143999647097272&product=caipiao&type=1.txt&noRedirect=1.txt'
    # print_headers_raw_to_dict(url_params)
