resource "aws_cloudwatch_log_group" "flaskbb_app" {
  name = "flaskbb_app"
  retention_in_days = 3
}

# CoRise TODO: create a new dashboard
resource "aws_cloudwatch_dashboard" "flaskbb_main" {
  dashboard_name = "flaskbb_main"

  dashboard_body = jsonencode({})
}