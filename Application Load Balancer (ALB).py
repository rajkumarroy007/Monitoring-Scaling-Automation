elb_client = boto3.client('elbv2')

load_balancer = elb_client.create_load_balancer(
    Name='rajkumar-web-lb',
    Subnets=['subnet-09bd0e0acc92d4efa', 'subnet-09bd0e0acc92d4efa'],  # Replace with your subnets
    SecurityGroups=['sgr-07fe0002251cafd87'],  # Replace with your security group
    Scheme='internet-facing',
    Type='application'
)

alb_arn = load_balancer['LoadBalancers'][0]['LoadBalancerArn']
print(f"ALB ARN: {alb_arn}")
