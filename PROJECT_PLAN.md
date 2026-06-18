Project 2: AWS Public S3 Bucket Auto-Remediation

Goal:
Detect when an S3 bucket becomes public and automatically remove public access.

Architecture:

S3 Bucket Becomes Public
           ↓
AWS Config Detects Change
           ↓
EventBridge Rule
           ↓
Lambda Function
           ↓
Remove Public Access
           ↓
SNS Alert

Services:
- S3
- AWS Config
- EventBridge
- Lambda
- SNS
- Terraform

Skills Demonstrated:
- Security Monitoring
- Automated Remediation
- Event-Driven Security
- Infrastructure as Code