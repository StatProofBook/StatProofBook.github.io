---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-04-07 09:19:00

title: "Distributional transformation using cumulative distribution function"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability functions"
theorem: "Distributional transformation"

sources:
  - authors: "Soch, Joram"
    year: 2020
    title: "Distributional Transformation Improves Decoding Accuracy When Predicting Chronological Age From Structural MRI"
    in: "Frontiers in Psychiatry"
    pages: "vol. 11, art. 604268"
    url: "https://www.frontiersin.org/articles/10.3389/fpsyt.2020.604268/full"
    doi: "10.3389/fpsyt.2020.604268"

proof_id: "P222"
shortcut: "cdf-dt"
username: "JoramSoch"
---


**Theorem:** Let $X$ and $Y$ be two [continuous](/D/rvar-disc) [random variables](/D/rvar) with [cumulative distribution function](/D/cdf) $F_X(x)$ and invertible [cumulative distribution function](/D/cdf) $F_Y(y)$. Then, the [random variable](/D/rvar)

$$ \label{eq:cdf-dt}
\tilde{X} = F_Y^{-1}(F_X(X))
$$

has the same [probability distribution](/D/dist) as $Y$.


**Proof:** The [cumulative distribution function](/D/cdf) of the transformation $\tilde{X} = F_Y^{-1}(F_X(X))$ can be derived as

$$ \label{eq:cdf-dt-qed}
\begin{split}
F_{\tilde{X}}(y) &= \mathrm{Pr}\left( \tilde{X} \leq y \right) \\
&= \mathrm{Pr}\left( F_Y^{-1}(F_X(X)) \leq y \right) \\
&= \mathrm{Pr}\left( F_X(X) \leq F_Y(y) \right) \\
&= \mathrm{Pr}\left( X \leq F_X^{-1}(F_Y(y)) \right) \\
&= F_X\left( F_X^{-1}(F_Y(y)) \right) \\
&= F_Y(y) \\
\end{split}
$$

which shows that $\tilde{X}$ and $Y$ have the same [cumulative distribution function](/D/cdf) and are thus [identically distributed](/D/dist).