<div align="center">

# 📱 SMSBridge

### Cloud-Native SMS Gateway using FastAPI • Docker • Kubernetes • AWS • Prometheus • Grafana

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi)

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker)

![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes)

![AWS](https://img.shields.io/badge/AWS-EC2-FF9900?style=for-the-badge&logo=amazonaws)

![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions)

![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus)

![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana)

![Docker Hub](https://img.shields.io/badge/Docker_Hub-2496ED?style=for-the-badge&logo=docker)

![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)

</p>

A cloud-native SMS Gateway built with **FastAPI** that securely sends SMS messages through an Android device using the **Traccar SMS Gateway**. The project demonstrates containerization, Kubernetes orchestration, CI/CD automation, monitoring, and secure private networking using Tailscale.

</div>

---

# 🚀 Overview

SMSBridge is a self-hosted SMS Gateway API designed to demonstrate modern DevOps practices while solving a practical problem.

Instead of relying on third-party SMS APIs, SMSBridge uses an Android phone running the **Traccar SMS Gateway** application to send SMS messages. The backend exposes REST APIs using FastAPI and is containerized with Docker before being deployed to a Kubernetes cluster.

The application is monitored using Prometheus and Grafana, while GitHub Actions automates the build pipeline and Docker Hub stores the application images.

The project combines software development, cloud deployment, monitoring, observability, and networking into a single end-to-end DevOps solution.

---

# 🎯 Why SMSBridge?

Many SMS providers require paid subscriptions or external API services.

SMSBridge demonstrates how to build a self-hosted SMS Gateway using modern DevOps technologies while learning:

- REST API Development
- Containerization
- Kubernetes
- Cloud Deployment
- CI/CD
- Monitoring
- Infrastructure Observability
- Secure Networking

This project was created as a portfolio project to showcase practical DevOps and Cloud Engineering skills.

---

# ✨ Key Highlights

- 📱 Self-hosted SMS Gateway
- ⚡ FastAPI REST API
- 📖 Interactive Swagger Documentation
- 🔐 API Key Authentication
- 🗄 SQLite SMS History
- 🐳 Docker Containerization
- ☸ Kubernetes Deployment using K3s
- ☁ AWS EC2 Hosting
- 🔄 GitHub Actions CI/CD Pipeline
- 📦 Docker Hub Image Registry
- 📊 Prometheus Metrics
- 📈 Grafana Dashboards
- 🔒 Secure Networking using Tailscale
- 📱 Android Traccar SMS Gateway Integration

---

# 🛠 Technologies Used

| Category | Technology |
|-----------|------------|
| Backend | FastAPI |
| Language | Python |
| Database | SQLite |
| API Documentation | Swagger UI |
| Containerization | Docker |
| Orchestration | Kubernetes (K3s) |
| Cloud | AWS EC2 |
| CI/CD | GitHub Actions |
| Image Registry | Docker Hub |
| Monitoring | Prometheus |
| Visualization | Grafana |
| VPN | Tailscale |
| SMS Gateway | Android Traccar SMS Gateway |

---

# 📸 Project Preview

The following screenshots are included in this repository:

- Architecture Diagram
- Swagger API Documentation
- End-to-End SMS Delivery
- API Monitoring Dashboard
- Infrastructure Dashboard
- GitHub Actions Pipeline
- Docker Hub Repository

These screenshots demonstrate the complete lifecycle of the project—from development and deployment to monitoring and SMS delivery.

---

# 🏗 Architecture

The following architecture illustrates the complete lifecycle of SMSBridge—from API requests to SMS delivery and monitoring.

<p align="center">
<img src="screenshots/architecture.png" width="950">
</p>

---

# 🔄 End-to-End Workflow

```text
                       Client Application
                              │
                              ▼
                    FastAPI REST API Server
                              │
                              ▼
                     API Key Authentication
                              │
                              ▼
                        SMS Processing Logic
                              │
          ┌───────────────────┴───────────────────┐
          │                                       │
          ▼                                       ▼
   Store SMS History                     Export Metrics
      (SQLite)                          (/metrics endpoint)
          │                                       │
          ▼                                       ▼
    Tailscale VPN                      Prometheus Server
          │                                       │
          ▼                                       ▼
 Android Traccar SMS Gateway          Grafana Dashboard
          │
          ▼
   Recipient Mobile Phone
```

---

# ⚙ System Components

### FastAPI

FastAPI provides the REST API used for sending SMS messages, retrieving SMS history, exposing metrics, and serving interactive API documentation through Swagger UI.

---

### SQLite

SQLite stores all SMS history locally. Each SMS request is recorded with relevant information, making it easy to retrieve delivery history.

---

### Docker

The application is packaged inside a Docker container to ensure consistent deployment across different environments.

---

### Kubernetes (K3s)

The Docker container is deployed inside a lightweight Kubernetes cluster (K3s), enabling container orchestration and simplified deployment management.

---

### AWS EC2

An Amazon EC2 instance hosts the Kubernetes cluster, making the SMSBridge application accessible for deployment and testing.

---

### GitHub Actions

GitHub Actions automatically builds the application whenever changes are pushed to the repository and publishes updated Docker images.

---

### Docker Hub

Docker Hub stores versioned Docker images, allowing Kubernetes to pull and deploy the latest application image.

---

### Prometheus

Prometheus continuously scrapes metrics from the FastAPI `/metrics` endpoint and stores time-series data for monitoring.

---

### Grafana

Grafana visualizes Prometheus metrics using dashboards that display API performance and infrastructure health.

---

### Tailscale

Tailscale creates a secure private network between the FastAPI server and the Android device running the Traccar SMS Gateway.

---

### Android Traccar SMS Gateway

The Android application receives SMS requests through the private network and sends them using the device's SIM card.

---

# 📂 Project Structure

```text
smsbridge/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── auth.py
│   ├── schemas.py
│   └── utils.py
│
├── monitoring/
│   └── prometheus/
│       └── prometheus.yml
│
├── K8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── namespace.yaml
│   └── secrets.yaml
│
├── .github/
│   └── workflows/
│       └── docker.yml
│
├── screenshots/
│   ├── architecture.png
│   ├── api-swagger.png
│   ├── sms-delivery.png
│   ├── api-dashboard.png
│   ├── infrastructure-dashboard.png
│   ├── github-actions.png
│   └── dockerhub.png
│
├── Dockerfile
├── requirements.txt
├── README.md
└── test_gateway.py
```

---

# 📚 REST API

SMSBridge exposes RESTful endpoints for interacting with the application.

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home page |
| GET | `/health` | Health check endpoint |
| POST | `/send-sms` | Send SMS |
| GET | `/sms-history` | Retrieve SMS history |
| GET | `/metrics` | Prometheus metrics |
| GET | `/docs` | Swagger API documentation |

---

# 📖 Interactive API Documentation

FastAPI automatically generates interactive Swagger documentation, allowing developers to test every endpoint directly from the browser.

Features available inside Swagger:

- Live API testing
- Request validation
- Response schema
- Authentication support
- Automatic documentation generation

<p align="center">
<img src="screenshots/api-swagger.png">
</p>

---

# 📩 End-to-End SMS Delivery

SMSBridge successfully delivers SMS messages through the Android Traccar SMS Gateway using a secure Tailscale network.

Every SMS request follows this process:

1. Client sends a request to the FastAPI API.
2. The API validates the API key.
3. SMS details are stored in SQLite.
4. The request is securely forwarded through Tailscale.
5. The Android Traccar SMS Gateway receives the request.
6. The Android device sends the SMS using its SIM card.
7. The recipient receives the message.

<p align="center">
<img src="screenshots/sms-delivery.png" width="350">
</p>

---

# ✨ Features

SMSBridge combines API development, containerization, cloud deployment, monitoring, and secure networking into a single project.

## 🚀 REST API

The application exposes a RESTful API built using FastAPI.

Features include:

- Send SMS through Android device
- Retrieve SMS history
- Health Check Endpoint
- Metrics Endpoint
- Interactive Swagger Documentation

---

## 🔐 API Key Authentication

Every request to protected endpoints is validated using an API Key.

Benefits include:

- Prevents unauthorized access
- Lightweight authentication
- Easy integration with automation tools
- Suitable for internal/private deployments

---

## 📖 Swagger UI

FastAPI automatically generates interactive API documentation.

Developers can:

- Test endpoints
- View request schemas
- View response schemas
- Authenticate requests
- Execute API calls directly

---

## 🗄 SMS History

Every SMS request is stored inside SQLite.

Stored information includes:

- Recipient Number
- Message Content
- Timestamp
- Delivery Status (if available)

This provides a lightweight history system without requiring an external database.

---

## ❤️ Health Monitoring

SMSBridge provides a dedicated health endpoint.

Endpoint:

```http
GET /health
```

Example Response:

```json
{
    "status": "healthy"
}
```

This endpoint is useful for:

- Kubernetes Liveness Probe
- Kubernetes Readiness Probe
- External Health Checks
- Monitoring Systems

---

## 📊 Prometheus Metrics

Application metrics are exposed through:

```http
GET /metrics
```

Metrics include:

- HTTP Request Count
- Request Duration
- Status Codes
- API Performance
- Python Process Metrics

These metrics are collected automatically using:

```
prometheus-fastapi-instrumentator
```

---

# 🔒 Security

SMSBridge includes several security mechanisms.

## API Key Authentication

Protects all sensitive endpoints.

---

## Private Networking

The Android device is never publicly exposed.

Communication occurs through:

- Tailscale VPN
- Private Network
- Encrypted Traffic

---

## Kubernetes Secrets

Sensitive configuration values can be stored securely using Kubernetes Secrets instead of hardcoding credentials.

---

## Container Isolation

The application runs inside Docker containers, providing:

- Process Isolation
- Dependency Isolation
- Consistent Runtime Environment

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/tharunkumaran11/smsbridge.git
```

```bash
cd smsbridge
```

---

## Create Virtual Environment

Linux/macOS

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

Windows

```powershell
python -m venv venv

venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 Running Locally

Start the FastAPI server.

```bash
uvicorn app.main:app --reload
```

Application URL

```
http://localhost:8000
```

Swagger Documentation

```
http://localhost:8000/docs
```

Prometheus Metrics

```
http://localhost:8000/metrics
```

Health Check

```
http://localhost:8000/health
```

---

# 🐳 Docker Deployment

## Build Docker Image

```bash
docker build -t smsbridge .
```

---

## Run Container

```bash
docker run -d \
-p 8000:8000 \
--name smsbridge \
smsbridge
```

---

## Verify Running Containers

```bash
docker ps
```

---

## View Logs

```bash
docker logs smsbridge
```

---

## Stop Container

```bash
docker stop smsbridge
```

---

## Remove Container

```bash
docker rm smsbridge
```

---

# ☸ Kubernetes Deployment

Deploy SMSBridge to the Kubernetes cluster.

Apply Namespace

```bash
kubectl apply -f K8s/namespace.yaml
```

Deploy Secrets

```bash
kubectl apply -f K8s/secrets.yaml
```

Deploy Application

```bash
kubectl apply -f K8s/deployment.yaml
```

Deploy Service

```bash
kubectl apply -f K8s/service.yaml
```

---

## Verify Deployment

```bash
kubectl get pods
```

---

## Verify Services

```bash
kubectl get svc
```

---

## Check Logs

```bash
kubectl logs <pod-name>
```

---

## Access Application

If using NodePort, access the application through:

```
http://<EC2-Public-IP>:<NodePort>
```

---

The application is now deployed and ready to receive SMS requests through the FastAPI API.

---

# 📊 Monitoring & Observability

Monitoring is an essential part of any production-ready application. SMSBridge includes monitoring for both the application and the infrastructure using Prometheus and Grafana.

---

# 📈 Prometheus

Prometheus continuously collects metrics from the FastAPI application through the `/metrics` endpoint.

The metrics help monitor:

- Total HTTP Requests
- HTTP Response Status Codes
- Request Duration
- API Latency
- Python Process Metrics
- Memory Usage
- CPU Usage
- Active Requests

Metrics are collected automatically using:

```python
prometheus-fastapi-instrumentator
```

Prometheus scrapes the metrics endpoint at regular intervals and stores time-series data for visualization.

---

# 📉 Grafana Dashboards

Grafana connects directly to Prometheus and displays real-time dashboards.

The dashboards provide insights into:

- API Performance
- Infrastructure Health
- Request Statistics
- Response Time
- Resource Utilization

This makes it easy to identify performance bottlenecks and monitor the application's health.

---

# 📊 API Monitoring Dashboard

The API dashboard focuses on monitoring application-level metrics.

Displayed metrics include:

- Total API Requests
- Requests by Endpoint
- HTTP Status Codes
- Request Duration
- Average Response Time
- 95th Percentile Response Time
- Failed Requests

<p align="center">
<img src="screenshots/api-dashboard.png" width="950">
</p>

---

# 🖥 Infrastructure Dashboard

The infrastructure dashboard provides insights into the server running SMSBridge.

Displayed metrics include:

- CPU Usage
- Memory Usage
- Available Memory
- CPU Trend
- System Load
- Prometheus Health
- Node Exporter Status

<p align="center">
<img src="screenshots/infrastructure-dashboard.png" width="950">
</p>

---

# 📱 End-to-End SMS Delivery

One of the main goals of SMSBridge is to demonstrate complete end-to-end SMS communication.

The following workflow is performed whenever a request is made:

```text
Client
   │
   ▼
FastAPI API
   │
   ▼
Authentication
   │
   ▼
SQLite Database
   │
   ▼
Tailscale VPN
   │
   ▼
Android Traccar SMS Gateway
   │
   ▼
Recipient Mobile Phone
```

The Android device acts as the SMS gateway and sends messages using its SIM card.

<p align="center">
<img src="screenshots/sms-delivery.png" width="350">
</p>

---

# 🔄 CI/CD Pipeline

SMSBridge uses GitHub Actions to automate the build process.

Whenever code is pushed to GitHub:

1. GitHub Actions starts automatically.
2. Dependencies are installed.
3. Docker image is built.
4. Docker image is pushed to Docker Hub.
5. The latest image becomes available for deployment.

This reduces manual work and ensures consistent builds.

---

# 🚀 GitHub Actions Workflow

The GitHub Actions workflow automates the application's build pipeline.

Workflow stages:

- Checkout Repository
- Set up Python
- Install Dependencies
- Build Docker Image
- Login to Docker Hub
- Push Docker Image

<p align="center">
<img src="screenshots/github-actions.png" width="950">
</p>

---

# 🐳 Docker Hub

Docker Hub is used as the container image registry.

Benefits include:

- Versioned Docker Images
- Easy Image Distribution
- Kubernetes Compatibility
- Automated Image Pulling

Example image:

```text
tharunkumaran11/smsbridge:latest
```

<p align="center">
<img src="screenshots/dockerhub.png" width="950">
</p>

---

# 📸 Project Screenshots

This repository includes screenshots demonstrating different parts of the project.

| Screenshot | Description |
|------------|-------------|
| architecture.png | Overall system architecture |
| api-swagger.png | FastAPI Swagger documentation |
| sms-delivery.png | Successful SMS delivery |
| api-dashboard.png | Grafana API dashboard |
| infrastructure-dashboard.png | Infrastructure monitoring |
| github-actions.png | CI/CD pipeline |
| dockerhub.png | Docker image repository |

These screenshots provide visual proof of the application's functionality, deployment, and monitoring capabilities.

---

# 📈 Benefits of Monitoring

Monitoring helps ensure that the application remains healthy and performs efficiently.

Key advantages include:

- Early issue detection
- Performance analysis
- Resource utilization tracking
- Capacity planning
- Easier troubleshooting
- Improved reliability
- Better operational visibility

With Prometheus and Grafana integrated, SMSBridge provides a complete monitoring solution suitable for learning modern DevOps practices.

---

# 🛡 Security Best Practices

Security was considered throughout the development of SMSBridge to ensure safe communication between components.

---

## 🔐 API Key Authentication

Protected endpoints require an API key before processing requests.

Benefits:

- Prevents unauthorized access
- Lightweight authentication mechanism
- Easy integration with automation tools
- Suitable for internal deployments

---

## 🌐 Secure Private Networking

SMSBridge communicates with the Android device using **Tailscale VPN**.

Advantages include:

- End-to-end encrypted communication
- No public exposure of the Android device
- Secure remote access
- Simplified network configuration

---

## 🐳 Container Isolation

Running the application inside Docker provides:

- Dependency isolation
- Consistent runtime environment
- Easier deployments
- Simplified updates

---

## ☸ Kubernetes

Kubernetes improves application management by providing:

- Automated deployment
- Restart on failures
- Better scalability
- Simplified service management

---

## 🔒 Sensitive Configuration

Sensitive values such as API keys should be stored securely using environment variables or Kubernetes Secrets instead of hardcoding them into the application.

---

# 📌 Future Improvements

Although SMSBridge is fully functional, there are several enhancements that could be implemented in future versions.

### Planned Improvements

- JWT Authentication
- HTTPS with TLS Certificates
- Rate Limiting
- SMS Delivery Reports
- Helm Chart Packaging
- Horizontal Scaling
- Multi-device SMS Gateway Support
- Logging Dashboard
- SMS Scheduling
- Message Templates
- Retry Mechanism for Failed SMS
- Email Notifications for Critical Failures

---

# 📚 Skills Demonstrated

This project demonstrates practical experience in multiple DevOps and cloud technologies.

### Backend Development

- FastAPI
- Python
- REST APIs
- SQLite
- Swagger Documentation

---

### DevOps

- Docker
- Kubernetes (K3s)
- GitHub Actions
- Docker Hub
- Linux

---

### Cloud

- AWS EC2
- Container Deployment
- Image Management

---

### Monitoring

- Prometheus
- Grafana
- Metrics Collection
- Dashboard Creation

---

### Networking

- Tailscale
- Android Traccar SMS Gateway
- Secure Private Communication

---

### Software Engineering

- API Design
- Authentication
- Modular Project Structure
- Documentation
- Version Control using Git

---

# 🎓 Learning Outcomes

Building SMSBridge provided practical experience in designing, deploying, and monitoring a cloud-native application.

Key learnings include:

- Designing RESTful APIs
- Dockerizing applications
- Deploying workloads to Kubernetes
- Managing container images
- Building CI/CD pipelines
- Configuring monitoring tools
- Understanding observability
- Implementing secure networking
- Deploying applications on AWS
- Organizing production-style project structures

---

# 🤝 Contributing

Contributions are welcome.

If you'd like to improve SMSBridge:

1. Fork the repository.
2. Create a new feature branch.

```bash
git checkout -b feature/new-feature
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push the branch.

```bash
git push origin feature/new-feature
```

5. Open a Pull Request.

---

# 🐛 Troubleshooting

### Docker container not starting

Check container logs.

```bash
docker logs smsbridge
```

---

### Kubernetes pod not running

View pod status.

```bash
kubectl get pods
```

Describe the pod for detailed information.

```bash
kubectl describe pod <pod-name>
```

---

### View application logs

```bash
kubectl logs <pod-name>
```

---

### Prometheus metrics unavailable

Verify the metrics endpoint.

```text
http://localhost:8000/metrics
```

Ensure Prometheus is scraping the correct endpoint.

---

### Swagger UI unavailable

Verify that the FastAPI application is running.

Open:

```text
http://localhost:8000/docs
```

---

### SMS not being delivered

Verify:

- Android device is online.
- Traccar SMS Gateway is running.
- Tailscale connection is active.
- API key is valid.
- Recipient number is correct.

---

# 📊 Project Status

| Component | Status |
|------------|--------|
| FastAPI REST API | ✅ Completed |
| Swagger Documentation | ✅ Completed |
| API Authentication | ✅ Completed |
| SQLite SMS History | ✅ Completed |
| Docker Support | ✅ Completed |
| Kubernetes Deployment | ✅ Completed |
| GitHub Actions CI/CD | ✅ Completed |
| Docker Hub Integration | ✅ Completed |
| Prometheus Monitoring | ✅ Completed |
| Grafana Dashboards | ✅ Completed |
| Tailscale Integration | ✅ Completed |
| Android SMS Gateway | ✅ Completed |

---

# ⭐ Support

If you found this project useful:

- ⭐ Star the repository
- 🍴 Fork the repository
- 🛠 Suggest improvements
- 🐞 Report issues
- 💬 Share feedback

Your support is greatly appreciated!

---

# 👨‍💻 Author

<div align="center">

## Tharun Kumaran

Aspiring DevOps Engineer | Cloud Enthusiast | Backend Developer

</div>

---

## 📫 Connect With Me

<p align="left">

<a href="https://github.com/tharunkumaran11">
<img src="https://img.shields.io/badge/GitHub-tharunkumaran11-181717?style=for-the-badge&logo=github">
</a>

<!-- Replace with your LinkedIn profile -->
<a href="https://linkedin.com/in/tharunkumaran11">
<img src="https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin">
</a>

<!-- Replace with your email -->
<a href="mailto:tharunkumaranm@outlook.com">
<img src="https://img.shields.io/badge/Email-Contact-red?style=for-the-badge&logo=gmail">
</a>

</p>

---

# 🙏 Acknowledgements

This project was developed as a practical learning experience to explore modern DevOps technologies and cloud-native application deployment.

Special thanks to the communities and projects that make learning accessible:

- FastAPI
- Docker
- Kubernetes
- Prometheus
- Grafana
- GitHub Actions
- Docker Hub
- AWS
- Tailscale
- Traccar SMS Gateway

Their excellent documentation and open-source contributions made this project possible.

---

# 📚 References

Official documentation used while developing SMSBridge:

- FastAPI Documentation
- Docker Documentation
- Kubernetes Documentation
- Prometheus Documentation
- Grafana Documentation
- GitHub Actions Documentation
- Docker Hub Documentation
- AWS EC2 Documentation
- Tailscale Documentation
- Traccar SMS Gateway Documentation

---

# 🎯 Project Goals

The primary objective of SMSBridge was to gain practical experience in designing, deploying, and monitoring a real-world cloud-native application.

The project demonstrates knowledge of:

- REST API Development
- Authentication
- Docker
- Kubernetes
- Cloud Deployment
- CI/CD
- Monitoring
- Infrastructure Observability
- Secure Networking

---

# 📈 What I Learned

Developing SMSBridge provided hands-on experience with:

- Designing scalable REST APIs
- Deploying containerized applications
- Working with Kubernetes resources
- Creating CI/CD pipelines
- Monitoring applications using Prometheus
- Building Grafana dashboards
- Connecting distributed systems securely
- Managing Docker images
- Hosting applications on AWS EC2
- Troubleshooting production-style deployments

---

# 🚀 Future Roadmap

Future versions of SMSBridge may include:

- OAuth2 / JWT Authentication
- HTTPS using TLS
- SMS Scheduling
- Delivery Status Tracking
- Helm Charts
- Multi-Device SMS Support
- Retry Queue
- Web Dashboard
- Message Templates
- High Availability Deployment

---

# 📊 Project Summary

SMSBridge combines several modern technologies into a single end-to-end project.

### Backend

- FastAPI
- Python
- SQLite

### Cloud

- AWS EC2

### DevOps

- Docker
- Kubernetes (K3s)
- GitHub Actions
- Docker Hub

### Monitoring

- Prometheus
- Grafana

### Networking

- Tailscale

### SMS Gateway

- Android Traccar SMS Gateway

This project demonstrates the complete lifecycle of a cloud-native application—from development and deployment to monitoring and secure communication.

---

# 📄 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project in accordance with the terms of the MIT License.

---

# ⭐ Show Your Support

If you found this project useful, please consider:

- ⭐ Starring the repository
- 🍴 Forking the project
- 🛠 Contributing improvements
- 🐛 Reporting issues
- 💬 Sharing feedback

Every contribution and suggestion is greatly appreciated.

---

<div align="center">

# 🚀 Thank You for Visiting SMSBridge

Built with ❤️ using

**FastAPI • Docker • Kubernetes • AWS • Prometheus • Grafana • GitHub Actions • Docker Hub • Tailscale**

---

### ⭐ Star this repository if you enjoyed the project!

</div>
