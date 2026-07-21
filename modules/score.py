def calculate_resume_score(
    ats_score,
    skill_score,
    metrics,
    sections
):

    breakdown = {}

    # ATS (20)
    breakdown["ATS Compatibility"] = ats_score

    # Skills (40)
    breakdown["Skill Match"] = skill_score

    # ---------------- Content ----------------

    content = 0

    if metrics["Words"] >= 300:
        content += 5
    elif metrics["Words"] >= 200:
        content += 3

    if metrics["Bullet Points"] >= 8:
        content += 5
    elif metrics["Bullet Points"] >= 4:
        content += 3

    if metrics["Email"]:
        content += 2

    if metrics["Phone"]:
        content += 2

    if metrics["LinkedIn"]:
        content += 3

    if metrics["GitHub"]:
        content += 3

    breakdown["Content Quality"] = min(content, 20)

    # ---------------- Structure ----------------

    structure = 0

    for present in sections.values():
        if present:
            structure += round(20 / len(sections))

    breakdown["Resume Structure"] = min(structure, 20)

    # ---------------- Final ----------------

    total = sum(breakdown.values())

    return total, breakdown