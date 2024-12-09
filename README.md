
# **Receipt Processor**

A Flask-based web service for processing receipts and calculating the points awarded from them.

---

## **Features**
- Submit a receipt for processing.
- Get reqard points from the receipt with a unique ID.

---

## **Endpoints**

### **1. `POST /receipts/process`**
- **Purpose**: Processes a receipt and calculates reward points.
- **Input**: JSON payload with receipt details.
- **Response**: A unique receipt ID.

#### Example Request:
```bash
curl -X POST http://127.0.0.1:5000/receipts/process \
-H "Content-Type: application/json" \
-d '{
    "retailer": "BestBuy",
    "purchaseDate": "2023-12-01",
    "purchaseTime": "15:15",
    "items": [
        {"shortDescription": "Wireless Mouse", "price": "29.99"},
        {"shortDescription": "USB-C Charger", "price": "19.99"},
        {"shortDescription": "Bluetooth Speaker", "price": "49.99"},
        {"shortDescription": "HDMI Cable", "price": "14.99"},
        {"shortDescription": "External Hard Drive", "price": "89.99"}
    ],
    "total": "204.95"
}'
```

#### Example Response:
```json
{
  "id": "5de61e85-efda-40c1-b58a-e942c970604a"
}
```

---

### **2. `GET /receipts/<id>/points`**
- **Purpose**: Retrieves reward points for a processed receipt using its unique ID.
- **Input**: Receipt ID in the URL path.
- **Response**: Points awarded for the receipt.

#### Example Request:
```bash
curl -X GET http://127.0.0.1:5000/receipts/123e4567-e89b-12d3-a456-426614174000/points
```

#### Example Response:
```json
{
  "points": 75
}
```

---

## **Requirements**
- Python 3.9 or later
- Flask 2.2.5
- Docker (optional for containerization)

---

## **Installation**

### **1. Clone the Repository**
```bash
git clone <repository-url>
cd receiptProcessor
```

### **2. Install Dependencies**
#### Using Python:
1. Set up a virtual environment (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

#### Using Docker:
1. Build the Docker image:
   ```bash
   docker build -t receipt-processor .
   ```
2. Run the container:
   ```bash
   docker run -p 5000:5000 receipt-processor
   ```

---

## **Usage**

### **1. Run the Application**
#### Using Python:
```bash
python app.py
```

#### Using Docker:
```bash
docker run -p 5000:5000 receipt-processor
```

### **2. Test the Endpoints**
Use `curl` to test the API.

#### Submit a Receipt:
```bash
curl -X POST http://127.0.0.1:5000/receipts/process \
-H "Content-Type: application/json" \
-d '{
    "retailer": "BestBuy",
    "purchaseDate": "2023-12-01",
    "purchaseTime": "15:15",
    "items": [
        {"shortDescription": "Wireless Mouse", "price": "29.99"},
        {"shortDescription": "USB-C Charger", "price": "19.99"},
        {"shortDescription": "Bluetooth Speaker", "price": "49.99"},
        {"shortDescription": "HDMI Cable", "price": "14.99"},
        {"shortDescription": "External Hard Drive", "price": "89.99"}
    ],
    "total": "204.95"
}'
```

#### Retrieve Points:
```bash
curl -X GET http://127.0.0.1:5000/receipts/123e4567-e89b-12d3-a456-426614174000/points
```

---
