from flask import Flask

app = Flask(__name__)

stores = [
    {
        "name":"myStore",
        "items" : [
            {
                "name" : "chair",
                "price": 14.99
            },
            {
                "name" :"table",
                "price":49.99 
            }
        ]
    }
]

@app.get("/store")

def get_stores():
    return {
        "stores": stores
    }

@app.post("/store")

def create_store():
    pass