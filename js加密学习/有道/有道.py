import execjs
js='''
var e = "b";
 var r = function(e) {
        var t = n.md5(navigator.appVersion)
          , r = "" + (new Date).getTime()
          , i = r + parseInt(10 * Math.random(), 10);
        return {
            ts: r,
            bv: t,
            salt: i,
            sign: n.md5("fanyideskweb" + e + i + "]BjuETDhU)zqSxf-=B#7m")
        }
    };
'''

data=execjs.compile(js).call()
print(data)