# CoRise TODO: create a new log group

# CoRise TODO: create a new dashboard
resource "aws_cloudwatch_dashboard" "flaskbb_main" {
  dashboard_name = "flaskbb_main"

  dashboard_body = jsonencode({})
}

#CoRise TODO: create metric alters
resource "aws_cloudwatch_metric_alarm" "bot_attack" {
  alarm_name                = "bot_attack"
  comparison_operator       = "GreaterThanOrEqualToThreshold"
  evaluation_periods        = 2
}

resource "aws_cloudwatch_metric_alarm" "too_busy" {
  alarm_name                = "too_busy"
  comparison_operator       = "LessThanOrEqualToThreshold"
  evaluation_periods        = 2
}