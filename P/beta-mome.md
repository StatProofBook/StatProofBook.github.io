---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-22 02:53:00

title: "Method of moments for beta-distributed data"
chapter: "Statistical Models"
section: "Probability data"
topic: "Beta-distributed data"
theorem: "Method of moments"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Beta distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-01-20"
    url: "https://en.wikipedia.org/wiki/Beta_distribution#Method_of_moments"

proof_id: "P28"
shortcut: "beta-mome"
username: "JoramSoch"
---


**Theorem:** Let $y = \left\lbrace y_1, \ldots, y_n \right\rbrace$ be a set of observed counts [independent and identically distributed](/D/iid) according to a [beta distribution](/D/beta) with shapes $\alpha$ and $\beta$:

$$ \label{eq:Beta}
y_i \sim \mathrm{Bet}(\alpha,\beta), \quad i = 1, \ldots, n \; .
$$

Then, the [method-of-moments estimates](/D/mome) for the shape parameters $\alpha$ and $\beta$ are given by

$$ \label{eq:Beta-MoM}
\begin{split}
\hat{\alpha} &= \bar{y} \left( \frac{\bar{y} (1-\bar{y})}{\bar{v}} - 1  \right) \\
\hat{\beta} &= (1-\bar{y}) \left( \frac{\bar{y} (1-\bar{y})}{\bar{v}} - 1  \right)
\end{split}
$$

where $\bar{y}$ is the [sample mean](/D/mean-samp) and $\bar{v}$ is the [unbiased sample variance](/D/var-samp):

$$ \label{eq:y-mean-var}
\begin{split}
\bar{y} &= \frac{1}{n} \sum_{i=1}^n y_i \\
\bar{v} &= \frac{1}{n-1} \sum_{i=1}^n (y_i - \bar{y})^2 \; .
\end{split}
$$


**Proof:** [Mean](/P/beta-mean) and [variance](/P/beta-var) of the [beta distribution](/D/beta) in terms of the parameters $\alpha$ and $\beta$ are given by

$$ \label{eq:Beta-E-Var}
\begin{split}
\mathrm{E}(X) &= \frac{\alpha}{\alpha+\beta} \\
\mathrm{Var}(X) &= \frac{\alpha\beta}{(\alpha+\beta)^2 (\alpha+\beta+1)} \; .
\end{split}
$$

Thus, [matching the moments](/D/mome) requires us to solve the following equation system for $\alpha$ and $\beta$:

$$ \label{eq:Beta-mean-var}
\begin{split}
\bar{y} &= \frac{\alpha}{\alpha+\beta} \\
\bar{v} &= \frac{\alpha\beta}{(\alpha+\beta)^2 (\alpha+\beta+1)} \; .
\end{split}
$$

From the first equation, we can deduce:

$$ \label{eq:beta-as-alpha}
\begin{split}
\bar{y}(\alpha+\beta) &= \alpha \\
\alpha \bar{y} + \beta \bar{y} &= \alpha \\
\beta \bar{y} &= \alpha - \alpha \bar{y} \\
\beta &= \frac{\alpha}{\bar{y}} - \alpha \\
\beta &= \alpha \left( \frac{1}{\bar{y}} - 1 \right) \; .
\end{split}
$$

If we define $q = 1/\bar{y} - 1$ and plug \eqref{eq:beta-as-alpha} into the second equation, we have:

$$ \label{eq:alpha-as-q}
\begin{split}
\bar{v} &= \frac{\alpha \cdot \alpha q}{(\alpha + \alpha q)^2 (\alpha + \alpha q + 1)} \\
&= \frac{\alpha^2 q}{(\alpha (1+q))^2 (\alpha (1+q) + 1)} \\
&= \frac{q}{(1+q)^2 (\alpha (1+q) + 1)} \\
&= \frac{q}{\alpha (1+q)^3 + (1+q)^2} \\
q &= \bar{v} \left[ \alpha (1+q)^3 + (1+q)^2 \right] \; .
\end{split}
$$

Noting that $1+q = 1/\bar{y}$ and $q = (1-\bar{y})/\bar{y}$, one obtains for $\alpha$:

$$ \label{eq:Beta-MoM-alpha}
\begin{split}
\frac{1-\bar{y}}{\bar{y}} &= \bar{v} \left[ \frac{\alpha}{\bar{y}^3} + \frac{1}{\bar{y}^2} \right] \\
\frac{1-\bar{y}}{\bar{y} \, \bar{v}} &= \frac{\alpha}{\bar{y}^3} + \frac{1}{\bar{y}^2} \\
\frac{\bar{y}^3(1-\bar{y})}{\bar{y} \, \bar{v}} &= \alpha + \bar{y} \\
\alpha &= \frac{\bar{y}^2(1-\bar{y})}{\bar{v}} - \bar{y} \\
&= \bar{y} \left( \frac{\bar{y} (1-\bar{y})}{\bar{v}} - 1 \right) \; .
\end{split}
$$

Plugging this into equation \eqref{eq:beta-as-alpha}, one obtains for $\beta$:

$$ \label{eq:Beta-MoM-beta}
\begin{split}
\beta &= \bar{y} \left( \frac{\bar{y} (1-\bar{y})}{\bar{v}} - 1 \right) \cdot \left( \frac{1-\bar{y}}{\bar{y}} \right) \\
&= (1-\bar{y}) \left( \frac{\bar{y} (1-\bar{y})}{\bar{v}} - 1 \right) \; .
\end{split}
$$

Together, \eqref{eq:Beta-MoM-alpha} and \eqref{eq:Beta-MoM-beta} constitute the method-of-moment estimates of $\alpha$ and $\beta$.