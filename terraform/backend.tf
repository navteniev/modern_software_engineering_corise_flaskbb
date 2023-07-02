terraform {
  backend "s3" {
    bucket = "terraform-state-flaskbb-mannyoliv15"
    key    = "core/terraform.tfstate"
    region = "us-east-2"
  }
}