#!/bin/bash

echo "🚀 Deploying Image Uploader to Minikube..."

cd "$(dirname "$0")" || exit

# Step 1: Apply all Kubernetes manifests
kubectl apply -f k8s/namespace.yml
kubectl apply -f k8s/pvc.yml
kubectl apply -f k8s/backend.yml
kubectl apply -f k8s/frontend.yml
kubectl apply -f k8s/ingress.yml

# Step 2: Show deployment status
echo
echo "✅ Deployment complete. Current status:"
kubectl get all -n image-uploader
echo
kubectl get ingress -n image-uploader
