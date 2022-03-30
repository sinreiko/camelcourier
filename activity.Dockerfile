FROM python:3-slim
WORKDIR /usr/src/app
COPY amqp.reqs.txt http.reqs.txt ./
RUN python -m pip install --no-cache-dir -r amqp.reqs.txt -r http.reqs.txt
COPY ./activity.py ./amqp_setup.py ./
CMD [ "python", "./activity.py" ]
