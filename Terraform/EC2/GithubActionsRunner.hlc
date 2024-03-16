terraform {
    source = "tfr://registry.terraform.io/terraform-aws-modules/ec2-instance/aws//?version=5.6.1"
}

include "root" {
  path = find_in_parent_folders()
  expose = true
}

dependency "vpc" {
  config_path = "../vpc"

  mock_outputs_allowed_terraform_commands = ["validate", "plan"]
  mock_outputs = {
      public_subnets = ["subnet-01"]
      vpc_id = "vpc-mock-id"
  }
}

dependency "eb_env" {
  config_path = "../beanstalk-environment"

  mock_outputs_allowed_terraform_commands = ["validate", "plan"]
  mock_outputs = {
      security_group_id = "sg-id"
  }
}

/*
  Remember to set up gh runner after setting up this instance:
*/
inputs = {
    name = "gh-runner"
    key_name = "test-key-pair-java-level-up"
    ami_ssm_parameter = "/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64"
    vpc_security_group_ids = [dependency.eb_env.outputs.security_group_id]
    subnet_id = dependency.vpc.outputs.public_subnets[0]
    associate_public_ip_address  = true
}