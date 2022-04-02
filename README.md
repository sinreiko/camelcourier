## API used and paths
<!-- ### Microservices -->
| Microservice name | Source | Related files |
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
| createOrderTest.sql | test data for test_order.py | Po Chien |




<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/sinreiko/camelcourier">
    <h2 style=";font-size:40px">CamelCourier</p>
  </a>

<h3 align="center">CamelCourier</h3>

  <p align="center">
    <i>IS213 Enterprise Solution Development Project for Singapore Management University</i>
    <br />
    CamelCourier is a courier company, similar to Ninja Van. This project is to build a courier service with various business scenarios/processes leveraging a microservices architecture rather than a monolithic one.
    <br />
    <a href="https://github.com/sinreiko/camelcourier"><strong>Explore the docs »</strong></a>
    <br />
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
| :white_large_square: | Shipper | shipper.py | shipper | Jun Hui |
| :white_large_square: | SMS | send_sms.py | - | Shao Ming |

<u><b>Composite/Complex Microservices</b></u>

| Done | Name | File Name | Author |  
|----|----|----|----|
| :white_large_square: | Cancel Delivery | cancel_order.py | Jun Hui |
| :white_check_mark: | Create Delivery | create_order.py | Po Chien |
| :white_check_mark: | Pick Parcel | pick_parcel.py | Vasilis |
| :white_large_square: | Update Delivery | update_order.py | Shao Ming |
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



<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)

<p align="right">(<a href="#top">back to top</a>)</p>
