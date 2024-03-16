terraform {
    source = "tfr://registry.terraform.io/cloudposse/elastic-beanstalk-environment/aws//?version=0.51.2"
}

include "root" {
  path = find_in_parent_folders()
  expose = true
}

dependency "vpc" {
  config_path = "../vpc"

  mock_outputs_allowed_terraform_commands = ["validate", "plan"]
  mock_outputs = {
      private_subnets = ["subnet-01", "subnet-02"]
      public_subnets = ["subnet-01"]
      vpc_id = "vpc-mock-id"
      vpc_cidr_block = "10.0.0.0/8"
  }
}

dependency "eb_application" {
  config_path = "../beanstalk-application"

  mock_outputs_allowed_terraform_commands = ["validate", "plan"]
  mock_outputs = {
      elastic_beanstalk_application_name = "eb-app-name"
  }
}

inputs = {
    application_subnets = dependency.vpc.outputs.public_subnets
    elastic_beanstalk_application_name = dependency.eb_application.outputs.elastic_beanstalk_application_name
    name = "Finance-Tracker"
    region = include.root.locals.aws_region
    solution_stack_name = "64bit Amazon Linux 2023 v4.2.1 running Corretto 21"
    vpc_id = dependency.vpc.outputs.vpc_id

    instance_type = "t3.micro"

    environment_type = "SingleInstance"
    updating_min_in_service = 0
    managed_actions_enabled  = false
    rolling_update_enabled = false

    keypair = "test-key-pair-java-level-up"
    associate_public_ip_address = true
    additional_security_group_rules = [
        {
            type              = "ingress"
            from_port         = 22
            to_port           = 22
            protocol          = "tcp"
            cidr_blocks       = ["0.0.0.0/0"]
        },
        {
            type              = "ingress"
            from_port         = 8080
            to_port           = 8080
            protocol          = "tcp"
            cidr_blocks       = ["0.0.0.0/0"]
        },
        {
            type              = "ingress"
            from_port         = 443
            to_port           = 443
            protocol          = "tcp"
            cidr_blocks       = [dependency.vpc.outputs.vpc_cidr_block]
        }
    ]

    env_vars = {
        PORT = 8080
    }
    application_port = 8080
}