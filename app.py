from flask import Flask, request, render_template, jsonify
import math

app = Flask(__name__)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Example: Addition API
@app.route('/add', methods=['POST'])
def add():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    result = num1 + num2
    return jsonify(result=result)

# Example: Factorial API
@app.route('/factorial', methods=['POST'])
def factorial():
    number = int(request.form['number'])
    result = math.factorial(number)
    return jsonify(result=result)
# problem -6
@app.route("/power", methods=["POST"])
def power():
    base = float(request.form['base'])
    exponent = float(request.form['exponent'])
    result = base ** exponent
    return jsonify(result=result)

# - problem -7
@app.route("/floor_division", methods=["POST"])
def floor_division():
    number1 = int(request.form['number1'])
    number2 = int(request.form['number2'])
    result = number1 // number2
    return jsonify(result=result)

# problem - 8
@app.route("/absolute", methods=["POST"])
def absolute():
    number = float(request.form['number'])
    result = abs(number)
    return jsonify(result=result)
# problem - 9
@app.route("/increment", methods=["POST"])
def increment():
    number = int(request.form['number'])
    result = number + 1
    return jsonify(result=result)
# problem -10
@app.route("/decrement", methods=["POST"])
def decrement():
    number = int(request.form['number'])
    result = number - 1
    return jsonify(result=result)
# Problem 12
@app.route("/square_root", methods=["POST"])
def square_root():
    number = float(request.form['number'])
    result = math.sqrt(number)
    return jsonify(result=result)

# Problem 13
@app.route("/cube_root", methods=["POST"])
def cube_root():
    number = float(request.form['number'])
    result = number ** (1/3)
    return jsonify(result=result)

# Problem 14
@app.route("/nth_root", methods=["POST"])
def nth_root():
    number = float(request.form['number'])
    n = float(request.form['n'])
    result = number ** (1/n)
    return jsonify(result=result)

# Problem 15
@app.route("/factorial", methods=["POST"])
def factorial():
    number = int(request.form['number'])
    result = math.factorial(number)
    return jsonify(result=result)

# Problem 16: 
@app.route("/fibonacci", methods=["POST"])
def fibonacci():
    n = int(request.form['n'])
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return jsonify(result=fib_sequence[:n])

# Problem 17
@app.route("/lcm", methods=["POST"])
def lcm():
    number1 = int(request.form['number1'])
    number2 = int(request.form['number2'])
    result = math.lcm(number1, number2)
    return jsonify(result=result)

# Problem 18
@app.route("/gcd", methods=["POST"])
def gcd():
    number1 = int(request.form['number1'])
    number2 = int(request.form['number2'])
    result = math.gcd(number1, number2)
    return jsonify(result=result)

# Problem 19
@app.route("/is_prime", methods=["POST"])
def is_prime():
    number = int(request.form['number'])
    if number < 2:
        return jsonify(result=False)
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return jsonify(result=False)
    return jsonify(result=True)

# Problem 20
@app.route("/prime_generator", methods=["POST"])
def prime_generator():
    n = int(request.form['n'])
    primes = []
    for num in range(2, n+1):
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
    return jsonify(result=primes)

# Problem 21
@app.route("/sum_n_numbers", methods=["POST"])
def sum_n_numbers():
    n = int(request.form['n'])
    result = n * (n + 1) // 2
    return jsonify(result=result)

# Problem 22
@app.route("/sum_of_squares", methods=["POST"])
def sum_of_squares():
    n = int(request.form['n'])
    result = (n * (n + 1) * (2 * n + 1)) // 6
    return jsonify(result=result)


# You can add more routes for each math function
# for example, multiplication, square roots, etc.

if __name__ == '__main__':
    app.run(debug=True)
