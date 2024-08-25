# Docker flask loadbalancer

The purpose of this service just to create a custom level 7 loadbalancer using Nginx and Flask server

Created a simpl flask app which has get requests

Using docker-compose.yml I have added 3 replicas to it so that 3 instances are up-for the same service
Now I have configured the flask app in Nginx to act as the main request server where it will serve all the request
And route it to the replicas based.

To track the number of request served by each replicas I am using prometheus and grafana.

As I am using podman below are the commands
```shell
podman-compose up --build -d

#In new terminal
podman stats

#To do load testing I install ab testing for mac. You can google how to install it. The command for ab testing
ab -n 20000 -c 200 http://localhost:8001/
# As my nginx was served at port 8001 so added that as the hostname
# -n stands for total number of requests
# -c stands for concurrent requests
# ab -n <total-number-of-request> -c <number-of-concurrent-requests> <host-for-your-nginx>
```