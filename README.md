<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/sinreiko/camelcourier">
    <img src="https://i.ibb.co/HnsV5XP/camel.png" alt="Logo" width="100" height="100">
  </a>

<h2 align="center">CamelCourier</h3>

  <p align="center">
    <i>IS213 Enterprise Solution Development Project for Singapore Management University</i>
    <br />
    CamelCourier is a courier/logistics company, similar to Ninja Van. In this project, we are building a courier service with various relevant business scenarios/processes leveraging a microservice(s) architecture rather than a monolithic one as well as other appropriate tools and technologies.
    <br />
    <a href="https://github.com/sinreiko/camelcourier"><strong>Explore GitHub Repository »</strong></a>
    <br />
    <br />
    <a href="https://docs.google.com/document/d/1oEI87EQHZk3OUR1rv38nPEV825Y1M5VQf3DGttq0Xgg/edit?usp=sharing">View API Documentation</a>
    ·
    <a href="https://docs.google.com/document/d/1dJoWSUa3_W_yBXOmVrcms0zxBURCweqW/edit?usp=sharing&ouid=103579897753241852301&rtpof=true&sd=true">View Report</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#microservices">Microservices</a></li>
    <li><a href="#beyond-the-lab">Beyond The Lab</a></li>
    <li><a href="#other-tasks">Other Tasks</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#troubleshooting">Troubleshooting</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
# About The Project

<a href="https://github.com/sinreiko/camelcourier"><img src="https://i.postimg.cc/qgHTDWQ4/photo-2022-04-07-00-10-52.jpg" alt="Logo" width="1000"></a>

We are CamelCourier! We provide logistics services to individuals and companies (similar to companies like NinjaVan & FedEx). This project is build to provide like services like accounts, status management, pricings, ordering, tracking, etc. For further details about the project, please view the report <a href="https://docs.google.com/document/d/1dJoWSUa3_W_yBXOmVrcms0zxBURCweqW/edit?usp=sharing&ouid=103579897753241852301&rtpof=true&sd=true">here</a>.

<p align="right">(<a href="#top">back to top</a>)</p>



## Built With

### Front-End Dependencies
* [Vue.js](https://vuejs.org/)
* [Bootstrap](https://getbootstrap.com)
* [JQuery](https://jquery.com)

### Back-End Dependencies
* [Flask](https://flask.palletsprojects.com/en/2.1.x/)
* [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/)
* [FlaskSQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
* [Pika](https://pika.readthedocs.io/en/stable/)

### External APIs
* [SWOP API](https://swop.cx/)
* [Google Distance Matrix API](https://developers.google.com/maps/documentation/distance-matrix)
* [Twilio](https://www.twilio.com/)
* [SendGrid](https://sendgrid.com/)

### Other Technologies Involved
* [Docker](https://www.docker.com/)
* [Kong](https://konghq.com/kong)
* [Konga](https://pantsel.github.io/konga/)
* [RabbitMQ (AMQP)](https://www.rabbitmq.com/)
* [GraphQL](https://graphql.org/)
* [Restful](https://restfulapi.net/)
* [GitHub](https://github.com/)



<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
# Getting Started

To get local copy of CamelCourier up and running by following these simple steps below.

## Prerequisites

These are the prerequisites required for CamelCourier.

* Docker Desktop: https://www.docker.com/products/docker-desktop/
* WAMP (Windows): https://www.wampserver.com/en/
* MAMP (Mac): https://www.mamp.info/en/mac/

## Installation

There are 3 areas you have to set up, Docker, mySQL and Kong API gateway.

### Docker Set Up
1. Start up Docker Desktop
2. Open Command Prompt/Terminal and navigate to the folder with docker-compose.yml
2. Build, create and start your containers (Note: This step may take a few minutes)
   ```
   docker-compose up
   ```

### MySQL/phpMyAdmin Set Up
1. Start up your WAMP/MAMP
2. Go to http://localhost/phpmyadmin/ > Login > Import
3. "Choose File" to import and select "cameldb.sql" (under the sql folder)
4. Click "Go" to run the sql

### Kong/Konga Set Up
1. You are required to have your docker containers up and running before continuing to the next step. If your containers are not running, see "Docker Set Up" above. Alternatively, you can check if your containers are running by running the following command below (Note: only kong-migration should be exited).
    ```
    docker-compose ps
    ```
2. Go to http://localhost:1337/ > Create account and login
3. Go to Connections > New Connection > Enter connection details stated below > Create Connection > Activate Connection
    ```
      Name: default
      Kong Admin URL: http://kong:8001
    ```
4. Go to Snapshots > Import from file
5. Select the "snapshot_1.json" (under the "kong snapshot" folder)
6. Go to the details of the snapshot you just imported
7. Click Restore (Note: It is common to encounter an error, just repeat this step and restore again)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MICROSERVICES/TRACKING SHEET -->
# Microservices

<u><b>Atomic/Simple Microservices</b></u>

<!-- DONE - :white_check_mark: -->
<!-- NOT DONE - :white_large_square: -->

| Done | Name | File Name | Table Name | Author |  
|----|----|----|----|----|
| :white_check_mark: | Activity | activity.py | activity | Vasilis |
| :white_check_mark: | Activity HTTP | activityhttp.py | activity | Vasilis |
| :white_check_mark: | Drop Point | droppoint.py | droppoint | Nicholas |
| :white_check_mark: | Email | email_test.py | - | Shao Ming |
| :white_check_mark: | Order | order.py | order | Po Chien |
| :white_check_mark: | Rates | rate.py | rate | Nicholas |
| :white_check_mark: | Shipper | shipper.py | shipper | Jun Hui |
| :white_check_mark: | SMS | send_sms.py | - | Shao Ming |
| :white_check_mark: | Drop Point | droppoint/index.php | droppoint | Po Chien |


<u><b>Composite/Complex Microservices</b></u>

| Done | Name | File Name | Author |  
|----|----|----|----|
| :white_check_mark: | Cancel Delivery | cancel_order.py | Jun Hui |
| :white_check_mark: | Create Delivery | create_order.py | Po Chien |
| :white_check_mark: | Pick Parcel | pick_parcel.py | Vasilis |
| :white_check_mark: | Update Delivery | update_order.py | Shao Ming |
| :white_check_mark: | Valuing | valuing.py | Nicholas |

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- BEYOND THE LAB -->
# Beyond The Lab

<!-- DONE - :white_check_mark: -->
<!-- NOT DONE - :white_large_square: -->

| Done | Name | Responsible | Description |
|----|----|----|----|
| :white_check_mark: | API Gateway | Vasilis | Implementing KONG/KONGA Gateway, Routing |
| :white_check_mark: | GraphQL | Po Chien | Implement SWOP API with GraphQL |
| :white_check_mark: | Multiple Programming Language | Po Chien | Implement Drop Point MS in PHP |

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- Other Tasks -->
# Other Tasks

<!-- DONE - :white_check_mark: -->
<!-- NOT DONE - :white_large_square: -->

| Done | Name | Responsible | Description |
|----|----|----|----|
| :white_check_mark: | Front End UI | Reiko | HTML, CSS, Javascript |
| :white_check_mark: | Consuming | Reiko | Connecting UI with Microservices |


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
# Contact

Vasilis - vasilis.ng.2020@scis.smu.edu.sg</br>
Po Chien - pochien.lin.2019@socsc.smu.edu.sg</br>
Jun Hui - junhui.lee.2020@scis.smu.edu.sg</br>
Nicholas - kwwong.2020@scis.smu.edu.sg</br>
Reiko - reiko.lee.2020@scis.smu.edu.sg</br>
Shao Ming - smlee.2020@scis.smu.edu.sg</br>

Project Link: [https://github.com/sinreiko/camelcourier](https://github.com/sinreiko/camelcourier)

<p align="right">(<a href="#top">back to top</a>)</p>

# Troubleshooting
## Droppoint (PHP ver) encounters connect refused error
**Case 1: Docker requires permission to folder**

This can occur if docker settings did not allow the file to be accessed.
As this app mounts folders to a path in docker-compose.yml, Docker needs permission to this folder path to work as intended.

_*Enabling file permission on Docker*_
1. Go to Docker Desktop -> click the top right ```gear icon``` to access ```settings``` 

2. In setting's left pane, click ```Resources```. A list will expand. Click ``File Sharing``

3. Go to the bottom of the list and hit the ```+``` sign. Browse the file explorer to find where CamelCourier is. Click ```open``` on bottom right corner.

4. In Docker Desktop, click ```Apply and Restart``` on the bottom right corner

**Case 2: Port for SQL is taken**

This can occur if the port for camel_courier_db_1 is taken. The container uses port 9906. It should not be a commonly used port.
There are two options to resolve this:
1. Option 1: Resolve from local machine by freeing up port 9906
  - Use ```docker ps``` command to check if there's a container currently running on 9906.
  - If the container is redundant, use ```docker stop <container id>``` to stop the container, then use ```docker rm <container id>```
  - Re-run ```docker-compose down``` then ```docker-compose up --force-recreate```
2. Option 2: Change a port for MySQL container
  - If the current connection in port 9906 cannot be used, first find an available port that we will call ```port XXXX```
  - Go to camelcourier > docker-compose.yml 
  - Under services > db > ports, change ```9906:3306``` to ```XXXX:3306```
  - Re-run ```docker-compose down``` then ```docker-compose up --force-recreate```

## CORS error when using localhost:8000 as origin
Even if Konga sets up a global plugin, it is likely the case that the CORS issue still persists. Instead, this workaround bypasses CORS from client-side.

**For OSX users**: terminal > run ```open -n -a /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --args --user-data-dir="/tmp/chrome_dev_test" --disable-web-security```

**For Windows users**: download a CORS bypass plugin like this one: https://chrome.google.com/webstore/detail/cors-unblock/lfhmikememgdcahcdlaciloancbhjino?hl=en run as per instructed

**For Linux users**: terminal > run ```google-chrome --disable-web-security```

## Not receiving SMS

As we are currently only own a trial Twilio account, please contact us (emails above) to get your number verified to receive any SMS notifications (not required for email notifications).

<p align="right">(<a href="#top">back to top</a>)</p>
