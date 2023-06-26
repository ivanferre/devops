# Notes from.  the DevOps Focus Track at PowerCoders Spring 2023

| Tool        | Use  |
|------------ |----- |
| Docker      | Implement Containers. |
| Terraform   | To deploy infraestracture: create and destroy. |
| Ansible     | Day-to-Day administration. |
| Kubernetes  | Container orchestration. Manage data. |

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

## Install Docker on Personal AWS EC2 Instance

ssh -i FirstEC2keyPair.pem <ubuntu@ec2-3-120-174-171.eu-central-1.compute.amazonaws.com>

[How to Install Docker on AWS Ubuntu](https://linuxhint.com/install-docker-aws-docker/)

Update and upgrade all the software. Reboot to ensure the kernel is updated.

    sudo apt install apt-transport-https ca-certificates curl software-properties-common

If you need to install PGP, here is how to do it: <https://central.sonatype.org/publish/requirements/gpg/>

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

### What is the difference between the ec2 and the elastic beanstalk? What are the possible use cases for both?

**Mustafa Cihan**:

EC2 (Elastic Compute Cloud) and Elastic Beanstalk are both services provided by Amazon Web Services (AWS), but they serve different purposes and have different use cases.
In summary, EC2 is a more general-purpose service that gives you full control over virtual servers, allowing you to customize the infrastructure to your specific needs. On the other hand, Elastic Beanstalk is a higher-level service that abstracts away infrastructure management, providing a simpler way to deploy and manage web applications. Elastic Beanstalk is often used for rapid application development, while EC2 is more flexible and suitable for a wide range of use cases.

**Kevin Kiruri**:

Let me add that when using an EC2, you are responsible for all the resources on the server such as memory, storage, updates etc. Elastic beanstalk uses a serverless model (it is a managed service), where AWS manages the underlying resources and you will only manage the app that you install. The underlying resources will be managed by AWS.

## TODO

Complete Docker Tutorial (see below).

<https://roadmap.sh/devops>

Conda: takes a lot of space, and you want your container to be as light as possible.

You don't really need a package manager.

### Docker Tutorial

<https://docker-curriculum.com/>
<https://github.com/prakhar1989/docker-curriculum>
<https://docs.docker.com/get-started/>

We've got until the "Beanstalk" section. Creating the Elastic Beanstalk Console is far more complex than depicted in the article, and could not complete it correctly. In particular, we did not know what the instance profile is.

The instance profile credentials are exposed on <http://169.254.169.254/latest/meta-data/iam/security-credentials/> . When you curl this URL on an EC2 instance, you will get the name of the instance profile attached to the instance.

[Docker Compose Tutorial](https://www.youtube.com/watch?v=HG6yIjZapSA)

### Continuous Deployment Pipeline

AWS Code Deploy.
Popular alternative products include: Jenkins and GitLab.

Here is the AWS Code Pipeline userguide:
<https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-simple-s3.html>
Here is a project guide you can follow:
<https://www.linkedin.com/pulse/set-up-continous-deployment-pipeline-less-than-15-min-mohit-sharma/>

## DevOps Commands

See cheat sheet at <https://dockercheatsheet.com/>

- Build image: `docker build -t my-image .`
- Push to hub.docker.com: `docker push myrepo/my-image:2.0`
- Pull from hub.docker.com: `docker image pull example`
- Run a container: `docker run
image:tag`

## Further learning

- <https://www.redhat.com/sysadmin/introduction-tmux-linux>
- <https://tmuxcheatsheet.com/>
- <https://dockercheatsheet.com/>
- <https://daphnia.com/powercoders-nag-intro.html#_stuff_to_try>

- <https://realpython.com/python-sockets/#echo-client-and-server>

- <https://drive.google.com/drive/u/1/folders/1_lltfXi_Pcf7rzYyJkQKKRPzbeglLaPf>
- <https://academy.socialbee.org/home/content/all>

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

### Wrong Permissions

The user to execute `docker` must belong to the `docker` group.

Follow <https://linuxopsys.com/topics/add-user-to-docker-group>

    $ sudo groupadd docker
    groupadd: group 'docker' already exists.
    sudo usermod -aG docker $USER
    exec su -l $USER
