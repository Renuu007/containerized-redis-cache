# Containerized Redis Cache

A simple, containerized key-value cache microservice built with Python, FastAPI, and Redis. Exposes REST endpoints to set/get values with optional TTL (Time To Live). Designed for easy local deployment using Docker Compose.

---

## Features
- **REST API**: Set and get key-value pairs
- **TTL Support**: Optional expiration for cache entries
- **Redis Backend**: High-performance, in-memory data store
- **Containerized**: Easy to run anywhere with Docker
- **Local Development**: One-command startup with Docker Compose

---

## Architecture
- **FastAPI**: Python web framework for REST endpoints
- **Redis**: In-memory cache store
- **Docker**: Containerizes both app and Redis
- **Docker Compose**: Orchestrates multi-container setup

See [`documentation.md`](documentation.md) for detailed architecture and diagrams.

---

## Quickstart

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (includes Docker Compose)

### Clone the Repository
```sh
git clone https://github.com/Renuu007/containerized-redis-cache
cd containerized-redis-cache
```

### Build and Run
```sh
docker compose up --build
```

### API Usage Examples

#### Set a Value
```sh
curl -X POST "http://localhost:8000/set" -H "Content-Type: application/json" -d '{"key":"foo","value":"bar","ttl":60}'
```

#### Get a Value
```sh
curl "http://localhost:8000/get?key=foo"
```

---

## Documentation
- [How to Run](howtorun.md)
- [Detailed Documentation & Architecture](documentation.md)

---

## License
MIT 
