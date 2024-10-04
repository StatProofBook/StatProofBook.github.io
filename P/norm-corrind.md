---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-10-04 10:59:19

title: "Normally distributed and uncorrelated does not imply independent"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Normal distribution"
theorem: "Normal and uncorrelated does not imply independent"

sources:
  - authors: "Wikipedia"
    year: 2024
    title: "Misconceptions about the normal distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2024-10-04"
    url: "https://en.wikipedia.org/wiki/Misconceptions_about_the_normal_distribution#A_symmetric_example"

proof_id: "P473"
shortcut: "norm-corrind"
username: "JoramSoch"
---


**Theorem:** Consider two [random variables](/D/rvar) $X$ and $Y$. If each of them is [normally distributed](/D/norm) and both are [uncorrelated](/D/corr), then $X$ and $Y$ are not necessarily [independent](/D/ind).


**Proof:** As an example, let $V$ follow a [Bernoulli distribution](/D/bern) with [success probability](/D/bern) $1/2$ and let $W$ be defined as a transformation of $V$:

$$ \label{eq:V-W}
\begin{split}
V &\sim \mathrm{Bern}\left( \frac{1}{2} \right) \\
W &= 2V-1 \; .
\end{split}
$$

By [definition of the Bernoulli distribution](/D/bern), it follows that

$$ \label{eq:V-W-dist}
p(V=0)  = p(V=1)  = \frac{1}{2}
\quad \Rightarrow \quad
p(W=-1) = p(W=+1) = \frac{1}{2} \; .
$$

Moreover, let $X$ follow a [standard normal distribution](/D/snorm) and let $Y$ be defined as a transformation of $X$ and $W$:

$$ \label{eq:X-Y}
\begin{split}
X &\sim \mathcal{N}(0,1) \\
Y &= WX \; .
\end{split}
$$

Then, by the nature of the [random variable](/D/rvar) $W$, it follows that

$$ \label{eq:X-Y-dist}
p(W=-1) = p(W=+1) = \frac{1}{2}
\quad \Rightarrow \quad
p(Y=-X) = p(Y=+X) = \frac{1}{2} \; .
$$

Since the negative of a [standard normal](/D/snorm) random variable [is also standard normally distributed](/P/norm-lincomb),

$$ \label{eq:X-dist}
 X \sim \mathcal{N}(0,1)
\quad \Rightarrow \quad
-X \sim \mathcal{N}(0,1) \; ,
$$

we can calculate the [probability density function](/D/pdf) belonging to the [mixture distribution](/D/dist-mixt) of $Y$ as follows:

$$ \label{eq:Y-pdf}
\begin{split}
   p(y)
&= p(y|Y=-X) \cdot p(Y=-X) + p(y|Y=+X) \cdot p(Y=+X) \\
&\overset{\eqref{eq:X-Y-dist}}{=} \mathcal{N}(y; 0, 1) \cdot \frac{1}{2} + \mathcal{N}(y; 0, 1) \cdot \frac{1}{2} \\
&= \mathcal{N}(y; 0, 1)
\end{split}
$$

where we have used the [law of marginal probability](/D/prob-marg) in the first line and $\mathcal{N}(x; \mu, \sigma^2)$ denotes the [probability density function of the normal distribution](/P/norm-pdf). Thus, $Y$ is also [standard normally distributed](/D/snorm):

$$ \label{eq:Y-dist}
Y \sim \mathcal{N}(0,1) \; .
$$

This means that both $X$ and $Y$ have expected value zero:

$$ \label{eq:X-Y-mean}
\mathrm{E}(X) = \mathrm{E}(Y) = 0 \; .
$$

With that, we can start to work out the covariance of $X$ and $Y$:

$$ \label{eq:X-Y-cov-s1}
\begin{split}
   \mathrm{Cov}(X,Y)
&= \mathrm{E}\left[ \left( X-\mathrm{E}(X) \right) \left( Y-\mathrm{E}(Y) \right) \right] \\
&\overset{\eqref{eq:X-Y-mean}}{=} \mathrm{E}\left[ XY \right] \\
&\overset{\eqref{eq:X-Y}}{=} \mathrm{E}\left[ XWX \right] \\
&= \mathrm{E}\left[ WX^2 \right] \; .
\end{split}
$$

Since $W$ and $X$ are [independent](/D/ind) by construction, their [expected values factorize](/P/mean-mult):

$$ \label{eq:X-Y-cov-s2}
\begin{split}
   \mathrm{Cov}(X,Y)
&= \mathrm{E}[W] \cdot \mathrm{E}[X^2] \\
&= \left( (-1) \cdot p(W=-1) + (+1) \cdot p(W=+1) \right) \cdot \mathrm{E}[X^2] \\
&\overset{\eqref{eq:V-W-dist}}{=} \left( (-1) \cdot \frac{1}{2} + (+1) \cdot \frac{1}{2} \right) \cdot \mathrm{E}[X^2] \\
&= 0 \cdot \mathrm{E}[X^2] \\
&= 0 \; .
\end{split}
$$

Thus, $X$ and $Y$ are [uncorrelated](/D/corr):

$$ \label{eq:X-Y-corr}
\mathrm{Corr}(X,Y) = \frac{\mathrm{Cov}(X,Y)}{\sqrt{\mathrm{Var}(X)} \sqrt{\mathrm{Var}(Y)}} = 0 \; .
$$

Yet, $X$ and $Y$ are not [independent](/D/ind), since the [marginal density](/D/dist-marg) of $Y$ is

$$ \label{eq:Y-dist-marg}
p(y) = \mathcal{N}(y; 0, 1) \; ,
$$

but the [conditional density](/D/dist-cond) of $Y$ given $X$ is

$$ \label{eq:Y-dist-cond}
p(y|x) = \left\{
\begin{array}{rl}
1/2 \; , & \text{if} \; y = -x \\
1/2 \; , & \text{if} \; y = +x \\
  0 \; , & \text{otherwise}
\end{array}
\right. \; ,
$$

thus violating the [behavior of probability under independence](/P/prob-ind):

$$ \label{eq:X-Y-dep}
p(Y) \neq p(Y|X) \; .
$$

Therefore, $X$ and $Y$ defined by \eqref{eq:X-Y} and \eqref{eq:V-W} constitute an example for two [random variables](/D/rvar) that are [normally distributed](/D/norm) and [uncorrelated](/D/corr), but not [independent](/D/ind).