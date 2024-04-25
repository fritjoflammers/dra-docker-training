FROM alpine

RUN apk add --update python3 py3-pip py3-matplotlib py3-numpy py3-pandas

WORKDIR /app

COPY plot.py /app

ENTRYPOINT ["python3", "plot.py"]

