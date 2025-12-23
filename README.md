# DevOps_Project
Project for train and learn concepts the DevOps

<img width="679" height="931" alt="Orders API drawio" src="https://github.com/user-attachments/assets/47795e24-86e4-47e7-a353-a7bc72d860fe" />

# Documentation

## Requirements

- Git
- [Python 3.12]
- Python dependecies in `app/requirements.txt`
- Docker
- Kubernetes
- Terraform

### Start App

1. Pull Repository
    - Git pull https://github.com/GabeCarl/DevOps_Project.git
2. Deploy infra from terraform
    - terraform init
    - Configure AWS Credentials
    - terraform plan (Preview what will be created)
    - terraform apply (Create Infra)

### Verification

1. Verify API
    - Verify if API is health in (URL/health)