terraform {
  backend "s3" {
    bucket = "terraform-state-flaskbb-sdwailah"
    key    = "core/terraform.tfstate"
    region = "ap-southeast-2"
  }
}