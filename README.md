<!-- ## API used and paths -->
<!-- ### Microservices -->
<!-- | Microservice name | Source | Related files |
|----|----|----
| Order | Self coded | test_order.py, createOrderTest.sql |

### Paths and descriptions
| API | Path | Method| Description |
|----|----|----|----|
| test_order.py | /order | POST | Creates a new order|
| test_order.py | /order/*<string:trackingID>*| GET | Retrieves order entry |
| test_order.py | /order/update | PUT | Updates order pickupAddress |

## Files
| File Name | Description | Author |
|-----|----|----|
| test_order.py | prototype for the Order microservice | Po Chien |
| createOrderTest.sql | test data for test_order.py | Po Chien | -->




<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/sinreiko/camelcourier">
    <img src="images/camel.png" alt="Logo" width="100" height="100">
  </a>

<h2 align="center">CamelCourier</h3>

  <p align="center">
    <i>IS213 Enterprise Solution Development Project for Singapore Management University</i>
    <br />
    CamelCourier is a courier/logistics company, similar to Ninja Van. In this project, we are building a courier service with various relevant business scenarios/processes leveraging a microservices architecture rather than a monolithic one as well as other appropriate tools and technology.
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
    <li><a href="#usage">Usage</a></li>
    <li><a href="#microservices">Microservices</a></li>
    <li><a href="#beyond-the-lab">Beyond The Lab</a></li>
    <li><a href="#other-tasks">Other Tasks</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following: `github_username`, `repo_name`, `twitter_handle`, `linkedin_username`, `email_client`, `email`, `project_title`, `project_description`

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Next.js](https://nextjs.org/)
* [React.js](https://reactjs.org/)
* [Vue.js](https://vuejs.org/)
* [Angular](https://angular.io/)
* [Svelte](https://svelte.dev/)
* [Laravel](https://laravel.com)
* [Bootstrap](https://getbootstrap.com)
* [JQuery](https://jquery.com)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MICROSERVICES/TRACKING SHEET -->
## Microservices

<u><b>Atomic/Simple Microservices</b></u>

<!-- DONE - :white_check_mark: -->
<!-- NOT DONE - :white_large_square: -->

| Done | Name | File Name | Table Name | Author |  
|----|----|----|----|----|
| :white_check_mark: | Activity | activity.py | activity | Vasilis |
| :white_check_mark: | Activity HTTP | activityhttp.py | activity | Vasilis |
| :white_large_square: | Drop Point | droppoint.py | droppoint | Nicholas |
| :white_check_mark: | Email | email_test.py | - | Shao Ming |
| :white_check_mark: | Order | order.py | order | Po Chien |
| :white_large_square: | Rates | rate.py | rate | Nicholas |
| :white_check_mark: | Shipper | shipper.py | shipper | Jun Hui |
| :white_large_square: | SMS | send_sms.py | - | Shao Ming |
| :white_check_mark: | Drop Point | droppoint/index.php | droppoint | Po Chien |


<u><b>Composite/Complex Microservices</b></u>

| Done | Name | File Name | Author |  
|----|----|----|----|
| :white_check_mark: | Cancel Delivery | cancel_order.py | Jun Hui |
| :white_check_mark: | Create Delivery | create_order.py | Po Chien |
| :white_check_mark: | Pick Parcel | pick_parcel.py | Vasilis |
| :white_check_mark: | Update Delivery | update_order.py | Shao Ming |
| :white_large_square: | Valuing | ?? | Nicholas |

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- BEYOND THE LAB -->
## Beyond The Lab

<!-- DONE - :white_check_mark: -->
<!-- NOT DONE - :white_large_square: -->

| Done | Name | Responsible | Description |
|----|----|----|----|
| :white_large_square: | API Gateway | Vasilis | Implementing KONG/KONGA Gateway |
| :white_large_square: | Facebook Login | Jun Hui | Implement Graph API |
| :white_large_square: | Multiple Programming Language | Po Chien | Implement Drop Point MS in PHP |

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- Other Tasks -->
## Other Tasks

<!-- DONE - :white_check_mark: -->
<!-- NOT DONE - :white_large_square: -->

| Done | Name | Responsible | Description |
|----|----|----|----|
| :white_large_square: | Front End UI | Reiko | HTML, CSS, Javascript |
| :white_large_square: | Consuming | Reiko | Connecting UI with Microservices |


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Vasilis - [@vasng](https://www.instagram.com/vasnjq/) - vasilis.ng.2020@scis.smu.edu.sg</br>
Po Chien - [@handle](link here) - pochien.lin.2019@socsc.smu.edu.sg</br>
Jun Hui - [@handle](link here) - junhui.lee.2020@scis.smu.edu.sg</br>
Nicholas - [@handle](link here) - kwwong.2020@scis.smu.edu.sg</br>
Reiko - [@handle](link here) - reiko.lee.2020@scis.smu.edu.sg</br>
Shao Ming - [@handle](link here) - smlee.2020@scis.smu.edu.sg</br>

Project Link: [https://github.com/sinreiko/camelcourier](https://github.com/sinreiko/camelcourier)

<p align="right">(<a href="#top">back to top</a>)</p>

## Troubleshooting
### Droppoint (PHP ver) encounters connect refused error
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

<p align="right">(<a href="#top">back to top</a>)</p>