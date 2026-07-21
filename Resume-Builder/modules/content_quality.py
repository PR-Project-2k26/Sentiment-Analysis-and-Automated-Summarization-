import re
from collections import Counter
from modules.ai_content import evaluate_ai_content

ACTION_VERBS = {
    "developed", "built", "implemented", "designed", "created",
    "optimized", "managed", "engineered", "led", "improved",
    "deployed", "automated", "integrated", "analyzed", "maintained"
}


def evaluate_content_quality(resume_text, metrics):
    """
    Evaluates different aspects of resume content.
    Every metric is scored out of 10.
    """

    report = {}

    text = resume_text.lower()

    # ---------------- Grammar (AI) ----------------

    try:
        ai_report = evaluate_ai_content(resume_text)
        report["Grammar"] = ai_report["grammar"]["score"]
    except Exception:
        report["Grammar"] = 8

    # ---------------- Bullet Points ----------------

    bullets = metrics["Bullet Points"]

    if bullets >= 10:
        report["Bullet Points"] = 10
    elif bullets >= 7:
        report["Bullet Points"] = 8
    elif bullets >= 4:
        report["Bullet Points"] = 6
    elif bullets >= 2:
        report["Bullet Points"] = 4
    else:
        report["Bullet Points"] = 2

    # ---------------- Resume Length ----------------

    words = metrics["Words"]

    if 300 <= words <= 700:
        report["Resume Length"] = 10
    elif 250 <= words <= 800:
        report["Resume Length"] = 8
    elif 200 <= words <= 900:
        report["Resume Length"] = 6
    else:
        report["Resume Length"] = 4

    # ---------------- Action Verbs ----------------

    count = 0

    for verb in ACTION_VERBS:
        count += len(re.findall(r"\b" + re.escape(verb) + r"\b", text))

    if count >= 12:
        report["Action Verbs"] = 10
    elif count >= 8:
        report["Action Verbs"] = 8
    elif count >= 5:
        report["Action Verbs"] = 6
    elif count >= 2:
        report["Action Verbs"] = 4
    else:
        report["Action Verbs"] = 2

    # ---------------- Date Consistency ----------------

    patterns = [
        r"\b(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s+\d{4}\b",
        r"\b\d{2}/\d{4}\b",
        r"\b\d{4}\b"
    ]

    date_matches = 0

    for pattern in patterns:
        date_matches += len(re.findall(pattern, text))

    if date_matches >= 6:
        report["Date Consistency"] = 10
    elif date_matches >= 4:
        report["Date Consistency"] = 8
    elif date_matches >= 2:
        report["Date Consistency"] = 6
    else:
        report["Date Consistency"] = 3

    # ---------------- Numbers & Impact ----------------

    numbers = re.findall(r"\d+%?|\d+\+", resume_text)

    if len(numbers) >= 10:
        report["Numbers & Impact"] = 10
    elif len(numbers) >= 7:
        report["Numbers & Impact"] = 8
    elif len(numbers) >= 5:
        report["Numbers & Impact"] = 6
    elif len(numbers) >= 3:
        report["Numbers & Impact"] = 4
    else:
        report["Numbers & Impact"] = 2

    # ---------------- Professional Writing ----------------

    informal = [
        "i ",
        "my ",
        "me ",
        "etc",
        "stuff",
        "things"
    ]

    informal_count = 0

    for word in informal:
        informal_count += text.count(word)

    if informal_count == 0:
        report["Professional Writing"] = 10
    elif informal_count <= 2:
        report["Professional Writing"] = 8
    elif informal_count <= 4:
        report["Professional Writing"] = 6
    else:
        report["Professional Writing"] = 3

    # ---------------- Contact Information ----------------

    contact = 0

    if metrics["Email"]:
        contact += 3

    if metrics["Phone"]:
        contact += 3

    if metrics["LinkedIn"]:
        contact += 2

    if metrics["GitHub"]:
        contact += 2

    report["Contact Information"] = contact

    # ---------------- Readability ----------------

    avg_words = metrics["Words"] / max(metrics["Lines"], 1)

    if avg_words <= 12:
        report["Readability"] = 10
    elif avg_words <= 18:
        report["Readability"] = 8
    elif avg_words <= 25:
        report["Readability"] = 6
    else:
        report["Readability"] = 4

    # ---------------- Formatting ----------------

    formatting = 10

    if metrics["Bullet Points"] == 0:
        formatting -= 4

    if not metrics["LinkedIn"]:
        formatting -= 1

    if not metrics["GitHub"]:
        formatting -= 1

    report["Formatting"] = max(formatting, 0)

    # ---------------- Overall ----------------

    report["Overall"] = round(
        sum(report.values()) / len(report),
        1
    )

    return report