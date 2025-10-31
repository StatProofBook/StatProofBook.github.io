---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2024-04-26 12:12:14

title: "Log Bayes factor for Bayesian linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Bayesian linear regression"
theorem: "Log Bayes factor for comparison of two regression models"

sources:

proof_id: "P449"
shortcut: "blr-lbf"
username: "JoramSoch"
---


**Theorem:** Let $y = \left[ y_1, \ldots, y_n \right]^\mathrm{T}$ be an $n \times 1$ vector of a [measured univariate signal](/D/data) and consider two [linear regression models](/D/mlr) with [design matrices](/D/mlr) $X_1, X_2$ and [precision matrices](/P/blr-prior) $P_1, P_2$, entailing potentially different [regression coefficients](/D/mlr) $\beta_1, \beta_2$ and [noise precisions](/P/blr-prior) $\tau_1, \tau_2$:

$$ \label{eq:GLM-NG-12}
\begin{split}
m_1: \; y &= X_1 \beta_1 + \varepsilon_1, \; \varepsilon_1 \sim \mathcal{N}(0, \sigma_1^2 V_1), \; \sigma_1^2 V_1 = (\tau_1 P_1)^{-1} \\
m_2: \; y &= X_2 \beta_2 + \varepsilon_2, \; \varepsilon_2 \sim \mathcal{N}(0, \sigma_2^2 V_2), \; \sigma_2^2 V_2 = (\tau_2 P_2)^{-1} \; .
\end{split}
$$

Moreover, assume [normal-gamma prior distributions](/P/blr-prior) over the model parameters $\beta_1$ and $\tau_1 = 1/\sigma_1^2$ as well as $\beta_2$ and $\tau_2 = 1/\sigma_2^2$:

$$ \label{eq:GLM-NG-prior-12}
\begin{split}
p(\beta_1,\tau_1) &= \mathcal{N}\left( \beta_1; \mu_0^{(1)}, \left( \tau_1 \Lambda_0^{(1)} \right)^{-1} \right) \cdot \mathrm{Gam}\left( \tau_1; a_0^{(1)}, b_0^{(1)} \right) \\
p(\beta_2,\tau_2) &= \mathcal{N}\left( \beta_2; \mu_0^{(2)}, \left( \tau_2 \Lambda_0^{(2)} \right)^{-1} \right) \cdot \mathrm{Gam}\left( \tau_2; a_0^{(2)}, b_0^{(2)} \right) \; .
\end{split}
$$

Then, the [log Bayes factor](/D/lbf) in favor of $m_1$ against $m_2$ is

$$ \label{eq:GLN-NG-LBF-12}
\begin{split}
\mathrm{LBF}_{12} &= \frac{1}{2} \log \frac{|P_1|}{|P_2|}  + \frac{1}{2} \log \frac{|\Lambda_0^{(1)}|}{|\Lambda_0^{(2)}|} - \frac{1}{2} \log \frac{|\Lambda_n^{(1)}|}{|\Lambda_n^{(2)}|} \\
&+ \log \frac{\Gamma\left( a_n^{(1)} \right)}{\Gamma\left( a_0^{(1)} \right)} + a_0^{(1)} \log b_0^{(1)} - a_n^{(1)} \log b_n^{(1)} \\
&+ \log \frac{\Gamma\left( a_n^{(2)} \right)}{\Gamma\left( a_0^{(2)} \right)} - a_0^{(2)} \log b_0^{(2)} + a_n^{(2)} \log b_n^{(2)}
\end{split}
$$

where $\mu_n^{(1)}, \Lambda_n^{(1)}, a_n^{(1)}, b_n^{(1)}$ and $\mu_n^{(2)}, \Lambda_n^{(2)}, a_n^{(2)}, b_n^{(2)}$ are the [posterior hyperparameters for Bayesian linear regression](/P/blr-post) for each of the two models which are functions of the design matrices, the precision matrices and the data vector.


**Proof:** For Bayesian linear regression with data vector $y$, design matrix $X$, precision matrix $P$ and [a normal-gamma prior distribution](/P/blr-prior) over $\beta$ and $\tau$, the [log model evidence is given by](/P/blr-lme)

$$ \label{eq:GLM-NG-LME}
\begin{split}
\log p(y|m) = \frac{1}{2} & \log |P| - \frac{n}{2} \log (2 \pi) + \frac{1}{2} \log |\Lambda_0| - \frac{1}{2} \log |\Lambda_n| + \\
& \log \Gamma(a_n) - \log \Gamma(a_0) + a_0 \log b_0 - a_n \log b_n
\end{split}
$$

where the [posterior hyperparameters are equal to](/P/blr-post)

$$ \label{eq:GLM-NG-post-par}
\begin{split}
\mu_n &= \Lambda_n^{-1} (X^\mathrm{T} P y + \Lambda_0 \mu_0) \\
\Lambda_n &= X^\mathrm{T} P X + \Lambda_0 \\
a_n &= a_0 + \frac{n}{2} \\
b_n &= b_0 + \frac{1}{2} (y^\mathrm{T} P y + \mu_0^\mathrm{T} \Lambda_0 \mu_0 - \mu_n^\mathrm{T} \Lambda_n \mu_n) \; .
\end{split}
$$

Thus, the [log model evidences](/D/lme) for $m_1$ and $m_2$ are given by:

$$ \label{eq:GLM-NG-LME-12}
\begin{split}
\mathrm{LME}(m_1) = \frac{1}{2} & \log |P_1| - \frac{n}{2} \log (2 \pi) + \frac{1}{2} \log |\Lambda_0^{(1)}| - \frac{1}{2} \log |\Lambda_n^{(1)}| + \\
& \log \Gamma(a_n^{(1)}) - \log \Gamma(a_0^{(1)}) + a_0^{(1)} \log b_0^{(1)} - a_n^{(1)} \log b_n^{(1)} \\
\mathrm{LME}(m_2) = \frac{1}{2} & \log |P_2| - \frac{n}{2} \log (2 \pi) + \frac{1}{2} \log |\Lambda_0^{(2)}| - \frac{1}{2} \log |\Lambda_n^{(2)}| + \\
& \log \Gamma(a_n^{(2)}) - \log \Gamma(a_0^{(2)}) + a_0^{(2)} \log b_0^{(2)} - a_n^{(2)} \log b_n^{(2)} \; .
\end{split}
$$

[The log Bayes factor is equal to the difference of two log model evidences](/P/lbf-lme):

$$ \label{eq:LBF-LME}
\mathrm{LBF}_{12} = \mathrm{LME}(m_1) - \mathrm{LME}(m_2) \; .
$$

Plugging \eqref{eq:GLM-NG-LME-12} into \eqref{eq:LBF-LME}, this gives:

$$ \label{eq:GLN-NG-LBF-12-s1}
\begin{split}
\mathrm{LBF}_{12} &= \frac{1}{2} \log |P_1| - \frac{1}{2} \log |P_2| \\
&+ \frac{1}{2} \log |\Lambda_0^{(1)}| - \frac{1}{2} \log |\Lambda_0^{(2)}| \\
&- \frac{1}{2} \log |\Lambda_n^{(1)}| + \frac{1}{2} \log |\Lambda_n^{(2)}| \\
&+ \log \Gamma\left( a_n^{(1)} \right) - \log \Gamma\left( a_0^{(1)} \right) + a_0^{(1)} \log b_0^{(1)} - a_n^{(1)} \log b_n^{(1)} \\
&- \log \Gamma\left( a_n^{(2)} \right) + \log \Gamma\left( a_0^{(2)} \right) - a_0^{(2)} \log b_0^{(2)} + a_n^{(2)} \log b_n^{(2)} \; .
\end{split}
$$

Applying $\log a - \log b = \log(a/b)$, we obtain:

$$ \label{eq:GLN-NG-LBF-12-s2}
\begin{split}
\mathrm{LBF}_{12} &= \frac{1}{2} \log \frac{|P_1|}{|P_2|}  + \frac{1}{2} \log \frac{|\Lambda_0^{(1)}|}{|\Lambda_0^{(2)}|} - \frac{1}{2} \log \frac{|\Lambda_n^{(1)}|}{|\Lambda_n^{(2)}|} \\
&+ \log \frac{\Gamma\left( a_n^{(1)} \right)}{\Gamma\left( a_0^{(1)} \right)} + a_0^{(1)} \log b_0^{(1)} - a_n^{(1)} \log b_n^{(1)} \\
&- \log \frac{\Gamma\left( a_n^{(2)} \right)}{\Gamma\left( a_0^{(2)} \right)} - a_0^{(2)} \log b_0^{(2)} + a_n^{(2)} \log b_n^{(2)} \; .
\end{split}
$$