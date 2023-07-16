terraform {
  backend "s3" {
    bucket = "terraform-state-flaskbb-tanupriya-singh"
    key    = "core/terraform.tfstate"
    region = "us-east-2"
  }
}