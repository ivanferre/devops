# Paper Notes

Transcript of notes taken on paper.

    docker-compose up
    docker-compose down -rmi all

Container: isolated environment for running an application.
Virtual Machine: an abstraction of a machine (physical hardware).

The container comprises of two parts:

- A Docker Engine, which is the server, and
- A client who communicates with the server through a REST API.

This container lays on top of an OS kernel.

To get Docker: docs.docker.com/getdocker

Dockfile: makes the image from the app.

- Cut-down OS.
- Runtime environment, such as Node.js or Python.
- Application files.
- Libraries.
- Environment variables.

Container: a process with its own file system, provided by the image.

    docker build -t hello-docker
    docker image ls
    docker run hello-docker
    docker pull <user>/<image>

hub.docker.com  Image repository à la GitHub.

    docker pull ubuntu
    docker run ubuntu
    docker run -it ubuntu

Package managers:

- npm
- yarn
- pip
- NuGet
- apt

Techs to learn:

- Ansible
- Jenkins
- CI/CD
- Terraform
