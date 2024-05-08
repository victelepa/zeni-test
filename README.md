# README

This document provides instructions on how to set up, run, and deploy a simple Flask application. This application includes 
basic authentication and role-based access control. I have already uploaded it to an EC2 instance, and you can access it
through http://3.137.167.63:80/

## Getting Started

These instructions will get your copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites

To run this application, you'll need:
- Python 3.8 or higher
- pip (Python package installer)
- Docker installed on your AWS EC2 instance
- An AWS account and a configured EC2 instance

## Installing
First, clone the repository to your local machine:

```
git clone https://github.com/victelepa/zeni-test
cd your-project-directory
```

Install the required Python packages
```
pip install -r requirements.txt
```

Running locally
```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

This will start the Flask development server, and the application will be accessible at http://localhost:5000.

## Deploying to AWS EC2

Follow these steps to deploy the application to an AWS EC2 instance using Docker:

1. Prepare your EC2 instance
```
sudo yum update -y
sudo amazon-linux-extras install docker
sudo service docker start
sudo usermod -a -G docker ec2-user
mkdir app
cd app
```

2. Add your PEM file to your local project directory, set the correct permissions, and securely copy your project files to your EC2 instance:
```
chmod 600 your_key_pair.pem
scp -i your_key_pair.pem Dockerfile app.py auth.py config.py schemas.py requirements.txt ec2-user@your_public_ip:/home/ec2-user/app
```

3. Build and run your Docker container on EC2:
```
sudo docker build -t aws-zeni-docker-test:latest -f Dockerfile .
sudo docker run -d -p 80:5000 aws-zeni-docker-test:latest
```

4. Access the application
- Open your browser and navigate to http://your_public_ip:80.
- Enter the username and password as defined in auth.py to see the welcome page.

### Note
Make sure you replace placeholders like your_project_directory, your_key_pair.pem, and your_public_ip with actual values specific to your AWS setup and project.

