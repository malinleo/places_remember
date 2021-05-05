# places_remember
Intership project

## Quick Start
Follow these steps to start project:
1. Install Docker on your computer
2. Clone this repository
3. Run Docker
4. Run this in your workdir:
```sh
$> docker build -t pr-image .
$> docker run -p 8000:8000 -d --name places_remember pr-image
```
This will initialize and run project inside Docker container. Now it's available at localhost:8000
5. To stop container, run:
```sh
$> docker stop places_remember
```
6. To start container again, run:
```sh
$> docker container start places_remember
```

## Coverage
[![Coverage Status](https://coveralls.io/repos/github/malinleo/places_remember/badge.svg?branch=master)](https://coveralls.io/github/malinleo/places_remember?branch=master)
