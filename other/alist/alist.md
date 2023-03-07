1、自行下载最新版的alist程序，下载地址: htps;//gthub,com/alist-org/alist/releases，选择 linux-amd64的包下载
2解压文件，将 alist 程序重命名为 replit
replit中新建repl，类型选择bash，上传改名后的alist
4.粘贴内容到 main.sh
01.
82
03
echo Hello world
URL=${REPL SLUG}.${REPL OWNER}.repl.co
while true; do curl -s "https://$URL" >/dev/nul] 2>81 && echo "$(date +'%Y%m%d%H%M%S') Keeping
online ..." && sleep 300; done &
24
85
chmod +x ./replit
nohup ./replit server
创代码
然后点最上边的 RUN 就可以了
查看密码，在shel框里输入
81.
./replit admin

该方法自动保活，不用做网页监视
