# 🎣 FishAPI

**FishAPI** is a Flask-based backend for storing and analyzing fishing sessions. If you're an avid angler, this API lets you record the location, time, number of rods, bait types, catches, and provides statistics across all sessions.

---

## 📦 Project Structure

FishAPIs/
├── app.py # Main Flask entry point
├── resources/ # Blueprints for sessions and statistics
│ ├── session.py
│ └── statistic.py
├── data/ # Mutable data (sessions.json)
├── test_data.json # Sample session data
├── Dockerfile # Docker image definition
├── docker-compose.yml # Container orchestration
└── README.md # Project description

---

## 🚀 Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/VolodymyrBoychuk/FishAPIs.git
   cd FishAPIs
   ```

# Start the application:

docker-compose up --build

# Open Swagger UI in your browser:

http://127.0.0.1:5050/swagger-ui

# API Endpoints

# Session

• GET /session — retrieve all sessions
• GET /session/<id> — retrieve a specific session
• POST /session — create a new session
• PUT /session/<id> — update a session
• DELETE /session/<id> — delete a session

# Statistic

• GET /statistic — get total number of fish, total weight, and species breakdown

# Sample Data (from `test_data.json`)

{
"session_id": "2025-08-10-003",
"date": "2025-08-10",
"location": {
"name": "Desna River",
"coordinates": {
"latitude": 51.0412,
"longitude": 30.9784
}
},
"fishing_rods": 2,
"bait": ["worm", "boilies"],
"catches": [
{
"species": "carp",
"weight_kg": 3.2,
"length_cm": 70.0,
"time": "06:50"
},
{
"species": "bream",
"weight_kg": 1.0,
"length_cm": 40.0,
"time": "08:15"
}
],
"notes": "Warm morning, slow start but picked up after sunrise"
}

## Technologies Used

• Flask
• Flask-Smorest
• Docker + Docker Compose
• Swagger UI (OpenAPI 3.0.3)
