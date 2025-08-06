# ANIME_RECOMMENDER_LLMOPS

An anime recommendation system powered by LLMs, containerized with Docker, deployed via Kubernetes, and built with a production-ready MLOps pipeline.

## 📌 Project Overview

This project builds an end-to-end **Large Language Model (LLM)**-based anime recommendation system.  
It takes user prompts, processes them through a language model, and provides meaningful anime suggestions.  
The project includes a modular architecture and is designed for **production deployment** using **Docker, Kubernetes, and GCP**.

---

## 🧱 Project Structure

```bash
├── app/                    # Streamlit frontend app
├── chroma_db/             # Local vector DB setup using Chroma
├── config/                # Configuration files
├── data/                  # Datasets
├── pipeline/              # Training and recommendation pipeline
├── src/                   # Core logic (loader, prompt handler, recommender)
├── utils/                 # Utility functions
├── dockerfile             # Docker image definition
├── llmops-k8s.yaml        # Kubernetes deployment configuration
├── requirements.txt       # Python dependencies
└── test.py                # Test script
```

---

## 🧠 Technologies Used

### 🤖 LLM & Prompt Engineering
- [Groq API](https://groq.com/) — High-performance LLM inference
- [Hugging Face API](https://huggingface.co/) — Model access
- Custom Prompt Templates — Tailored prompts for better recommendations

### 🧪 Data Pipeline
- Modular `DataLoader`, `PromptHandler`, and `AnimeRecommender` classes
- Vector embedding storage via **ChromaDB**

### 🐳 Containerization
- Fully containerized using Docker
- Dockerfile for reproducible builds

### ☸️ Kubernetes Deployment
- `llmops-k8s.yaml` for K8s deployment
- Tested with **Minikube** and **GCP**
- Managed using `kubectl`

### ☁️ GCP (Google Cloud Platform)
- Hosted on a GCP VM instance
- Firewall and access rules configured for Kubernetes cluster

### 🔄 CI/CD & Version Control
- GitHub used for version control and integration
- Environment configurations and deployment specs are tracked

---

## 📊 Monitoring (Coming Soon)

Monitoring stack to be integrated:

- **Grafana Cloud** — For real-time Kubernetes cluster metrics
- **Prometheus** — For metrics collection and alerting
- Track pod performance, latency, memory/CPU usage, and error logs

🔧 *This section will be updated once monitoring is fully set up.*

---

## ⚙️ Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🐳 Docker Usage

```bash
# Build Docker image
docker build -t anime-recommender .

# Run container
docker run -p 8501:8501 anime-recommender
```

---

## ☸️ Kubernetes Deployment

```bash
# Deploy using kubectl
kubectl apply -f llmops-k8s.yaml

# Check running pods
kubectl get pods

# View logs
kubectl logs <pod-name>
```

---

## 📍 Roadmap

- [x] HuggingFace & Groq API Integration
- [x] ChromaDB vector DB
- [x] Docker containerization
- [x] Kubernetes deployment
- [x] GCP instance setup
- [ ] Monitoring with Grafana + Prometheus

---

## 👩‍💻 Developer

- [Elif Sakin](https://github.com/sakinnn) — AI / MLOps Developer
---

