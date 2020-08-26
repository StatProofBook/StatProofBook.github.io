---
layout: page
title: "Special: Statistical Models"
---


Proofs and Definitions on [Statistical Models](/I/Table_of_Contents#Statistical%20Models) in the StatProofBook, as of 2020-08-26.

| Model | Definition | Estimation | Maximum<br>likelihood<br>estimation | Conjugate<br>prior | Posterior<br>distribution | Log<br>model<br>evidence | Other |
|:----- |:---------- |:---------- |:----------------------------------- |:------------------------------- |:------------------------- |:--------------------- |:----- |
| **Univariate<br>normal data** |  |  |  |  |  |  |  |
| Multiple linear regression | *[mlr](/D/mlr)* | **[mlr-ols](/P/mlr-ols)**<br>**[mlr-wls](/P/mlr-wls)** | **[mlr-mle](/P/mlr-mle)** |  |  |  | **[mlr-pss](/P/mlr-pss)**<br>**[mlr-mat](/P/mlr-mat)**<br>**[mlr-idem](/P/mlr-idem)** |
| Bayesian linear regression |  |  |  | **[blr-prior](/P/blr-prior)** | **[blr-post](/P/blr-post)** | **[blr-lme](/P/blr-lme)** | **[blr-pp](/P/blr-pp)**<br>**[blr-pcr](/P/blr-pcr)** |
| **Multivariate<br>normal data** |  |  |  |  |  |  |  |
| General linear model | *[glm](/D/mlr)* | **[glm-ols](/P/glm-ols)**<br>**[glm-wls](/P/glm-wls)** | **[glm-mle](/P/glm-mle)** |  |  |  |  |
| **Poisson data** |  |  |  |  |  |  |  |
| Poisson-distributed data | *[poiss](/D/poiss-data)* |  | **[poiss-mle](/P/poiss-mle)** |  |  |  |  |
| Poisson distribution with exposure values | *[poissexp](/D/poissexp)* |  |  | **[poissexp-prior](/P/poissexp-prior)** | **[poissexp-post](/P/poissexp-post)** | **[poissexp-lme](/P/poissexp-lme)** |  |
| **Probability data** |  |  |  |  |  |  |  |
| Beta-distributed data | *[beta](/D/beta-data)* | **[beta-mom](/P/beta-mom)** |  |  |  |  |  |
| Logistic regression | *[logreg](/D/logreg)* |  |  |  |  |  | **[logreg-pnlo](/P/logreg-pnlo)**<br>**[logreg-lonp](/P/logreg-lonp)** |
| **Categorical data** |  |  |  |  |  |  |  |
| Binomial observations | *[bin](/D/bin-data)* |  |  | **[bin-prior](/P/bin-prior)** | **[bin-post](/P/bin-post)** | **[bin-lme](/P/bin-lme)** |  |
| Multinomial observations | *[mult](/D/mult-data)* |  |  | **[mult-prior](/P/mult-prior)** | **[mult-post](/P/mult-post)** | **[mult-lme](/P/mult-lme)** |  |