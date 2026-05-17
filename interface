def moving_average_forecast(values, window, steps):
    data = values.copy()
    forecast = []

    for _ in range(steps):
        avg = sum(data[-window:]) / window
        forecast.append(round(avg, 2))
        data.append(avg)

    return forecast
