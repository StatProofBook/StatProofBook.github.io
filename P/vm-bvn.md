---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-04-22 15:24:48

title: "Relationship between bivariate normal distribution and von Mises distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "von Mises distribution"
theorem: "Relationship to bivariate normal distribution"

sources:
  - authors: "Bishop CM"
    year: 2006
    title: "Periodic variables"
    in: "Pattern Recognition for Machine Learning"
    pages: "sect. 2.3.8, pp. 107-108, eqs. 2.173-2.180"
    url: "http://users.isr.ist.utl.pt/~wurmd/Livros/school/Bishop%20-%20Pattern%20Recognition%20And%20Machine%20Learning%20-%20Springer%20%202006.pdf"
  - authors: "Abramowitz M, Stegun IA"
    year: 1965
    title: "Handbook of Mathematical Functions"
    url: "https://books.google.de/books?hl=en&lr=&id=oTl9wunfepIC&oi=fnd&pg=PR3&dq=abramowitz+%26+stegun&ots=yIXf-SweEC&sig=TOX5SU7zgEGX2cULwgGxaYi1awI&redir_esc=y#v=onepage&q&f=false"

proof_id: "P536"
shortcut: "vm-bvn"
username: "JoramSoch"
---


**Theorem:** Let $Y_1$ and $Y_2$ follow a [bivariate normal distribution](/D/bvn) with means $\mu_1$ and $\mu_2$ and [spherical covariance matrix](/D/spher):

$$ \label{eq:bvn}
Y =  \left[ \begin{matrix} Y_1 \\ Y_2 \end{matrix} \right]
\sim \mathcal{N}\left( \left[ \begin{matrix} \mu_1 \\ \mu_2 \end{matrix} \right], \sigma^2 \left[ \begin{matrix} 1 & 0 \\ 0 & 1 \end{matrix} \right] \right) \; .
$$

Consider the polar-coordinate representation of the complex numbers $Y_1 + i Y_2$ and $\mu_1 + i \mu_2$ using the [random variables](/D/rvar) $X$ and $R$ as well as the constants $x_0 \in [0, 2 \pi)$ and $r_0 \in [0, \infty)$:

$$ \label{eq:Y12-mu12-rX-rX0}
\begin{split}
Y_1   &= R \cdot \cos X, \quad
Y_2    = R \cdot \sin X  \\
\mu_1 &= r_0 \cdot \cos x_0, \quad 
\mu_2  = r_0 \cdot \sin x_0  \; .
\end{split}
$$

Then, the [circular random variable](/D/rvar-circ) $X$, i.e. the angular direction of the [random vector](/D/rvec) $Y$ follows a von Mises distribution with circular mean $\mu = x_0$ and reciprocal dispersion $\kappa = r_0 / \sigma^2$:

$$ \label{eq:vm}
X \sim \mathrm{vM}(\mu, \kappa) \; .
$$


**Proof:** The [probability density function of the bivariate normal distribution](/P/bvn-pdf) with the parameters specified in \eqref{eq:bvn} is equal to

$$ \label{eq:bvn-pdf}
\begin{split}
   p(y_1,y_2)
&= \frac{1}{2 \pi \sqrt{\sigma^2 \sigma^2 - 0}} \cdot \exp \left[ -\frac{1}{2} \frac{\sigma^2 (y_1-\mu_1)^2 - 2 \cdot 0 \cdot (y_1-\mu_1)(y_2-\mu_2) + \sigma^2 (y_2-\mu_2)^2}{\sigma^2 \sigma^2 - 0} \right] \\
&= \frac{1}{2 \pi \sigma^2} \cdot \exp \left[ -\frac{1}{2} \frac{(y_1-\mu_1)^2 + (y_2-\mu_2)^2}{\sigma^2} \right] \; .
\end{split}
$$

Substituting the expressions from \eqref{eq:Y12-mu12-rX-rX0}, we obtain an unnormalized distribution over $X$ and $R$:

$$ \label{eq:vm-pdf-s1}
\begin{split}
         p(x,r)
&\propto \frac{1}{2 \pi \sigma^2} \cdot \exp \left[ -\frac{1}{2 \sigma^2} \left( (r \cos x - r_0 \cos x_0)^2 + (r \sin x - r_0 \sin x_0)^2 \right) \right] \\
&\propto \frac{1}{2 \pi \sigma^2} \cdot \exp \left[ -\frac{1}{2 \sigma^2} \left( (r^2 \cos^2 x - 2 r r_0 \cos x \cos x_0 + r_0^2 \cos^2 x_0) + \right. \right. \\
&\hphantom{= \frac{1}{2 \pi \sigma^2} \cdot \exp \left[ -\frac{1}{2 \sigma^2} \right]} \left. \left. (r^2 \sin^2 x - 2 r r_0 \sin x \sin x_0 + r_0^2 \sin^2 x_0) \right) \right] \; .
\end{split}
$$

Using the trigonometric identities

$$ \label{eq:sin-cos}
\begin{split}
\sin^2 x + \cos^2 x &= 1 \\
\cos x \cos y + \sin x \sin y &= \cos(x-y) \; ,
\end{split}
$$

this can be further developped into:

$$ \label{eq:vm-pdf-s2}
\begin{split}
         p(x,r)
&\propto \frac{1}{2 \pi \sigma^2} \cdot \exp \left[ -\frac{1}{2 \sigma^2} \left( r^2 + r_0^2 - 2 r r_0 (\cos x \cos x_0 + \sin x \sin x_0) \right) \right] \\
&\propto \frac{1}{2 \pi \sigma^2} \cdot \exp \left[ -\frac{1}{2 \sigma^2} \left( r^2 + r_0^2 - 2 r r_0 \cos(x-x_0) \right) \right] \; .
\end{split}
$$

Conditioning on the unit circle, i.e. setting $r = 1$ and eliminanting this random variable, and collecting all terms not depending on $x$ into a constant, we get:

$$ \label{eq:vm-pdf-s3}
\begin{split}
         p(x)
&\propto \frac{1}{2 \pi \sigma^2} \cdot \exp \left[ -\frac{1}{2 \sigma^2} \left( 1 + r_0^2 - 2 r_0 \cos(x-x_0) \right) \right] \\
&\propto \frac{1}{2 \pi \sigma^2} \cdot \exp \left[ \frac{r_0}{\sigma^2} \cos(x-x_0) + \mathrm{const.} \right] \; .
\end{split}
$$

Finally, substituing $x_0 = \mu$ and $r_0 / \sigma^2 = \kappa$, and normalizing the right-hand side to get a [probability density function](/D/pdf), we obtain

$$ \label{eq:vm-pdf-qed}
\begin{split}
p(x) &= \frac{1}{2 \pi I_0(\kappa)} \cdot \exp \left[ \kappa \cos(x-\mu) \right] \\ \mathrm{with} \quad
I_0(\kappa) &= \frac{1}{2\pi} \int_0^{2\pi} \exp \left[ \kappa \cos(x) \right] \, \mathrm{d}x
\end{split}
$$

which is equivalent to the [probability density function of the von Mises distribution](/P/vm-pdf).