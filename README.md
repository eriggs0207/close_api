# close_api
### source close_api_env/bin/activate
# README

# Close API Take Home

## Table of Contents

1. [Logic of the Script](#logic-of-the-script)
2. [Built With](#built-with)
- [Gems](#gems)
- [Versions](#versions)
3. [Local Setup](#local-setup)
4. [Contributors](#contributors)

## Logic of the Script

Tea club is a REST API for a subscription service for different kinds of teas.  This Back End App uses
Service Orientated Architecture to expose different endpoints to a Front End app based on the
specifications of a JSON Contract and wireframes.

## Built With

![Ruby](https://img.shields.io/badge/Ruby-CC342D?style=for-the-badge&logo=ruby&logoColor=white)
![Ruby on Rails](https://img.shields.io/badge/Ruby_on_Rails-CC0000?style=for-the-badge&logo=ruby-on-rails&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white)

### Gems

![rspec](https://img.shields.io/gem/v/rspec-rails?label=rspec&style=flat-square)
![jsonapi-serializer](https://img.shields.io/badge/jsonapi--serializer-v%202.2.0-green)
![shoulda](https://img.shields.io/gem/v/shoulda-matchers?label=shoulda-matchers&style=flat-square)
![simplecov](https://img.shields.io/gem/v/simplecov?label=simplecov&style=flat-square)
![factory bot](https://img.shields.io/gem/v/factory_bot_rails?color=blue&label=factory_bot_rails)
![faker](https://img.shields.io/gem/v/faker?color=blue&label=faker)
![rubocop](https://img.shields.io/gem/v/rubocop?color=blue&label=rubocop)
![pry](https://img.shields.io/gem/v/pry?color=blue&label=pry)

### Versions

This project uses `Ruby 2.7.2`

- with Rails `5.2.8.1`
- and uses `PostgreSQL`

## Local Setup

* Fork this repository
* Clone your fork
* From the command line, install gems and set up your DB:
    * `bundle install`
    * `rails db:{create,migrate,seed}`
* Run the test suite with `bundle exec rspec`.
* Run your development server with `rails s` to see the app in action.

## Database Schema

![image](app/assets/Tea_club_schema.png)


## All Available End Points:

### Subscription End Points

#### Subscription Create



`POST  /api/v1/subscriptions`

or

`POST http://localhost:3000/api/v1/subscriptions`



<b>Example Input:</b>

```json
{
          "customer_id": "1",
          "tea_id": "1",
          "title": "enthusiast",
          "price": "250.00",
          "status": 0 ,
          "frequency": 1
        }
```
<b>Example Output:</b>
```json
{
    "success": {
        "message": "Subscription has been created"
    }
}
```

#### Subscription Update


`PATCH /api/v1/subscriptions/{subscription_id}`

or

`PATCH http://localhost:3000/api/v1/subscriptions/13`

<b>Example Input:</b>
```json
{
          "status": 1
        }
```


<b>Example Output:</b>
```json
{
    "success": {
        "message": "Subscription has been updated"
    }
}
```
#### Subscriptions Index

Gets all subscriptions by customer

`GET /api/v1/subscriptions`

or

`GET http://localhost:3000/api/v1/favorites{customer_id}`

<b>Example Input:</b>

`GET http://localhost:3000/api/v1/favorites?customer_id?=1`

<b>Example Output:</b>
```json
{
    "data": [
        {
            "id": "1",
            "type": "subscription",
            "attributes": {
                "title": "williamsburg",
                "price": 56.9,
                "status": "inactive",
                "frequency": "annually",
                "customer_id": 1,
                "tea_id": 1
            }
        },
        {
            "id": "2",
            "type": "subscription",
            "attributes": {
                "title": "roof",
                "price": 38.94,
                "status": "active",
                "frequency": "monthly",
                "customer_id": 1,
                "tea_id": 2
            }
        },
        {
            "id": "13",
            "type": "subscription",
            "attributes": {
                "title": "enthusiast",
                "price": 250.0,
                "status": "inactive",
                "frequency": "monthly",
                "customer_id": 1,
                "tea_id": 1
            }
        }
    ]
}
```
##


## Contributors


<img src="https://avatars.githubusercontent.com/u/106836658?s=120&v=4" />

Erik Riggs | [Github](https://github.com/eriggs0207) | [LinkedIn](https://www.linkedin.com/in/erik-riggs/) |

##

[Back To Top](#back-end-repository-for-lunch-and-learn)
