FROM centos:7

COPY src /app/korea_tv_play_download

WORKDIR /app/korea_tv_play_download/rely

# 安装必要组件
RUN set -x;\
yum install unzip lrzsz python3 -y;\
tar -xvf ffmpeg-git-amd64-static.tar.xz -C /usr/local/;\
rm -rf ffmpeg-git-amd64-static.tar.xz;\
ln -s /usr/local/ffmpeg-git-20211108-amd64-static/ffmpeg /usr/bin/ffmpeg;\
tar xvf jre.tar.gz -C /usr/local/;\
rm -rf jre.tar.gz;\
ln -s /usr/local/jre/bin/java /usr/bin/java;

WORKDIR /app/korea_tv_play_download/

# 安装chrome
RUN set -x;\
sh module/install_chrome_driver.sh;
# 安装python脚本运行依赖模块组件
RUN set -x;\
pip3 install -r requestsment.txt;

# 解决运行时编码问题
RUN set -x;\
echo 'export LC_ALL="en_US.utf8"' >> /etc/profile;\
source /etc/profile

# 编写自启动脚本
RUN set -x;\
echo '#!/bin/sh' >> /auto_start.sh;\
echo 'source /etc/profile' >> /auto_start.sh;\
echo 'python3 korea_tv_play_download.py $1 $2' >> /auto_start.sh;\
chmod +x /auto_start.sh;


VOLUME /app/korea_tv_play_download/log

ENTRYPOINT ["/auto_start.sh"]
CMD ["-h"]




