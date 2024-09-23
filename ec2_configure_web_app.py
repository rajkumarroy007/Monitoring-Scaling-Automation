ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
    ImageId='ami-084f1c3f244e0f2ce',  # Replace with appropriate AMI ID
    MinCount=1,
    MaxCount=1,
    InstanceType='t4g.micro',
    KeyName='Rajkumar_Vired_Ubantu',
    SecurityGroupIds=['sgr-07fe0002251cafd87'],  # Replace with security group
    UserData='''#!/bin/bash
                yum update -y
                yum install httpd -y
                systemctl start httpd
                systemctl enable httpd
                echo "Welcome to My Web App" > /var/www/html/index.html
                '''
)

instance_id = instance[0].id
print(f"EC2 Instance {instance_id} launched")
