def reconstruct_toc(markdown_content):
    """
    Backtransforms a simplified markdown Table of Contents (with unnumbered sections/subsections)
    into the original I/ToC.md format, using internal counters for numbering.

    Args:
        markdown_content (str): The content of the simplified structure.md file.

    Returns:
        str: The reconstructed I/ToC.md content.
    """
    final_output_lines = []

    # Helper to convert integer to Roman numeral
    def to_roman(num):
        romans = {
            1: 'I', 2: 'II', 3: 'III', 4: 'IV',
            5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
            50: 'L', 90: 'XC', 100: 'C', 400: 'CD',
            500: 'D', 900: 'CM', 1000: 'M'
        }
        result = ""
        # Iterate in descending order of values to build the Roman numeral
        for value, symbol in sorted(romans.items(), reverse=True):
            while num >= value:
                result += symbol
                num -= value
        return result

    # Initial fixed lines matching I/ToC.md template
    final_output_lines.extend([
        "---",
        "layout: page",
        "title: \"Table of Contents\"",
        "---",
        "", # Blank line
        "", # Blank line
        "**[Proofs](/P/-temp-)** are printed in **bold** – *[Definitions](/D/-temp-)* are set in *italics* <br>",
        "**Proofs**: [by Number](/I/PbN), [by Topic](/I/PbT) – *Definitions*:  [by Number](/I/DbN), [by Topic](/D/DbT) <br>",
        "<u>Specials:</u> [General Theorems](/S/ChI), [Probability Distributions](/S/ChII), [Statistical Models](/S/ChIII), [Model Selection Criteria](/S/ChIV) <br>",
        "", # First <br> before Chapter I h3
        "", # Second <br> before Chapter I h3
    ])

    chapter_index = 0
    current_section_num = 0
    current_subsection_num = 0
    current_subsub_num = 0

    lines = markdown_content.strip().splitlines()

    for i, line_str in enumerate(lines):
        line = line_str.strip()

        if line.startswith("# Chapter "):
            if chapter_index > 0:
                final_output_lines.extend(
                    [""]*2
                )
            final_output_lines.append("<br>") # Add <br> before subsequent chapters

            chapter_index += 1
            roman_chapter = to_roman(chapter_index)
            chapter_title = line[len("# Chapter ") + line.find(': ') - len("Chapter ")-1 :].strip() # Extracts "General Theorems" etc.
            final_output_lines.append(f'<h3 id="{chapter_title}">Chapter {roman_chapter}: {chapter_title}</h3>')
            final_output_lines.append("") # Always a blank line after an h3

            # Reset counters for a new chapter
            current_section_num = 0
            current_subsection_num = 0
            current_subsub_num = 0

        elif line.startswith("## "):
            # Reset sub-subsection counter when a new section starts
            current_subsection_num = 0
            current_subsub_num = 0

            current_section_num += 1
            section_title = line[len("## "):].strip()
            final_output_lines.append("   ") # Indented blank line after section <p> tag, matching original
            final_output_lines.append(f'{current_section_num}. <p id="{section_title}">{section_title}</p>')

        elif line.startswith("### "):
            # Reset sub-subsection counter when a new subsection starts
            current_subsub_num = 0

            current_subsection_num += 1
            subsection_title = line[len("### "):].strip() # Extracts "Random experiments"
            # In the original, the p id is the title, and the text below is also the title
            final_output_lines.append("   ")
            final_output_lines.append(f'   <p id="{subsection_title}"></p>')
            final_output_lines.append(f'   {current_section_num}.{current_subsection_num}. {subsection_title} <br>')

        elif line.startswith("- "):
            current_subsub_num += 1
            item_content = line[len("- "):] # Get content after "- "
            final_output_lines.append(f'   &emsp;&ensp; {current_section_num}.{current_subsection_num}.{current_subsub_num}. {item_content} <br>')

    return "\n".join(final_output_lines)

if __name__ == '__main__':

    with open('./book_content.md', 'r') as f:
        md = f.read()

    with open("./I/ToC.md", 'w') as f:
        f.write(
            reconstruct_toc(md)
        )