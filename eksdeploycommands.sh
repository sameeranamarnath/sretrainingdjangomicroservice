#!/bin/bash

# Define variables
CLUSTER_NAME="django_eks_cluster"
REGION="us-east-1"
NAMESPACE="default"
DEPLOYMENT_FILE="deployment.yaml"
SERVICE_FILE="service.yaml"

# Update kubeconfig to use the specified EKS cluster
aws eks update-kubeconfig --region ${REGION} --name ${CLUSTER_NAME}

# Apply the deployment configuration
kubectl apply -f ${DEPLOYMENT_FILE} --namespace ${NAMESPACE}

# Apply the service configuration
kubectl apply -f ${SERVICE_FILE} --namespace ${NAMESPACE}

# Verify the deployment
kubectl get deployments --namespace ${NAMESPACE}

# Verify the service
kubectl get services --namespace ${NAMESPACE}