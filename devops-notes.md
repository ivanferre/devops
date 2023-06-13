# Notes from.  the DevOps Focus Track at PowerCoders Spring 2023

## Connecting to AWS virtual machine

Connect to remote host:

    ssh -i ~/.ssh/powercoders ivan@3.76.193.102

Copy file to remote host:

    scp -i ~/.ssh/powercoders filename ivan@3.76.193.102:/path/to/folder/destination

Copy file from remote host to local computer:

    scp -i ~/.ssh/powercoders ivan@3.76.193.102:/path/to/folder /path/to/local/destination

Link worked:
<https://us06web.zoom.us/j/83452349295?pwd=ckJMb0E2SW5ncForenVSd1dRaTdKdz09>

Link channel:
<https://us02web.zoom.us/j/136553440?pwd=N1RRd2RPSGFhV1JxYnFRYnFxZU5wUT09>

## Introduction to Linux

Reading material: <https://daphnia.com/powercoders-linux-intro.html>

## Linux Networking

Reading material:

- <https://daphnia.com/powercoders-nag-intro.html>
- <https://developer.ibm.com/tutorials/l-lpic1-109-1/>

## Install Docker

- <https://www.youtube.com/watch?v=pTFZFxd4hOI&amp;ab_channel=ProgrammingwithMosh>

- <docs.docker.com/desktop/install/linux-install>

<https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-containers>

- <https://learn.microsoft.com/en-us/training/modules/intro-to-docker-containers/>

- <https://ubuntu.com/blog/kvm-hyphervisor>
- <https://www.cyberciti.biz/faq/how-to-check-kvm-qemu-kvm-version-in-linux/>
- <https://ubuntu.com/server/docs/virtualization-qemu>

- <https://docs.docker.com/engine/install/>
- <https://docs.docker.com/desktop/windows/wsl/#download>
- <https://docs.docker.com/desktop/install/linux-install/>
- <https://docs.docker.com/desktop/install/windows-install/>

<https://www.redhat.com/sysadmin/introduction-tmux-linux>

## hub.docker.com

docker login -u ivanferre
Password is in file ~/.ssh/hub-docker-com.pswd

How to push an image to hub.docker.com:

- <https://www.techrepublic.com/article/how-to-build-a-docker-image-and-upload-it-to-docker-hub/>

The command that actually work is

    docker image push ivanferre/hello:latest
