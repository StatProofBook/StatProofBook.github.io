---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-08-19 08:09:00

title: "Linear transformation theorem for the moment-generating function"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability functions"
theorem: "Moment-generating function of linear transformation"

sources:
  - authors: "ProofWiki"
    year: 2020
    title: "Moment Generating Function of Linear Transformation of Random Variable"
    in: "ProofWiki"
    pages: "retrieved on 2020-08-19"
    url: "https://proofwiki.org/wiki/Moment_Generating_Function_of_Linear_Transformation_of_Random_Variable"

proof_id: "P154"
shortcut: "mgf-ltt"
username: "JoramSoch"
---


**Theorem:** Let $X$ be an $n \times 1$ [random vector](/D/rvec) with the [moment-generating function](/D/mgf) $M_X(t)$. Then, the moment-generating function of the linear transformation $Y = A X + b$ is given by

$$ \label{eq:mgf-ltt}
M_Y(t) = \exp \left[ t^\mathrm{T} b \right] \cdot M_X(At)
$$

where $A$ is an $m \times n$ matrix and $b$ is an $m \times 1$ vector.


**Proof:** The [moment-generating function of a random vector](/D/mgf) $X$ is

$$ \label{eq:mfg-vect}
M_X(t) = \mathrm{E} \left( \exp \left[ t^\mathrm{T} X \right] \right)
$$

and therefore the moment-generating function of the [random vector](/D/rvec) $Y$ is given by

$$ \label{eq:mgf-ltt-qed}
\begin{split}
M_Y(t) &= \mathrm{E} \left( \exp \left[ t^\mathrm{T} (AX + b) \right] \right) \\
&= \mathrm{E} \left( \exp \left[ t^\mathrm{T} A X \right] \cdot \exp \left[ t^\mathrm{T} b \right] \right) \\
&= \exp \left[ t^\mathrm{T} b \right] \cdot \mathrm{E} \left( \exp \left[ (A t)^\mathrm{T} X \right] \right) \\
&= \exp \left[ t^\mathrm{T} b \right] \cdot M_X(At) \; .
\end{split}
$$