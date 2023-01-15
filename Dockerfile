docker run -d --name="zdir" \
  -v /data/apps/zdir/data:/data/apps/zdir/data \
  -v /data/public:/data/apps/zdir/data/public \
  -p 6080:6080 \
  --restart=always \
  helloz/zdir:3.2.0