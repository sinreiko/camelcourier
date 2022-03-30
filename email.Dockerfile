FROM python:3-slim
WORKDIR /usr/src/app
COPY amqp.reqs.txt ./
RUN python -m pip install -r amqp.reqs.txt \
    && python -m pip install starkbank-ecdsa \
    && python -m pip install elliptic-curve \
    && python -m pip install sendgrid
COPY ./email_test.py ./amqp_setup.py ./
CMD [ "python", "./email_test.py" ]
