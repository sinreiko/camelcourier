FROM python:3-slim
WORKDIR /usr/src/app
COPY http.reqs.txt ./
RUN python -m pip install -r http.reqs.txt
COPY ./create_order.py ./
CMD [ "python", "./create_order.py" ]