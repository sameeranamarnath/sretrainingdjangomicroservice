# Define variables
ECR_NAME="appreposfortrainingtrinet"
REGION="us-east-1"
MICROSERVICE_NAME="django-microservice"
ACCOUNT_ID="825765380838"

# Build the Docker image
docker  build -t ${ECR_NAME}:${MICROSERVICE_NAME}-latest . 

# Authenticate Docker to your ECR
aws ecr get-login-password --region ${REGION} | docker login --username AWS --password-stdin ${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com

# Tag the Docker image for ECR
docker tag ${ECR_NAME}:${MICROSERVICE_NAME}-latest ${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${ECR_NAME}:${MICROSERVICE_NAME}-latest

# Push the Docker image to ECR
docker push ${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${ECR_NAME}:${MICROSERVICE_NAME}-latest