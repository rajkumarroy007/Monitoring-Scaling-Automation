target_group = elb_client.create_target_group(
    Name='rajkumar-web-tg',
    Protocol='HTTP',
    Port=80,
    VpcId='vpc-0321f38a7b594180d',  # Replace with your VPC ID
    TargetType='instance'
)

target_group_arn = target_group['TargetGroups'][0]['TargetGroupArn']

elb_client.register_targets(
    TargetGroupArn=target_group_arn,
    Targets=[{'Id': instance_id}]
)

listener = elb_client.create_listener(
    LoadBalancerArn=alb_arn,
    Protocol='HTTP',
    Port=80,
    DefaultActions=[{'Type': 'forward', 'TargetGroupArn': target_group_arn}]
)
