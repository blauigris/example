def plot_metrics(metrics, title="Metrics Over Time"):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 6))
    for key, values in metrics.items():
        plt.plot(values, label=key)
    
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.title(title)
    plt.show()