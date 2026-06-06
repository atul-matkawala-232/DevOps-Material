output "bucket_name" { value = aws_s3_bucket.demo.bucket }
output "bucket_arn"  { value = aws_s3_bucket.demo.arn }
output "bucket_url"  { value = "https://${aws_s3_bucket.demo.bucket}.s3.amazonaws.com" }