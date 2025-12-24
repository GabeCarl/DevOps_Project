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
- KinD

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


### Start App Local

1. Clone Repository
    - Git clone https://github.com/GabeCarl/DevOps_Project.git

3. Init Kind
    - kind create cluster
        - Use --name flag for a context (default is "kind")
        - For delete cluster use "kind delete cluster"
    - load image in cluster
        - *Change the image in "k8s/deployments.yaml" for the local name image*
        - Use "kubectl apply -f k8s/"

### Test

1. Health Test
    - URL "localhost:5000/health"
    