from flask import Flask,redirect,render_template,request,url_for
from flask.globals import request, session
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.secret_key="!@#$%^&*"

#Database configuration
#app.config['SQLALCHEMY_DATABASE_URI']=mysql+pymysql://username:password@localhost/databasename

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/crudguvi'
db=SQLAlchemy(app)

class Products(db.Model):
    product_id=db.Column(db.Integer,primary_key=True)
    productName=db.Column(db.String(100))
    productDescription=db.Column(db.String(500))
    rating=db.Column(db.Integer)
    stocks=db.Column(db.Integer)
    prize=db.Column(db.Integer)



@app.route("/")
def index():
    products=Products.query.all()
    return render_template("index.html",products=products)
    
@app.route("/create",methods=['GET','POST'])
def create():
    if request.method=='POST':
        productName=request.form.get("productName")
        productDescription=request.form.get("product_description")
        rating=request.form.get("rating")
        stocks=request.form.get("stocks")
        prize=request.form.get("prize")
        query=Products(productName=productName,productDescription=productDescription,rating=rating,stocks=stocks,prize=prize)
        db.session.add(query)
        db.session.commit()
    return redirect("/")


@app.route("/edit/<int:id>",methods=['GET','POST'])
def edit(id):
    product=Products.query.filter_by(product_id=id).first()
    if request.method=='POST':
        product.productName = request.form.get("productName")
        product.productDescription = request.form.get("product_description")
        product.rating = request.form.get("rating")
        product.stocks = request.form.get("stocks")
        product.prize = request.form.get("prize")
        # query=Products(productName=productName,productDescription=productDescription,rating=rating,stocks=stocks,prize=prize)
        # db.session.add(query)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("edit.html",product=product)

@app.route("/delete/<int:id>",methods=['GET'])
def delete(id):
    product=Products.query.filter_by(product_id=id).first()
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for("index"))
    
    
app.run(debug=True)



# @app.route("/testf/")
# def Test_connection():
#     try:
#         # query = Test.query.all()
#         # print(query)  # This will print the results of the query to the console
#         sql_query="select * from test"
#         with db.engine.begin() as conn:
#             response=conn.exec_driver_sql(sql_query).all()
#             print(response)
#         return "Database is connected successfully"
#     except Exception as e:
#         print(f"Error: {e}")  # Print the actual error for troubleshooting
#         return "Database is not connected"

# class Test(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     name=db.Column(db.String(50))