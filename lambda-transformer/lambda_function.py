import json

def lambda_handler(event, context):
    try:
        # Try to parse the body if it exists
        body = json.loads(event.get('body', '{}'))  # Defaults to empty dict if body is missing
        sentence = body.get('sentence', 'Default sentence')
        check = body.get('check', 300)
    except json.JSONDecodeError:
        # Handle cases where body is not valid JSON
        return {
            'statusCode': 400,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'error': 'Invalid JSON input'})
        }

    print(f"sentence '{sentence}'")
    # For now, returning a constant vector
    vector = [0.1, 0.2, 0.3, 0.4, check]
    
    # Create the response body
    response = {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(vector)
    }
    
    return response
