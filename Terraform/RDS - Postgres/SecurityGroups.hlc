terraform {
    source = "tfr://registry.terraform.io/terraform-aws-modules/security-group/aws//modules/postgresql?version=5.1.1"
}

include "root" {
  path = find_in_parent_folders()
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

inputs = {
    name = "rds-security-group"
    vpc_id = dependency.vpc.outputs.vpc_id
    ingress_cidr_blocks  = [dependency.vpc.outputs.vpc_cidr_block]
}