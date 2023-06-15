# Docker in AWS EC2

I did my work on docker through ec2. Instead of doing configuration and installation  like Hyper-V and WSL 2, you can work directly on a Linux machine via EC2

  sudo yum update -y
  sudo yum install -y docker
  sudo service docker start
  docker --version

I found out my ip address

  curl ifconfig.me
  pwd

create a newfolder

  mkdir my-app
  sudo yum install -y node
  npm init

create a Dockerfile

  touch Dockerfile
  vim Dockerfile

Dockerfile

  FROM node:18
  WORKDIR /app
  COPY package*.json ./
  RUN npm install
  COPY . .
  CMD [ "npm", "start" ]
  touch app.js
  vim app.js

insert into this file console.log("Hi IVAN")
Build (Port:8080 )(you can enter your port number here example 8088:8080 ) Port Num => 8088)

  docker build -t my-app .

  docker run -p 8080:8080 my-app
h
ttp://{Your IP Address}:8088/   You can access the page you made here. You need to enter your own(EC2) ip address.
