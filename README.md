Points Management Backend (Flask API)
This project is a Flask-based backend API for managing a point-based transaction system, where points can be added and spent from multiple payers. The points are spent using a first-in-first-out (FIFO) method based on the transaction timestamp.

Features
Add points to specific payers.
Spend points across all payers starting from the oldest transaction.
Retrieve the current balance of all payers.
Endpoints
1. Add Points
URL: /add
Method: POST
Description: Adds points for a specific payer.
Request Body:
{
  "payer": "DANNON",
  "points": 1000,
  "timestamp": "2023-09-29T10:00:00Z"
}
Response: Status code 200 on success.
2. Spend Points
URL: /spend
Method: POST
Description: Spends a specified number of points across all payers using the FIFO method.
Request Body:
{
  "points": 500
}
Response: A list of points spent for each payer:
[
  {
    "payer": "DANNON",
    "points": -100
  },
  {
    "payer": "UNILEVER",
    "points": -400
  }
]
3. Get Balance
URL: /balance
Method: GET
Description: Retrieves the current point balances of all payers.
Response:
{
  "DANNON": 1000,
  "UNILEVER": 500
}
Setup Instructions
Prerequisites
Python 3.x
Flask (pip install Flask)
Steps to Run
Clone the repository:
git clone https://github.com/olakt-ogun/Fetch-Backend-Coding-Exercise.git
Navigate to the project directory on Command Prompt or a terminal:
cd your repository
Install dependencies: pip install Flask
Run the application: python Fetch_Backend.py
The server will start at http://127.0.0.1:8000.
Notes
This project uses in-memory storage, so the data will be lost when the application restarts.
Points are spent starting from the oldest transaction based on the timestamp (FIFO).
Negative balances are not explicitly handled, so it's assumed that no negative point transactions will be added.

Feel free to copy or modify it as needed!
