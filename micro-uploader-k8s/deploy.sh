#!/bin/bash

echo "🚀 Deploying Image Uploader to Minikube..."

cd "$(dirname "$0")" || exit


kubectl apply -f k8s/namespace.yml
kubectl apply -f k8s/pvc.yml
kubectl apply -f k8s/backend.yml
kubectl apply -f k8s/frontend.yml
kubectl apply -f k8s/ingress.yml

echo
echo "✅ Deployment complete. Current status:"
kubectl get all -n image-uploader
echo
kubectl get ingress -n image-uploader
