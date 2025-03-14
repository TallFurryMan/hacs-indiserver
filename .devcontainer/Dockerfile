FROM mcr.microsoft.com/devcontainers/python:1-3.13-bullseye

RUN pip install --upgrade pip

RUN pip install numpy
RUN pip install aiousbwatcher
RUN pip install aiodhcpwatcher
RUN pip install async_upnp_client
RUN pip install hassil
RUN pip install go2rtc_client
RUN pip install av
RUN pip install home-assistant-frontend
RUN pip install homeassistant

RUN apt update && apt install -y zlib1g isal libturbojpeg0 ffmpeg && apt clean

RUN pip install aiodiscover
RUN pip install serial

RUN pip install home-assistant-intents