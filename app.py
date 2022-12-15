from flask import Flask, jsonify,request

app = Flask(__name__)#app es mi aplicación de servidor osea que es mi servidor

from products import products#importamos los datos de la lista de productos

@app.route('/ping')
def ping():
    return jsonify({"message":"Pong"})

@app.route('/products')
def getproducts():
    return jsonify({"products":products,"message": "Product's List"})

@app.route('/products/<string:product_name>')
def getProduct(product_name):#para buscar un producto
    productsFound = [product for product in products if product['name'] == product_name]
    if(len(productsFound) > 0):
        return jsonify({'produc':productsFound[0]})
    return jsonify({"messaje": "Produc not found"})

@app.route('/products', methods = ['post'])#para agrgar un producto nuevo
def addProduct():
    #print(request.json)#Para saber si me esta devolviendo los datos que me está envando el cliente
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'], #nuevo producto para agragar a mi lista principal
        "quantity": request.json['quantity']
    }
    products.append(new_product)
    return jsonify({"message": "product added succesfully","products":products})

@app.route('/products/<string:product_name>',methods = ['put'])#para actualizar un producto ponemos el metodo 'put'
def editproducts(product_name):#creamos una función para buscar el producto a editar
    productFound = [product for product in products if product['name'] == product_name]#para buscar y encontrar una lista con los productos que coincidan con mi busqueda
    if (len(productFound) > 0):#lo validamos con if del producto que buscamos
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            "message": "Product Updated",
            "product": productFound[0]
        })
    return jsonify({"messaje": "Produc not found"})

@app.route('/products/<string:product_name>', methods = ['DELETE'])#para eliminar un producto
def deleteProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]#para buscar y encontrar una lista con los productos que coincidan con mi busqueda
    if (len(productFound) > 0):
        products.remove(productFound[0])
        return jsonify({
           "message": "Product Delete",
           "products": products
        })
    return jsonify({"messaje": "Produc not found"})    
        

if __name__=='__main__': # para inicializar hacemos una condicional que pregunta si por el archivo pricipal 
    app.run(debug = True, port = 4000)# que  sería main, ejecutamos app con run y en modo debug por si hacemos algún cambio,
                                      #la aplicación se va a reiniciar, tambien especificamos el puerto donde queremos
                                      #que escuche nuestro servidor en esta caso sería 4000