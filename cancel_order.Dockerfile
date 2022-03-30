FROM python:3-slim
WORKDIR /usr/src/app
COPY http.reqs.txt ./
RUN python -m pip install -r http.reqs.txt
COPY ./cancel_order.py ./invokes.py ./amqp_setup.py ./
CMD [ "python", "./cancel_order.py" ]