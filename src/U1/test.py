import matplotlib.pyplot as plt

colors = ["g", "y", "c", "m", "b", "r", "k"]


def visualize_data(data, centroids=None, labels=None, figsize=(5, 4)):
    plt.figure(figsize=figsize)
    if labels is not None:
        color_data = [colors[x] for x in labels]
        if centroids is not None:
            color_centroid = colors[: len(centroids)]
    else:
        color_data = color_centroid = "C0"
    # plot the data
    plt.scatter([x[0] for x in data], [x[1] for x in data], c=color_data, s=20)
    # plot the centroids if they are given
    if centroids is not None:
        plt.scatter(
            [x[0] for x in centroids],
            [x[1] for x in centroids],
            c=color_centroid,
            marker="X",
            s=80,
            linewidths=1,
            edgecolors="k",
        )

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
