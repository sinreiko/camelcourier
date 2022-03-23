FROM python:3-slim
WORKDIR /usr/src/app
COPY http.reqs.txt ./
RUN pip install -r http.reqs.txt
COPY ./send_sms.py ./
CMD [ "python", "./send_sms.py" ]