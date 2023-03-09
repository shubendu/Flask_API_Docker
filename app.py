from flask import Flask
from flask_smorest import Api

from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint


app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)


# #all stores data
# @app.get("/store")
# def get_stores():
    
#     return {"stores": list(stores.values())}

# #create store
# @app.post("/store")
# def create_store():
#     store_data = request.get_json()
#     if "name" not in store_data:
#         abort(400, message="bad request, ensure name is included in the json payload")
#     for store in stores.values():
#         if store_data["name"] == store["name"]:
#             abort(400, message="store already exists")
#     store_id =  uuid.uuid4().hex
#     store = {**store_data, "id":store_id}
#     stores[store_id] = store 
#     return store, 201

# #create item
# @app.post("/item")
# def create_item():
#     item_data = request.get_json()
#     #error handling
#     #here not only we need to validate data exitst,
#     #but also what type of data. for example price should be in float
#     if ("price" not in item_data or "store_id" not in item_data or "name" not in item_data):
#         abort(400, message="Bad request. Ensure price storeid and name are  included in the  JSON payload")
        
#     for item in items.values():
#         if(
#             item_data["name"] == item["name"]
#             and item_data["store_id"] == item["store-id"]
#         ):
#             abort(400,message="item already exists")
            
#     if item_data["store_id"] not in stores:
#         abort(404, message="store not found")
    
#     item_id =  uuid.uuid4().hex
#     item = {**item_data, "id":item_id}
#     items[item_id] = item 
#     return item, 201

# #get all items information
# @app.get("/item")
# def get_all_items():
#     return {"items": list(items.values())}

# #get individual store
# @app.get("/store/<string:store_id>")
# def get_store(store_id):
#     try:   
#         return stores[store_id]
#     except KeyError:
#         abort(404, message="store not found")
        
# #updating item
# @app.put("/item/<string:item_id>")
# def upddate_item(item_id):
#     item_data  = request.get_json()

#     if ("price" not in item_data or "name" not in item_data):
#         abort(400, message="Bad request. Ensure price and name are  included in the  JSON payload")
    
#     try:
#         item = items[item_id]
        
#         #inpace update of dictionary
#         item |= item_data
#         return item
#     except KeyError:
#         abort(404, message="Item not found")


# #get individual item
# @app.get("/item/<string:item_id>")
# def get_item(item_id):
#     try:   
#         return items[item_id]
#     except KeyError:
#         abort(404, message="item not found")
        

# #delete an item
# @app.delete("/item/<string:item_id>")
# def delete_item(item_id):
#     try:
#         del items[item_id]
#         return {"message":"Item deleted"}
#     except KeyError:
#         abort(404, message="Item not found")
        
# #delete store
# @app.delete("/store/<string:store_id>")
# def delete_store(store_id):
#     try:
#         del stores[store_id]
#         return {"message":"store deleted"}
#     except KeyError:
#         abort(404, message="store not found")

    
