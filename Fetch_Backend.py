from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for transactions
transactions = []
balances = {}

@app.route('/add', methods=['POST'])
def add_points():
    data = request.json
    payer = data['payer']
    points = data['points']
    timestamp = data['timestamp']

    # Store the transaction
    transactions.append({
        'payer': payer,
        'points': points,
        'timestamp': timestamp
    })

    # Update the balance for the payer
    if payer in balances:
        balances[payer] += points
    else:
        balances[payer] = points

    return '', 200

@app.route('/spend', methods=['POST'])
def spend_points():
    spend_request = request.json
    points_to_spend = spend_request['points']
    total_points = sum(balances.values())

    # Check if the user has enough points
    if points_to_spend > total_points:
        return 'Not enough points', 400

    # Spend the points, oldest first
    transactions.sort(key=lambda x: x['timestamp'])  # Sort by oldest timestamp
    spend_result = []
    points_spent = 0

    for transaction in transactions:
        if points_spent >= points_to_spend:
            break

        payer = transaction['payer']
        points_available = balances[payer]
        points_in_transaction = transaction['points']

        # Calculate the points to deduct
        deduct_points = min(points_in_transaction, points_to_spend - points_spent)

        if deduct_points > 0:
            balances[payer] -= deduct_points
            spend_result.append({"payer": payer, "points": -deduct_points})
            points_spent += deduct_points

    return jsonify(spend_result), 200

@app.route('/balance', methods=['GET'])
def get_balance():
    return jsonify(balances), 200

if __name__ == '__main__':
    app.run(port=8000)
