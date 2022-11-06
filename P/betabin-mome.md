---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-10-07 15:13:00

title: "Method of moments for beta-binomial data"
chapter: "Statistical Models"
section: "Frequency data"
topic: "Beta-binomial data"
theorem: "Method of moments"

sources:
  - authors: "statisticsmatt"
    year: 2022
    title: "Method of Moments Estimation Beta Binomial Distribution"
    in: "YouTube"
    pages: "retrieved on 2022-10-07"
    url: "https://www.youtube.com/watch?v=18PWnWJsPnA"
  - authors: "Wikipedia"
    year: 2022
    title: "Beta-binomial distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-10-07"
    url: "https://en.wikipedia.org/wiki/Beta-binomial_distribution#Method_of_moments"

proof_id: "P357"
shortcut: "betabin-mome"
username: "JoramSoch"
---


**Theorem:** Let $y = \left\lbrace y_1, \ldots, y_N \right\rbrace$ be a set of observed counts independent and identically distributed according to a [beta-binomial distribution](/D/betabin) with number of trials $n$ as well as parameters $\alpha$ and $\beta$:

$$ \label{eq:binbeta}
y_i \sim \mathrm{BetBin}(n, \alpha, \beta), \quad i = 1, \ldots, N \; .
$$

Then, the [method-of-moments estimates](/D/mome) for the parameters $\alpha$ and $\beta$ are given by

$$ \label{eq:binbeta-mome}
\begin{split}
\hat{\alpha} &= \frac{n m_1 - m_2}{n \left( \frac{m_2}{m_1} - m_1 - 1 \right) + m_1} \\
\hat{\beta} &= \frac{\left( n - m_1 \right)\left( n - \frac{m_2}{m_1} \right)}{n \left( \frac{m_2}{m_1} - m_1 - 1 \right) + m_1}
\end{split}
$$

where $m_1$ and $m_2$ are the [first two raw sample moments](/D/mom-raw):

$$ \label{eq:y-m1-m2}
\begin{split}
m_1 &= \frac{1}{N} \sum_{i=1}^N y_i \\
m_2 &= \frac{1}{N} \sum_{i=1}^N y_i^2 \; .
\end{split}
$$


**Proof:** The first two [raw moments of the beta-binomial distribution](/D/betabin-mom) in terms of the parameters $\alpha$ and $\beta$ are given by

$$ \label{eq:binbeta-mu1-mu2}
\begin{split}
\mu_1 &= \frac{n \alpha}{\alpha + \beta} \\
\mu_2 &= \frac{n \alpha (n \alpha + \beta + n)}{(\alpha + \beta)(n \alpha + \beta + 1)}
\end{split}
$$

Thus, [matching the moments](/D/mome) requires us to solve the following equation system for $\alpha$ and $\beta$:

$$ \label{eq:binbeta-m1-m2}
\begin{split}
m_1 &= \frac{n \alpha}{\alpha + \beta} \\
m_2 &= \frac{n \alpha (n \alpha + \beta + n)}{(\alpha + \beta)(n \alpha + \beta + 1)} \; .
\end{split}
$$

From the first equation, we can deduce:

$$ \label{eq:beta-as-alpha}
\begin{split}
m_1(\alpha+\beta) &= n \alpha \\
m_1 \alpha + m_1 \beta &= n \alpha \\
m_1 \beta &= n \alpha - m_1 \alpha \\
\beta &= \frac{n \alpha}{m_1} - \alpha \\
\beta &= \alpha \left( \frac{n}{m_1} - 1 \right) \; .
\end{split}
$$

If we define $q = n/m_1 - 1$ and plug \eqref{eq:beta-as-alpha} into the second equation, we have:

$$ \label{eq:alpha-as-q}
\begin{split}
m_2 &= \frac{n \alpha (n \alpha + \alpha q + n)}{(\alpha + \alpha q)(\alpha + \alpha q + 1)} \\
&= \frac{n \alpha (\alpha (n + q) + n)}{\alpha (1 + q)(\alpha (1 + q) + 1)} \\
&= \frac{n (\alpha (n + q) + n)}{(1 + q)(\alpha (1 + q) + 1)} \\
&= \frac{n (\alpha (n + q) + n)}{\alpha (1 + q)^2 + (1 + q)} \; .
\end{split}
$$

Noting that $1+q = n/m_1$ and expanding the fraction with $m_1$, one obtains:

$$ \label{eq:binbeta-mome-alpha}
\begin{split}
m_2 &= \frac{n \left(\alpha \left( \frac{n}{m_1} + n - 1 \right) + n \right)}{n \left( \alpha \frac{n}{m_1^2} + \frac{1}{m_1} \right)} \\
m_2 &= \frac{\alpha \left( n + n m_1 - m_1 \right) + n m_1}{\alpha \frac{n}{m_1} + 1} \\
m_2 \left( \frac{\alpha n}{m_1} + 1 \right) &= \alpha \left( n + n m_1 - m_1 \right) + n m_1 \\
\alpha \left( n \frac{m_2}{m_1} - (n + n m_1 - m_1) \right) &= n m_1 - m_2 \\
\alpha \left( n \left( \frac{m_2}{m_1} - m_1 - 1 \right) + m_1 \right) &= n m_1 - m_2 \\
\alpha &= \frac{n m_1 - m_2}{n \left( \frac{m_2}{m_1} - m_1 - 1 \right) + m_1} \; .
\end{split}
$$

Plugging this into equation \eqref{eq:beta-as-alpha}, one obtains for $\beta$:

$$ \label{eq:binbeta-mome-beta}
\begin{split}
\beta &= \alpha \left( \frac{n}{m_1} - 1 \right) \\
\beta &= \left( \frac{n m_1 - m_2}{n \left( \frac{m_2}{m_1} - m_1 - 1 \right) + m_1} \right) \left( \frac{n}{m_1} - 1 \right) \\
\beta &= \frac{n^2 - n m_1 - n \frac{m_2}{m_1} + m_2}{n \left( \frac{m_2}{m_1} - m_1 - 1 \right) + m_1} \\
\hat{\beta} &= \frac{\left( n - m_1 \right)\left( n - \frac{m_2}{m_1} \right)}{n \left( \frac{m_2}{m_1} - m_1 - 1 \right) + m_1} \; .
\end{split}
$$

Together, \eqref{eq:binbeta-mome-alpha} and \eqref{eq:binbeta-mome-beta} constitute the method-of-moment estimates of $\alpha$ and $\beta$.