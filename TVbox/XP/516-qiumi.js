{
    "author": "xyl",
    "ua": "",
    "homeUrl": "http://www.jrskan.com/",
    //"homeUrl": "http://jrsbxj.com/",
    //"homeUrl": "http://jrsyyds.com/",
    
    "cateManual": {
        "体育直播": "1"
    },
	
	// 首页推荐视频的节点
    "homeVodNode": "//ul[@data-stype='zqlq']",
	// 首页推荐视频的名称
    //"homeVodName": "/li[@class='lab_events']/span/text()",
	"homeVodName": "concat(/li[@class='lab_time']/text(),'-',/li[@class='lab_events']/span/text())",
	// 首页推荐视频的id
    "homeVodId": "/li[@class='lab_channel']/a[1]/@href",
	// 二次处理正则
    "homeVodIdR": "http://play.sportsteam365.com/play/steam(\\d+).html",
	//"cateVodIdR": "\\S+/(\\d+).html",
	// 首页推荐视频的图片
    "homeVodImg": "/li[@class='lab_team_home']/span/img/@src",  
	// 首页推荐视频的简介
    "homeVodMark": "concat(//li[@class='lab_team_home']/strong/text(),'-',//li[@class='lab_team_away']/strong/text(),'-xyl')",
	"home": "xyl",
	// 分类页地址 {cateId} 分类id {catePg} 当前页
    "cateUrl": "http://www.jrskan.com/",
	  // 同上面的homeVod字段 分类列表中的视频信息
	"cateVodNode": "//ul[@data-stype='zqlq']",
    //"cateVodName": "/li[@class='lab_events']/span/text()",
    "cateVodName": "concat(/li[@class='lab_time']/text(),'-',/li[@class='lab_events']/span/text(),'xyl')",
    "cateVodId": "/li[@class='lab_channel']/a[1]/@href",
    "cateVodIdR": "http://play.sportsteam365.com/play/steam(\\d+).html",
	//"cateVodIdR": "\\S+/(\\d+).html",
    "cateVodImg": "/li[@class='lab_team_home']/span/img/@src",
    "cateVodMark": "concat(//li[@class='lab_team_home']/strong/text(),'-',//li[@class='lab_team_away']/strong/text())",
	//"cateVodMark": "{vid}",
	"cate": "xyl",
	// 详情页地址 用于获取详情页信息 及 播放列表和地址
    //"dtUrl": "{vid}",
	"dtUrl": "http://play.sportsteam333.com/play/steam{vid}.html",
	// 详情节点
    "dtNode": "//ul[@data-stype='zqlq']",
	// 视频名
    "dtName": "/li[1]/span/text()",
	// 视频图片
    "dtImg": "/li[3]/span/img/@src",
	// 视频分类
    "dtCate": "/li[1]/span/text()",
    //演员
    "dtActor": "/li[1]/span/text()",
    // 导演
    "dtDirector": "concat('xxx -','Never underestimate the heart of a champion! ')",
    "dtDirectorR": "",
    // 视频简介
    "dtDesc": "concat(/li[3]/strong/text(),'-',/li[5]/strong/text(),'-xyl')",
	
	// 播放源节点
    "dtFromNode": "//div[@class='sub_channel']/a/strong",
	// 播放源名称
    "dtFromName": "concat('xyl-',/text())",
    "dtFromNameR": "",
	// 播放列表节点
    "dtUrlNode": "//div[@class='sub_channel']",
	// 播放地址节点
    "dtUrlSubNode": "/a",
    "dtUrlSub": "/ff",
	// 播放地址
    "dtUrlId": "@data-play",
    "dtUrlIdR": "/play/(\\S+)",
	//"dtUrlIdR": "\\S+/(\\d+)&id2=",
	// 剧集名称
    "dtUrlName": "/strong/text()",
    "dtUrlNameR": "",
	
	//播放页面的地址 {playUrl} 对应上面 dtUrlId 获取到的地址
    "playUrl":"http://play.sportsteam333.com/play/{playUrl}#ff",
    //"playUrl":"http://play.sportsteam666.com/play/{playUrl}",
    //"playUrl": "http://play.sportsteam365.com/play/{playUrl}",
    //"playUa": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36", 
    //"playUa": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
	
    "searchUrl": "http://www.jrskan.com?key={wd}",
    "scVodNode": "//div[@class='play_xg']/li",
    "scVodName": "//div[@class='name']/a/@title",
    "scVodId": "//div[@class='name']/a/@href",
    "scVodIdR": "/play/(\\d+).html",
    "scVodImg": "//div[@class='pic']/a/img/@src",
    "scVodMark": ""
}