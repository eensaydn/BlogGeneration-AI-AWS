import boto3
import json
from botocore.exceptions import ClientError

def blog_generation_using_bedrock(blogtopic: str) -> str:
    client = boto3.client("bedrock-runtime", region_name="us-east-1")
    model_id = "meta.llama3-70b-instruct-v1:0"

    prompt = f"Write a 200 words blog on the topic {blogtopic}"

    formatted_prompt = f"""<|begin_of_text|><|start_header_id|>user<|end_header_id|>
    {prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
    """

    native_request = {
        "prompt": formatted_prompt,
        "max_gen_len": 512,
        "temperature": 0.5
    }

    try:
        response = client.invoke_model(
            modelId=model_id,
            body=json.dumps(native_request),
            contentType="application/json",
            accept="application/json"
        )

        model_response = json.loads(response["body"].read())
        response_text = model_response["generation"]
        return response_text

    except (ClientError, Exception) as e:
        print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
        return ""
    
def save_blog_details_s3(s3_key,s3_bucket,generate_blog):
    s3=boto3.client('s3')

    try:
        s3.put_object(Bucket = s3_bucket, Key = s3_key, Body =generate_blog )
        print("Code saved to s3")

    except Exception as e:
        print("Error when saving the code to s3")

def lambda_handler(event, context):
    # TODO implement
    event=json.loads(event['body'])
    blogtopic=event['blog_topic']

    generate_blog=blog_generation_using_bedrock(blogtopic=blogtopic)

    if generate_blog:
        current_time=datetime.now().strftime('%H%M%S')
        s3_key=f"blog-output/{current_time}.txt"
        s3_bucket='aws_bedrock_course1'
        save_blog_details_s3(s3_key,s3_bucket,generate_blog)


    else:
        print("No blog was generated")

    return{
        'statusCode':200,
        'body':json.dumps('Blog Generation is completed')
    }
