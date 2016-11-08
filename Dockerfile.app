FROM alpine:3.4

RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    rm -r /root/.cache

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh

RUN mkdir -p /work
WORKDIR /work
ADD . /work/
RUN pip install -r requirements.txt

CMD ["python", "-m", "rt_bot"] 
