FROM python:3.7
MAINTAINER renyumeng
WORKDIR /usr/src/app
ADD ./judger /usr/src/app/judger
ADD ./judgeServer /usr/src/app/judgeServer


ENV PYTHONPATH /usr/src/app
ENV PYTHONUNBUFFERED 1

RUN cd ./judger/Lo-runner-master && python setup.py build && python setup.py install
RUN pip3 install -i http://mirrors.aliyun.com/pypi/simple/ mysqlclient --trusted-host mirrors.aliyun.com
RUN pip3 install -i http://mirrors.aliyun.com/pypi/simple/ flask==2.1.2 --trusted-host mirrors.aliyun.com
RUN pip3 install -i http://mirrors.aliyun.com/pypi/simple/ asgiref --trusted-host mirrors.aliyun.com
RUN pip3 install -i http://mirrors.aliyun.com/pypi/simple/ pymysql --trusted-host mirrors.aliyun.com
# RUN pip3 install -i http://mirrors.aliyun.com/pypi/simple/ logging --trusted-host mirrors.aliyun.com
RUN ls

EXPOSE 4000:4000

CMD ['python','./judgeServer/main.py']


