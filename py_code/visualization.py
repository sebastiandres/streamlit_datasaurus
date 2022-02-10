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


def animate_from_path(shape_start, shape_end):
    # Placeholders to be filled in later
    progress_bar_placeholder = st.empty()
    altair_placeholder = st.empty()
    # Iterate
    num_frames = 100
    for i in range(num_frames):
        time.sleep(0.01)
        filename = f"data/{shape_start}->{shape_end}/frame-{i:05}.csv"
        df = pd.read_csv(filename)
        animate_from_df(df, progress_bar_placeholder, altair_placeholder, progress=i, num_frames=num_frames)
    progress_bar_placeholder.empty()


def animate_from_df(df, progress_bar_placeholder, altair_placeholder, 
                    progress=-1, num_frames=100):
    if progress==-1 or progress==num_frames-1:
        progress_bar_placeholder.empty()
    else:
        plot = plot_frame(df)
        altair_placeholder.altair_chart(plot)
        progress_bar_placeholder.progress(progress)


