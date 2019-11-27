---
layout: page
title: Contribution Guide
permalink: /contribute/
---


Everyone can contribute to **The Book of Statistical Proofs**! Depending on your mathematical knowledge, your computer science skills and the time you are willing to invest, there are five different levels of contributing to the project, with contribution intensity increasing from first to last level.

<br>
### Level 1: suggest a theorem to be proven

*Required: a web browser and access to Google Docs*

1. Go to the [online document for suggesting a theorem](https://docs.google.com/document/d/1J2t0MXsPYckhoN8-Out8qJv7espX-xAQurYcPUXJMV8/edit?usp=sharing).
2. Enter the name of the theorem and, if possible, a URL for more information.

<br>
### Level 2: provide source for existing proof

*Required: a web browser and access to Google Sheets*

1. Go to the [online sheet for providing proof sources](https://docs.google.com/spreadsheets/d/1MIqVvAgcQL72HCPZ9KDaCZXZRVxBhkrEiLX1Dr7p4Kg/edit?usp=sharing).
2. Enter one proof source per row, following the instructions in the sheet.

<br>
### Level 3: send a LaTeX file to the archive

*Required: LaTeX processing software and an e-mail address*

1. Pick a theorem of your choice and write (or retrieve) a LaTeX document proving this theorem.
2. Send this file to [StatProofBook@gmail.com](mailto:StatProofBook@gmail.com) and/or [joram.soch@bccn-berlin.de](mailto:joram.soch@bccn-berlin.de).

<br>
### Level 4: send a Markdown file to the archive

*Required: LaTeX/Markdown processing software and an e-mail address*

1. Pick a theorem of your choice and write a LaTeX document proving this theorem.
2. Download the [Markdown template for "The Book of Statistical Proofs"](https://raw.githubusercontent.com/StatProofBook/StatProofBook.github.io/master/Proofs/-temp-.md)
3. Paste your LaTeX proof into the lower half of that document (starting from line 35).
4. Fill in the proof metadata in the upper half of that document (up until line 33).
5. Send this file to [StatProofBook@gmail.com](mailto:StatProofBook@gmail.com) and/or [joram.soch@bccn-berlin.de](mailto:joram.soch@bccn-berlin.de).

<br>
### Level 5: add a proof to the archive yourself

*Required: GitHub account and LaTeX/Markdown processing software*

1. Login to GitHub and fork the [repository](https://github.com/StatProofBook/StatProofBook.github.io) belonging to this website.
2. In the subfolder "Proofs", duplicate the file "-temp-.md" and rename it to "\[shortcut\].md" where "shortcut" is an abbreviation of your proof.
3. Paste your LaTeX proof into the lower half of this new file (starting from line 35).
4. Fill in the proof metadata in the upper half of that document (up until line 33).
5. (optional:) Edit the file "/Indexes/Table_of_Contents.md" to include a link to "/Proofs/\[shortcut\].md" in the corresponding section.
6. (optional:) Run the Python script "update.py" that rewrites the index pages which are linked to on the homepage.
7. Launch a pull request. Your branch with the new proof will then be merged into the master branch and become live.
8. The proof that you wrote will link to your GitHub profile. Additionally, you can earn money!