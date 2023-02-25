FROM python:3.11.2-bullseye
COPY . /ewcode
WORKDIR /src
ENTRYPOINT ["python3", "/ewcode/ewcode.py"]
