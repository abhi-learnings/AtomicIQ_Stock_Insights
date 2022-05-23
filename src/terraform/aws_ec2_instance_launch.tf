# Terraform Settings Block
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      #version = "~> 3.21" # Optional but recommended in production
    }
  }
}

# Provider Block
provider "aws" {
  profile = "default" # AWS Credentials Profile configured on your local desktop terminal  $HOME/.aws/credentials
  region  = "ap-south-1"
}

# Resource Block
resource "aws_instance" "ansible_control_node" {
  ami           = "ami-04893cdb768d0f9ee" # Amazon Linux in ap-south-1, update as per your region
  instance_type = "t2.micro"
  count = 1
}
