import sys
from utils import summarize_text


def read_input(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_output(path, result):
    with open(path, "w", encoding="utf-8") as f:
        f.write("SUMMARY:\n" + result["summary"] + "\n\n")
        f.write("EMOTION: " + result["emotion"] + "\n")
        f.write("READABILITY: " + result["readability"] + "\n\n")
        f.write("KEY TOPICS:\n" + "\n".join(f"- {t}" for t in result["topics"]) + "\n\n")
        f.write("KEYWORDS:\n" + ", ".join(result["keywords"]) + "\n\n")
        f.write(f"SENTIMENT (VADER): {result['sentiment']}\n")
        f.write(f"STATS: {result['stats']}\n")


if __name__ == "__main__":
    input_file = "input/text.txt"
    output_file = "output/summary.txt"
    length = sys.argv[1] if len(sys.argv) > 1 else "Medium"  # Short | Medium | Long

    text = read_input(input_file)
    result = summarize_text(text, length=length)

    write_output(output_file, result)

    print("✅ Summary generated!")
    print(f"Compression: {result['stats']['compression_pct']}% | Latency: {result['latency_sec']}s")
