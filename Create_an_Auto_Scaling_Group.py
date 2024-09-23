asg_client = boto3.client('autoscaling')

launch_template = asg_client.create_launch_template(
    LaunchTemplateName='rajkumar-web-template',
    LaunchTemplateData={
        'ImageId': 'ami-084f1c3f244e0f2ce',
        'InstanceType': 't4g.micro',
        'KeyName': 'Rajkumar_Vired_Ubantu',
        'SecurityGroupIds': ['sgr-07fe0002251cafd87'],
        'UserData': '... your user data script ...',
    }
)

asg_client.create_auto_scaling_group(
    AutoScalingGroupName='my-auto-scaling-group',
    LaunchTemplate={
        'LaunchTemplateId': launch_template['LaunchTemplate']['LaunchTemplateId']
    },
    MinSize=1,
    MaxSize=5,
    DesiredCapacity=1,
    VPCZoneIdentifier='subnet-09bd0e0acc92d4efa,subnet-09bd0e0acc92d4efa'
)
