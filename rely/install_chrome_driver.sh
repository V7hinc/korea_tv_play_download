#!/bin/sh

BASEDIR=`dirname $0`/..
BASEDIR=`(cd "$BASEDIR"; pwd)`

install(){
echo "开始安装google-chrome"
cat>/etc/yum.repos.d/google-chrome.repo<<EOF
[google-chrome]
name=google-chrome
baseurl=http://dl.google.com/linux/chrome/rpm/stable/basearch
enabled=1
gpgcheck=1
gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub
EOF
sed -i 's/basearch/$basearch/g' /etc/yum.repos.d/google-chrome.repo
yum -y install google-chrome-stable --nogpgcheck;
}

# 判断是否安装了google-chrome
if command -v google-chrome &> /dev/null
then
    echo "google-chrome exist"
else
    install
fi

# 安装 chromedriver
