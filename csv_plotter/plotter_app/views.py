import pandas as pd
import matplotlib.pyplot as plt
from django.shortcuts import render
from io import BytesIO
from io import StringIO
import base64


def csv_plotter(request):
    if request.method == "POST":
        
        plot_data = request.POST["plot_data"]
        print(plot_data)
        csv_file = request.FILES['csv_file']
        file_data = csv_file.read().decode("utf-8")
        io_string = StringIO(file_data)
        data = pd.read_csv(io_string)
        print(type(csv_file))

        # Plot the data
        plt.plot(data.iloc[:, 0], data.iloc[:, 2], label="Column 1")
        plt.xlabel('x(m)')
        buffer = BytesIO()
        plt.savefig(buffer, format="png")
        plt.clf()
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.read()).decode("utf-8")
        image_src = f"data:image/png;base64,{image_base64}"
        # plt.show()
        return render(request, "plotter_app/index.html", {"image_src": image_src})
    return render(request, "plotter_app/index.html")