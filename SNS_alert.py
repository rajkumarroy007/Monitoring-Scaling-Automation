sns = boto3.client('sns')

scaling_topic = sns.create_topic(Name='scaling-alerts')['TopicArn']
health_topic = sns.create_topic(Name='health-alerts')['TopicArn']
