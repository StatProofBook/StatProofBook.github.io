---
layout: proof
mathjax: true

author: "Leo Hope-Kaufman"
affiliation: "Harvard University Extension School"
e_mail: "leohopekaufman@gmail.com"
date: 2024-12-26 12:00:00

title: "Relationship Between Gamma and Chi-Squared Distributions"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Gamma distribution"
theorem: "Relationship between Gamma and Chi-squared distributions"

sources:
  - authors: "Irene Vrbik"
    year: 2025
    title: "MGF of a Gamma and Chi square"
    in: "Stat 205"
    url: "https://irene.vrbik.ok.ubc.ca/quarto/stat205/lectures/proofs/mgf-gamma.html"
  - authors: "John Rice"
    year: 2007
    title: "Mathematical Statistics, Third Edition"
    in: "Cengage"
    pages: "p. 155 and p. A2"
  - authors: "Wikipedia"
    year: 2025
    title: "Chi-squared distribution"
    url: "https://en.wikipedia.org/wiki/Chi-squared_distribution"
  - authors: "Wikipedia"
    year: 2025
    title: "Gamma distribution"
    url: "https://en.wikipedia.org/wiki/Gamma_distribution"
  - authors: "Joram Soch"
    year: 2024
    title: "Proof: Moment-generating function of the gamma distribution"
    url: "https://statproofbook.github.io/P/gam-mgf.html"



proof_id: "P521"
shortcut: "gma-chi"
username: "natrium-256"
---


**Theorem:** 

$$\label{eq:Theorem}$$
The chi-squared distribution with n degrees of freedom,  $\chi^2_n$ with $n \in \mathbb{Z}^*$, is a special case of the Gamma distribution $\textrm{Gamma}(\alpha, \beta)$ with parameters $\alpha=\frac{n}{2}$, $\beta=\frac{1}{2}$, and support $t< \frac{1}{2}$. 


**Proof:** 
$$\label{eq:Proof}$$
1. One formulation of the moment-generating function of a Gamma random variable $X \sim \textrm{Gamma}(\alpha, \beta)$ is $$M_X (t) = (1-\frac{t}{\beta})^{-\alpha}, \ t < {\beta},\ \beta>0$$ (Vrbik, 2025) (Rice, 2007, p. A2) (Wikipedia, 2025).
2. It is known that the moment-generating function of the a chi-square random variable with n degrees of freedom, $X_{chi} \sim \chi^2_{n}$,  is $$M_{X_{chi}} (t) = (1-2t)^{-n/2}, t<\frac{1}{2}$$ according to Vrbik (2025). 

3. If there is a random variable $X_{Gamma} \sim \textrm{Gamma} (\alpha = n/2, \beta = 1/2)$, then $$M_{X_{Gamma}} (t) = (1-\frac{t}{\frac{1}{2}})^{-(n/2)} = (1-2t)^{-n/2} = M_{X_{chi}} (t) \ \mathrm{for } \ t<\frac{1}{2} $$ 
4. "If the moment-generating function exists for t in an open interval containing zero, it uniquely determines the probability distribution," (Rice, 2007, p. 155) and both of these moment-generating functions satisfy this condition. Specifically, $M_{X_{chi}}(t)$ is defined for $t<\frac {1}{2}$, and for $M_{X_{Gamma}}(t), t < \beta$ with $ \beta>0$, as shown by Vrbik (2025), Rice (2007), and Wikipedia (2025); both of these intervals contain 0. 

$\therefore$ By the uniqueness of the moment-generating function, the chi-squared distribution with n degrees of freedom,  $\chi^2_n$ with $n \in \mathbb{Z}^*$,  is a special case of the Gamma distribution $\textrm{Gamma}(\alpha, \beta)$ with parameters $\alpha=\frac{n}{2}$ and $\beta=\frac{1}{2}$, and support $t< \frac {1}{2}$. This completes the proof of \eqref{eq:Theorem} $\blacksquare$
