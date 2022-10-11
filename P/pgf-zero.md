---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-10-11 08:06:00

title: "Value of the probability-generating function for argument zero"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability functions"
theorem: "Probability-generating function of zero"

sources:
  - authors: "ProofWiki"
    year: 2022
    title: "Probability Generating Function of Zero"
    in: "ProofWiki"
    pages: "retrieved on 2022-10-11"
    url: "https://proofwiki.org/wiki/Probability_Generating_Function_of_Zero"

proof_id: "P361"
shortcut: "pgf-zero"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) with [probability-generating function](/D/pgf) $G_X(z)$ and [probability mass function](/D/pmf) $f_X(x)$. Then, the value of the probability-generating function at zero is equal to the value of the probability mass function at zero:

$$ \label{eq:pgf-zero}
G_X(0) = f_X(0) \; .
$$


**Proof:** The [probability-generating function](/D/pgf) of $X$ is defined as

$$ \label{eq:pgf}
G_X(z) = \sum_{x=0}^{\infty} f_X(x) \, z^x
$$

where $f_X(x)$ is the [probability mass function](/D/pmf) of $X$. Setting $z = 0$, we obtain:

$$ \label{eq:pgf-zero-qed}
\begin{split}
G_X(0) &= \sum_{x=0}^{\infty} f_X(x) \cdot 0^x \\
&= f_X(0) + 0^1 \cdot f_X(1)  + 0^2 \cdot f_X(2) + \ldots \\
&= f_X(0) + 0 + 0 + \ldots \\
&= f_X(0) \; .
\end{split}
$$