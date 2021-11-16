FROM centos:7

WORKDIR /app/korea_tv_play_download

COPY src /app/korea_tv_play_download

# 安装必要组件
RUN set -x;\
yum install java lrzsz python3 -y;\
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




