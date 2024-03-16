terraform {
    source = "tfr://registry.terraform.io/cloudposse/elastic-beanstalk-application/aws//?version=0.12.0"
}

include "root" {
  path = find_in_parent_folders()
  expose = true
}

inputs = {
    name = "Finance-Tracker"
}