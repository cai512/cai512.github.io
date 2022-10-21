#coding=utf-8
#!/usr/bin/python
import sys
sys.path.append('..') 
from base.spider import Spider
import json
import time
import base64

class Spider(Spider):  # 元类 默认的元类 type
	def getName(self):
		return "哔哩"
	def init(self,extend=""):
		print("============{0}============".format(extend))
		pass
	def isVideoFormat(self,url):
		pass
	def manualVideoCheck(self):
		pass
	def homeContent(self,filter):
		result = {}
		cateManual = {
						"单口相声": "单口相声",
"群口相声": "群口相声",
"评书": "评书",
"快板书": "快板书",
"天津快板": "天津快板",
"京东大鼓": "京东大鼓",
"京韵大鼓": "京韵大鼓",
"莲花落": "莲花落",
"德云社": "德云社",
"青曲社": "青曲社",
"郭德纲": "郭德纲",
"岳云鹏": "岳云鹏",
"孟鹤堂": "孟鹤堂",
"何伟": "何伟",
"曹云金": "曹云金",
"郭麒麟": "郭麒麟",
"陶阳": "陶阳",
"春晚小品": "春晚小品",
"赵本山": "赵本山",
"冯巩": "冯巩",
"贾玲": "贾玲",
"宋小宝": "宋小宝",
"宋丹丹": "宋丹丹",
"赵丽蓉": "赵丽蓉",
"小沈阳": "小沈阳",
"文松": "文松",
"鸭蛋": "鸭蛋",
"大衣哥": "大衣哥",
"朱之文": "朱之文",
"郭达": "郭达",
"黄宏": "黄宏",
"蔡明": "蔡明",
"小沈龙": "小沈龙",
"马三立": "马三立",
"马志明": "马志明",
"常宝华": "常宝华",
"姜昆": "姜昆",
"洛桑.尼玛": "洛桑.尼玛",
"师胜杰": "师胜杰",
"牛群": "牛群",
"刘伟": "刘伟",
"李金斗": "李金斗",
"刘宝瑞": "刘宝瑞",
"陈佩斯": "陈佩斯",
"方清平": "方清平",
"笑林": "笑林",
"高英培": "高英培",
"魏文亮": "魏文亮",
"苏文茂": "苏文茂",
"李润杰": "李润杰",
"侯长喜": "侯长喜",
"周培岩": "周培岩",
"王佩元": "王佩元",
"玉浩": "玉浩",
"刘文亨": "刘文亨",
"侯耀文": "侯耀文",
"石富宽": "石富宽",
"马季": "马季",
"侯宝林": "侯宝林",
"潘长江": "潘长江",
"郭冬临": "郭冬临",
"尹博林": "尹博林",
"郭启儒": "郭启儒",
"李伯祥": "李伯祥",
"孟凡贵": "孟凡贵",
"赵振铎": "赵振铎",
"赵炎": "赵炎",
"赵宝乐": "赵宝乐",
"郝爱民": "郝爱民",
"王谦祥": "王谦祥",
"常宝林": "常宝林",
"陈永泉": "陈永泉",
"魏文亮": "魏文亮",
"莲花落": "莲花落",
"小曲": "小曲",
"二人转": "二人转",
"开心麻花": "开心麻花",
"屌丝男士": "屌丝男士",
"喜剧综艺": "喜剧综艺"
		}
		classes = []
		for k in cateManual:
			classes.append({
				'type_name':k,
				'type_id':cateManual[k]
			})
		result['class'] = classes
		if(filter):
			result['filters'] = self.config['filter']
		return result
	def homeVideoContent(self):
		result = {
			'list':[]
		}
		return result
	cookies = ''
	def getCookie(self):
		rsp = self.fetch("https://www.bilibili.com/")
		self.cookies = rsp.cookies
		return rsp.cookies
	def categoryContent(self,tid,pg,filter,extend):		
		result = {}
		url = 'https://api.bilibili.com/x/web-interface/search/type?search_type=video&keyword={0}&duration=4&page={1}'.format(tid,pg)
		if len(self.cookies) <= 0:
			self.getCookie()
		rsp = self.fetch(url,cookies=self.cookies)
		content = rsp.text
		jo = json.loads(content)
		if jo['code'] != 0:			
			rspRetry = self.fetch(url,cookies=self.getCookie())
			content = rspRetry.text		
		jo = json.loads(content)
		videos = []
		vodList = jo['data']['result']
		for vod in vodList:
			aid = str(vod['aid']).strip()
			title = vod['title'].strip().replace("<em class=\"keyword\">","").replace("</em>","")
			img = 'https:' + vod['pic'].strip()
			remark = str(vod['duration']).strip()
			videos.append({
				"vod_id":aid,
				"vod_name":title,
				"vod_pic":img,
				"vod_remarks":remark
			})
		result['list'] = videos
		result['page'] = pg
		result['pagecount'] = 9999
		result['limit'] = 90
		result['total'] = 999999
		return result
	def cleanSpace(self,str):
		return str.replace('\n','').replace('\t','').replace('\r','').replace(' ','')
	def detailContent(self,array):
		aid = array[0]
		url = "https://api.bilibili.com/x/web-interface/view?aid={0}".format(aid)

		rsp = self.fetch(url,headers=self.header)
		jRoot = json.loads(rsp.text)
		jo = jRoot['data']
		title = jo['title'].replace("<em class=\"keyword\">","").replace("</em>","")
		pic = jo['pic']
		desc = jo['desc']
		typeName = jo['tname']
		vod = {
			"vod_id":aid,
			"vod_name":title,
			"vod_pic":pic,
			"type_name":typeName,
			"vod_year":"",
			"vod_area":"",
			"vod_remarks":"",
			"vod_actor":"",
			"vod_director":"",
			"vod_content":desc
		}
		ja = jo['pages']
		playUrl = ''
		for tmpJo in ja:
			cid = tmpJo['cid']
			part = tmpJo['part']
			playUrl = playUrl + '{0}${1}_{2}#'.format(part,aid,cid)

		vod['vod_play_from'] = 'B站'
		vod['vod_play_url'] = playUrl

		result = {
			'list':[
				vod
			]
		}
		return result
	def searchContent(self,key,quick):
		result = {
			'list':[]
		}
		return result
	def playerContent(self,flag,id,vipFlags):
		# https://www.555dianying.cc/vodplay/static/js/playerconfig.js
		result = {}

		ids = id.split("_")
		url = 'https://api.bilibili.com:443/x/player/playurl?avid={0}&cid=%20%20{1}&qn=112'.format(ids[0],ids[1])
		rsp = self.fetch(url)
		jRoot = json.loads(rsp.text)
		jo = jRoot['data']
		ja = jo['durl']
		
		maxSize = -1
		position = -1
		for i in range(len(ja)):
			tmpJo = ja[i]
			if maxSize < int(tmpJo['size']):
				maxSize = int(tmpJo['size'])
				position = i

		url = ''
		if len(ja) > 0:
			if position == -1:
				position = 0
			url = ja[position]['url']

		result["parse"] = 0
		result["playUrl"] = ''
		result["url"] = url
		result["header"] = {
			"Referer":"https://www.bilibili.com",
			"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
		}
		result["contentType"] = 'video/x-flv'
		return result

	config = {
		"player": {},
		"filter": {}
	}
	header = {}

	def localProxy(self,param):
		return [200, "video/MP2T", action, ""]