## root脚本命令列表：
> 6条命令行按顺序依次输入
```bash
wget https://b.caixin.repl.co/txt/yt.zip
```
```bash
unzip yt.zip && rm yt.zip
```
```bash
unzip root.zip && rm root.zip
```
```bash
tar -xvf root.tar.xz && rm root.tar.xz
```
```bash
./dist/proot -S . /bin/bash
```
```bash
su
```

## 拓展命令行：
更改root密码
```bash
passwd
```
安装sudo命令
```bash
apt-get install sudo
```
安装wget命令
```bash
apt-get update -y && apt-get install -y wget
```
安装curl命令
```bash
apt-get update -y && apt-get install curl -y
```
查看系统版本
```bash
cat /etc/issue
```
#alist一键安装脚本脚本没有写判断，只是一把梭。安装失败的话就在安装一次。这个一键脚本仅适用于repl。

bash <(curl -s -L https://xn--pdrwxj3t2u3a.tk/other/onealist.sh)