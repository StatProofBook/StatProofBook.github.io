---

layout: proof
mathjax: true

author: "Kenneth Petrykowski"
affiliation: "Ku Leuven"
e_mail: "kenneth.petrykowski@gmail.com"
date: 2020-10-12 22:15:00

title: "Relationship between gamma and chi-squared distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Chi-square distribution"
theorem: "Relationship between gamma and chi-squared distribution"

sources:

proof_id: "P174"
shortcut: "chi-2-gam"
username: "kjpetrykowski"
---


**Theorem:** The [chi-square distribution](/D/chi-2) with $k$ degrees of freedom $X\sim \chi _{k}^{2}$ is a special case of the [gamma distribution](/D/gam) that $X\sim \Gamma \left({\frac {k}{2}},{\frac {1}{2}}\right) $


**Proof:** The [probability density function of the gamma distribution](/P/gam-pdf) for $x > 0$,  where $\alpha$ is the shape parameter and $\beta$ is the rate paramete, is as follows:

$$ \label{eq:gamm-pdf}
{ \mathrm{Gam}(x; \alpha, \beta) =\frac {\beta ^{\alpha }}{\Gamma (\alpha )}}x^{\alpha -1}e^{-\beta x}
$$

If we let $\alpha = k/2$ and $\beta = 1/2$ we obtain:

$$
{ \mathrm{Gam}(x; \frac{k}{2}, \frac{1}{2}) = \frac{x ^ {\frac{k}{2} - 1} e ^ {-x / 2}}{\Gamma(k / 2) 2 ^ {k / 2}} = {\frac {1}{2^{k/2}\Gamma (k/2)}}\;x^{k/2-1}e^{-x/2}\;} 
$$\

which is equivalent to the [probability density function of the chi-square distribution](/D/chi-2).
