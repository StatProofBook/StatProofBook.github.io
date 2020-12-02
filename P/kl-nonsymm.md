---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-08-11 06:57:00

title: "Non-symmetry of the Kullback-Leibler divergence"
chapter: "General Theorems"
section: "Information theory"
topic: "Kullback-Leibler divergence"
theorem: "Non-symmetry"

sources:
  - authors: "Kullback, Solomon"
    year: 1959
    title: "Divergence"
    in: "Information Theory and Statistics"
    pages: "ch. 1.3, pp. 6ff."
    url: "http://index-of.co.uk/Information-Theory/Information%20theory%20and%20statistics%20-%20Solomon%20Kullback.pdf"
  - authors: "Wikipedia"
    year: 2020
    title: "Kullback-Leibler divergence"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-08-11"
    url: "https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence#Basic_example"

proof_id: "P147"
shortcut: "kl-nonsymm"
username: "JoramSoch"
---


**Theorem:**  The [Kullback-Leibler divergence](/D/kl) is non-symmetric, i.e.

$$ \label{eq:KL-nonsymm}
\mathrm{KL}[P||Q] \neq \mathrm{KL}[Q||P]
$$

for some [probability distributions](/D/dist) $P$ and $Q$.


**Proof:** Let $X \in \mathcal{X} = \left\lbrace 0, 1, 2 \right\rbrace$ be a discrete [random variable](/D/rvar) and consider the two [probability distributions](/D/dist)

$$ \label{eq:P-Q}
\begin{split}
P : \, X &\sim \mathrm{Bin}(2, 0.5) \\
Q : \, X &\sim \mathcal{U}(0, 2)
\end{split}
$$

where $\mathrm{Bin}(n, p)$ indicates a [binomial distribution](/D/bin) and $\mathcal{U}(a, b)$ indicates a [discrete uniform distribution](/D/duni).

Then, the [probability mass function of the binomial distribution](/P/bin-pmf) entails that

$$ \label{eq:p(x)}
p(x) = \left\{
\begin{array}{rl}
1/4 \; , & \text{if} \; x = 0 \\
1/2 \; , & \text{if} \; x = 1 \\
1/4 \; , & \text{if} \; x = 2
\end{array}
\right.
$$

and the [probability mass function of the discrete uniform distribution](/P/duni-pmf) entails that

$$ \label{eq:q(x)}
q(x) = \frac{1}{3} \; ,
$$

such that the [Kullback-Leibler divergence](/D/kl) of $P$ from $Q$ is

$$ \label{eq:KL-P-Q}
\begin{split}
\mathrm{KL}[P||Q] &= \sum_{x \in \mathcal{X}} p(x) \cdot \log \frac{p(x)}{q(x)} \\
&= \frac{1}{4} \log \frac{3}{4} + \frac{1}{2} \log \frac{3}{2} + \frac{1}{4} \log \frac{3}{4} \\
&= \frac{1}{2} \log \frac{3}{4} + \frac{1}{2} \log \frac{3}{2} \\
&= \frac{1}{2} \left( \log \frac{3}{4} + \log \frac{3}{2} \right) \\
&= \frac{1}{2} \log \left( \frac{3}{4} \cdot \frac{3}{2} \right) \\
&= \frac{1}{2} \log \frac{9}{8} = 0.0589
\end{split}
$$

and the [Kullback-Leibler divergence](/D/kl) of $Q$ from $P$ is

$$ \label{eq:KL-Q-P}
\begin{split}
\mathrm{KL}[Q||P] &= \sum_{x \in \mathcal{X}} q(x) \cdot \log \frac{q(x)}{p(x)} \\
&= \frac{1}{3} \log \frac{4}{3} + \frac{1}{3} \log \frac{2}{3} + \frac{1}{3} \log \frac{4}{3} \\
&= \frac{1}{3} \left( \log \frac{4}{3} + \log \frac{2}{3} + \log \frac{4}{3} \right) \\
&= \frac{1}{3} \log \left( \frac{4}{3} \cdot \frac{2}{3} \cdot \frac{4}{3} \right) \\
&= \frac{1}{3} \log \frac{32}{27} = 0.0566
\end{split}
$$

which provides an example for

$$ \label{eq:KL-nonsymm-qed}
\mathrm{KL}[P||Q] \neq \mathrm{KL}[Q||P]
$$

and thus proves the theorem.