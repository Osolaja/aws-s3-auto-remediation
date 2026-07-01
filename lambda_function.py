def lambda_handler(event, context):
    print("Received AWS Config non-compliance event:")
    print(event)

    return {
        "statusCode": 200,
        "body": "Event received"
    }