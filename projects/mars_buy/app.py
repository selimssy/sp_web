from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.dhof2yp.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta



@app.route('/')
def home():
   return render_template('index.html')



@app.route("/mars", methods=["POST"])
def web_mars_post():

    name_receive = request.form['name_give']
    address_receive = request.form['address_give']
    size_receive = request.form['size_give']


    doc = {
        'name': name_receive,
        'address': address_receive,
        'size': size_receive
    }
    db.mars.insert_one(doc)


    return jsonify({'msg': '주문이 완료되었습니다!'})




# @app.route("/mars_update", methods=["POST"])
# def web_mars_post2():
#
#     name_receive2 = request.form['name_give2']
#
#
#     db.mars.delete_one({'name':name_receive2})
#     db.mars.update_one({'name': name_receive2}, {'$set': {'name': name_receive2}})
#
#     return jsonify({'msg': '삭제되었습니다.'})

#이건 나중에ㅠㅠ



@app.route("/mars_delete", methods=["POST"])
def web_mars_post3():

    name_receive3 = request.form['name_give3']


    db.mars.delete_one({'name':name_receive3})


    return jsonify({'msg': '삭제되었습니다.'})




@app.route("/mars", methods=["GET"])
def web_mars_get():
    order_list = list(db.mars.find({}, {'_id': False}))
    return jsonify({'orders': order_list})



if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)