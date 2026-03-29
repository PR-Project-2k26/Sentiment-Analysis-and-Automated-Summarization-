from utils import summarize_text

def read_input(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_output(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    input_file = "Text-Summarizer/input/text.txt"
    output_file = "Text-Summarizer/output/summary.txt"

    text = read_input(input_file)
    summary = summarize_text(text)

    write_output(output_file, summary)

    print("✅ Summary generated!")