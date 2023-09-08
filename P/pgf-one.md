---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-10-11 08:17:00

title: "Value of the probability-generating function for argument one"
chapter: "General Theorems"
section: "Probability theory"
topic: "Other probability functions"
theorem: "Probability-generating function of one"

sources:
  - authors: "ProofWiki"
    year: 2022
    title: "Probability Generating Function of One"
    in: "ProofWiki"
    pages: "retrieved on 2022-10-11"
    url: "https://proofwiki.org/wiki/Probability_Generating_Function_of_One"

proof_id: "P362"
shortcut: "pgf-one"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) with [probability-generating function](/D/pgf) $G_X(z)$ and set of possible values $\mathcal{X}$. Then, the value of the probability-generating function at one is equal to one:

$$ \label{eq:pgf-one}
G_X(1) = 1 \; .
$$


**Proof:** The [probability-generating function](/D/pgf) of $X$ is defined as

$$ \label{eq:pgf}
G_X(z) = \sum_{x=0}^{\infty} f_X(x) \, z^x
$$

where $f_X(x)$ is the [probability mass function](/D/pmf) of $X$. Setting $z = 1$, we obtain:

$$ \label{eq:pgf-zero-s1}
\begin{split}
G_X(1) &= \sum_{x=0}^{\infty} f_X(x) \cdot 1^x \\
&= \sum_{x=0}^{\infty} f_X(x) \cdot 1 \\
&= \sum_{x=0}^{\infty} f_X(x) \; .
\end{split}
$$

Because the [probability mass function](/D/pmf) sums up to one, this becomes:

$$ \label{eq:pgf-zero-s2}
\begin{split}
G_X(1) &= \sum_{x \in \mathcal{X}} f_X(x) \\
&= 1 \; .
\end{split}
$$