# Linear Equation Solver

## Description
This project implements a web application using Flask and JavaScript to solve a system of linear equations using the Gaussian Elimination method. The solution is displayed step-by-step in a matrix format.

## Installation
1. Clone the repository:
````
git clone https://github.com/NelushGayashan/Linear_Equation_Solver.git
cd Linear_Equation_Solver
````

2. Install dependencies:
````
pip install flask
````


## Usage
1. Run the Flask application:
````
python Linear_Equation_Solver.py
````

This will start a development server at `http://127.0.0.1:5000/`.

2. Open your web browser and go to `http://127.0.0.1:5000/` to access the application.

3. Enter the coefficients of the linear equations and submit the form to solve.

## Technologies Used
- Flask: Python web framework for backend.
- HTML/CSS/JavaScript: Frontend interface and interaction.
- Numpy: Python library for numerical operations.

## Features
- Solves a system of linear equations using Gaussian Elimination method.
- Displays step-by-step solution in a matrix format on the web interface.

## Example
Given system of equations:

76x - 25y - 50z = 10
-25x + 56y - z = 0
-50x - y + 81z = 0


The solution (x, y, z) is displayed as:

x = 0.2992
y = 0.1369
z = 0.1864



## License
This project is licensed under the MIT License - see the LICENSE file for details.
