# README pysock

This is a project following the [Socket Programming in Python (Guide)](https://realpython.com/python-sockets/).

## Applications

### echo-client

`echo-client`: client sends one message to `echo-server` on a unique connection. The server replies with the same content, and connection is closed.

### multiconn

`multiconn` manages a range of simultaneous connections between client and server.

For the server, pass the `host` and `port` numbers:

    $ python multiconn-server.py
    Usage: multiconn-server.py <host> <port>

For the client, also pass the number of connections to create to the server:

    $ python multiconn-client.py
    Usage: multiconn-client.py <host> <port> <num_connections>

## TODO

Carry on with the tutorial from *Application Client and Server*.

If you want to change the socket connection examples, remember to change the address to “::1” and also change AF_INET to AFI_NET6. There are other options you can specify for IPv6 sockets, but this should get you started.

## References

Other information sources include:

- [Python - How to check if a port is in use](https://twin.sh/articles/17/python-how-to-check-if-a-port-is-in-use)
- [How to Install netstat on Ubuntu 20.04 LTS (Focal Fossa)](https://www.cyberithub.com/how-to-install-netstat-on-ubuntu-20-04-lts-focal-fossa/#Step_3_Install_Netstat)
