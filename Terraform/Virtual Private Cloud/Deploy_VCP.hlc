terraform {
    source = "tfr://registry.terraform.io/terraform-aws-modules/vpc/aws//?version=5.5.2"
}

include "root" {
  path = find_in_parent_folders()
}

inputs = {

    name = "FinanceTracker-VPC"
    cidr = "10.0.0.0/24"
    azs = ["eu-west-1a", "eu-west-1b"]


    public_subnets = ["10.0.0.0/25"]
    public_subnet_suffix = "public"
    
    private_subnets = ["10.0.0.128/26", "10.0.0.192/26"]
    private_subnet_suffix = "private"
}