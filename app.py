from flask import Flask, jsonify

app = Flask(__name__)#app es mi aplicación de servidor osea que es mi servidor

from products import products#importamos los datos de la lista de productos

@app.route('/ping')
def ping():
    return jsonify({"message":"Pong"})

@app.route('/products')
def getproducts():
    return jsonify({"products":products,"message": "Product's List"})

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if(len(productsFound) > 0):
        return jsonify({'produc':productsFound[0]})
    return jsonify({"messaje": "Produc not found"})

if __name__=='__main__': # para inicializar hacemos una condicional que pregunta si por el archivo pricipal 
    app.run(debug = True, port = 4000)# que  sería main, ejecutamos app con run y en modo debug por si hacemis algún cambio
                                      #la aplicación se va a reiniciar tambien especificamos el puerto donde queremos
                                      #que escuche nuestro servidor en esta caso sería 4000