FROM python:3.7
MAINTAINER renyumeng
WORKDIR /usr/src/app
ADD ./judger /usr/src/app/judger
ADD ./judgeServer /usr/src/app/judgeServer


ENV PYTHONPATH /usr/src/app
ENV PYTHONUNBUFFERED 1

RUN cd ./judger/Lo-runner-master && python setup.py build && python setup.py install
RUN pip3 install -i http://mirrors.cloud.tencent.com/pypi/simple mysqlclient --trusted-host mirrors.cloud.tencent.com
RUN pip3 install -i http://mirrors.cloud.tencent.com/pypi/simple flask==2.1.2 --trusted-host mirrors.cloud.tencent.com
RUN pip3 install -i http://mirrors.cloud.tencent.com/pypi/simple gunicorn gevent --trusted-host mirrors.cloud.tencent.com
RUN pip3 install -i http://mirrors.cloud.tencent.com/pypi/simple asgiref --trusted-host mirrors.cloud.tencent.com
RUN pip3 install -i http://mirrors.cloud.tencent.com/pypi/simple pymysql --trusted-host mirrors.cloud.tencent.com
# RUN pip3 install -i http://mirrors.aliyun.com/pypi/simple/ logging --trusted-host mirrors.aliyun.com
EXPOSE 4000

WORKDIR /usr/src/app/judgeServer

CMD ["gunicorn", "app:app", "-c", "./gunicorn.conf.py"]



