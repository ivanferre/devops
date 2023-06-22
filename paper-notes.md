# Paper Notes

Transcript of notes taken on paper.

## Definitions

Container: isolated environment for running an application.
Virtual Machine: an abstraction of a machine (physical hardware).

The container comprises of two parts:

- A Docker Engine, which is the server, and
- A client who communicates with the server through a REST API.

This container lays on top of an OS kernel.

To get Docker: docs.docker.com/getdocker

### Dockfile

Dockfile: makes the image from the app.

- Cut-down OS.
- Runtime environment, such as Node.js or Python.
- Application files.
- Libraries.
- Environment variables.

### Container

Container: a process with its own file system, provided by the image.

    docker build -t hello-docker
    docker image ls
    docker run hello-docker
    docker pull <user>/<image>

### Docker Hub

hub.docker.com  Image repository à la GitHub.

    docker pull ubuntu
    docker run ubuntu
    docker run -it ubuntu

## Package managers

- npm
- yarn
- pip
- NuGet
- apt

<!-- TODO -->
## Docker Compose

    docker-compose up
    docker-compose down -rmi all

- <https://docs.docker.com/desktop/install/linux-install>

    $ kvm-ok
    $ /usr/bin/qem-system-x86_64 --version

## Testing

Play with Docker: <https://labs.play-with-docker.com>

    docker run my-app sh

This opens a shell in the container, which helps to debut the app.

## Techs to learn

- Ansible: <https://www.redhat.com/en/topics/automation/learning-ansible-tutorial>
- Jenkins
- Kubernetes
- CI/CD
- Terraform

- Conda

Conda takes a lot of space, and you want your container to be as light as possible.
You don't really need a package manager.

COPY command in Docker to copy any file from host machine to Docker image.
