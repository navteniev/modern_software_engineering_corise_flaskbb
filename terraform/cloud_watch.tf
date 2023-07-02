# CoRise TODO: create a new log group

# CoRise TODO: create a new dashboard
resource "aws_cloudwatch_dashboard" "flaskbb_main" {
  dashboard_name = "flaskbb_main"

  dashboard_body = jsonencode({})
}