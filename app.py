from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

receipts = {}

@app.route('/receipts/process', methods=['POST'])
def processReceipt():
    print("starting now")
    try:
        data = request.get_json()
        if not data:
            return jsonify({"Error": "Invalid JSON payload"}), 400
        
        # Generate UUid and Calculate Points
        receiptId = str(uuid.uuid4())
        points = calculatePoints(data)
        
        # Storing Receipt information
        receipts[receiptId] = {"points": points, "receipt": data}
        return jsonify({"id": receiptId}), 200
    except Exception as e:
        return jsonify({"Error": str(e)}), 500

@app.route('/receipts/<receiptId>/points', methods=['GET'])
def getPoints(receiptId):
    if receiptId not in receipts:
        return jsonify({"Error": "Receipt ID not found"}), 404
    return jsonify({"points": receipts[receiptId]["points"]}), 200

def calculatePoints(receipt):
    points = 0
    retailer = receipt.get("retailer", "")
    total = receipt.get("total", "0")
    purchaseDate = receipt.get("purchaseDate", "")
    purchaseTime = receipt.get("purchaseTime", "")
    items = receipt.get("items", [])
    
    # Calculate points based off of retailer name
    points += sum(c.isalnum() for c in retailer)
    
    # Add 50 points if the total is a round dollar amount
    if total.endswith(".00"):
        points += 50
    # Add 25 points if the total is a multiple of 0.25
    if float(total) % 0.25 == 0:
        points += 25

    # For every 2 items on the receipt 5 points are added
    points += (len(items) // 2) * 5

    # Checks trimmed length condition 
    for item in items:
        description = item.get("shortDescription", "").strip()
        price = float(item.get("price", "0"))
        if len(description) % 3 == 0:
            points += int(price * 0.2 + 0.5)

    # Add 6 points if the purchase date day is odd
    if purchaseDate and int(purchaseDate.split("-")[2]) % 2 == 1:
        points += 6

    # adds 10 points if the time of the purchase is between 2-4 pm
    if purchaseTime and "14:00" <= purchaseTime <= "16:00":
        points += 10

    return points

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
