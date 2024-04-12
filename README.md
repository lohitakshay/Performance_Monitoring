# Performance Monitoring App

This project is a self-initiated endeavor focusing on AWS, Kubernetes, Docker, Python, and HTML technologies.

## Project Overview
The primary goal of this project is to develop a web application that can monitor system metrics such as CPU and memory usage. It utilizes Python's `psutil` library to collect system metrics and Flask to build a web interface for presenting these metrics. Docker is employed for containerizing the application, facilitating easy deployment and management. Kubernetes is utilized to deploy the application in a clustered environment, ensuring scalability and reliability.

## Project Steps
### Step 1: Deploying the Flask Application Locally
- Clone the repository
- Install the necessary dependencies
- Run the Flask application

### Step 2: Dockerizing the Flask Application
- Create a Dockerfile
- Build the Docker image
- Run the Docker container

### Step 3: Pushing the Docker Image to Amazon ECR
- Create an Amazon ECR repository
- Push the Docker image to Amazon ECR

### Step 4: Creating an Amazon EKS Cluster and Deploying the Application Using Python
- Create an Amazon EKS cluster
- Create a node group
- Deploy the application using Python by creating a deployment and service

This structured approach ensures that the application can be developed, containerized, and deployed in a scalable and efficient manner, leveraging the capabilities of AWS and Kubernetes.

Screenshots
![image](https://github.com/lohitakshay/Performance_Monitoring/assets/95850420/5548a9e1-1eb9-4bc1-9669-ca2b002bf116)
![image](https://github.com/lohitakshay/Performance_Monitoring/assets/95850420/22f86cad-fadc-4506-9ea5-a50302a29a66)
![image](https://github.com/lohitakshay/Performance_Monitoring/assets/95850420/669b6adf-f5fe-473e-abd7-77df9c96d799)
![image](https://github.com/lohitakshay/Performance_Monitoring/assets/95850420/e8ef5217-28c6-4365-93bc-f1f37a118496)



