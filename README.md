# Camel Couriers - Documentation

## Overview
Camel Couriers is a courier company, similar to Ninja Van. This git hosts an enterprise solution to this hypothetical company 

## API used and paths
### Microservices
| Microservice name | Source | Related files |
|----|----|----|
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