# Terraform

## Install

[Install Terraform on Ubuntu/Debian](https://developer.hashicorp.com/terraform/tutorials/docker-get-started/install-cli)

    sudo apt-get update && sudo apt-get install -y gnupg software-properties-common

<https://registry.terraform.io/providers/hashicorp/aws/latest/docs>

## Terraform - Docker

[Get Started - Docker](https://developer.hashicorp.com/terraform/tutorials/docker-get-started)

Use `resource` blocks to define components of your infrastructure. A resource might be a physical or virtual component such as a Docker container, or it can be a logical resource such as a Heroku application.

When you create a new configuration — or check out an existing configuration from version control — you need to initialize the directory with `terraform init`.

Initializing a configuration directory downloads and installs the providers defined in the configuration, which in this case is the docker provider.

The `terraform fmt` command automatically updates configurations in the current directory for readability and consistency.

You can also make sure your configuration is syntactically valid and internally consistent by using the `terraform validate` command.

Apply the configuration now with the `terraform apply` command. Before it applies any changes, Terraform prints out the execution plan which describes the actions Terraform will take in order to change your infrastructure to match the configuration.

Inspect the current state using `terraform show`.

Terraform has a built-in command called `terraform state` for advanced state management. Use the `list` subcommand to list of the resources in your project's state.

The terraform destroy command terminates resources managed by your Terraform project. This command is the inverse of terraform apply in that it terminates all the resources specified in your Terraform state. It does not destroy resources running elsewhere that are not managed by the current Terraform project.

## Terraform - AWS

[Get Started - AWS](https://developer.hashicorp.com/terraform/tutorials/aws-get-started)

**Infrastructure as code (IaC)** tools allow you to manage infrastructure w)ith configuration files rather than through a graphical user interface.

Terraform is HashiCorp's infrastructure as code tool. It lets you define resources and infrastructure in human-readable, declarative configuration files, and manages your infrastructure's lifecycle.

Terraform plugins called **providers** let Terraform interact with cloud platforms and other services via their application programming interfaces (APIs). HashiCorp and the Terraform community have written over 1,000 providers to manage resources on Amazon Web Services (AWS), Azure, Google Cloud Platform (GCP), Kubernetes, Helm, GitHub, Splunk, and DataDog, just to name a few. Find providers for many of the platforms and services you already use in the [Terraform Registry](https://registry.terraform.io/browse/providers). If you don't find the provider you're looking for, you can write your own.

Providers define individual units of infrastructure, for example compute instances or private networks, as resources. You can compose resources from different providers into reusable Terraform configurations called modules, and manage them with a consistent language and workflow.

Terraform's configuration language is declarative, meaning that it describes the desired end-state for your infrastructure, in contrast to procedural programming languages that require step-by-step instructions to perform tasks. Terraform providers automatically calculate dependencies between resources to create or destroy them in the correct order.

Terraform Cloud (free for up to five users)

You can also connect Terraform Cloud to version control systems (VCSs) like GitHub, GitLab, and others.
