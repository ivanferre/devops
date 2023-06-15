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

Docker playground to test images:

- <https://labs.play-with-docker.com/>

[Docker Desktop WSL 2 backend on Windows](https://docs.docker.com/desktop/windows/wsl/)

## TODO

- <https://www.redhat.com/sysadmin/introduction-tmux-linux>
- <https://tmuxcheatsheet.com/>
- <https://daphnia.com/powercoders-nag-intro.html#_stuff_to_try>

- <https://realpython.com/python-sockets/#echo-client-and-server>

- <https://drive.google.com/drive/u/1/folders/1_lltfXi_Pcf7rzYyJkQKKRPzbeglLaPf>
- <https://academy.socialbee.org/home/content/all>

## Docker Tutorial

<https://docker-curriculum.com/>
<https://github.com/prakhar1989/docker-curriculum>
<https://docs.docker.com/get-started/>

## Troubleshooting

### Unrecognized docker

    > wsl docker --version

    The command 'docker' could not be found in this WSL 2 distro.
    We recommend to activate the WSL integration in Docker Desktop settings.

    See <https://docs.docker.com/docker-for-windows/wsl/> for details.

I have found the solution in [StackOverflow](https://stackoverflow.com/questions/63497928/ubuntu-wsl-with-docker-could-not-be-found). I followed the advice by **Fabrício Pereira**, who answered on Jan 26, 2021 at 15:15.

Open windows shell (maybe as admin), and run:

    > wsl -t docker-desktop
    > wsl --shutdown
    > wsl --unregister docker-desktop

Then go to windows services, stop the Docker Desktop Service, OR to do this running the command in windows shell as admin:

    > Stop-Service -Name "com.docker.service"

And finally, restart the Docker Desktop App.

Test in the windows shell:

    > wsl docker --version
    Docker version 20.10.2, build 2291f61