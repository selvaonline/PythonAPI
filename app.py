from flask import Flask,request

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
    request_data = request.get_json()
    print("Request Data",request_data)
    new_store = {"name":request_data["name"],"items":[]}
    stores.append(new_store)
    return new_store,201