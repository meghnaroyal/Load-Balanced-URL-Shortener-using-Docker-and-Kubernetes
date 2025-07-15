# Load-Balanced URL Shortener using Docker & Kubernetes

A scalable and containerized URL shortening service built using Docker and Kubernetes. The application allows users to shorten long URLs and redirect to them using generated short links. It features horizontal scaling, load balancing, and monitoring in a Kubernetes cluster with optional persistent storage and CI/CD enhancements.

---

## 🚀 Features

- REST API for shortening and redirecting URLs
- In-memory key-value store (e.g., Redis or Python dictionary)
- Dockerized microservices
- Kubernetes deployment with:
  - LoadBalancer/NodePort service
  - ConfigMaps & Secrets
  - Horizontal Pod Autoscaler (HPA)
- Optional:
  - Persistent database (PostgreSQL/MongoDB)
  - GitHub Actions or Jenkins CI/CD pipeline
  - Kubernetes Ingress for advanced routing

---

## 🛠️ Tech Stack

- **Backend**: Python / Node.js
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **Storage**: In-memory (e.g., Redis)
- **Monitoring**: `kubectl logs`, HPA, etc.
- **Load Balancing**: Kubernetes Service or Ingress

---

## 🧱 Architecture

Client → LoadBalancer (K8s) → URL Shortener Pods → Key-Value Store (Redis)


- Multiple URL shortener pods ensure scalability and fault tolerance.
- A single Redis pod or service stores the URL mappings.
- LoadBalancer service or Ingress routes incoming traffic to backend pods.

---

## 📦 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

2. Build and Run with Docker
docker build -t url-shortener .
docker run -p 8080:8080 url-shortener

3. Deploy on Kubernetes

kubectl apply -f k8s/
Ensure k8s/ contains:

Deployment files for app and Redis

Services (ClusterIP for Redis, NodePort/LoadBalancer for app)

ConfigMaps and Secrets (if needed)

🔁 Optional Enhancements
Database Integration: Replace Redis with PostgreSQL or MongoDB

CI/CD: Set up GitHub Actions to automate build/test/deploy

Ingress: Use Kubernetes Ingress for better routing

Monitoring: Integrate Prometheus/Grafana for advanced metrics


📂 Folder Structure

.
├── app/                   # Source code for the URL shortener
├── Dockerfile
├── k8s/                   # Kubernetes manifests
│   ├── deployment.yaml
│   ├── service.yaml
│   └── redis.yaml
├── README.md


📈 Project Milestones

Week 1: Build URL Shortener and Dockerize

Week 2: Deploy with Kubernetes

Week 3: Implement scaling, load balancing, and monitoring
