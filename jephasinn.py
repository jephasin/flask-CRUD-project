import flask
from flask import request, jsonify
app = flask.Flask(__name__)
app.config["DEBUG"]=True

#We'll create some test data for our shop inventory called shop_inventory
Shop_inventory=[
{
 'id' : '0',
 'item' : 'Handbag',
 'price' : '$500',
 'quantity' : '20'
},
{
 'id' : '1',
 'item' : 'shoe',
 'price' : '$200',
 'quantity' : '30'
},
{
 'id' : '2',
 'item' : 'belt',
 'price' : '$100',
 'quantity' : '200'
},
{
 'id' : '3',
 'item' : 'wrist-watch',
 'price' : '$40',
 'quantity' : '25'
 }
]

@app.route("/", methods=['GET'])
def home():
    return jsonify("<h1>Shop inventory</h1>")
    
#To get all the items in the database we created, we use the object below
@app.route('/api/inventory', methods=['GET'])
def getallinventory():
    return jsonify({'Inventory':Shop_inventory})
    
#To get the details of a particular item with ID, we use the object below
@app.route('/api/inventory/<itemId>', methods=['GET'])
def getitemId(itemId):
    ID = [theitem for theitem in Shop_inventory if (theitem['id'] == itemId)]
    return jsonify({'theitem':ID})

#To update an item in the inventory we use the object below   
@app.route('/api/inventory/<itemId>',methods=['PUT'])
def updateItem(itemId):
    Id = [theitem for theitem in Shop_inventory if (theitem['id'] == itemId)]
    if 'item' in request.json:
        Id[0]['item'] = request.json['item']
    if 'price' in request.json:
        Id[0]['price'] = request.json['price']
    if 'quantity' in request.json:
        Id[0]['quantity'] = request.json['quantity']
    return jsonify({'theitem':Id[0]})

#The object below is used to add a new item to the inventory    
@app.route('/api/inventory', methods=['POST'])
def createItem():
    data={
    'id':request.json['id'],
    'item':request.json['item'],
    'price':request.json['price'],
    'quantity':request.json['quantity']
         }
    Shop_inventory.append(data)
    return jsonify(data)

#The object below is used to delete an item from the inventory    
@app.route('/api/inventory/<itemId>', methods=['DELETE'])
def deleteitem(itemId):
    Id = [item for item in Shop_inventory if (item['id'] == itemId)]
    if len(Id) == 0:
        abort(404)
    
    Shop_inventory.remove(Id[0])
    return jsonify({'feedback': 'Done'})

if __name__ == '__main__':
    app.run()