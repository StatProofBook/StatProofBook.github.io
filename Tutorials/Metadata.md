---
layout: page
title: Metadata Fields
---


The metadata specification in the header of the [template proof](/Tutorials/Template.html) helps to automatically generate a proof page and makes proof properties machine-readable. It consists of the following six sections.


1\. Default properties that may not be changed:

```yaml
layout: proof
mathjax: true
```


2\. Information about the submitter of the proof:

```yaml
author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2019-09-27 16:40:00
```


<section class="chapter" id="Taxonomy"> </section>
3\. Taxonomy information locating a proof in the [Table of Contents](/Indexes/Table_of_Contents.html):

```yaml
title: "Template for The Book of Statistical Proofs"
chapter: "enter chapter here"
section: "enter section here"
topic: "enter topic here"
theorem: "enter theorem here"
```


4\. Other theorems this proof depends on (with shortcut, if already in the archive):

```yaml
dependencies:
  - theorem: "a theorem this proof depends on (with internal reference)"
    shortcut: "-temp-"
  - theorem: "another theorem this proof requires (without reference)"
    shortcut: 
```


5\. Sources used when writing down this proof (author/year/title are required):

```yaml
sources:
  - authors: "Author(s) of the source of the proof*"
    year: year when published*
    title: "Title of the source of the proof*"
    in: "Title of monography or name of journal**"
    pages: "volume, issue and/or page information** [* required, ** optional]"
    url: "https://optional.url/to-source/"
    doi: "optional.doi/of.source"
```


6\. Metadata that is displayed at the bottom of a proof page:

```yaml
proof_id: "P0"
shortcut: "-temp-"
username: "StatProofBook"
```