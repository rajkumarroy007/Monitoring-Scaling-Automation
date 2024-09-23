asg_client.put_scaling_policy(
    AutoScalingGroupName='rajkumar-asg',
    PolicyName='scale-out',
    PolicyType='TargetTrackingScaling',
    TargetTrackingConfiguration={
        'PredefinedMetricSpecification': {
            'PredefinedMetricType': 'ASGAverageCPUUtilization',
        },
        'TargetValue': 50.0,  # Scale out when CPU is above 50%
    }
)
