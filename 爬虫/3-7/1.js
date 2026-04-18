
const  n = require('crypto')

function E(e) {
                return n.createHash("md5").update(e.toString()).digest("hex")
            }

const g = "fanyideskweb"
const h = "webfanyi"


function I(e, t) {
                return E(`client=${g}&mysticTime=${e}&product=${h}&key=${t}`)
            }

function C(e, t) {
                const o = (new Date).getTime();
                return {
                    sign: I(o, e),
                    client: g,
                    product: h,
                    appVersion: "12.0.0",
                    vendor: "web",
                    pointParam: "client,mysticTime,product",
                    mysticTime: "webfanyi.webmain",
                    keyfrom: "fanyi.web",
                    mid: 1,
                    screen: 1,
                    model: 1,
                    network: "wifi",
                    abtest: 0,
                    yduuid: t || "abcdefg"
                }
            }



console.log(C( "t2he2k4m2g6QKRigK0KAmSpXKgAezywG"))

//加密参数解决----发请求，获取响应数据

// 加密参数解决----发请求,获取响应数据
// js文件运行没有报错,获取到了加密参数,那代表加密参数一定没有问题 大错特错
// 你参与加密的参数跟你所携带的参数一定保持一致







