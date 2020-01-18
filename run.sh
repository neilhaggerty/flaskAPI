#!/bin/bash

docker build -t buoyhealth .
docker run --rm -it -p 5000:5000 buoyhealth
