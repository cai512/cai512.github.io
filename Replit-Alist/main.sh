# Written by Redball1017
ALIST_DOWNLOAD_URL=$(curl -s "https://api.github.com/repos/alist-org/alist/releases/latest"  | jq .assets[3].browser_download_url  | sed s/\"//  | sed s/\"//)
wget "$ALIST_DOWNLOAD_URL"
tar -zxvf ./alist-linux-amd64.tar.gz
chmod +x alist
./alist server