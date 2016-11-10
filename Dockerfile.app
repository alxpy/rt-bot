FROM frolvlad/alpine-python3

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh

RUN mkdir -p /work
WORKDIR /work
ADD . /work/

RUN pip install -r requirements.txt

CMD ["python3", "-m", "rt_bot"] 
