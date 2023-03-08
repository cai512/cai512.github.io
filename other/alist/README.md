#### 1、自行下载最新版的alist程序。下载地址: https://github.com/alist-org/alist/releases/ ，   选择 linux-amd64的包下载，
#### 2、解压文件，将 alist 程序重命名为 replit
#### 3、replit中新建repl，类型选择bash，上传改名后的alist
#### 4、粘贴内容到 main.sh
```bash
echo Hello World
URL=${REPL_SLUG}.${REPL_OWNER}.repl.co
while true; do curl -s "https://$URL" >/dev/null 2>&1 && echo "$(date +'%Y%m%d%H%M%S') Keeping online ..." && sleep 300; done &
chmod +x ./replit
nohup ./replit server
```

#### 5、然后点最上边的 run 就可以了


#### 6、查看密码，在shel框里输入

```bash
./replit admin
```

#### 注：该方法自动保活，不用做网页监视

