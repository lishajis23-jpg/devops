# Exercise 1: Kubernetes Getting Started

## Objective
Deploy an Nginx application as a Kubernetes Pod using Minikube and verify that it is running successfully.

## Steps

### 1. Install Minikube
    brew install minikube

### 2. Start Minikube
    minikube start --driver=docker

![Minikube start](Screenshots/01-minikube-start.png)

### 3. Create the Nginx Pod
    kubectl run hello-k8s --image=nginx --port=80

### 4. Verify the Pod
    kubectl get pods

### 5. Expose the Pod
    kubectl expose pod hello-k8s --type=NodePort --port=80
    kubectl get services

![Pod and service](Screenshots/02-pod-and-service.png)

### 6. Access the Nginx Application
    minikube service hello-k8s --url

![Nginx access](Screenshots/03-nginx-access.png)

## Result
Successfully deployed and accessed an Nginx application using Kubernetes and Minikube.
