---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-11-25 04:47:00

title: "Gaussian integral"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Normal distribution"
theorem: "Gaussian integral"

sources:
  - authors: "ProofWiki"
    year: 2020
    title: "Gaussian Integral"
    in: "ProofWiki"
    pages: "retrieved on 2020-11-25"
    url: "https://proofwiki.org/wiki/Gaussian_Integral"
  - authors: "ProofWiki"
    year: 2020
    title: "Integral to Infinity of Exponential of minus t squared"
    in: "ProofWiki"
    pages: "retrieved on 2020-11-25"
    url: "https://proofwiki.org/wiki/Integral_to_Infinity_of_Exponential_of_-t%5E2"

proof_id: "P196"
shortcut: "norm-gi"
username: "JoramSoch"
---


**Theorem:** The definite integral of $\mathrm{exp}\left[ -x^2 \right]$ from $-\infty$ to $+\infty$ is equal to the square root of $\pi$:

$$ \label{eq:norm-gi}
\int_{-\infty}^{+\infty} \mathrm{exp}\left[ -x^2 \right] \, \mathrm{d}x = \sqrt{\pi} \; .
$$


**Proof:** Let

$$ \label{eq:I}
I = \int_{0}^{\infty} \mathrm{exp}\left[ -x^2 \right] \, \mathrm{d}x
$$

and 

$$ \label{eq:IP}
I_P = \int_{0}^{P} \mathrm{exp}\left[ -x^2 \right] \, \mathrm{d}x = \int_{0}^{P} \mathrm{exp}\left[ -y^2 \right] \, \mathrm{d}y \; .
$$

Then, we have

$$ \label{eq:IP-I}
\lim\limits_{P \rightarrow \infty} I_P = I
$$

and

$$ \label{eq:IP2-I2}
\lim\limits_{P \rightarrow \infty} I_P^2 = I^2 \; .
$$

Moreover, we can write

$$ \label{eq:IP2}
\begin{split}
I_P^2 &\overset{\eqref{eq:IP}}{=} \left( \int_{0}^{P} \mathrm{exp}\left[ -x^2 \right] \, \mathrm{d}x \right) \left( \int_{0}^{P} \mathrm{exp}\left[ -y^2 \right] \, \mathrm{d}y \right) \\
&= \int_{0}^{P} \int_{0}^{P} \mathrm{exp}\left[ - \left( x^2 + y^2 \right) \right] \, \mathrm{d}x \, \mathrm{d}y \\
&= \iint_{S_P} \mathrm{exp}\left[ - \left( x^2 + y^2 \right) \right] \, \mathrm{d}x \, \mathrm{d}y
\end{split}
$$

where $S_P$ is the square with corners $(0,0)$, $(0,P)$, $(P,P)$ and $(P,0)$. For this integral, we can write down the following inequality

$$ \label{eq:IP2-ineq}
\iint_{C_1} \mathrm{exp}\left[ - \left( x^2 + y^2 \right) \right] \, \mathrm{d}x \, \mathrm{d}y \leq I_P^2 \leq \iint_{C_2} \mathrm{exp}\left[ - \left( x^2 + y^2 \right) \right] \, \mathrm{d}x \, \mathrm{d}y
$$

where $C_1$ and $C_2$ are the regions in the first quadrant bounded by circles with center at $(0,0)$ and going through the points $(0,P)$ and $(P,P)$, respectively. The radii of these two circles are $r_1 = \sqrt{P^2} = P$ and $r_2 = \sqrt{2 P^2} = P \sqrt{2}$, such that we can rewrite equation \eqref{eq:IP2-ineq} using polar coordinates as

$$ \label{eq:IP2-ineq-PC}
\int_{0}^{\frac{\pi}{2}} \int_{0}^{r_1} \mathrm{exp}\left[ -r^2 \right] \, r \, \mathrm{d}r \, \mathrm{d}\theta \leq I_P^2 \leq \int_{0}^{\frac{\pi}{2}} \int_{0}^{r_2} \mathrm{exp}\left[ -r^2 \right] \, r \, \mathrm{d}r \, \mathrm{d}\theta \; .
$$

Solving the definite integrals yields:

$$ \label{eq:IP2-ineq-PC-int}
\begin{split}
\int_{0}^{\frac{\pi}{2}} \int_{0}^{r_1} \mathrm{exp}\left[ -r^2 \right] r \, \mathrm{d}r \, \mathrm{d}\theta &\leq I_P^2 \leq \int_{0}^{\frac{\pi}{2}} \int_{0}^{r_2} \mathrm{exp}\left[ -r^2 \right] r \, \mathrm{d}r \, \mathrm{d}\theta \\
\int_{0}^{\frac{\pi}{2}} \left[ -\frac{1}{2} \mathrm{exp}\left[ -r^2 \right] \right]_{0}^{r_1} \, \mathrm{d}\theta &\leq I_P^2 \leq \int_{0}^{\frac{\pi}{2}} \left[ -\frac{1}{2} \mathrm{exp}\left[ -r^2 \right] \right]_{0}^{r_2} \, \mathrm{d}\theta \\
-\frac{1}{2} \int_{0}^{\frac{\pi}{2}} \left( \mathrm{exp}\left[ -r_1^2 \right] - 1 \right) \, \mathrm{d}\theta &\leq I_P^2 \leq -\frac{1}{2} \int_{0}^{\frac{\pi}{2}} \left( \mathrm{exp}\left[ -r_2^2 \right] - 1 \right) \, \mathrm{d}\theta \\
-\frac{1}{2} \left[ \left( \mathrm{exp}\left[ -r_1^2 \right] - 1 \right) \theta \right]_{0}^{\frac{\pi}{2}} &\leq I_P^2 \leq -\frac{1}{2} \left[ \left( \mathrm{exp}\left[ -r_2^2 \right] - 1 \right) \theta \right]_{0}^{\frac{\pi}{2}} \\
\frac{1}{2} \left( 1 - \mathrm{exp}\left[ -r_1^2 \right] \right) \frac{\pi}{2} &\leq I_P^2 \leq \frac{1}{2} \left( 1 - \mathrm{exp}\left[ -r_2^2 \right] \right) \frac{\pi}{2} \\
\frac{\pi}{4} \left( 1 - \mathrm{exp}\left[ -P^2 \right] \right) &\leq I_P^2 \leq \frac{\pi}{4} \left( 1 - \mathrm{exp}\left[ -2 P^2 \right] \right)
\end{split}
$$

Calculating the limit for $P \rightarrow \infty$, we obtain

$$ \label{eq:IP2-ineq-PC-int-lim}
\begin{split}
\lim\limits_{P \rightarrow \infty} \frac{\pi}{4} \left( 1 - \mathrm{exp}\left[ -P^2 \right] \right) \leq \lim\limits_{P \rightarrow \infty} I_P^2 &\leq \lim\limits_{P \rightarrow \infty} \frac{\pi}{4} \left( 1 - \mathrm{exp}\left[ -2 P^2 \right] \right) \\
\frac{\pi}{4} \leq I^2 &\leq \frac{\pi}{4} \; ,
\end{split}
$$

such that we have a preliminary result for $I$:

$$ \label{eq:I-qed}
I^2 = \frac{\pi}{4} \quad \Rightarrow \quad I = \frac{\sqrt{\pi}}{2} \; .
$$

Because the integrand in \eqref{eq:norm-gi} is an even function, we can calculate the final result as follows:

$$ \label{eq:norm-gi-qed}
\begin{split}
\int_{-\infty}^{+\infty} \mathrm{exp}\left[ -x^2 \right] \, \mathrm{d}x &= 2 \int_{0}^{\infty} \mathrm{exp}\left[ -x^2 \right] \, \mathrm{d}x \\
&\overset{\eqref{eq:I-qed}}{=} 2 \, \frac{\sqrt{\pi}}{2} \\
&= \sqrt{\pi} \; . 
\end{split}
$$