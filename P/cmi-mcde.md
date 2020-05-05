---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-21 16:53:00

title: "Relation of continuous mutual information to marginal and conditional differential entropy"
chapter: "General Theorems"
section: "Information theory"
topic: "Continuous mutual information"
theorem: "Relation to marginal and conditional differential entropy"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Mutual information"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-02-21"
    url: "https://en.wikipedia.org/wiki/Mutual_information#Relation_to_conditional_and_joint_entropy"

proof_id: "P58"
shortcut: "cmi-mcde"
username: "JoramSoch"
---

**Theorem:** Let $X$ and $Y$ be continuous [random variables](/D/rvar) with the [joint probability](/D/prob-joint) $p(x,y)$ for $x \in \mathcal{X}$ and $y \in \mathcal{Y}$. Then, the [mutual information](/D/mi) of $X$ and $Y$ can be expressed as

$$ \label{eq:cmi-mcde}
\begin{split}
\mathrm{I}(X,Y) &= \mathrm{h}(X) - \mathrm{h}(X|Y) \\
&= \mathrm{h}(Y) - \mathrm{h}(Y|X)
\end{split}
$$

where $\mathrm{h}(X)$ and $\mathrm{h}(Y)$ are the [marginal differential entropies](/D/dent) of $X$ and $Y$ and $\mathrm{h}(X \vert Y)$ and $\mathrm{h}(Y \vert X)$ are the [conditional differential entropies](/D/dent-cond).


**Proof:** The [mutual information](/D/mi) of $X$ and $Y$ is defined as

$$ \label{eq:MI}
\mathrm{I}(X,Y) = \int_{\mathcal{X}} \int_{\mathcal{Y}} p(x,y) \log \frac{p(x,y)}{p(x)\,p(y)} \, \mathrm{d}y \, \mathrm{d}x \; .
$$

Separating the logarithm, we have:

$$ \label{eq:MI-s1}
\mathrm{I}(X,Y) = \int_{\mathcal{X}} \int_{\mathcal{Y}} p(x,y) \log \frac{p(x,y)}{p(y)} \, \mathrm{d}y \, \mathrm{d}x - \int_{\mathcal{X}} \int_{\mathcal{Y}} p(x,y) \log p(x) \, \mathrm{d}x \, \mathrm{d}y \; .
$$

Applying the [law of conditional probability](/D/prob-cond), i.e. $p(x,y) = p(x \vert y) \, p(y)$, we get:

$$ \label{eq:MI-s2}
\mathrm{I}(X,Y) = \int_{\mathcal{X}} \int_{\mathcal{Y}} p(x|y) \, p(y) \log p(x|y) \, \mathrm{d}y \, \mathrm{d}x - \int_{\mathcal{X}} \int_{\mathcal{Y}} p(x,y) \log p(x) \, \mathrm{d}y \, \mathrm{d}x \; .
$$

Regrouping the variables, we have:

$$ \label{eq:MI-s3}
\mathrm{I}(X,Y) = \int_{\mathcal{Y}} p(y) \int_{\mathcal{X}} p(x|y) \log p(x|y) \, \mathrm{d}x \, \mathrm{d}y - \int_{\mathcal{X}} \left( \int_{\mathcal{Y}} p(x,y) \, \mathrm{d}y \right) \log p(x)\, \mathrm{d}x \; .
$$

Applying the [law of marginal probability](/D/prob-marg), i.e. $p(x) = \int_{\mathcal{Y}} p(x,y) \, \mathrm{d}y$, we get:

$$ \label{eq:MI-s4}
\mathrm{I}(X,Y) = \int_{\mathcal{Y}} p(y) \int_{\mathcal{X}} p(x|y) \log p(x|y) \, \mathrm{d}x \, \mathrm{d}y - \int_{\mathcal{X}} p(x) \log p(x) \, \mathrm{d}x \; .
$$

Now considering the definitions of [marginal](/D/dent) and [conditional](/D/dent-cond) differential entropy

$$ \label{eq:MDE-CDE}
\begin{split}
\mathrm{h}(X) &= - \int_{\mathcal{X}} p(x) \log p(x) \, \mathrm{d}x \\
\mathrm{h}(X|Y) &= \int_{\mathcal{Y}} p(y) \, \mathrm{h}(X|Y=y) \, \mathrm{d}y \; ,
\end{split}
$$

we can finally show:

$$ \label{eq:MI-qed}
\mathrm{I}(X,Y) = - \mathrm{h}(X|Y) + \mathrm{h}(X) = \mathrm{h}(X) - \mathrm{h}(X|Y) \; .
$$

The conditioning of $X$ on $Y$ in this proof is without loss of generality. Thus, the proof for the expression using the reverse conditional differential entropy of $Y$ given $X$ is obtained by simply switching $x$ and $y$ in the derivation.