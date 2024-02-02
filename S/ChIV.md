---
layout: special
title: "Model Selection"
shortcut: "ChIV"
---


**Proofs** and *Definitions* on [Model Selection Criteria](/I/ToC#Model%20Selection) in the StatProofBook, as of 2023-12-23.

| Criterion | Definition | Derivation | Relationships | Other |
|:--------- |:---------- |:---------- |:------------- |:----- |
| **Goodness-of-<br>fit measures** |  |  |  |  |
| Residual variance | *[resvar](/D/resvar)* |  |  | **[resvar-bias](/P/resvar-bias)**<br>**[resvar-biasp](/P/resvar-biasp)**<br>**[resvar-unb](/P/resvar-unb)** |
| R-squared | *[rsq](/D/rsq)* | **[rsq-der](/P/rsq-der)** | **[rsq-mll](/P/rsq-mll)** |  |
| Signal-to-noise ratio | *[snr](/D/snr)* | | **[snr-rsq](/P/snr-rsq)** |  |
| **Classical infor-<br>mation criteria** |  |  |  |  |
| Akaike information criterion | *[aic](/D/aic)*<br>*[aicc](/D/aicc)* |  | **[aicc-aic](/P/aicc-aic)**<br>**[aicc-mll](/P/aicc-mll)** |  |
| Bayesian information criterion | *[bic](/D/bic)* | **[bic-der](/P/bic-der)** |  |  |
| Deviance information criterion | *[dev](/D/dev)*<br>*[dic](/D/dic)* |  |  |  |
| **Bayesian<br>model selection** |  |  |  |  |
| Model evidence | *[me](/D/me)*<br>*[lme](/D/lme)*<br>*[uplme](/D/uplme)*<br>*[cvlme](/D/cvlme)*<br>*[eblme](/D/eblme)*<br>*[vblme](/D/vblme)* | **[me-der](/P/me-der)**<br>**[lme-der](/P/lme-der)** | *[lme-pnp](/P/lme-pnp)** | **[lme-anc](/P/lme-anc)**<br>**[lme-mean](/P/lme-mean)** |
| Family evidence | *[fe](/D/fe)*<br>*[lfe](/D/lfe)* | **[fe-der](/P/fe-der)**<br>**[lfe-der](/P/lfe-der)** | **[lfe-lme](/P/lfe-lme)** | **[lfe-approx](/P/lfe-approx)** |
| Bayes factor | *[bf](/D/bf)*<br>*[lbf](/D/lbf)* | **[lbf-der](/P/lbf-der)** | **[lbf-lme](/P/lbf-lme)** | **[bf-trans](/P/bf-trans)**<br>**[bf-sddr](/P/bf-sddr)**<br>**[bf-ep](/P/bf-ep)** |
| Posterior model probability | *[pmp](/D/pmp)* | **[pmp-der](/P/pmp-der)** | **[pmp-bf](/P/pmp-bf)**<br>**[pmp-lbf](/P/pmp-lbf)**<br>**[pmp-lme](/P/pmp-lme)** |  |
| Bayesian model averaging | *[bma](/D/bma)* | **[bma-der](/P/bma-der)** | **[bma-lme](/P/bma-lme)** |  |