FROM python:3-slim
WORKDIR /usr/src/app
COPY http.reqs.txt ./
RUN python -m pip install -r http.reqs.txt \
    && python -m pip install starkbank-ecdsa \
    && python -m pip install elliptic-curve \
    && docker run -d --hostname esd-rabbit --name rabbitmq-mgmt -p 5672:5672 -p 15672:15672 rabbitmq:3-management
COPY ./email_test.py ./invokes.py ./amqp_setup.py ./
CMD [ "python", "./email_test.py" ]
