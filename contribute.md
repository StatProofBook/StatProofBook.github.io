---
layout: page
title: Contribution Guide
permalink: /contribute/
---


Everyone can contribute to **The Book of Statistical Proofs**! Depending on your mathematical knowledge, your computer science skills and the time you are willing to invest, there are three different levels of contributing to the project, with contribution intensity increasing from first to last level.

[GitHub Repository](https://github.com/StatProofBook/StatProofBook.github.io) – [Proof Template](https://raw.githubusercontent.com/StatProofBook/StatProofBook.github.io/master/Proofs/-temp-.md) – [Table of Contents](/Indexes/Table_of_Contents.md) – [Old ToC](https://github.com/JoramSoch/TBSP/blob/master/Contents.pdf) – [Wanted Theorems](https://docs.google.com/spreadsheets/d/1MIqVvAgcQL72HCPZ9KDaCZXZRVxBhkrEiLX1Dr7p4Kg/edit?usp=sharing) – [Submission Form](https://docs.google.com/forms/d/e/1FAIpQLSdxak_oUsAMws6Xjs7wGNNPdxLwO8Qez0IdZRvLoTuiycibpg/viewform?usp=sf_link)


<br>
### Level 1: suggest a theorem to be proven

*Required: a web browser and access to Google Documents*

1. Go to the [online document for suggesting a theorem](https://docs.google.com/spreadsheets/d/1MIqVvAgcQL72HCPZ9KDaCZXZRVxBhkrEiLX1Dr7p4Kg/edit?usp=sharing).
2. Enter one proof source per row, following the instructions in the sheet.

<br>
### Level 2: send a formatted file to the archive

*Required: LaTeX processing software and a Google Drive account*

1. Pick a theorem of your choice and write (or retrieve) a [LaTeX document](https://en.wikipedia.org/wiki/LaTeX) proving this theorem.
2. Optionally, [embed your proof](/Tutorials/Template.md) into the [Markdown template](https://raw.githubusercontent.com/StatProofBook/StatProofBook.github.io/master/Proofs/-temp-.md) for "The Book of Statistical Proofs".
3. Submit your LaTeX or Markdown file via the [online submission form](https://docs.google.com/forms/d/e/1FAIpQLSdxak_oUsAMws6Xjs7wGNNPdxLwO8Qez0IdZRvLoTuiycibpg/viewform?usp=sf_link).

<br>
### Level 3: add a proof to the archive yourself

*Required: Markdown processing software and a GitHub account*

1. Login to GitHub and fork the [repository](https://github.com/StatProofBook/StatProofBook.github.io) belonging to this website.
2. In the subfolder `Proofs`, duplicate the file `-temp-.md` and rename it to `[shortcut].md` where `[shortcut]` is [an abbreviation of your proof](/Tutorials/Naming.md).
3. Now [rewrite this template](/Tutorials/Template.md) to become the proof of your theorem and [fill in the metadata](/Tutorials/Metadata.md) in the header of that document (enclosed by "– – –").
4. Optionally, edit the file `/Indexes/Table_of_Contents.md` to include a link to `/Proofs/[shortcut].html` in the corresponding section.
5. Optionally, run the Python script `update.py` in the main folder to rewrite the index pages which are linked to [on the homepage](/).
6. Commit your changes and launch a pull request using the subject `added proof "[shortcut]"`.

* Your branch with the new proof will then be merged into the [master branch](https://github.com/StatProofBook/StatProofBook.github.io) and become live.
* The proof that you wrote will [link to your GitHub profile](/credits/). Additionally, you can [earn money](/credits/)!