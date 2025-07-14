# How to Run: Containerized Redis Cache

This guide walks you through running the Containerized Redis Cache microservice locally on Windows using Docker Compose.

---

## Prerequisites
- **Docker Desktop** (includes Docker Compose)
- **Windows 10/11** (PowerShell recommended)

---

## Setup Steps

### 1. Clone the Repository
```powershell
git clone <your-repo-url>
cd containerized-redis-cache
```

### 2. Build and Start the Services
```powershell
docker compose up --build
```
- This will build the FastAPI app and start both the app and Redis containers.

### 3. Test the API Endpoints

#### Set a Value (PowerShell)
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/set" -Method Post -Body '{"key":"foo","value":"bar","ttl":60}' -ContentType "application/json"
```

#### Or with curl.exe
```powershell
curl.exe -X POST "http://localhost:8000/set" -H "Content-Type: application/json" -d '{"key":"foo","value":"bar","ttl":60}'
```

#### Get a Value
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/get?key=foo" -Method Get
```

---

## Stopping the Services
- Press `Ctrl+C` in the terminal to stop.
- To remove containers:
```powershell
docker compose down
```

---

## Troubleshooting
- **Cannot connect to localhost:8000**: Ensure both containers are running (`docker ps`).
- **422 Unprocessable Entity**: Check your JSON formatting and use single quotes for the data argument in PowerShell.
- **Redis connection errors**: The app connects to Redis using the service name `redis` (see `docker-compose.yml`).
- **Logs**: View logs with `docker compose logs`.

---

For more details, see [documentation.md](documentation.md). 