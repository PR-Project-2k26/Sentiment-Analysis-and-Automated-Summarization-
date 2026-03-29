def save_summary(summary, filename="summary.txt"):
    with open(filename, "w") as f:
        f.write(summary)
