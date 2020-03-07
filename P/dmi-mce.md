---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-13 18:20:00

title: "Relation of mutual information to marginal and conditional entropy"
chapter: "General Theorems"
section: "Information theory"
topic: "Discrete mutual information"
theorem: "Relation to marginal and conditional entropy"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Mutual information"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-01-13"
    url: "https://en.wikipedia.org/wiki/Mutual_information#Relation_to_conditional_and_joint_entropy"

proof_id: "P19"
shortcut: "dmi-mce"
username: "JoramSoch"
---


**Theorem:** Let $X$ and $Y$ be discrete [random variables](/D/rvar) with the [joint probability](/D/prob-joint) $p(x,y)$ for $x \in \mathcal{X}$ and $y \in \mathcal{Y}$. Then, the [mutual information](/D/mi) of $X$ and $Y$ can be expressed as

$$ \label{eq:dmi-mce}
\begin{split}
\mathrm{I}(X,Y) &= \mathrm{H}(X) - \mathrm{H}(X|Y) \\
&= \mathrm{H}(Y) - \mathrm{H}(Y|X)
\end{split}
$$

where $\mathrm{H}(X)$ and $\mathrm{H}(Y)$ are the [marginal entropies](/D/ent) of $X$ and $Y$ and $\mathrm{H}(X \vert Y)$ and $\mathrm{H}(Y \vert X)$ are the [conditional entropies](/D/ent-cond).


**Proof:** The [mutual information](/D/mi) of $X$ and $Y$ is defined as

$$ \label{eq:MI}
\mathrm{I}(X,Y) = \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} p(x,y) \log \frac{p(x,y)}{p(x)\,p(y)} \; .
$$

Separating the logarithm, we have:

$$ \label{eq:MI-s1}
\mathrm{I}(X,Y) = \sum_x \sum_y p(x,y) \log \frac{p(x,y)}{p(y)} - \sum_x \sum_y p(x,y) \log p(x) \; .
$$

Applying the [law of conditional probability](/D/prob-cond), i.e. $p(x,y) = p(x \vert y) \, p(y)$, we get:

$$ \label{eq:MI-s2}
\mathrm{I}(X,Y) = \sum_x \sum_y p(x|y) \, p(y) \log p(x|y) - \sum_x \sum_y p(x,y) \log p(x) \; .
$$

Regrouping the variables, we have:

$$ \label{eq:MI-s3}
\mathrm{I}(X,Y) = \sum_y p(y) \sum_x p(x|y) \log p(x|y) - \sum_x \left( \sum_y p(x,y) \right) \log p(x) \; .
$$

Applying the [law of marginal probability](/D/prob-marg), i.e. $p(x) = \sum_y p(x,y)$, we get:

$$ \label{eq:MI-s4}
\mathrm{I}(X,Y) = \sum_y p(y) \sum_x p(x|y) \log p(x|y) - \sum_x p(x) \log p(x) \; .
$$

Now considering the definitions of [marginal](/D/ent) and [conditional](/D/ent-cond) entropy

$$ \label{eq:ME-CE}
\begin{split}
\mathrm{H}(X) &= - \sum_{x \in \mathcal{X}} p(x) \log p(x) \\
\mathrm{H}(X|Y) &= \sum_{y \in \mathcal{Y}} p(y) \, \mathrm{H}(X|Y=y) \; ,
\end{split}
$$

we can finally show:

$$ \label{eq:MI-qed}
\begin{split}
\mathrm{I}(X,Y) &= - \mathrm{H}(X|Y) + \mathrm{H}(X) \\
&= \mathrm{H}(X) - \mathrm{H}(X|Y) \; .
\end{split}
$$

The conditioning of $X$ on $Y$ in this proof is without loss of generality. Thus, the proof for the expression using the reverse conditional entropy of $Y$ given $X$ is obtained by simply switching $x$ and $y$ in the derivation.