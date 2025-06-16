# Superheroes & Powers API

A simple Flask API that manages **Heroes**, their **Powers**, and the relationships between them using a `HeroPower` join model.


## Tech Stack

- Python 3.8+
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLite (default DB)
- Postman (for testing)


## Project Structure

server/
├── app.py
├── config.py
├── extensions.py
├── models.py
├── migrations/
├── seed.py
├── db.sqlite3
└── README.md

## Setup Instructions

1. Clone the repo
   ```bash
   git clone <https://github.com/aminacherop/   Phase-4-Code-Challenge-Superheroes>
   cd server
---
2. Create virtual environment and activate
 ```bash
python3 -m venv venv
source venv/bin/activate 

3. **Set environment variables**
  ```bash
 export FLASK_APP=app
 export FLASK_ENV=development

4.Run migrations
 ```bash
flask db init
flask db migrate -m "initial"
flask db upgrade

5.Seed the database
  ```bash
python seed.py

6.Run the server
  ```bash
flask run


7.Testing with Postman
Import the provided Postman Collection (Superheroes.postman_collection.json) into Postman.
Use the base URL: http://127.0.0.1:5000

8.API Endpoints

Heroes

GET /heroes - List all heroes
GET /heroes/<id> - Get details of a specific hero

Powers

GET /powers - List all powers
GET /powers/<id> - Get a specific power
PATCH /powers/<id> - Update a power’s description

Hero Powers

POST /hero_powers - Assign a power to a hero

9.Validations
Power.description must be present and at least 20 characters

HeroPower.strength must be one of: "Strong", "Weak", or "Average"
8.License
MIT