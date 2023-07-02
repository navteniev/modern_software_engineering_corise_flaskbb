resource "aws_cloudwatch_log_group" "flaskbb_app" {
  name = "flaskbb_app"
  retention_in_days = 3
}