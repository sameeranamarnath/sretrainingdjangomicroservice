ECR_NAME="appreposfortrainingtrinet"
REGION="us-east-1"
MICROSERVICE_NAME="django-microservice"
ACCOUNT_ID="825765380838"
HOST_PORT="8000"
TARGET_PORT="8100"


docker run -p ${HOST_PORT}:${TARGET_PORT} ${ECR_NAME}:${MICROSERVICE_NAME}-latest