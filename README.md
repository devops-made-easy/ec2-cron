# EC2 CRON
==============
[![SonarCloud](https://img.shields.io/badge/scanned%20on-sonarcloud-orange?style=flat&logo=SonarCloud)](https://sonarcloud.io/dashboard?id=devops-made-easy_ec2-cron) || 
[![AWSSAM](https://img.shields.io/badge/view%20on-Serverless_Repo-orange?style=flat&logo=amazon%20aws)](https://console.aws.amazon.com/lambda/home?#/create/app?applicationId=arn:aws:serverlessrepo:us-west-2:604621407125:applications/ec2-cron) 
## Features

* Allows you to schedule a CRON job(cloudwatch rule) to perform START, STOP or REBOOT for EC2 INSTANCES for given tag key and its value.

## Architecture Diagram
![High Levl Architecture ](https://github.com/devops-made-easy/ec2-cron/raw/master/images/HLA.png)

## How to Deploy

Step 1: Go to the [![AWSSAM](https://img.shields.io/badge/click%20me%20to%20start%20deploy-Serverless_Repo-orange?style=flat&logo=amazon%20aws)](https://console.aws.amazon.com/lambda/home?#/create/app?applicationId=arn:aws:serverlessrepo:us-west-2:604621407125:applications/ec2-cron) 

Step 2: Enter Values for the following as per your needs
* Application name [ Stack Name of the application created via AWS Cloudformation]
* EC2CronFunction [ Name of the Lambda Function Name ]
* Action [Supported Values are STOP, START or REBOOT - This is Action that will be performed on fitlered ec2 instances]
* CronSchedule [ Cron Schedule for CloudWatch Event Refer: [Link for syntax help](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html) ]        
* TagKey [ Name of the Tag Key that you want to use in filter]
* TagValue [ Value of the Tag Key that you want to use in filter]

Step 3: Select the check box "I acknowledge that this app creates custom IAM roles" and Click on Deploy

Resources that get created with this deployment are as follows:
1. Lambda Function
2. Cloud Watch Event
3. CloudWatchEventPermission
4. IAM Role with default AWSLambdaBasicExecutionRole Policy and below custom policy
Policy
```
{
    "Statement": [
        {
            "Action": [
                "ec2:RebootInstances",
                "ec2:StartInstances",
                "ec2:StopInstances"
            ],
            "Resource": "arn:aws:ec2:us-east-2:013472794367:instance:*",
            "Effect": "Allow"
        },
        {
            "Action": [
                "ec2:DescribeInstances"
            ],
            "Resource": "*",
            "Effect": "Allow"
        }
    ]
}
```


## Deploy the sample application

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

To use the SAM CLI, you need the following tools.

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 installed](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

## Local Development 

To use the SAM CLI, you need the following tools.

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 installed](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)


To build and deploy your application for the first time, run the following in your shell:

```bash
sam build --use-container
sam deploy --guided
```

```bash
AWS$ sam local invoke --env-vars env.json
```

## License Summary
This sample code is made available under MIT license. See the [LICENSE](LICENSE) file.

## Share the Love

Like this project? Please give it a ★ on  [our GitHub!](https://github.com/devops-made-easy/ec2-cron) it helps us a lot

## Contributing
Have an idea for a feature to enhance this serverless application? Open an [issue](https://github.com/devops-made-easy/ec2-cron/issues/new) or [pull request](https://github.com/devops-made-easy/ec2-cron/pulls) !

