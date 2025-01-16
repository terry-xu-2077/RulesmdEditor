import js2py
import requests
import re


class baidu_Translate():
    get_sign = js2py.eval_js('''
                var i = null;

                function n(r, o) {
                    for (var t = 0; t < o.length - 2; t += 3) {
                        var a = o.charAt(t + 2);
                        a = a >= "a" ? a.charCodeAt(0) - 87 : Number(a),
                        a = "+" === o.charAt(t + 1) ? r >>> a: r << a,
                        r = "+" === o.charAt(t) ? r + a & 4294967295 : r ^ a
                    }
                    return r
                }
                var hash = function e(r,gtk) {
                    var o = r.match(/[\uD800-\uDBFF][\uDC00-\uDFFF]/g);
                    if (null === o) {
                        var t = r.length;
                        t > 30 && (r = "" + r.substr(0, 10) + r.substr(Math.floor(t / 2) - 5, 10) + r.substr( - 10, 10))
                    } else {
                        for (var e = r.split(/[\uD800-\uDBFF][\uDC00-\uDFFF]/), C = 0, h = e.length, f = []; h > C; C++)"" !== e[C] && f.push.apply(f, a(e[C].split(""))),
                        C !== h - 1 && f.push(o[C]);
                        var g = f.length;
                        g > 30 && (r = f.slice(0, 10).join("") + f.slice(Math.floor(g / 2) - 5, Math.floor(g / 2) + 5).join("") + f.slice( - 10).join(""))
                    }
                    var u = void 0,
                    u = null !== i ? i: (i = gtk || "") || "";
                    for (var d = u.split("."), m = Number(d[0]) || 0, s = Number(d[1]) || 0, S = [], c = 0, v = 0; v < r.length; v++) {
                        var A = r.charCodeAt(v);
                        128 > A ? S[c++] = A: (2048 > A ? S[c++] = A >> 6 | 192 : (55296 === (64512 & A) && v + 1 < r.length && 56320 === (64512 & r.charCodeAt(v + 1)) ? (A = 65536 + ((1023 & A) << 10) + (1023 & r.charCodeAt(++v)), S[c++] = A >> 18 | 240, S[c++] = A >> 12 & 63 | 128) : S[c++] = A >> 12 | 224, S[c++] = A >> 6 & 63 | 128), S[c++] = 63 & A | 128)
                    }

                    for (
                    var p = m,F = "+-a^+6", D = "+-3^+b+-f", b = 0;
                    b < S.length; b++) p += S[b],p = n(p, F);

                    return p = n(p, D),
                    p ^= s,
                    0 > p && (p = (2147483647 & p) + 2147483648),
                    p %= 1e6,
                    p.toString() + "." + (p ^ m)
                }
            ''')

    def __init__(self):
        headers = {
            'referer': 'https://fanyi.baidu.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'}
        self.session = requests.Session()
        self.session.get('https://fanyi.baidu.com', headers=headers)
        response = self.session.get('https://fanyi.baidu.com', headers=headers)
        self.token = re.findall("token: '(.*?)',", response.text)[0]
        self.gtk = re.findall("window.gtk = '(.*?)';", response.text, re.S)[0]

    def fanyi(self, query: str, from_lang='en', to_lang='zh'):
        # 连续翻译请延时1秒
        data = {
            'from': from_lang,
            'to': to_lang,
            'query': query,
            'transtype': 'realtime',
            'simple_means_flag': '3',
            'sign': self.get_sign(query, self.gtk),
            'token': self.token,
            'domain': 'common'
        }
        response = self.session.post(
            'https://fanyi.baidu.com/v2transapi?from={0}&to={1}'.format(from_lang, to_lang),
            data=data
        )
        try:
            return response.json()['trans_result']['data'][0]['dst']
        except:
            if response.headers.get('Server') == 'yunjiasu':
                print('好像暂时被封了...')
            else:
                print(response.json())
            return

    def close(self):
        self.session.close()
