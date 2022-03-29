FROM python:3-slim
WORKDIR /usr/src/app
COPY http.reqs.txt ./
RUN pip install -r http.reqs.txt
COPY ./shipper.py ./
CMD [ "python", "./shipper.py" ]