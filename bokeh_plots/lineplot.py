import random
from bokeh.plotting import figure, output_file, show

if __name__ == "__main__":
    fig = figure(title = "Lineplot with random numbers")
    x_vals = range(10)
    y_vals = [random.randint(i, 100) for i in x_vals]
    fig.line(x_vals, y_vals, line_width=3, color="red")
    output_file('lineplot.html')
    show(fig)
