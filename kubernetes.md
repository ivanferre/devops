# Kubernetes

<www.techworld-with-nana.com>

Kubernetes does not take responsibility on data persistance.

Does this mean that DB and files in Containers' applications disappear when services shutdown or restart?

Services have persistance IP addresses, though. In practice, you work with deploymentes and not with pods.

Ingres -> Service -> Pod

Configuration: ConfigMaps and Secrets

Volumes for data persistance.
Deployments and Stateful Sets (replication).

To replicate databases, use Stateful Sets and not Deployments.
