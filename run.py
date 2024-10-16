import matplotlib.pyplot as plt
import pandas as pd  # type: ignore


def main():
    df = pd.read_csv("daily_commits.csv", names=["num", "date"])
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace=True)

    plt.plot(df.index, df["num"])
    plt.title("Git Commits by Date")
    fontsize_dict = {"fontsize": 8}
    plt.xlabel("Date", fontsize_dict)
    plt.ylabel("Commits", fontsize_dict)

    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("graph.png")


if __name__ == "__main__":
    main()
