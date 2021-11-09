---
layout: page
title: Contribution Guide
permalink: /contribute/
---


Everyone can contribute to **The Book of Statistical Proofs**! Depending on your mathematical knowledge, your computer science skills and the time you are willing to invest, there are three different levels of contributing to the project, with contribution intensity increasing from first to last level.

*Quick Access:* [GitHub Repository](https://github.com/StatProofBook/StatProofBook.github.io) – [Repository Wiki](https://github.com/StatProofBook/StatProofBook.github.io/wiki/Main-Page) – [Proof Template](https://raw.githubusercontent.com/StatProofBook/StatProofBook.github.io/master/P/-temp-.md) – [Definition Template](https://raw.githubusercontent.com/StatProofBook/StatProofBook.github.io/master/D/-temp-.md) – [Template Guidelines](https://github.com/StatProofBook/StatProofBook.github.io/wiki/Template-Files) – [Table of Contents](/I/ToC) – [Wanted Theorems](https://docs.google.com/spreadsheets/d/1MIqVvAgcQL72HCPZ9KDaCZXZRVxBhkrEiLX1Dr7p4Kg/edit?usp=sharing) – [Wanted Definitions](https://docs.google.com/spreadsheets/d/1jH173bODx8C1Hj8xhPNJDs4oLs00GsSbNC9BpwtZsoQ/edit?usp=sharing) – [Proofs without Source](/I/PwS) – [Definitions without Source](/I/DwS) – [Dead Links](https://github.com/StatProofBook/StatProofBookTools/blob/master/report_links/Dead_Links.txt)


<br>
### Level 1: suggest a theorem to be proven

*Required: a web browser and access to Google Documents*

1. Go to the online document for [suggesting a theorem](https://docs.google.com/spreadsheets/d/1MIqVvAgcQL72HCPZ9KDaCZXZRVxBhkrEiLX1Dr7p4Kg/edit?usp=sharing) or [suggesting a definition](https://docs.google.com/spreadsheets/d/1jH173bODx8C1Hj8xhPNJDs4oLs00GsSbNC9BpwtZsoQ/edit?usp=sharing).
2. Enter one proof source per row, following the instructions in the sheet.

<br>
### Level 2: send a formatted file to the archive

*Required: LaTeX processing software and a Google Drive account*

1. Pick a proof or definition of your choice and write it down as a [LaTeX document](https://en.wikipedia.org/wiki/LaTeX).
2. Optionally, embed your submission into the [Markdown templates](https://github.com/StatProofBook/StatProofBook.github.io/wiki/Template-Files) for [proof](https://raw.githubusercontent.com/StatProofBook/StatProofBook.github.io/master/P/-temp-.md) or [definition](https://raw.githubusercontent.com/StatProofBook/StatProofBook.github.io/master/D/-temp-.md).
3. Submit your LaTeX or Markdown file via the [online submission form](https://docs.google.com/forms/d/e/1FAIpQLSdxak_oUsAMws6Xjs7wGNNPdxLwO8Qez0IdZRvLoTuiycibpg/viewform?usp=sf_link).

<br>
### Level 3: add a page to the archive yourself

*Required: Markdown processing software and a GitHub account*

1. Login to GitHub and fork the [repository](https://github.com/StatProofBook/StatProofBook.github.io) belonging to this website.
2. In the subfolder `P` (or `D`), duplicate the file `-temp-.md` and rename it to `[shortcut].md` where `[shortcut]` is [an abbreviation of your proof (or definition)](https://github.com/StatProofBook/StatProofBook.github.io/wiki/Naming-Conventions).
3. Now [rewrite this template](https://github.com/StatProofBook/StatProofBook.github.io/wiki/Template-Files) to become a proof (or definition) of your theorem and [fill in the metadata](https://github.com/StatProofBook/StatProofBook.github.io/wiki/Metadata-Fields) in the header of that document (enclosed by "– – –").
4. Commit your changes and launch a pull request, e.g. using the subject `added "[shortcut]"`.

* Optionally, you can also [update the index pages](https://github.com/StatProofBook/StatProofBook.github.io/wiki/Updating-the-Index-Pages) before committing your changes.
* Your branch with the new submission will be merged into the [master branch](https://github.com/StatProofBook/StatProofBook.github.io) and become live.
* Your proof or definition will then [link to your GitHub profile](/credits/). Additionally, you can [earn money](https://docs.google.com/spreadsheets/d/1h5MO-14GKWsqNL8aZsqGtIqgKGIa-rNIBiO-Bw6_m04/edit?usp=sharing)!