# Workout App Summative

## Description

The **Workout App Summative** is a Flask REST API that allows users to manage workout routines and exercises. It demonstrates the use of **Flask**, **Flask-SQLAlchemy**, **Marshmallow**, and **Flask-Migrate** to build a backend application with proper data validation, database relationships, and RESTful API endpoints.

The application manages three related entities:

* **Workout** – stores workout sessions including the workout date, duration, and notes.
* **Exercise** – stores available exercises and their categories.
* **WorkoutExercise** – serves as the association table between workouts and exercises while storing workout-specific details such as sets, repetitions, and duration.

This project demonstrates:

* RESTful API endpoints
* SQLAlchemy models and relationships
* Marshmallow serialization and validation
* Model-level validations
* Database table constraints
* Database migrations
* Database seeding

---

# Project Layout

```text
workout-app-summative/
│
├── migrations/                 # Flask-Migrate migration files
│   └── versions/
│
├── instance/
│   └── app.db                  # SQLite database
│
├── server/
│   ├── app.py                  # Flask application and API routes
│   ├── models.py               # SQLAlchemy models, relationships & validations
│   ├── schemas.py              # Marshmallow schemas and serialization
│   ├── seed.py                 # Populates the database with starter data
│   └── __init__.py
│
├── Pipfile
├── Pipfile.lock
├── README.md

```

---

# Technologies Used

* Python 3
* Flask
* Flask-SQLAlchemy
* Marshmallow
* Flask-Migrate
* SQLite
* Pipenv
* Postman

---

# Installation

Clone the repository.

```bash
git clone <repository-url>
cd workout-app-summative
```

Install project dependencies.

```bash
pipenv install
```

Activate the virtual environment.

```bash
pipenv shell
```

---

# Database Setup and Migrations

The project uses **Flask-Migrate** to manage database migrations.

All commands should be run from the **project root directory**:

```text
workout-app-summative/
```

Set the Flask application.

### Git Bash / Linux / macOS

```bash
export FLASK_APP=server.app
```

### Windows PowerShell

```powershell
$env:FLASK_APP="server.app"
```

Apply the existing migrations:

```bash
flask db upgrade
```

This creates the required database tables:

* `workouts`
* `exercises`
* `workout_exercises`

---

# Seeding the Database

The project includes a seed file that creates starter records for every model.

Run:

```bash
python -m server.seed
```

The seed file creates:

* Six exercises
* Three workouts
* Six workout-exercise relationships

---

# Running the Application

Start the Flask development server from the project root:

```bash
python -m server.app
```

The application will start on:

```text
http://127.0.0.1:5555
```

The API is now ready for testing using **Postman**.

> Do not run the application from inside the `server` directory. Running from the project root ensures Flask uses the correct database location.

---

# Complete Setup Flow

After cloning the project:

```bash
pipenv install

pipenv shell

export FLASK_APP=server.app

flask db upgrade

python -m server.seed

python -m server.app
```

---

# Database Migration Commands

If SQLAlchemy models are changed:

Create a migration:

```bash
flask db migrate -m "describe changes"
```

Apply the migration:

```bash
flask db upgrade
```

Check the current migration version:

```bash
flask db current
```

---

# API Endpoints

## Workout Endpoints

| Method | Endpoint         | Description                 |
| ------ | ---------------- | --------------------------- |
| GET    | `/workouts`      | Retrieve all workouts       |
| GET    | `/workouts/<id>` | Retrieve a specific workout |
| POST   | `/workouts`      | Create a new workout        |
| DELETE | `/workouts/<id>` | Delete a workout            |

## Exercise Endpoints

| Method | Endpoint          | Description                  |
| ------ | ----------------- | ---------------------------- |
| GET    | `/exercises`      | Retrieve all exercises       |
| GET    | `/exercises/<id>` | Retrieve a specific exercise |
| POST   | `/exercises`      | Create a new exercise        |
| DELETE | `/exercises/<id>` | Delete an exercise           |

## Workout Exercise Endpoint

| Method | Endpoint                                         | Description                  |
| ------ | ------------------------------------------------ | ---------------------------- |
| POST   | `/workouts/<workout_id>/exercises/<exercise_id>` | Add an exercise to a workout |

---

# Testing the API with Postman

The API endpoints can be tested using **Postman**.

## Create a Workout

**Method:** POST

**URL:**

```text
http://127.0.0.1:5555/workouts
```

JSON Body:

```json
{
  "date": "2025-07-20",
  "duration_minutes": 45,
  "notes": "Upper body workout"
}
```

---

## Get All Workouts

**Method:** GET

**URL:**

```text
http://127.0.0.1:5555/workouts
```

---

## Create an Exercise

**Method:** POST

**URL:**

```text
http://127.0.0.1:5555/exercises
```

JSON Body:

```json
{
  "name": "Mountain Climbers",
  "category": "Cardio",
  "equipment_needed": false
}
```

---

## Add an Exercise to a Workout

**Method:** POST

**URL:**

```text
http://127.0.0.1:5555/workouts/1/exercises/2
```

JSON Body:

```json
{
  "sets": 3,
  "reps": 15,
  "duration_seconds": 60
}
```

---

# Serialization

The project uses Marshmallow schemas to serialize and deserialize application data.

Schemas included:

* WorkoutSchema
* ExerciseSchema
* WorkoutExerciseSchema

Nested schemas are used to serialize related objects while preventing circular references.

---

# Relationships

The application implements a **many-to-many relationship** between **Workout** and **Exercise** using the **WorkoutExercise** association model.

```text
Workout
    │
    ├── One-to-Many
    │
WorkoutExercise
    │
    ├── Many-to-One
    │
Exercise
```

This design allows one workout to contain multiple exercises, while the same exercise can belong to multiple workouts.

---

# Schema Validations

Marshmallow validates incoming request data before it reaches the database.

Implemented validations include:

* Exercise name must contain at least two characters.
* Exercise category must be one of:

  * Strength
  * Cardio
  * Flexibility
  * Balance
* Workout duration must be greater than zero.

Invalid requests return a **400 Bad Request** response.

---

# Model Validations

SQLAlchemy model validators enforce business rules before data is committed.

Examples include:

* Exercise name cannot be empty.
* Exercise name must contain at least two characters.
* Workout duration must be positive.
* WorkoutExercise repetitions cannot be negative.
* WorkoutExercise sets cannot be negative.
* WorkoutExercise duration cannot be negative.

---

# Table Constraints

Database constraints ensure data integrity.

Implemented constraints include:

* Unique exercise names.
* Workout duration must be greater than zero.
* Repetitions must be non-negative.
* Sets must be non-negative.
* Exercise duration must be non-negative.

---

# Error Handling

The API returns meaningful HTTP status codes.

| Status Code | Description                     |
| ----------- | ------------------------------- |
| 200         | Successful request              |
| 201         | Resource created successfully   |
| 400         | Validation or bad request error |
| 404         | Resource not found              |

---

# Future Improvements

* Add update (PATCH) endpoints
* User authentication
* Workout plans
* Exercise search and filtering
* Pagination
* Workout statistics and reporting

---

# Author

**Kimathi**

Flask SQLAlchemy Workout App Summative

