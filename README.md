# README

This document provides instructions on how to set up, run, and deploy a simple Flask application. This application includes 
basic authentication and role-based access control. I have already uploaded it to an EC2 instance, and you can access it
through http://3.137.167.63:80/. The username and password can be found in auth.py.

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

## Environment Setup

To run this application, you need to configure several environment variables that the application uses to determine its behavior and how it connects to external resources.

### Required Environment Variables

- `FLASK_APP`: Specifies the entry point of your Flask application; set this to `app.py`.
- `FLASK_ENV`: Sets the environment in which the Flask app is running. Common values are `development`, `production`, or `testing`.
- `DEVELOPMENT_DATABASE_URI`, `PRODUCTION_DATABASE_URI`, `TESTING_DATABASE_URI`: Specifies the database URIs for different environments.
- `SECRET_KEY`: Used by Flask to keep sessions secure. Ensure this key is kept secret and never exposed in public code repositories.

### Setting Environment Variables

#### On Unix/Linux/MacOS:

Open your terminal and type the following commands to set up the environment variables for development:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
export DEVELOPMENT_DATABASE_URI='your_development_database_uri_here'
export SECRET_KEY='your_secret_key_here'
````

#### On Windows

Open Command Prompt and use the following commands to set up the environment variables for development:

```
set FLASK_APP=app.py
set FLASK_ENV=development
set DEVELOPMENT_DATABASE_URI=your_development_database_uri_here
set SECRET_KEY=your_secret_key_here
```
This will start the Flask development server, and the application will be accessible at http://localhost:5000.

### Running the application

Once the environment variables are set, you can run the application using the following command:

```
flask run
```

## Instructions on building the Docker image

To simplify development and deployment, you can run this application using Docker. Follow these steps to build and run the Docker container locally.

1. If you haven't already, clone the repository to your local machine.
2. Build the Docker image using the Dockerfile provided in the project. Run the following command in the root directory of the project: ```docker build -t your-app-name .```
3. Run the container ```docker run -p 5000:5000 your-app-name```
4. To run the Docker container with necessary environment variables, use the -e option to set each variable. For example:```docker run -p 5000:5000 -e FLASK_ENV=development -e SECRET_KEY=your_secret_key_here your-app-name```

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

#### Note
Make sure you replace placeholders like your_project_directory, your_key_pair.pem, and your_public_ip with actual values specific to your AWS setup and project.

## Assumptions

The development and usage of this Flask application are based on several key assumptions:

### Environment
- **Cross-Platform Compatibility**: The application is developed to be compatible across Linux, MacOS, and Windows.

### Security
- **Basic Security Practices**: The application assumes a secure operating environment. Users are responsible for securing sensitive data, including the `SECRET_KEY` and database connections, particularly in production environments.

### User Knowledge
- **Technical Proficiency**: Users are assumed to have basic knowledge of Flask environment management and database setup. 

