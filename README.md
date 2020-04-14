# aws_ec2_py
Interaction with AWS EC2 Instances and Snapshots

## About

This project makes use of boto3 to interact with AWS EC2 instances and snapshots

## Configuring

shotty uses the configuration file created by the AWS cli:

```aws configure --profile shotty```

## Running

```pipenv run "python shotty/shotty.py <command> <subcommand> <--project=PROJECT>"```

*command* is instances, volumes, snapshots

*subcommand* depends on command

*project* is optional

## Commands

### List Instances

```pipenv run "python shotty/shotty.py instances list"```

To filter by project then pass the argument --project

```pipenv run "python shotty/shotty.py instances list --project=<project tag data>"```

### Start/Stop Instances

```pipenv run "python shotty/shotty.py instances start|stop```

### List Volumes

```pipenv run "python shotty/shotty.py volumes list"```

To filter by project then pass the argument --project

```pipenv run "python shotty/shotty.py volumes list --project=<project tag data>"```

