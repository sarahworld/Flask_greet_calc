from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

# ***/add***   Adds ***a*** and ***b*** and returns result as the body.

# ***/sub***   Same, subtracting ***b*** from ***a***.

# ***/mult***   Same, multiplying ***a*** and ***b***.

# ***/div***   Same, dividing ***a*** by ***b***.

@app.route("/add")
def do_add():
    """
    Add the params a and b
    """
    a = int(request.args.get("a"));
    b = int(request.args.get("b"));
    result = add(a,b)
    return str(result)


@app.route("/sub")
def do_sub():
      """
    Subtract the params b from a
    """
    a = int(request.args.get("a"));
    b = int(request.args.get("b"));
    result = sub(a,b)
    return str(result)

@app.route("/mult")
def do_mult():
      """
    Multiply the params a and b
    """
    a = int(request.args.get("a"));
    b = int(request.args.get("b"));
    result = mult(a,b)
    return str(result)

@app.route("/div")
def do_div():
      """
    Divide the params a from b
    """
    a = int(request.args.get("a"));
    b = int(request.args.get("b"));
    result = div(a,b)
    return str(result)


# /////PART TWO////////////////
operators = {
    "add":add,
    "sub":sub,
    "mult":mult,
    "div":div
}

@app.route("/math/<str:operation>")
def do_operation(operation):
    a = request.args.get("a");
    b = request.args.get("b");

    result = operators[operation](a,b);
    return str(result)
