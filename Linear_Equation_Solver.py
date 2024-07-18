from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    # Get coefficients from form input
    try:
        a11 = float(request.form['a11'])
        a12 = float(request.form['a12'])
        a13 = float(request.form['a13'])
        a21 = float(request.form['a21'])
        a22 = float(request.form['a22'])
        a23 = float(request.form['a23'])
        a31 = float(request.form['a31'])
        a32 = float(request.form['a32'])
        a33 = float(request.form['a33'])
        b1 = float(request.form['b1'])
        b2 = float(request.form['b2'])
        b3 = float(request.form['b3'])
    except ValueError:
        return "Invalid input. Please enter numerical values."

    # Coefficient matrix
    A = np.array([[a11, a12, a13],
                  [a21, a22, a23],
                  [a31, a32, a33]])

    # Right-hand side vector
    B = np.array([b1, b2, b3])

    try:
        # Gaussian Elimination Method
        A_aug = np.column_stack((A, B.astype(float)))  # Augmented matrix

        n = A_aug.shape[0]

        # Forward elimination
        for i in range(n):
            # Divide the current row by the diagonal element to make it 1
            divisor = A_aug[i, i]
            A_aug[i] /= divisor
            # Eliminate below the diagonal
            for j in range(i + 1, n):
                multiplier = A_aug[j, i]
                A_aug[j] -= multiplier * A_aug[i]

        # Backward substitution
        sol = np.zeros(n)
        for i in range(n - 1, -1, -1):
            sol[i] = A_aug[i, -1] - np.dot(A_aug[i, :-1], sol)

        x, y, z = sol

        return render_template('result.html', x=x, y=y, z=z)

    except np.linalg.LinAlgError:
        return "Matrix is singular. Unable to solve."

if __name__ == '__main__':
    app.run(debug=True)
