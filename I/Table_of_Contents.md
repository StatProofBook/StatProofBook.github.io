---
layout: page
title: "Table of Contents"
---


**[Proofs](/P/-temp-)** are printed in **bold** – *[Definitions](/D/-temp-)* are set in *italics* <br>
Proofs by **[Number](/I/Proof_by_Number)** and **[Topic](/I/Proof_by_Topic)** – Definitions by *[Number](/I/Definition_by_Number)* and *[Topic](/I/Definition_by_Topic)* <br>


<section class="chapter" id="General Theorems">
<h3>General Theorems</h3>
</section>

1. Probability theory

   1.1. Probability distributions <br>
   &emsp;&ensp; 1.1.1. *[Probability mass function](/D/pmf)* <br>
   &emsp;&ensp; 1.1.2. *[Probability density function](/D/pdf)* <br>
   &emsp;&ensp; 1.1.3. *[Cumulative distribution function](/D/cdf)* <br>
   &emsp;&ensp; 1.1.4. *[Quantile function](/D/qf)* <br>
   &emsp;&ensp; 1.1.5. *[Moment-generating function](/D/mgf)* <br>
   
   1.2. Expected value <br>
   &emsp;&ensp; 1.2.1. *[Definition](/D/mean)* <br>
   &emsp;&ensp; 1.2.2. **[Non-negativity](/P/mean-nonneg)** <br>
   &emsp;&ensp; 1.2.3. **[Linearity](/P/mean-lin)** <br>
   &emsp;&ensp; 1.2.4. **[Monotonicity](/P/mean-mono)** <br>
   &emsp;&ensp; 1.2.5. **[(Non-)Multiplicitavity](/P/mean-mult)** <br>
   
   1.3. Variance <br>
   &emsp;&ensp; 1.3.1. *[Definition](/D/var)* <br>

2. Bayesian statistics

   2.1. Bayesian inference <br>
   &emsp;&ensp; 2.1.1. **[Bayes' theorem](/P/bayes-th)** <br>
   &emsp;&ensp; 2.1.2. **[Bayes' rule](/P/bayes-rule)** <br>

3. Estimation theory

   3.1. Point estimates <br>
   &emsp;&ensp; 3.1.1. **[Partition of the mean squared error into bias and variance](/P/mse-bnv)** <br>
   
   3.2. Interval estimates <br>
   &emsp;&ensp; 3.2.1. **[Construction of confidence intervals using Wilks' theorem](/P/ci-wilks)** <br>
   
4. Information theory

   4.1. Shannon entropy <br>
   &emsp;&ensp; 4.1.1. *[Definition](/D/ent)* <br>
   &emsp;&ensp; 4.1.2. **[Non-negativity](/P/ent-nonneg)** <br>
   &emsp;&ensp; 4.1.3. *[Conditional entropy](/D/ent-cond)* <br>
   &emsp;&ensp; 4.1.4. *[Joint entropy](/D/ent-joint)* <br>
   
   4.2. Differential entropy <br>
   &emsp;&ensp; 4.2.1. *[Definition](/D/dent)* <br>

   4.3. Discrete mutual information <br>
   &emsp;&ensp; 4.3.1. *[Definition](/D/mi)* <br>
   &emsp;&ensp; 4.3.2. **[Relation to marginal and conditional entropy](/P/dmi-mce)** <br>
   &emsp;&ensp; 4.3.3. **[Relation to marginal and joint entropy](/P/dmi-mje)** <br>
   &emsp;&ensp; 4.3.4. **[Relation to joint and conditional entropy](/P/dmi-jce)** <br>
   
   4.4. Continuous mutual information <br>
   &emsp;&ensp; 4.4.1. *[Definition](/D/mi)* <br>
   &emsp;&ensp; 4.4.2. **[Relation to marginal and conditional differential entropy](/P/cmi-mcde)** <br>
   &emsp;&ensp; 4.4.3. **[Relation to marginal and joint differential entropy](/P/cmi-mjde)** <br>
   &emsp;&ensp; 4.4.4. **[Relation to joint and conditional differential entropy](/P/cmi-jcde)** <br>


<section class="chapter" id="Probability Distributions">
<h3>Probability Distributions</h3>
</section>

1. Univariate discrete distributions

   1.1. Bernoulli distribution <br>
   &emsp;&ensp; 1.1.1. **[Mean](/P/bern-mean)** <br>

   1.2. Binomial distribution <br>
   &emsp;&ensp; 1.2.1. **[Mean](/P/bin-mean)** <br>

2. Multivariate discrete distributions

   2.1. Categorical distribution <br>
   &emsp;&ensp; 2.1.1. **[Mean](/P/cat-mean)** <br>

   2.2. Multinomial distribution <br>
   &emsp;&ensp; 2.2.1. **[Mean](/P/mult-mean)** <br>

3. Univariate continuous distributions

   3.1. Continuous uniform distribution <br>
   &emsp;&ensp; 3.1.1. *[Definition](/D/cuni)* <br>
   &emsp;&ensp; 3.1.2. **[Probability density function](/P/cuni-pdf)** <br>
   &emsp;&ensp; 3.1.3. **[Cumulative distribution function](/P/cuni-cdf)** <br>
   &emsp;&ensp; 3.1.4. **[Quantile function](/P/cuni-qf)** <br>

   3.2. Normal distribution <br>
   &emsp;&ensp; 3.2.1. *[Definition](/D/norm)* <br>
   &emsp;&ensp; 3.2.2. **[Probability density function](/P/norm-pdf)** <br>
   &emsp;&ensp; 3.2.3. **[Mean](/P/norm-mean)** <br>
   &emsp;&ensp; 3.2.4. **[Median](/P/norm-med)** <br>
   &emsp;&ensp; 3.2.5. **[Mode](/P/norm-mode)** <br>
   &emsp;&ensp; 3.2.6. **[Variance](/P/norm-var)** <br>

   3.3. Gamma distribution <br>
   &emsp;&ensp; 3.3.1. *[Definition](/D/gam)* <br>
   &emsp;&ensp; 3.3.2. **[Probability density function](/P/gam-pdf)** <br>

   3.4. Exponential distribution <br>
   &emsp;&ensp; 3.4.1. *[Definition](/D/exp)* <br>
   &emsp;&ensp; 3.4.2. **[Probability density function](/P/exp-pdf)** <br>
   &emsp;&ensp; 3.4.3. **[Cumulative distribution function](/P/exp-cdf)** <br>
   &emsp;&ensp; 3.4.4. **[Quantile function](/P/exp-qf)** <br>
   &emsp;&ensp; 3.4.5. **[Mean](/P/exp-mean)** <br>
   &emsp;&ensp; 3.4.6. **[Median](/P/exp-med)** <br>
   &emsp;&ensp; 3.4.7. **[Mode](/P/exp-mode)** <br>

4. Multivariate continuous distributions

   4.1. Multivariate normal distribution <br>
   &emsp;&ensp; 4.1.1. *[Definition](/D/mvn)* <br>
   &emsp;&ensp; 4.1.2. **[Probability density function](/P/mvn-pdf)** <br>
   &emsp;&ensp; 4.1.3. **[Linear transformation theorem](/P/mvn-ltt)** <br>
   &emsp;&ensp; 4.1.4. **[Marginal distributions](/P/mvn-marg)** <br>
   
   4.2. Normal-gamma distribution <br>
   &emsp;&ensp; 4.2.1. *[Definition](/D/ng)* <br>
   &emsp;&ensp; 4.2.2. **[Probability density function](/P/ng-pdf)** <br>
   &emsp;&ensp; 4.2.3. **[Kullback-Leibler divergence](/P/ng-kl)** <br>
   &emsp;&ensp; 4.2.4. **[Marginal distributions](/P/ng-marg)** <br>

5. Matrix-variate continuous distributions

   5.1. Matrix-normal distribution <br>
   &emsp;&ensp; 5.1.1. *[Definition](/D/matn)* <br>
   &emsp;&ensp; 5.1.2. **[Equivalence to multivariate normal distribution](/P/matn-mvn)** <br>


<section class="chapter" id="Statistical Models">
<h3>Statistical Models</h3>
</section>

1. Normal data

   1.1. Multiple linear regression <br>
   &emsp;&ensp; 1.1.1. **[Ordinary least squares (1)](/P/mlr-ols)** <br>
   &emsp;&ensp; 1.1.2. **[Ordinary least squares (2)](/P/mlr-ols2)** <br>
   
   1.2. Bayesian linear regression <br>
   &emsp;&ensp; 1.2.1. **[Conjugate prior distribution](/P/blr-prior)** <br>
   &emsp;&ensp; 1.2.2. **[Posterior distribution](/P/blr-post)** <br>
   &emsp;&ensp; 1.2.3. **[Log model evidence](/P/blr-lme)** <br>
   
   1.3. General linear model <br>
   &emsp;&ensp; 1.3.1. **[Maximum likelihood estimation](/P/glm-mle)** <br>

2. Poisson data

   2.1. Poisson-distributed data <br>
   &emsp;&ensp; 2.1.1. **[Maximum likelihood estimation](/P/poiss-mle)** <br>
   
   2.2. Poisson distribution with exposure values <br>
   &emsp;&ensp; 2.2.1. **[Conjugate prior distribution](/P/poissexp-prior)** <br>
   &emsp;&ensp; 2.2.2. **[Posterior distribution](/P/poissexp-post)** <br>
   &emsp;&ensp; 2.2.3. **[Log model evidence](/P/poissexp-lme)** <br>
   
3. Probability data

   3.1. Beta-distributed data <br>
   &emsp;&ensp; 3.1.1. **[Method of moments](/P/beta-mom)** <br>

4. Categorical data
   
   4.1. Binomial observations <br>
   &emsp;&ensp; 4.1.1. **[Conjugate prior distribution](/P/bin-prior)** <br>
   &emsp;&ensp; 4.1.2. **[Posterior distribution](/P/bin-post)** <br>
   &emsp;&ensp; 4.1.3. **[Log model evidence](/P/bin-lme)** <br>


<section class="chapter" id="Model Selection">
<h3>Model Selection</h3>
</section>

1. Goodness-of-fit measures

   1.1. Residual variance <br>
   &emsp;&ensp; 1.1.1. *[Definition](/D/resvar)* <br>
   &emsp;&ensp; 1.1.2. **[Maximum likelihood estimator is biased](/P/resvar-bias)** <br>
   &emsp;&ensp; 1.1.3. **[Construction of unbiased estimator](/P/resvar-unb)** <br>
   
   1.2. R-squared <br>
   &emsp;&ensp; 1.2.1. *[Definition](/D/rsq)* <br>
   &emsp;&ensp; 1.2.2. **[Derivation of R² and adjusted R²](/P/rsq-der)** <br>
   &emsp;&ensp; 1.2.3. **[Relationship to maximum log-likelihood](/P/rsq-mll)** <br>
   
   1.3. Signal-to-noise ratio
   &emsp;&ensp; 1.3.1. *[Definition](/D/snr)*
   &emsp;&ensp; 1.3.1. **[Relationship with R²](/P/snr-rsq)**

2. Classical information criteria

   2.1. Akaike information criterion <br>
   &emsp;&ensp; 2.1.1. *[Definition](/D/aic)* <br>
   
   2.2. Bayesian information criterion <br>
   &emsp;&ensp; 2.2.1. *[Definition](/D/bic)* <br>
   &emsp;&ensp; 2.2.2. **[Derivation](/P/bic-der)** <br>
   
   2.3. Deviance information criterion <br>
   &emsp;&ensp; 2.3.1. *[Definition](/D/dic)* <br>

3. Bayesian model selection

   3.1. Log model evidence <br>
   &emsp;&ensp; 3.1.1. *[Definition](/D/lme)* <br>
   &emsp;&ensp; 3.1.2. **[Derivation](/P/lme-der)** <br>
   &emsp;&ensp; 3.1.3. **[Partition into accuracy and complexity](/P/lme-anc)** <br>
