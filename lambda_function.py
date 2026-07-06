import json
import boto3

s3 = boto3.client("s3")


def lambda_handler(event, context):
    print("Received event:")
    print(json.dumps(event, indent=2))

    bucket_name = event["detail"]["resourceId"]

    print(f"Remediating bucket: {bucket_name}")

    s3.put_public_access_block(
        Bucket=bucket_name,
        PublicAccessBlockConfiguration={
            "BlockPublicAcls": True,
            "IgnorePublicAcls": True,
            "BlockPublicPolicy": True,
            "RestrictPublicBuckets": True,
        },
    )

    print(f"Public access blocked for bucket: {bucket_name}")

    return {
        "statusCode": 200,
        "body": f"Remediated bucket: {bucket_name}",
    }