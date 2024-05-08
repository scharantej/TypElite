
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for
import time

# Create a Flask application
app = Flask(__name__)

# Set session variables to store test results
app.secret_key = 'abc'

# Define the route for the home page
@app.route('/')
def index():
    # Render the index.html page
    return render_template('index.html')

# Define the route to start the pretyping test
@app.route('/start-test', methods=['POST'])
def start_test():
    # Get the initial typing speed and accuracy
    initial_speed = request.form['initial-speed']
    initial_accuracy = request.form['initial-accuracy']

    # Store the initial values in session variables
    session['initial_speed'] = initial_speed
    session['initial_accuracy'] = initial_accuracy

    # Start the timer
    session['start_time'] = time.time()

    # Redirect to the test page
    return redirect(url_for('test'))

# Define the route for the pretyping test
@app.route('/test')
def test():
    # Render the test.html page
    return render_template('test.html')

# Define the route to end the pretyping test
@app.route('/end-test', methods=['POST'])
def end_test():
    # Stop the timer
    end_time = time.time()

    # Calculate the final typing speed and accuracy
    final_speed = request.form['final-speed']
    final_accuracy = request.form['final-accuracy']

    # Calculate the improvement in typing speed and accuracy
    speed_improvement = final_speed - session['initial_speed']
    accuracy_improvement = final_accuracy - session['initial_accuracy']

    # Store the final values in session variables
    session['final_speed'] = final_speed
    session['final_accuracy'] = final_accuracy

    # Redirect to the results page
    return redirect(url_for('results'))

# Define the route to display the results
@app.route('/results')
def results():
    # Get the test results from session variables
    initial_speed = session['initial_speed']
    initial_accuracy = session['initial_accuracy']
    final_speed = session['final_speed']
    final_accuracy = session['final_accuracy']

    # Render the results.html page
    return render_template('results.html', initial_speed=initial_speed, initial_accuracy=initial_accuracy, final_speed=final_speed, final_accuracy=final_accuracy)

# Run the Flask application
if __name__ == '__main__':
    app.run()
