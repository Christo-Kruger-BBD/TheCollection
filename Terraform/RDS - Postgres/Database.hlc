terraform {
    source = "tfr://registry.terraform.io/terraform-aws-modules/rds/aws//?version=6.4.0"
}

include "root" {
  path = find_in_parent_folders()
}

dependency "vpc" {
  config_path = "../vpc"

  mock_outputs_allowed_terraform_commands = ["validate", "plan"]
  mock_outputs = {
      private_subnets = ["subnet-01", "subnet-02"]
  }
}

dependency "rds_sg" {
  config_path = "../rds-security-group"

  mock_outputs_allowed_terraform_commands = ["validate", "plan"]
  mock_outputs = {
    security_group_id = "sg-id"
  }
}

inputs = {
  identifier  = "finance-tracker-db"
  engine            = "postgres"
  engine_version    = "16"

  instance_class    = "db.t3.micro"
  create_db_instance = true

  allocated_storage = 5

  vpc_security_group_ids = [dependency.rds_sg.outputs.security_group_id]

  # DB subnet group
  create_db_subnet_group = true
  subnet_ids             = dependency.vpc.outputs.private_subnets

  # DB parameter group
  family = "postgres16"

  # DB option group
  major_engine_version = "16"

  # Database Deletion Protection
  deletion_protection = true
  skip_final_snapshot = true

  publicly_accessible = true

  # Login details
  db_name  = "ftdb"
  port     = "5432"
  iam_database_authentication_enabled = false
  manage_master_user_password = false
}