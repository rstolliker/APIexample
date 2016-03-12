import bottle as b
from dbmanager import all_vals, insert_vals

# bottle server specifications

# client sends info here
# add message to db
@b.post("/send/")
def recieve_data():
    data = b.request.forms
    insert_vals(**data)
    #print(all_vals())

# sends raw data back
@b.route("/data")
@b.route("/data/")
def give_data():
    return {"data" : all_vals()}

if __name__ == '__main__':
    b.run(port=8000, host="0.0.0.0", debug=True)

