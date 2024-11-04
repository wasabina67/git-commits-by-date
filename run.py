import sys

import matplotlib.pyplot as plt
import pandas as pd  # type: ignore


def main(style):
    df = pd.read_csv("daily_commits.csv", names=["num", "date"])
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace=True)

    if style == "plot":
        plt.plot(df.index, df["num"], color="blue")
    elif style == "bar":
        plt.bar(df.index, df["num"], color="blue")
    else:
        raise Exception("Invalid style provided. Use 'plot' or 'bar'.")

    plt.title("Git Commits by Date")
    plt.xlabel("Date", fontsize=8)
    plt.ylabel("Commits", fontsize=8)

    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(f"images/{style}.png")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        style = sys.argv[1]
        if style in ["plot", "bar"]:
            main(style)
