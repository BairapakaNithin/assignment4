import boto3

sns = boto3.client('sns', region_name='us-east-1')
topic_name = 'firsttopic'
response = sns.create_topic(Name=topic_name)
topic_arn = response['TopicArn']
print(f'Topic ARN: {topic_arn}')

