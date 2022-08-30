FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ=Europe/Prague

RUN apk update && apk add gcc git postgresql-dev musl-dev tzdata libxml2-dev libxslt-dev g++
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev libwebp-dev libffi libffi-dev cairo py3-pynacl libsodium-dev ffmpeg opus-dev
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

VOLUME /ministrant
WORKDIR /ministrant
COPY . .

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt --user
RUN /usr/local/bin/python -m pip install -U discord.py[voice]

ENTRYPOINT [ "python3", "main.py" ]
