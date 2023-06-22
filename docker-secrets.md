# Docker Secrets

Research on how to include credentials, hostnames, and other sensitive data in a secure manner.

[Manage sensitive data with Docker secrets](https://docs.docker.com/engine/swarm/secrets/)

> **Note**: Docker secrets are only available to swarm services, not to standalone containers. To use this feature, consider adapting your container to run as a service. Stateful containers can typically run with a scale of 1 without changing the container code.

[How to Keep Docker Secrets Secure: Complete Guide](https://spacelift.io/blog/docker-secrets)

Avoid using environment variables to communicate sensitive data, because they are transmitted in plain text from outside the container. You can easily retrieve environment variables' values by using `docker inspect`.

In addition, environment variables often fall into configuration files like `docker-compose.yml`.

Docker includes a secrets management solution, but it **doesn’t work with standalone containers**. You can supply secrets to your containers when you’re using either [Docker Compose](https://docs.docker.com/compose) or [Docker Swarm](https://docs.docker.com/engine/swarm). There’s no alternative for containers created manually with a plain `docker run` command.

## Using Secrets With Docker Compose

Secrets are defined in Compose files within the top-level `secrets` field.

The process is as follows:

- Place the secret into a file;
- set the name of the file in the Compose file;
- When executing `docker compose up`, the file shall be fetched and mounted in a memory filesystem;
- And the secret will be read.

This file is not reachable outside the container.

## Using Docker Swarm Secrets

## TODO

<https://spacelift.io/blog/container-security>
