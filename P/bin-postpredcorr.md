---
layout: proof
mathjax: true

author: "Kenneth Petrykowski"
affiliation: "University of Warsaw"
e_mail: "kenneth.petrykowski@gmail.com"
date: 2026-10-17 23:10:00

title: "Posterior predictive covariance and correlation of future Bernoulli observations based on observed binomial data"
chapter: "Statistical Models"
section: "Count data"
topic: "Binomial observations"
theorem: "Posterior predictive correlation"

sources:
  - authors: "Gary Koop, Dale J. Poirier, Justin L. Tobias"
    year: 2007
    title: "Prediction"
    in: "Bayesian Econometric Methods"
    pages: "Exercise 7.1, p. 73"

proof_id: "P559"
shortcut: "bin-postpredcorr"
username: "kjpetrykowski"
---

**Theorem:** For fixed observed [binomial data](/D/bin-data) $x$, suppose the [posterior distribution](/D/post) of the success probability $\theta$ is a beta distribution with shape parameters $\alpha$ and $\beta$:

$$ \label{eq:posterior}
\theta\mid x\sim\mathrm{Bet}(\alpha,\beta),\qquad \alpha,\beta>0 \; .
$$

Let the future observations $Y\_1,Y\_2$ be [conditionally independent](/D/ind-cond) given $\theta$ and $x$, each with a [Bernoulli distribution](/D/bern) of success probability $\theta$. Both observations use the same random parameter. Then

$$ \label{eq:bern-postpredcorr-result}
\begin{split}
\mathrm{Cov}(Y_1,Y_2\mid x)&=\frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)},\\
\mathrm{Corr}(Y_1,Y_2\mid x)&=\frac{1}{\alpha+\beta+1} \; .
\end{split}
$$


**Proof:** Throughout the proof, $x$ is fixed. Write $\mathrm{B}(u,v)$ for the beta function. It supplies the normalizing constant in the [beta density](/D/beta):

$$ \label{eq:bern-postpredcorr-beta}
p(\theta\mid x)=\frac{\theta^{\alpha-1}(1-\theta)^{\beta-1}}{\mathrm{B}(\alpha,\beta)},
\qquad0<\theta<1 \; .
$$

To calculate the first two moments, multiply this density by $\theta^r$ for $r=1,2$ and integrate. Combining the powers of $\theta$ gives the [defining beta integral](/D/beta) with first argument $\alpha+r$ and second argument $\beta$:

$$ \label{eq:beta-moment-integral}
\begin{split}
\mathrm{E}(\theta^r\mid x)
&=\frac{1}{\mathrm{B}(\alpha,\beta)}
  \int_0^1\theta^r\theta^{\alpha-1}(1-\theta)^{\beta-1}\,\mathrm{d}\theta\\
&=\frac{1}{\mathrm{B}(\alpha,\beta)}
  \int_0^1\theta^{\alpha+r-1}(1-\theta)^{\beta-1}\,\mathrm{d}\theta\\
&=\frac{\mathrm{B}(\alpha+r,\beta)}{\mathrm{B}(\alpha,\beta)},\qquad r=1,2 \; .
\end{split}
$$

Let $\Gamma$ denote the [gamma function](/D/gam). The [beta–gamma relation](/P/beta-mean), $\mathrm{B}(u,v)=\Gamma(u)\Gamma(v)/\Gamma(u+v)$ for $u,v>0$, gives

$$ \label{eq:bern-postpredcorr-beta-ratio}
\begin{split}
\frac{\mathrm{B}(\alpha+r,\beta)}{\mathrm{B}(\alpha,\beta)}
&=\frac{\Gamma(\alpha+r)\Gamma(\beta)}{\Gamma(\alpha+\beta+r)}
  \frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}\\
&=\frac{\Gamma(\alpha+r)\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\alpha+\beta+r)} \; .
\end{split}
$$

Using $\Gamma(z+1)=z\Gamma(z)$ for $z>0$, the first two moments are

$$ \label{eq:bern-postpredcorr-beta-moments}
\begin{split}
\mathrm{E}(\theta\mid x)
&=\frac{\Gamma(\alpha+1)\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\alpha+\beta+1)}
=\frac{\alpha}{\alpha+\beta},\\
\mathrm{E}(\theta^2\mid x)
&=\frac{\Gamma(\alpha+2)\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\alpha+\beta+2)}
=\frac{\alpha(\alpha+1)}{(\alpha+\beta)(\alpha+\beta+1)} \; .
\end{split}
$$

The [variance is the second moment minus the squared mean](/P/var-mean). Therefore,

$$ \label{eq:bern-postpredcorr-beta-var}
\begin{split}
\mathrm{Var}(\theta\mid x)
&=\frac{\alpha(\alpha+1)}{(\alpha+\beta)(\alpha+\beta+1)}-\frac{\alpha^2}{(\alpha+\beta)^2}\\
&=\frac{\alpha(\alpha+1)(\alpha+\beta)-\alpha^2(\alpha+\beta+1)}{(\alpha+\beta)^2(\alpha+\beta+1)}\\
&=\frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)} \; .
\end{split}
$$

These are the usual [beta mean](/P/beta-mean) and [beta variance](/P/beta-var). A Bernoulli variable of success probability $\theta$ [has mean](/P/bern-mean) $\theta$. For $j=1,2$, the [law of total expectation](/P/mean-tot) gives

$$ \label{eq:bern-postpredcorr-future-mean}
\begin{split}
\mathrm{E}(Y_j\mid x)
&=\mathrm{E}[\mathrm{E}(Y_j\mid\theta,x)\mid x]\\
&=\mathrm{E}(\theta\mid x)=\frac{\alpha}{\alpha+\beta} \; .
\end{split}
$$

The product $Y\_1Y\_2$ is one exactly when both observations are one. [Conditional independence](/D/ind-cond) therefore gives

$$ \label{eq:bern-postpredcorr-conditional-product}
\begin{split}
\mathrm{E}(Y_1Y_2\mid\theta,x)
&=\mathrm{Pr}(Y_1=1,Y_2=1\mid\theta,x)\\
&=\mathrm{Pr}(Y_1=1\mid\theta,x)\mathrm{Pr}(Y_2=1\mid\theta,x)\\
&=\theta^2 \; .
\end{split}
$$

Taking the expectation over $\theta$ gives $\mathrm{E}(Y\_1Y\_2\mid x)=\mathrm{E}(\theta^2\mid x)$. Substitute this into the [covariance identity](/P/cov-mean):

$$ \label{eq:bern-postpredcorr-covariance}
\begin{split}
\mathrm{Cov}(Y_1,Y_2\mid x)
&=\mathrm{E}(Y_1Y_2\mid x)
 -\mathrm{E}(Y_1\mid x)\mathrm{E}(Y_2\mid x)\\
&=\mathrm{E}(\theta^2\mid x)-[\mathrm{E}(\theta\mid x)]^2\\
&=\mathrm{Var}(\theta\mid x)
=\frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)} \; .
\end{split}
$$

Each $Y\_j$ is zero or one, so $Y\_j^2=Y\_j$. Put $q=\alpha/(\alpha+\beta)$. Its predictive variance is

$$ \label{eq:bern-postpredcorr-future-variance}
\mathrm{Var}(Y_j\mid x)=q-q^2
=\frac{\alpha}{\alpha+\beta}\frac{\beta}{\alpha+\beta}
=\frac{\alpha\beta}{(\alpha+\beta)^2} \; .
$$

Both variances are positive because $\alpha,\beta>0$. The [definition of conditional correlation](/D/corr-cond) now gives

$$ \label{eq:predictive-correlation}
\begin{split}
\mathrm{Corr}(Y_1,Y_2\mid x)
&=\frac{\mathrm{Cov}(Y_1,Y_2\mid x)}
 {\sqrt{\mathrm{Var}(Y_1\mid x)\mathrm{Var}(Y_2\mid x)}}\\
&=\frac{\alpha\beta/[(\alpha+\beta)^2(\alpha+\beta+1)]}{\alpha\beta/(\alpha+\beta)^2}
=\frac{1}{\alpha+\beta+1} \; .
\end{split}
$$

The observations are independent when their shared parameter is given. Averaging over uncertainty about that parameter makes their predictive covariance positive.
