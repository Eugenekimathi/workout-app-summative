# Flask SQLAlchemy Workout Application Backend

## Project Description

This project is a RESTful backend API built with **Flask**, **SQLAlchemy**, and **Marshmallow** for a workout tracking application. It allows personal trainers to create workouts, manage reusable exercises, and associate exercises with workouts through a join table that stores workout-specific details such as sets, reps, and duration.

The project demonstrates:

* Flask application structure
* SQLAlchemy models and relationships
* Database migrations with Flask-Migrate
* Model and schema validations
* Marshmallow serialization
* RESTful API endpoints
* Database seeding

## Installation Instructions

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Navigate to the project directory:

```bash
cd workout-app-summative
```

3. Install the project dependencies:

```bash
pipenv install
```

4. Activate the virtual environment:

```bash
pipenv shell
```

5. Navigate to the server directory:

```bash
cd server
```

6. Initialize the database (first time only):

```bash
flask db init
```

7. Generate a migration:

```bash
flask db migrate -m "Initial migration"
```

8. Apply the migration:

```bash
flask db upgrade
```

9. Seed the database:

```bash
python seed.py
```

## Run Instructions

Start the Flask development server:

```bash
flask run --port 5555
```

The API will be available at:

```
http://127.0.0.1:5555
```

## API Endpoints

### Workouts

* `GET /workouts` — Retrieve all workouts.
* `GET /workouts/<id>` — Retrieve a single workout and its associated exercises.
* `POST /workouts` — Create a new workout.
* `DELETE /workouts/<id>` — Delete a workout.

### Exercises

* `GET /exercises` — Retrieve all exercises.
* `GET /exercises/<id>` — Retrieve a single exercise and its associated workouts.
* `POST /exercises` — Create a new exercise.
* `DELETE /exercises/<id>` — Delete an exercise.

### Workout Exercises

* `POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises` — Associate an exercise with a workout while recording workout-specific details such as sets, reps, and duration.

## Technologies Used

* Python 3
* Flask
* Flask-SQLAlchemy
* Flask-Migrate
* Marshmallow
* SQLite
* Pipenv
