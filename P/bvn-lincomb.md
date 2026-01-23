---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2024-10-25 11:59:37

title: "Linear combination of bivariate normal random variables"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Bivariate normal distribution"
theorem: "Linear combination"

sources:
  - authors: "Wikipedia"
    year: 2024
    title: "Misconceptions about the normal distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2024-10-25"
    url: "https://en.wikipedia.org/wiki/Misconceptions_about_the_normal_distribution"

proof_id: "P475"
shortcut: "bvn-lincomb"
username: "JoramSoch"
---


**Theorem:** Let $X$ and $Y$ follow a [bivariate normal distribution](/D/bvn):

$$ \label{eq:bvn}
\left[ \begin{matrix} X \\ Y \end{matrix} \right] \sim
\mathcal{N}\left( \left[ \begin{matrix} \mu_1 \\ \mu_2 \end{matrix} \right], \left[ \begin{matrix} \sigma_1^2 & \sigma_{12} \\ \sigma_{12} & \sigma_2^2 \end{matrix} \right] \right) \; .
$$

Then, any linear combination of $X$ and $Y$ follows a [univariate normal distribution](/D/norm):

$$ \label{eq:bvn-lincomb}
Z = a X + b Y \sim
\mathcal{N}\left( a \mu_1 + b \mu_2, a^2 \sigma_1^2 + 2ab \sigma_{12} + b^2 \sigma_2^2 \right) \; .
$$


**Proof:** The [linear transformation theorem for the multivariate normal distribution](/P/mvn-ltt) states that

$$ \label{eq:mvn-ltt}
X \sim \mathcal{N}(\mu, \Sigma) \quad \Rightarrow \quad Y = AX + c \sim \mathcal{N}(A\mu + c, A \Sigma A^\mathrm{T})
$$

where $X \in \mathbb{R}^n$, $A \in \mathbb{R}^{n \times n}$ and $c \in \mathbb{R}^n$. In the present case, we have

$$ \label{eq:X-A-a}
X \in \mathbb{R}^2
\quad \text{and} \quad
A = \left[ \begin{matrix} a & b \end{matrix} \right] \in \mathbb{R}^{1 \times 2}
\quad \text{and} \quad
c = 0 \in \mathbb{R} \; ,
$$

such that

$$ \label{eq:Z-X-Y}
Z
= A \left[ \begin{matrix} X \\ Y \end{matrix} \right] + c
= \left[ \begin{matrix} a & b \end{matrix} \right] \left[ \begin{matrix} X \\ Y \end{matrix} \right] + 0
= a X + b Y \; .
$$

Combining \eqref{eq:mvn-ltt}, \eqref{eq:bvn} and \eqref{eq:Z-X-Y}, it follows that

$$ \label{eq:bvn-lincomb-qed}
\begin{split}
Z
&\sim \mathcal{N}\left( \left[ \begin{matrix} a & b \end{matrix} \right] \left[ \begin{matrix} \mu_1 \\ \mu_2 \end{matrix} \right], \left[ \begin{matrix} a & b \end{matrix} \right] \left[ \begin{matrix} \sigma_1^2 & \sigma_{12} \\ \sigma_{12} & \sigma_2^2 \end{matrix} \right] \left[ \begin{matrix} a \\ b \end{matrix} \right] \right) \\
&\sim \mathcal{N}\left( a \mu_1 + b \mu_2, \left[ \begin{matrix} a \sigma_1^2 + b \sigma_{12} & a \sigma_{12} + b \sigma_2^2 \end{matrix} \right] \left[ \begin{matrix} a \\ b \end{matrix} \right] \right) \\
&\sim \mathcal{N}\left( a \mu_1 + b \mu_2, (a^2 \sigma_1^2 + ab \sigma_{12}) + (ab \sigma_{12} + b^2 \sigma_2^2) \right) \\
&\sim \mathcal{N}\left( a \mu_1 + b \mu_2, a^2 \sigma_1^2 + 2ab \sigma_{12} + b^2 \sigma_2^2 \right) \; .
\end{split}
$$