# korea_tv_play_download
1、基于selenium和browsermobproxy爬取视频的m3u8链接，
2、再通过m3u8Downloader ffmpeg下载ts合并
3、目前仅对centos7做了适配，其他有兴趣可以自行修改。大同小异


## 使用命令
> python运行,需要配置google浏览器驱动环境
```shell script
python3 korea_tv_play_download.py -u https://www.kan.cc/play/2563-0-0.html
```

> 自行构建docker
```shell script
docker build -t korea_tv_play_download .
docker run --rm  -v `pwd`/log:/app/korea_tv_play_download/src/log -it korea_tv_play_download -u https://www.kan.cc/play/2563-0-0.html
```

> docker镜像直接拉取（推荐）
```shell script
docker pull ghcr.io/v7hinc/korea_tv_play_download:latest
docker run --rm  -v `pwd`/log:/app/korea_tv_play_download/src -it ghcr.io/v7hinc/korea_tv_play_download:latest -u https://www.kan.cc/play/2563-0-0.html
```

## 报错解决
如果centos7使用docker运行时遇到挂载的目录提示Permission denied
可以尝试以下办法：
```
1.在运行容器的时候，给容器加特权，及加上 --privileged=true 参数：
docker run --privileged=true --rm  -v `pwd`/log:/app/korea_tv_play_download/src/log -it ghcr.io/v7hinc/korea_tv_play_download:latest -u https://www.kan.cc/play/2563-0-0.html
2.临时关闭selinux：
setenforce 0
```