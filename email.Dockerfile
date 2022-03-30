FROM python:3-slim
WORKDIR /usr/src/app
COPY amqp.reqs.txt ./
RUN python -m pip install --no-cache-dir -r amqp.reqs.txt
COPY ./email_test.py ./amqp_setup.py ./
CMD [ "python", "./email_test.py" ]

