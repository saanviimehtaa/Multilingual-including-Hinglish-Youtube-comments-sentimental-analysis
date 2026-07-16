"""
utils.py
==========================================================
Simple shared data-loading and evaluation helpers so any
notebook can load the project's data and plot results with
one import, e.g.:

    from utils import load_raw_data, load_cleaned_data, plot_confusion_matrix
==========================================================
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_raw_data(path="../data/comments.csv"):
    """Load the raw comments.csv file."""
    return pd.read_csv(path)


def load_cleaned_data(path="../data/cleaned_comments.csv"):
    """Load the cleaned/preprocessed dataset produced by 02_preprocessing.ipynb."""
    return pd.read_csv(path)


def plot_confusion_matrix(cm, classes, title="Confusion Matrix", cmap=plt.cm.Blues, normalize=False):
    """
    Plot a confusion matrix as a heatmap with annotated cell values.

    Parameters
    ----------
    cm : array-like of shape (n_classes, n_classes)
        The confusion matrix, e.g. from sklearn.metrics.confusion_matrix.
    classes : list of str
        Class labels, in the same order used to compute cm.
    title : str
        Plot title.
    cmap : matplotlib colormap
        Colormap for the heatmap.
    normalize : bool
        If True, normalize counts to proportions (row-wise).
    """
    cm = np.array(cm)

    if normalize:
        cm = cm.astype("float") / cm.sum(axis=1, keepdims=True)
        fmt = ".2f"
    else:
        fmt = "d"

    fig, ax = plt.subplots(figsize=(6, 5))
    im = ax.imshow(cm, interpolation="nearest", cmap=cmap)
    ax.set_title(title)
    fig.colorbar(im, ax=ax)

    tick_marks = np.arange(len(classes))
    ax.set_xticks(tick_marks)
    ax.set_xticklabels(classes, rotation=45, ha="right")
    ax.set_yticks(tick_marks)
    ax.set_yticklabels(classes)

    thresh = cm.max() / 2.0
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(
                j, i, format(cm[i, j], fmt),
                ha="center", va="center",
                color="white" if cm[i, j] > thresh else "black"
            )

    ax.set_ylabel("True label")
    ax.set_xlabel("Predicted label")
    fig.tight_layout()
    return fig
