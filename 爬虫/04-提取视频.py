import os
import requests
from requests_html import HTMLSession

session = HTMLSession()


class KSSpisder(object):
    ospath = os.getcwd() + f"/快手/"
    if not os.path.exists(ospath):
        os.makedirs(ospath)

    def __init__(self):
        """
        爬虫原理的第一步：准备数据
        :return:
        """
        self.start_url = 'https://www.kuaishou.com/graphql'
        self.headers = {
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Cookie': 'kpf=PC_WEB; clientid=3; did=web_9ca6cac1d136582a204fa03ff1c8bf26; ktrace-context=1|MS44Nzg0NzI0NTc4Nzk2ODY5LjM5NDg0NTQ1LjE3NzIyMDE2Mjc2MTUuMTA5MDAzNjg=|MS44Nzg0NzI0NTc4Nzk2ODY5LjMzMTQ1NTM2LjE3NzIyMDE2Mjc2MTUuMTA5MDAzNjk=|0|webservice-user-growth-node|webservice|true|src-Js; kwpsecproductname=kuaishou-vision; kwssectoken=Qpz6ZXSa9AkrKnJvpz6j1hmVp2M7dtejeECSYqtUpIsC7VgIDDqZqypIJ1wBmkg2ipghw+YXDlvTKiolU6Z34A==; kwscode=47ab2e018ffd9a5082f18bdb7573fdbd8685d52802237835ce948df0fea3c848; kwpsecproductname=kuaishou-vision; kwfv1=PnGU+9+Y8008S+nH0U+0mjPf8fP08f+98f+nLlwnrIP9+Sw/ZFGfzY+eGlGf+f+e4SGfbYP0QfGnLFwBLU80mYG9PEP/PMPfr7PBcE+AcMwerAP0PMPePAGnbjG0PUwePM+n+D+nQ0weLMw/DIG0rIG0bY8eH9+0Qj8fzD+/cFwer=; kwssectoken=B5XcfXj62/TmGXBp/wRVuvhe4dX674JOl3mSUKEF9vgjmTEk/QZqlCSsWUyu49KLy8ceY8rv1UUJI3mof4N/gA==; kwscode=acff395a12d69fbbf74338fc5c1c9fd16dd1c2739f087ddebb263ed7d7ccaa24; kpn=KUAISHOU_VISION',
            'Host': 'www.kuaishou.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0',
            'Content-Type': 'application/json'
        }

        self.data = {"operationName":"brilliantTypeDataQuery","variables":{"hotChannelId":"00","page":"brilliant"},"query":"fragment photoContent on PhotoEntity {\n  __typename\n  id\n  duration\n  caption\n  originCaption\n  likeCount\n  viewCount\n  commentCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  disableSensitivePhoto\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  musicBlocked\n  riskTagContent\n  riskTagUrl\n}\n\nfragment recoPhotoFragment on recoPhotoEntity {\n  __typename\n  id\n  duration\n  caption\n  originCaption\n  likeCount\n  viewCount\n  commentCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  musicBlocked\n  riskTagContent\n  riskTagUrl\n}\n\nfragment feedContent on Feed {\n  type\n  author {\n    id\n    name\n    headerUrl\n    following\n    headerUrls {\n      url\n      __typename\n    }\n    verifiedDetail {\n      description\n      iconType\n      newVerified\n      musicCompany\n      type\n      __typename\n    }\n    __typename\n  }\n  photo {\n    ...photoContent\n    ...recoPhotoFragment\n    __typename\n  }\n  canAddComment\n  llsid\n  status\n  currentPcursor\n  tags {\n    type\n    name\n    __typename\n  }\n  __typename\n}\n\nfragment photoResult on PhotoResult {\n  result\n  llsid\n  expTag\n  serverExpTag\n  pcursor\n  feeds {\n    ...feedContent\n    __typename\n  }\n  webPageArea\n  __typename\n}\n\nquery brilliantTypeDataQuery($pcursor: String, $hotChannelId: String, $page: String, $webPageArea: String) {\n  brilliantTypeData(pcursor: $pcursor, hotChannelId: $hotChannelId, page: $page, webPageArea: $webPageArea) {\n    ...photoResult\n    __typename\n  }\n}\n"}

    def parse_start_url(self):
        """
        爬虫原理第二步：发送请求，获取响应
        :return:
        """
        for page in range(1):
            try:
                response = session.post(self.start_url, headers=self.headers, json=self.data)
                print(f"响应状态码: {response.status_code}")
                print(f"响应内容: {response.text[:200]}...")  # 打印前200个字符查看响应内容
                response_json = response.json()
                self.parse_response_data(response_json)
            except Exception as e:
                print(f"请求失败: {e}")

    def parse_response_data(self, response):
        data_list = response['data']['brilliantTypeData']['feeds']
        for i in data_list:
            title = i['photo']['caption']
            if not title:
                title = i['photo']['originCaption']
            video_url = i['photo']['photoUrl']
            if not video_url:
                video_url = i['photo']['photoH265Url']
            data = session.get(video_url).content
            self.parse_save_data(data, title)


    def parse_save_data(self, data, title):
        # 清理文件名中的非法字符
        title = "".join([c for c in title if c not in '\\/:*?"<>|\n\r'])
        # 限制文件名长度
        title = title[:50]
        try:
            with open(self.ospath + title + '.mp4', 'wb') as f:
                f.write(data)
            print(f"视频: {title}-------采集完成！！！")
        except Exception as e:
            print(f"保存失败: {e}")



if __name__ == '__main__':

    i = KSSpisder()
    i.parse_start_url()
