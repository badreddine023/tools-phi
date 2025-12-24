# 🏗️ Φ-Chain Build and Deployment Guide

This document outlines the steps required to build, test, and deploy the Φ-Chain components.

---

## 1. Prerequisites

Ensure you have the following tools installed on your system:

- **Git**: For cloning the repository.
- **Python 3.11+**: The core language for Φ-Chain.
- **pip**: Python package installer.
- **Docker** and **Docker Compose**: For containerized deployment.
- **Make**: For simplified build commands (optional but recommended).

---

## 2. Setting Up the Development Environment

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/badreddine023/phi-chain.git
    cd phi-chain
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    # Note: If requirements.txt is missing, use the following:
    # pip install uvicorn fastapi sqlalchemy requests pycryptodome matplotlib
    ```

---

## 3. Building the Core Components

The build process involves compiling the core mathematical and cryptographic modules.

### 3.1. Mathematical Primitives (Core)

The core logic relies on high-precision integer arithmetic for consensus.

```bash
# Compile the core Fibonacci and Golden Ratio logic
python3 core/build_math_primitives.py
```

### 3.2. Docker Image Build

For production and testing environments, build the Docker images:

```bash
# Build the base image for all services
docker build -t phichain/base:latest -f Dockerfile.base .

# Build individual service images
docker-compose build
```

---

## 4. Testing and Validation

Before deployment, all components must pass the security and mathematical integrity tests.

1.  **Run Unit and Integration Tests:**
    ```bash
    python3 -m pytest tests/
    ```

2.  **Run the Phi-Security-Tool (Static Analysis):**
    ```bash
    # This tool checks for hardcoded secrets, SQL injection, and mathematical errors.
    python3 tools/phi_security_tool.py --scan-all
    ```

---

## 5. Deployment

### 5.1. Local Deployment (Docker Compose)

Use Docker Compose for a quick, isolated local testnet:

```bash
# Start the services (consensus, API, monitoring)
docker-compose up -d
```

### 5.2. Mainnet Deployment (Kubernetes/Terraform)

Refer to the `deployments/` directory for production-ready scripts:

-   `deployments/kubernetes/`: Helm charts and YAML files.
-   `deployments/terraform/`: Infrastructure as Code for cloud providers.

---

## 6. Clean Up

To stop and remove the local Docker containers:

```bash
docker-compose down
```
