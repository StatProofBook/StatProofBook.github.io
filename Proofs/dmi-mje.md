---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-13 21:53:00

title: "Relation of mutual information to marginal and joint entropy"
chapter: "General Theorems"
section: "Information theory"
topic: "Discrete mutual information"
theorem: "Relation to marginal and joint entropy"

dependencies:
  - theorem: "law of marginal probability"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Mutual information"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-01-13"
    url: "https://en.wikipedia.org/wiki/Mutual_information#Relation_to_conditional_and_joint_entropy"

proof_id: "P20"
shortcut: "dmi-mje"
username: "JoramSoch"
---


**Theorem:** Let $X$ and $Y$ be discrete random variables with the joint probability $p(x,y)$ for $x \in \mathcal{X}$ and $y \in \mathcal{Y}$. Then, the mutual information of $X$ and $Y$ can be expressed as

$$ \label{eq:dmi-mje}
\mathrm{I}(X,Y) = \mathrm{H}(X) + \mathrm{H}(Y) - \mathrm{H}(X,Y)
$$

where $\mathrm{H}(X)$ and $\mathrm{H}(Y)$ are the marginal entropies of $X$ and $Y$ and $\mathrm{H}(X,Y)$ is the joint entropy.


**Proof:** The mutual information of $X$ and $Y$ is defined as

$$ \label{eq:MI}
\mathrm{I}(X,Y) = \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} p(x,y) \log \frac{p(x,y)}{p(x)\,p(y)} \; .
$$

Separating the logarithm, we have:

$$ \label{eq:MI-s1}
\mathrm{I}(X,Y) = \sum_x \sum_y p(x,y) \log p(x,y) - \sum_x \sum_y p(x,y) \log p(x) - \sum_x \sum_y p(x,y) \log p(y) \; .
$$

Regrouping the variables, this reads:

$$ \label{eq:MI-s2}
\mathrm{I}(X,Y) = \sum_x \sum_y p(x,y) \log p(x,y) - \sum_x \left( \sum_y p(x,y) \right) \log p(x) - \sum_y \left( \sum_x p(x,y) \right) \log p(y) \; .
$$

Applying the law of marginal probability, i.e. $p(x) = \sum_y p(x,y)$, we get:

$$ \label{eq:MI-s3}
\mathrm{I}(X,Y) = \sum_x \sum_y p(x,y) \log p(x,y) - \sum_x p(x) \log p(x) - \sum_x p(y) \log p(y) \; .
$$

Now considering the definitions of marginal and joint entropy

$$ \label{eq:ME-JE}
\begin{split}
\mathrm{H}(X) &= - \sum_{x \in \mathcal{X}} p(x) \log p(x) \\
\mathrm{H}(X,Y) = - \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} p(x,y) \log p(x,y) \; ,
\end{split}
$$

$$ \label{eq:MI-qed}
\begin{split}
\mathrm{I}(X,Y) &= - \mathrm{H}(X,Y) + \mathrm{H}(X) + \mathrm{H}(Y) \\
&= \mathrm{H}(X) + \mathrm{H}(Y) - \mathrm{H}(X,Y) \; .
\end{split}
$$