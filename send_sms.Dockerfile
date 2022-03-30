FROM python:3-slim
WORKDIR /usr/src/app
COPY amqp.reqs.txt ./
RUN pip install -r amqp.reqs.txt
COPY ./send_sms.py ./amqp_setup.py ./
CMD [ "python", "./send_sms.py" ]