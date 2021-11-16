# korea_tv_play_download
1、基于selenium和browsermobproxy爬取视频的m3u8链接，
2、再通过m3u8Downloader下载ts合并


## 使用命令
```shell script
python3 korea_tv_play_download.py -u https://www.kan.cc/play/2563-0-0.html
```

> 如果使用docker
```shell script
docker build -t korea_tv_play_download .
docker run --rm  -v ./log:/app/korea_tv_play_download/log -it korea_tv_play_download -u https://www.kan.cc/play/2563-0-0.html
```