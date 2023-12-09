from sympy import symbols, diff, solve, I

def find_extrema(f, x):
  """
  This function finds the minimum or maximum value of a function using calculus methods.

  Args:
    f: The function to be analyzed.
    x: The symbolic variable representing the independent variable.

  Returns:
    A dictionary containing the following information:
      - extrema: A list of tuples (x, y) representing the extremum points.
      - type: A string indicating the type of extremum (minimum or maximum).
  """

  # Find the derivative of the function.
  df = diff(f, x)

  # Find the critical points by setting the derivative equal to zero.
  critical_points = solve(df, x)

  # Check if the function is defined at the critical points and its boundaries.
  defined_points = [point for point in critical_points if abs(f.subs(x, point)).is_finite()]

  # Analyze the second derivative at each point to determine the type of extremum.
  extrema = []
  for point in defined_points:
    d2f = diff(df, x)
    second_derivative = d2f.subs(x, point)
    if second_derivative > 0:
      # Minimum
      extrema.append((point, f.subs(x, point)))
      type = "minimum"
    elif second_derivative < 0:
      # Maximum
      extrema.append((point, f.subs(x, point)))
      type = "maximum"
    else:
      # Inconclusive
      pass

  return {"extrema": extrema, "type": type}

# Example usage
x = symbols("x")
f = x**3 - 3*x**2 + 4

extrema_data = find_extrema(f, x)

print("Extrema points:", extrema_data["extrema"])
print("Type of extremum:", extrema_data["type"])
