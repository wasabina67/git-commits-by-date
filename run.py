import matplotlib.pyplot as plt
import pandas as pd  # type: ignore


def main():
    df = pd.read_csv("daily_commits.csv", names=["num", "date"])
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace=True)

    plt.plot(df.index, df["num"])
    # plt.bar(df.index, df["num"], color="skyblue")

    plt.title("Git Commits by Date")
    plt.xlabel("Date", fontsize=8)
    plt.ylabel("Commits", fontsize=8)

    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("graph.png")


if __name__ == "__main__":
    main()
