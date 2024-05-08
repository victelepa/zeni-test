# README

This document provides instructions on how to set up, run, and deploy a simple Flask application. This application includes basic authentication and role-based access control.

## Getting Started

These instructions will get your copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites

To run this application, you'll need:
- Python 3.8 or higher
- pip (Python package installer)

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