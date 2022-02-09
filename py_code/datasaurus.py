# Wrapper for the online code
import streamlit as st
import pandas as pd
import altair as alt
import time


def get_values(df):
    """Calculates the summary statistics for the given set of points

    Args:
        df (pd.DataFrame): A ``DataFrame`` with ``x`` and ``y`` columns

    Returns:
        list: ``[x-mean, y-mean, x-stdev, y-stdev, correlation]``
    """
    xm = df.x.mean()
    ym = df.y.mean()
    xsd = df.x.std()
    ysd = df.y.std()
    pc = df.corr().x.y

    return [xm, ym, xsd, ysd, pc]


def gen_label(label, value, max_label_length):
    return (
        f'{label: <{max_label_length}}: {value:{"+" if label == "Corr." else ""}0.9f}'
    )


def plot_frame(df, size=300):
    labels = ("X Mean", "Y Mean", "X SD", "Y SD", "Corr.")
    max_label_length = max([len(l) for l in labels])
    values = get_values(df)

    stats_short = [
        gen_label(label, values[i], max_label_length)[:-7]
        for i, label in enumerate(labels)
    ]
    stats_long = [
        gen_label(label, values[i], max_label_length)[:-2]
        for i, label in enumerate(labels)
    ]

    fontSize = 0.1 * size
    labels_9_dec = (
        alt.Chart(alt.Data(values=[1]))
        .mark_text(
            fontSize=fontSize,
            font="monospace",
            baseline="top",
            align="left",
            color="grey",
        )
        .encode(
            x=alt.value(0),
            y=alt.value((size - 5 * fontSize) / 2),
            text=alt.value(stats_long),
        )
        .properties(width=1, height=1)
    )

    labels_2_dec = (
        alt.Chart(alt.Data(values=[1]))
        .mark_text(
            fontSize=fontSize,
            font="monospace",
            baseline="top",
            align="left",
            color="black",
        )
        .encode(
            x=alt.value(0),
            y=alt.value((size - 5 * fontSize) / 2),
            text=alt.value(stats_short),
        )
        .properties(width=1, height=1)
    )
    scatterplot = (
        alt.Chart(df)
        .mark_circle()
        .encode(
            alt.X("x", scale=alt.Scale(domain=(0, 100))),
            alt.Y("y", scale=alt.Scale(domain=(0, 100))),
        )
        .properties(width=size, height=size)
    )
    return scatterplot | labels_9_dec + labels_2_dec


def run(shape_start, shape_end):
    datasaurus_dozen = pd.read_csv(
        "https://raw.githubusercontent.com/jmatejka/same-stats-different-graphs/master/samestats/datasets/generated/DatasaurusDozen.tsv",
        sep="\t",
    )
    dsets = datasaurus_dozen["dataset"].unique()
    n = len(dsets)

    ph0 = st.empty()
    ph1 = st.empty()
    ph2 = st.empty()
    for i in range(101):
        time.sleep(0.01)
        df = datasaurus_dozen[datasaurus_dozen["dataset"] == dsets[i % n]]
        plot = plot_frame(df)
        ph0.altair_chart(plot)
        ph1.write(shape_start + " -> " + shape_end)
        ph2.progress(i)
    ph2.empty()
