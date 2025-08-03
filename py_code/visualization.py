# Wrapper for the online code
import streamlit as st
import pandas as pd
import altair as alt
#import time
import glob

# Colors
yellow = "#fde000"
red = "#e30721"
black = "#14100d"
white = "#fdfefd"

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
            color="#fff9",
        )
        .encode(
            x=alt.value(0),
            y=alt.value((size - 5 * fontSize) / 2),
            text=alt.value(stats_long),
        )
        .properties(width=size, height=size)
    )

    labels_2_dec = (
        alt.Chart(alt.Data(values=[1]))
        .mark_text(
            fontSize=fontSize,
            font="monospace",
            baseline="top",
            align="left",
            color="white",
        )
        .encode(
            x=alt.value(0),
            y=alt.value((size - 5 * fontSize) / 2),
            text=alt.value(stats_short),
        )
        .properties(width=size, height=size)
    )
    scatterplot = (
        alt.Chart(df)
        .mark_circle(color="white", opacity=1)
        .encode(
            alt.X("x", scale=alt.Scale(domain=(0, 100))),
            alt.Y("y", scale=alt.Scale(domain=(0, 100))),
        )
        .properties(width=size, height=size)
    )

    chart = (
        (scatterplot | labels_9_dec + labels_2_dec)
        .properties(
            background=black,
            padding={"left": 20, "top": 20, "right": 20, "bottom": 20},
        )
        .configure_axis(
            gridColor=white,
            domainColor=white,
            labelColor=white,
            tickColor=white,
            titleColor=white,
        )
        .configure_view(strokeOpacity=0)
    )

    return chart

def scatterplot_from_df(df, size=300, themed=True):
    scatterplot = (
        alt.Chart(df)
        .mark_circle(color="white", opacity=1)
        .encode(
            alt.X("x", scale=alt.Scale(domain=(0, 100))),
            alt.Y("y", scale=alt.Scale(domain=(0, 100))),
        )
        .properties(width=size, height=size)
    )
    if themed:
        return themed_plot(scatterplot)
    else:
        return scatterplot

def themed_plot(my_plot):
    chart = (
        (my_plot)
        .properties(
            background=black,
            padding={"left": 20, "top": 20, "right": 20, "bottom": 20},
        )
        .configure_axis(
            gridColor=white,
            gridOpacity=0.5,
            domainColor=white,
            labelColor=white,
            tickColor=white,
            titleColor=white,
        )
        .configure_view(strokeOpacity=0)
    )
    return chart

def chart_from_lines(lines):
    # Draw current lines
    plot = alt.LayerChart() # Starting value, empty chart
    for line in lines:
        df_lines = pd.DataFrame(data=line, columns=["x", "y"])
        plot = plot + alt.Chart(df_lines).mark_line(point=True, strokeWidth=5, color="#FFFFFF").encode(
            alt.X("x", scale=alt.Scale(domain=(0, 100))),
            alt.Y("y", scale=alt.Scale(domain=(0, 100))),
        )
    return themed_plot(plot).configure_point(size=200)

def animate_from_path(shape_start, shape_end):
    # Placeholders to be filled in later
    progress_bar_placeholder = st.empty()
    altair_placeholder = st.empty()
    # Iterate
    num_frames = 100
    for i in range(num_frames):
        #time.sleep(0.01)
        filename = f"data/precomputed_transitions/{shape_start}_to_{shape_end}/frame-{i:05}.csv"
        df = pd.read_csv(filename)
        animate_from_df(
            df,
            progress_bar_placeholder,
            altair_placeholder,
            progress=i,
            num_frames=num_frames,
        )
    progress_bar_placeholder.empty()


def animate_from_df(
    df, progress_bar_placeholder, altair_placeholder, progress=-1, num_frames=100
):
    if progress == -1 or progress == num_frames - 1:
        progress_bar_placeholder.empty()
    else:
        plot = plot_frame(df)
        altair_placeholder.altair_chart(plot)
        progress_bar_placeholder.progress(progress)


def plot_datasaurus_sets(size=200):
    vplots = []
    filename = "data/datasaurus_datasets/DatasaurusDozen-wide.tsv"
    for i in range(3):
        hplots = []
        for j in range(4):
            n = i * 4 + j
            df = pd.read_csv(filename, skiprows=1, usecols=(2*n, 2*n+1), sep="\t")
            df.columns = ["x", "y"]
            #st.write(get_values(df))
            hplots.append(scatterplot_from_df(df, size=size, themed=False))
        vplots.append(alt.hconcat(*hplots))
    # Plot them all
    st.altair_chart(alt.vconcat(*vplots), use_container_width=False)
    return
