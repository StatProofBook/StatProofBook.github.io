---
layout: page
title: Template File
---


The easiest way to write a proof for "The Book of Statistical Proofs" is to duplicate the [template file](https://raw.githubusercontent.com/StatProofBook/StatProofBook.github.io/master/Proofs/-temp-.md), go through and edit it from top to bottom. Essentially, this proof template consists of two sections.


The first section (currently up to line 34) consists of **proof metadata** and is written in [YAML](https://en.wikipedia.org/wiki/YAML). When you edit this section, fill in as many fields of the [metadata specification](/Tutorials/Metadata.md) as you can, because this will ease cross-referencing in the archive and make proof properties machine-readable.

```yaml
---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2019-09-27 16:40:00

title: "Template for The Book of Statistical Proofs"
chapter: "enter chapter here"
section: "enter section here"
topic: "enter topic here"
theorem: "enter theorem here"

dependencies:
  - theorem: "a theorem this proof depends on (with internal reference)"
    shortcut: "-temp-"
  - theorem: "another theorem this proof requires (without reference)"
    shortcut: 

sources:
  - authors: "Author(s) of the source of the proof*"
    year: year when published*
    title: "Title of the source of the proof*"
    in: "Title of monography or name of journal**"
    pages: "volume, issue and/or page information** [* required, ** optional]"
    url: "https://optional.url/to-source/"
    doi: "optional.doi/of.source"

proof_id: "P0"
shortcut: "-temp-"
username: "StatProofBook"
---
```


The second section (currently starting from line 35) consists of the **proof itself** and is written in [Markdown](https://en.wikipedia.org/wiki/Markdown) and [LaTeX](https://en.wikipedia.org/wiki/LaTeX). When you edit this section, be sure to use `$...$` for in-line math, `$$...$$` for stand-alone equations and give a label to each equation.

```tex
**Theorem:** Statement of the theorem.

$$ \label{eq:Theorem}
\textbf{an equation belonging to the theorem}
$$

This holds under some conditions.


**Proof:** Statement of the proof.

$$ \label{eq:Proof}
\textbf{an equation belonging to the proof}
$$

This completes the proof of \eqref{eq:Theorem}.
```