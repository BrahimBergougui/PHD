# Five-part summaries of the portfolio papers

Framework used for every paper:

1. **Lead statement.** The problem the paper addresses inside its theme.
2. **Research question / hypothesis.** The specific gap it fills.
3. **Methods & data.** One or two sentences.
4. **Key findings.** The results that matter for the thesis narrative.
5. **Contribution.** How the paper advances the theme and the overall argument.

Theme mapping follows the Part Two list: Theme 1, Technological Innovation and Environmental Quality (P01-P13); Theme 2, Environmental Inequality and Technological Justice (P14-P18); Theme 3, Energy Security in the Digital Age (P19-P25).

A short list of points to verify against the published versions appears at the end. It covers only places where the extraction notes in `summaries/*.md` flag a conflict that touches a statement I would otherwise make here.

---

## Theme 1. Technological Innovation and Environmental Quality (P01-P13)

### P01. Energy research budgets and the load capacity factor

Bergougui, B., Boudjana, R. H., Mehibel, S., Ben-Salha, O., and Zambrano-Monserrate, M. A. (2025). *Journal of Environmental Management* 395, 127823.

1. **Lead statement.** The paper asks whether public energy research improves environmental quality, and whether the composition of that research matters as much as its size. Within Theme 1 it opens the sequence at the financing stage, before any funded technology is adopted.
2. **Research question / hypothesis.** It examines how total, clean and fossil energy RD&D budgets affect the load capacity factor (LCF). It also tests whether the effects vary across countries and along the joint distribution of spending and ecological position, a question that mean-based, symmetric designs cannot separate.
3. **Methods & data.** Eight advanced economies with contrasting industrial and ecological profiles, 1990 to 2023, with IEA RD&D budgets and the Global Footprint Network LCF. Estimation uses quantile-on-quantile Granger causality, multivariate quantile-on-quantile kernel-based regularised least squares (MQQKRLS), and MQQR as a robustness check.
4. **Key findings.** Composition matters more than volume. Effects are non-monotonic and country-specific: clean research performs best where innovation capacity and the energy system are mature, and fossil research delivers limited and localised gains. Countries already high in the LCF distribution gain least from additional spending.
5. **Contribution.** The paper sets the first recurring regularity of the thesis, that technology effects are asymmetric and position dependent, at the earliest point of the innovation chain. It shows that only disaggregated budgets reveal which research directions pay off, and it hands the sequence forward to what happens once funded technologies are deployed.

### P02. Artificial intelligence, institutional adaptability, and skills

Bergougui, B. (2025). *Sustainable Development*, early view.

1. **Lead statement.** The paper asks whether artificial intelligence (AI) advances environmental sustainability, and under which institutional and labour-market conditions it does so. It moves Theme 1 from research budgets to the deployment of a general-purpose technology whose environmental sign is contested.
2. **Research question / hypothesis.** Three hypotheses are tested: AI patenting improves ecological sustainability; AI-induced skill-biased and routine-biased labour transformation contributes to that improvement; and institutional quality moderates it, with stronger effects in adaptable economies. The paper fills the gap left by AI studies that are either institution-blind or undifferentiated in their technology measure.
3. **Methods & data.** A 29-country panel, 2005 to 2024, measuring AI with PCT patent filings from the WIPO AI Index and sustainability with the LCF. The design combines two-way fixed effects with an instrument built from geographic distance to the United States and lagged United States AI patenting. GMM and FMOLS provide checks, and interaction models test labour structure and three institutional indexes.
4. **Key findings.** Higher AI activity is associated with a higher LCF, and the result survives instrumental-variable and robustness work. The effect strengthens with legal adaptability, labour market efficiency, regulatory quality and the share of high-skill and non-routine work. It is significant in economies close to the AI frontier and in high fossil-fuel-reliant economies.
5. **Contribution.** The paper establishes institutional conditioning as the second pillar of the thesis argument and separates AI capability from AI deployment. It places absorptive capacity, governance flexibility and skills ahead of technology adoption in the causal story, and it leaves the mechanisms of transmission to be traced directly in P03.

### P03. AI patents and decarbonisation pathways

Bergougui, B. (2025). *Technology in Society* 83, 103029.

1. **Lead statement.** The paper asks whether AI innovation lowers carbon emissions and through which channels, at a time when much of the literature proxies AI with industrial robots. It supplies the mechanism layer that P02 could only infer from interactions.
2. **Research question / hypothesis.** Four hypotheses are tested: AI patents accelerate decarbonisation; energy efficiency carries the effect; skill-biased and routine-biased technological shifts deepen it; and adaptable institutions strengthen it. The gap is the absence of tested mechanisms and the use of robots as a stand-in for AI knowledge.
3. **Methods & data.** A 29-economy panel, 2005 to 2023, with carbon intensity of output as the outcome and PCT AI patents as the regressor. The design uses two-way fixed effects, IV-2SLS with geographic and breakthrough-year instruments, GMM, propensity score matching and Oster stability checks, plus mechanism regressions on energy intensity, per capita emissions, labour structure and institutions.
4. **Key findings.** AI patenting is associated with lower carbon intensity, with the largest contribution from energy-management patents. The channels run through lower primary energy intensity and lower per capita emissions, a labour-market shift towards high-skill and non-routine tasks, and institutional adaptability. Effects are larger in lower-income economies and in countries closer to the AI frontier.
5. **Contribution.** The paper makes the AI result conditional and mechanism-based, which is what the thesis needs to move from association to explanation. It also shows that not all AI is alike, since energy-management applications carry the effect, which supports the disaggregation logic used across the portfolio and prepares the shift to embodied automation in P04.

### P04. Industrial robots and ecological quality in the G7

Bergougui, B. (2025). *Technology in Society* 83, 103021.

1. **Lead statement.** The paper asks whether the environmental effect of AI adoption changes as automation matures, and whether that effect differs across the G7. It turns from AI invention to the physical deployment of robots in production.
2. **Research question / hypothesis.** H1 expects a significant but weak positive effect at early adoption stages, and H2 expects a significant and strong positive effect at mature stages. The gap is the assumption of a single, monotonic AI-environment relationship in leading economies.
3. **Methods & data.** Seven G7 economies estimated country by country from January 2000 to December 2019, with monthly series built from annual data. Industrial robot stocks serve as the AI proxy and the LCF as the ecological outcome, estimated with quantile-on-quantile regression supported by nonlinearity, unit root and quantile cointegration tests and IVMQR and KRLS checks.
4. **Key findings.** The effect of automation is stage dependent and country specific. Early adoption shows weak or modest gains, the transition phase is variable, and mature adoption produces the strongest improvements, with diminishing returns at the highest quantiles. Country paths differ, with U-shaped, N-shaped and W-shaped profiles, and a brief negative range appearing only in France.
5. **Contribution.** The paper establishes adoption-stage dependence as a third regularity alongside asymmetry and institutional conditioning. It documents the pattern without explaining it, which is exactly the question P06 takes up through mechanisms and thresholds, and it confirms that distributional position matters at the level of the adopting economy.

### P05. Environmental governance and resource overuse in the OECD

Bergougui, B., and Satrovic, E. (2025). *Ecological Informatics* 87, 103093.

1. **Lead statement.** The paper asks whether environmental governance can restrain the ecological damage caused by excessive natural resource use in advanced economies. It introduces institutions as moderators of a resource-driven pressure rather than as additional controls.
2. **Research question / hypothesis.** It tests how excess resource use affects eco-efficiency, how the energy transition, research spending and trade contribute, and whether environmental policy stringency weakens the resource-use effect, especially where eco-efficiency is low. The gap is the untested moderating role of governance in this setting.
3. **Methods & data.** Nine OECD economies, 1997 to 2020, annual and balanced, with overall and services eco-efficiency as outcomes. After second-generation unit root and cointegration tests, method of moments quantile regression estimates an augmented environmental Kuznets specification with an interaction between environmental policy stringency and resource overuse.
4. **Key findings.** Excess resource use reduces eco-efficiency in a nonlinear pattern, with a positive quadratic term indicating a turning point. Energy transition, research and development, and trade all raise eco-efficiency, and environmental governance both improves eco-efficiency directly and offsets part of the resource-use damage. The moderation is strongest in countries with the lowest eco-efficiency.
5. **Contribution.** The paper shows that institutions act as moderators of an environmental damage channel, not merely as drivers, and that their value is highest where environmental performance is weakest. It gives Theme 1 its clearest institutional-conditioning result before P06, and it prepares the mechanism analysis that follows.

### P06. When do robots go green: mechanisms, thresholds, spillovers

Bergougui, B., and Sulimany, H. G. H. (2026). *Business Strategy and the Environment*, early view.

1. **Lead statement.** The paper asks through which mechanisms, under which structural conditions and where in space industrial robotics improves ecological capacity. It provides the explanation that P04 deliberately left open.
2. **Research question / hypothesis.** Five questions are posed about robotics and biocapacity. They cover the direct effect, mediation through government flexibility and technological progress, thresholds in industrial upgrading, and spillovers from proximity to Japan. A fifth question asks whether trade openness and global value chain participation condition the outcome. The gap is the absence of tested channels and regimes in this literature.
3. **Methods & data.** Fifty countries, 2000 to 2024, with biocapacity per capita as the outcome and robot density as the regressor. The design combines two-way fixed effects, IV-GMM and lagged and winsorised checks, mediation analysis, Hansen threshold regression on industrial structure, and sample splits by distance to Japan and by trade and value chain integration.
4. **Key findings.** Robotics raises biocapacity, and the gain is transmitted mainly through green-biased technological progress, with government flexibility a secondary channel. The relationship follows a J-curve across three upgrading regimes: positive in nascent structures, negative in transition, and strongly positive in advanced structures. Effects are positive near Japan, positive in highly integrated economies, and absent or negative in low-income and low-integration settings.
5. **Contribution.** The paper converts the stage dependence of P04 into named mechanisms and measurable regimes, and it shows that the same technology can harm or help according to industrial and institutional position. It also adds geographic diffusion to the thesis, which matters for the claim that benefits concentrate rather than spread on their own.

### P07. Sectoral foreign direct investment and emissions in MENA

Bergougui, B., and Murshed, S. M. (2026). *Natural Resources Forum* 50, 1299-1319.

1. **Lead statement.** The paper asks whether foreign direct investment affects emissions in the same way across sectors, in a region where investment is concentrated in extraction. It brings the theme from global panels to a regional setting and from aggregate investment to its components.
2. **Research question / hypothesis.** It tests the pollution haven and pollution halo hypotheses at aggregate and sectoral levels for resource, manufacturing and services investment, across total and sectoral emissions. The gap is that aggregate FDI measures hide components that pull in opposite directions.
3. **Methods & data.** Thirteen MENA countries, 1990 to 2022, with annual data averaged into four-year intervals and missing values filled by multiple imputation. System GMM estimates sixteen regressions that cross four FDI measures with four emission measures.
4. **Key findings.** Total FDI lowers total emissions and tertiary emissions, which supports the halo view, but it raises secondary-sector emissions. Resource extraction and manufacturing investment raise emissions in every sector, while services investment lowers them, including in other sectors. Aggregate investment therefore conceals the sectoral split.
5. **Contribution.** The paper supplies the disaggregation result that Theme 1 needed on the investment channel, and it shows that technology and practices entering through services differ from those entering through extraction. It also sets the regional stage for the Algerian time-series block that follows, since Algeria is exposed to the harmful channel and weak in the beneficial one.

### P08. Fossil energy, renewable energy and innovation in Algeria

Bergougui, B. (2024). *Energy Strategy Reviews* 51, 101281.

1. **Lead statement.** The paper asks whether increases and decreases in technological innovation, fossil energy and renewable energy have the same effect on Algerian CO2 emissions. It opens the country-level block of Theme 1 and shows what a single-country asymmetric design adds to the global evidence.
2. **Research question / hypothesis.** Three hypotheses are tested: positive innovation shocks reduce emissions and negative shocks raise them; positive renewable shocks reduce emissions; and fossil energy shocks raise them. The gap is the symmetric treatment of drivers in a country undergoing rapid structural change.
3. **Methods & data.** Algeria, 1980Q1 to 2021Q4, with quarterly series obtained from annual data. The design applies nonlinearity and break unit root tests, then NARDL for long-run asymmetry, with QARDL quantile estimates and bootstrap asymmetric causality as checks.
4. **Key findings.** Positive innovation shocks reduce emissions while negative shocks raise them, and renewable energy reduces emissions mainly when it expands. Both directions of fossil energy use raise emissions, and the negative shock has almost twice the effect of the positive one. The quantile results place the strongest effects at middle and upper quantiles of the emission distribution, and long-run asymmetry is confirmed for all three drivers.
5. **Contribution.** The paper shows that the asymmetry established in cross-country work also holds inside a resource-dependent economy, and that deterioration can cost more than improvement gains at this level of aggregation. Its broad innovation measure leaves open which technologies do the work, which is the question P09 answers with green patents.

### P09. Green technology patents and Algeria's ecological footprint

Bergougui, B., and Aldawsari, M. I. (2024). *Journal of Environmental Management* 355, 120426.

1. **Lead statement.** The paper isolates green technology from general innovation and asks whether it reduces ecological pressure in Algeria. It replaces the aggregate patent count of P08 with patents that are environmentally relevant.
2. **Research question / hypothesis.** It tests whether positive and negative shocks in green technology patents, economic growth and energy consumption have asymmetric effects on the ecological footprint. The gap is that total patent counts mix clean and dirty invention, which blurs the direction of the innovation effect.
3. **Methods & data.** Algeria, 1990Q1 to 2022Q4, quarterly, with the ecological footprint as the outcome and OECD green technology patents as the regressor. After nonlinearity and break unit root tests, NARDL estimates long-run and short-run asymmetry, with FMOLS, DOLS and CCR checks and asymmetric causality tests.
4. **Key findings.** Both directions of green patenting reduce the ecological footprint, and the positive shock is larger. Economic growth raises the footprint when it accelerates but has no significant effect when it slows. Energy consumption raises the footprint in both directions. Short-run results show that only the positive green technology shock is significant, and the Wald test confirms long-run asymmetry.
5. **Contribution.** The paper confirms that measurement choice matters: green patents behave differently from total patents, which supports the disaggregation argument of the thesis. It also extends the outcome beyond CO2 to the ecological footprint, showing that the asymmetry result is not an artefact of one indicator.

### P10. Policy uncertainty, green technology and the EKC in Algeria

Bergougui, B., Mehibel, S., and Boudjana, R. H. (2024). *Journal of Environmental Management* 360, 121172.

1. **Lead statement.** The paper asks how economic policy uncertainty and green technology affect emissions in Algeria, and whether the environmental Kuznets curve holds there. It adds the policy environment to the technology story developed in P08 and P09.
2. **Research question / hypothesis.** It tests whether positive uncertainty shocks help or hinder environmental progress, whether positive green technology shocks reduce emissions, and whether the income-emissions relationship supports the EKC. The gap is the absent evidence on asymmetric uncertainty effects and green technology in a single resource-dependent economy.
3. **Methods & data.** Algeria, 1980Q1 to 2022Q4, quarterly, with the World Uncertainty Index and environmental patents as the main variables. The design uses BDS and Fourier unit root tests, Fourier-NARDL with bounds testing, asymmetric and gradual-shift causality tests, and FMOLS, DOLS and CCR checks.
4. **Key findings.** Positive uncertainty shocks reduce emissions, while negative shocks have no significant effect. Positive green technology shocks reduce emissions, again with no significant effect from negative shocks. Income raises emissions and its square lowers them, which supports the EKC, and the asymmetry tests confirm that the two shock directions are not mirror images.
5. **Contribution.** The paper shows that the direction of change carries the result, since only improvements move emissions in this setting. It also places policy uncertainty in the sequence as a condition on green investment, and it leaves the efficiency channels through which green technology works to be examined in P11.

### P11. Material efficiency, energy productivity and environmental technology

Bergougui, B. (2024). *Energy Strategy Reviews* 55, 101541.

1. **Lead statement.** The paper asks whether material resource efficiency, energy productivity and environmental technology improve Algeria's environmental performance, and whether gains and losses act alike. It moves the country block from innovation counts to efficiency and productivity.
2. **Research question / hypothesis.** The stated hypothesis is that material resource efficiency, energy productivity and environmental technology are positive predictors of environmental sustainability. The gap is the treatment of these variables with linear, symmetric methods and their near absence from the Algerian evidence.
3. **Methods & data.** Algeria, 1990Q1 to 2022Q4, quarterly, with CO2 emissions as the outcome and the ecological footprint as an alternative. The design applies nonlinearity and break unit tests, then NARDL with a Fourier cointegration check, supported by FMOLS, CCR and subsample specifications.
4. **Key findings.** Improvements in material efficiency, energy productivity and environmental technology all reduce emissions, and improvements matter more than equivalent deteriorations. Energy productivity is the strongest of the three, and its deterioration has no significant effect. Trade openness lowers emissions when it rises and raises them when it falls, while growth raises emissions in both directions.
5. **Contribution.** The paper shows that efficiency and productivity transmit the technology effect, which supports the mechanism logic of P03 at country level. It also confirms the asymmetry rule in a second Algerian setting, and it raises the financial question that P12 addresses, namely who funds these efficiency gains.

### P12. Green technology, financial development and the ecological footprint

Bergougui, B. (2024). *Sustainable Cities and Society* 112, 105621.

1. **Lead statement.** The paper asks whether financial development harms Algeria's environment and whether green technology changes that relationship. It introduces the funding side of the transition into the country block.
2. **Research question / hypothesis.** Three questions are posed: the ecological effect of green technology, the effect of financial development, and whether green technology moderates the finance-environment link. The gap is that financial depth is usually treated as environmentally neutral or beneficial, without a technology condition.
3. **Methods & data.** Algeria, 1990Q1 to 2021Q4, quarterly, with the ecological footprint as the outcome and environment-related patents and a financial development index as regressors. A Fourier ARDL bounds approach, chosen for its tolerance of mixed integration orders and smooth structural change, estimates the long run, with Toda-Yamamoto causality tests.
4. **Key findings.** Green technology reduces the ecological footprint, while financial development raises it. The interaction between the two is negative, so green technology weakens the harmful finance effect. Causality runs from both green technology and financial development to the footprint.
5. **Contribution.** The paper shows that finance without green technology adds ecological pressure, which makes absorptive and directional conditions central rather than incidental. It also shows that structural-break-aware methods preserve the asymmetric findings of the earlier Algerian studies, and it hands the resource base to P13.

### P13. Aggregate and disaggregated natural resource rents in Algeria

Meziane, S., and Bergougui, B. (2026). *Resources Policy* 113, 105830.

1. **Lead statement.** The paper asks whether different natural resource rents have different environmental effects in Algeria. It closes Theme 1 by testing whether resource dependence can be treated as one variable.
2. **Research question / hypothesis.** The aim is to estimate the asymmetric long-run effects of aggregate rents and of oil, gas, mineral, coal and forest rents on the ecological footprint, controlling for income and energy consumption. The gap is the aggregate treatment of rents, which mixes point resources with diffuse ones.
3. **Methods & data.** Algeria, 1970Q1 to 2022Q4, quarterly, with the ecological footprint as the outcome. Normality, nonlinearity and break unit root tests precede six NARDL models estimated on aggregate rents and on each rent type, with quantile regression and spectral causality checks.
4. **Key findings.** Aggregate rents and oil rents follow an asymmetric pattern: positive shocks raise the footprint and negative shocks lower it. Gas and mineral rents raise the footprint in both directions, coal has no clear effect, and forest rents are sharply asymmetric, with positive shocks raising pressure and negative shocks reducing it. Quantile estimates show the pressures are strongest in the lower and middle ranges of the footprint distribution, and long-run asymmetry holds in all six models.
5. **Contribution.** The paper completes the disaggregation argument for Theme 1 and identifies a resource asymmetry trap, in which rents that could finance transition also drive degradation. Because it shows that a hydrocarbon economy cannot exit the problem through technology alone, it sets up the energy-composition question that Theme 3 examines for Algeria in P25.

---

## Theme 2. Environmental Inequality and Technological Justice (P14-P18)

### P14. Eco-innovation and emissions inequality in the G7

Bergougui, B., Doğan, B., Cobbold, E. Y., Soltani, H., Sulimany, H. G. H., and Ebrahim, E. E. M. (2025). *Sustainable Development*, early view.

1. **Lead statement.** The paper asks who benefits from green technology, by testing whether eco-innovation narrows or widens income-based emissions inequality in the G7. It opens Theme 2 by re-examining a technology that Theme 1 treated as environmentally beneficial.
2. **Research question / hypothesis.** It examines the asymmetric effects of comprehensive eco-innovation and process eco-innovation on emissions inequality across the quantiles of that distribution. The gap is that innovation is studied for its effect on aggregate emissions, not on who emits.
3. **Methods & data.** The G7, 1990 to 2023, with emissions inequality measured as the per capita emissions of the wealthiest tenth from the World Inequality Database. Positive and negative shocks in each innovation type are estimated with method of moments quantile regression, with DOLS, FMOLS and CCR checks and Granger non-causality tests.
4. **Key findings.** Positive shocks to eco-innovation reduce emissions inequality, and the reductions are larger where inequality is already low, weakening towards the top of the distribution. Negative shocks to comprehensive eco-innovation reduce inequality at low quantiles and raise it at high quantiles, while declines in process eco-innovation raise inequality at every quantile. Growth and globalisation widen inequality, and economic complexity and trade narrow it.
5. **Contribution.** The paper establishes that green technology carries a distributional signature rather than a uniform equalising effect, and that the type of innovation and the position of the country decide who gains. It supplies the distributional regularity that Theme 2 builds on and passes to P15 the question of whether frontier digital technology behaves differently.

### P15. Artificial intelligence and environmental inequality

Bergougui, B. (2025). *Borsa Istanbul Review* 25, 1316-1336.

1. **Lead statement.** The paper asks whether the adoption of industrial robotics reduces or widens carbon emissions inequality in the leading automation economies. It brings the AI question of Theme 1 into the distributional frame of Theme 2.
2. **Research question / hypothesis.** H1 expects early adoption to raise emissions inequality, and H2 expects mature adoption to reduce it. The gap is that AI is assessed for its aggregate environmental effect while its distributional effect is untested.
3. **Methods & data.** Ten robotics-driven economies, 2000 to 2023, with monthly series and country-by-country estimation. Multivariate quantile-on-quantile regression maps the joint distribution of robot density and emissions inequality, with IVQR checks using lagged AI adoption.
4. **Key findings.** The effect is stage dependent and country specific. In most European economies early adoption raises inequality, the middle range stabilises it, and advanced integration reduces it, most clearly in Denmark, France and Sweden. Germany shows increases at all quantiles, Japan and Singapore move from increases to reductions, South Korea increases throughout, and China and the United States alternate. About seventy percent of the countries show reductions once adoption is advanced.
5. **Contribution.** The paper shows that the adoption-stage pattern found for aggregate outcomes in P04 reappears when the outcome is distributional, which suggests it is a property of the technology rather than of the indicator. It also demonstrates that diffusion alone does not equalise, since access conditions decide who captures the gains, and it hands the driver role to income distribution in P16.

### P16. Income inequality and climate inequality in the largest emitters

Bergougui, B., Ben-Salha, O., and Murshed, S. M. (2025). *Journal of Cleaner Production* 513, 145666.

1. **Lead statement.** The paper asks whether income inequality drives carbon emissions inequality in the six largest emitting nations. It shifts the driver of Theme 2 from technology to economic distribution.
2. **Research question / hypothesis.** It examines how income inequality affects emissions inequality across quantiles, countries and time horizons. The gap is that income has usually entered emissions models as a control, and its distributional effect has not been tested directly.
3. **Methods & data.** China, the United States, India, Russia, Japan and Germany, January 1980 to December 2023, monthly series, estimated country by country. Multivariate quantile-on-quantile regression and wavelet quantile regression trace quantile and horizon effects, with IV quantile regression, multivariate quantile regression, KRLS and quantile Granger causality as checks.
4. **Key findings.** The relationship is nonlinear and differs by country: China and Russia display U-shaped patterns, India a W-shaped one, and Japan and the United States show threshold transitions from negative to positive effects. Germany reduces emissions inequality in the middle quantiles but raises it at the top. Over time, the United States reverses sign from negative in the short run to positive in the long run, while China, India, Japan and Russia amplify the effect as the horizon lengthens.
5. **Contribution.** The paper establishes income distribution as a driver in its own right rather than a background condition, and it shows that the same income level can produce opposite distributional outcomes depending on position. It leaves open whether governance explains those differences, which is the question P17 takes up.

### P17. Institutional quality, income and emissions inequality

Bergougui, B., Boudjana, R. H., Mehibel, S., and Zambrano-Monserrate, M. A. (2024). *Journal of Cleaner Production* 483, 144215.

1. **Lead statement.** The paper asks whether institutional quality can reduce carbon emissions inequality and whether income widens it, in the six major emitters. It brings the institutional pillar of the thesis into the distributional outcome.
2. **Research question / hypothesis.** It examines the asymmetric effects of institutional quality and income on emissions inequality, and the interaction between them. The gap is that institutional quality had been related to total emissions but not to their distribution.
3. **Methods & data.** Six emitters, 1995Q1 to 2019Q3, quarterly, with emissions inequality from the World Inequality Database and an institutional index built from the worldwide governance indicators. Quantile-on-quantile regression carries the estimation, with quantile Granger causality, quantile regression and KRLS checks.
4. **Key findings.** Improvements in institutional quality generally reduce emissions inequality, and the reductions are largest where governance starts weak, with diminishing returns at higher levels. Income shows an inverted U: growth widens emissions inequality at first and moderates it later. Country patterns vary, with the United States, Germany and Japan showing transitions between regimes.
5. **Contribution.** The paper reproduces for a distributional outcome the pattern found in P05 for eco-efficiency: institutions matter most where they are weakest. It shows that who captures the gains from growth depends on governance, and it leaves the joint operation of technology, structure and external shocks to P18.

### P18. Environmental technology, economic complexity and geopolitical risk

Bergougui, B., Doğan, B., Ghosh, S., and Ayad, H. (2024). *Environment, Development and Sustainability*, online first.

1. **Lead statement.** The paper asks how environmental technology, economic complexity, geopolitical risk and resource rents shape emissions inequality when they operate together. It closes Theme 2 by treating the distribution of emissions as the outcome of a system rather than of single drivers.
2. **Research question / hypothesis.** The main question is how environmental technology mitigates emissions inequality, with geopolitical risk, economic complexity, resource rents and growth as further influences. The gap is the static, single-equation treatment of drivers that also affect each other.
3. **Methods & data.** A panel of 41 developed and developing countries, 1990 to 2020, with emissions inequality measured as the per capita emissions of the wealthiest tenth. A GMM panel vector autoregression with impulse response functions and heterogeneous causality tests handles endogeneity and feedback.
4. **Key findings.** Environmental technology reduces emissions inequality, and economic complexity reduces it further. Geopolitical risk, natural resource rents and income growth all raise it. A shock to environmental technology produces an initial inverse response in inequality followed by oscillating negative responses, and the causality test supports a unidirectional path from technology to inequality.
5. **Contribution.** The paper widens the technology result of P14 and P15 to 41 countries and adds conditions that technology policy cannot reach on its own, namely geopolitical exposure and resource dependence. It completes the movement of Theme 2 from technology to structure, and it returns to technology with the distributional and institutional findings in hand.

---

## Theme 3. Energy Security in the Digital Age (P19-P25)

### P19. The digital economy and the energy transition in Belt and Road economies

Doğan, B., Khalfaoui, R., Bergougui, B., and Ghosh, S. (2025). *Research in International Business and Finance* 76, 102837.

1. **Lead statement.** The paper asks whether the digital economy supports the energy transition and renewable energy innovation in Belt and Road economies. It opens Theme 3 by treating digitalisation as an enabling condition whose effect may vary across countries.
2. **Research question / hypothesis.** Three hypotheses are tested: renewable innovation and the digital economy jointly advance the energy transition; the transition in turn drives renewable innovation; and both relationships differ across the quantile distribution. The gap is the reliance on Chinese provincial or advanced-economy evidence.
3. **Methods & data.** Forty Belt and Road countries, 1995 to 2020, with an energy transition index and a digital economy index built by entropy weighting. Renewable innovation is split into solar, wind, biomass and geothermal patent classes, and method of moments quantile regression estimates two models, one for the transition and one for innovation.
4. **Key findings.** Renewable innovation and the digital economy both raise the energy transition across all quantiles, with the effects growing as the transition advances. The transition drives renewable innovation only from the middle quantiles upward. Income raises innovation but reduces the transition index, and institutional quality reduces innovation in this sample.
5. **Contribution.** The paper disaggregates renewable innovation by technology class and confirms that digitalisation supports transition speed. It stops short of security, since a faster transition need not make an energy system safer, and that distinction becomes the object of P20.

### P20. Energy transition, technology and digitalisation in Chinese cities

Bergougui, B., Murshed, S. M., Shahbaz, M., Zambrano-Monserrate, M. A., Samour, A., and Aldawsari, M. I. (2025). *Renewable Energy* 238, 121883.

1. **Lead statement.** The paper asks whether the energy transition, environmental technology and digitalisation improve energy security, measured at the level of Chinese cities. It makes energy security itself the outcome rather than transition speed.
2. **Research question / hypothesis.** It examines the asymmetric effects of positive and negative shocks in the three drivers across the distribution of energy security. The gap is the absence of city-level evidence and of any test of whether improvements and deteriorations act alike.
3. **Methods & data.** A panel of 275 Chinese cities, 2007 to 2019, with a composite energy security index built by entropy weighting and drivers split into positive and negative partial sums. Method of moments quantile regression, preceded by cross-sectional dependence, slope heterogeneity, unit root and cointegration tests, with Dumitrescu-Hurlin causality.
4. **Key findings.** Positive transition shocks raise security only in cities with moderate to high baseline security, while negative shocks raise it at the bottom of the distribution and lower it at the top. Positive digitalisation shocks raise security from the middle quantiles upward, and negative digitalisation shocks have little effect. Positive environmental technology shocks raise security except at the very bottom, and negative shocks reduce it at the bottom and raise it higher up.
5. **Contribution.** The paper shows that the digital and transition effects are asymmetric and depend on where a city already stands, which is the positional dependence the thesis claims. It also establishes energy security as a distinct outcome and leaves open what threatens it from outside, the question P21 takes up.

### P21. Climate change, energy security risk and buffering factors in the GCC

Ben Ali, M. S., Al-Maadid, A., and Bergougui, B. (2025). *Sustainable Development*, early view.

1. **Lead statement.** The paper asks whether climate change raises energy security risk in the Gulf economies, and whether green patents, institutional quality and human capital buffer that risk. It introduces an external pressure the energy system does not choose.
2. **Research question / hypothesis.** Four hypotheses are tested: climate change raises energy security risk; green patents, institutional quality and human capital each weaken that relationship. The gap is the unexamined transmission from climate stress to energy insecurity in resource-rich Gulf states.
3. **Methods & data.** Six Gulf Cooperation Council economies, 1990 to 2023, with annual data converted to monthly intervals, and the Global Energy Institute risk index as the outcome. Two-way fixed effects with interaction terms estimates the moderation, supported by an IV-Lewbel check and method of moments quantile regression.
4. **Key findings.** Rising emissions and extreme weather all raise energy security risk. Green patents, institutional quality and human capital each weaken the link, with threshold levels of about 1.43, 0.03 and 0.58, beyond which the marginal effect of emissions shrinks. Country sensitivity varies widely, with Oman and Kuwait far more exposed than the others, and the emissions effect intensifies at higher quantiles of risk.
5. **Contribution.** The paper shows that the same factors that raise emissions also create security exposure, and that the buffers only work beyond measurable thresholds. It gives the institutional-conditioning claim a threshold form, and it leaves open who funds the green technologies that do the buffering, which is the question P22 answers for public research budgets.

### P22. When does high-tech research investment enable the energy transition

Bergougui, B., Ghosh, S., Doğan, B., Samour, A., and Nepal, R. (2026). *Energy Conversion and Management: X* 30, 101598.

1. **Lead statement.** The paper asks whether public research budgets enable the energy transition, and whether the answer depends on a country's stage of transition. It identifies the financing behind the capacity that P21 found to be protective.
2. **Research question / hypothesis.** Six hypotheses cover renewable, efficiency and storage research budgets, high-tech industry, economic complexity, income and institutional quality. The gap is the aggregation of research spending into one variable and the reporting of mean effects only.
3. **Methods & data.** Twenty advanced economies with complete IEA research reporting, 1995 to 2022, with an energy transition index as the outcome and public RD&D budgets split into renewable, efficiency and power storage categories. Method of moments quantile regression estimates three models, with panel corrected standard errors, Driscoll-Kraay, fixed effects quantile and system GMM checks.
4. **Key findings.** Renewable research budgets raise the transition at every quantile, with diminishing returns as the transition advances. Efficiency research has no significant effect, and storage research matters only from the sixtieth quantile upward. High-tech industry and technological innovation raise the transition and grow stronger at higher quantiles, economic complexity is negative at low quantiles, and income turns negative at the top.
5. **Contribution.** The paper shows that research budgets are not interchangeable, and that their returns depend on how far the transition has already gone. It supplies the funding side of the security story and marks the point where the portfolio turns from deliberate energy policy to automation, a technology that reshapes energy demand without being designed for it.

### P23. Industrial robots and energy security risk

Bergougui, B., Ben-Salha, O., and Murshed, S. M. (2026). *Energy Nexus* 23, 100760.

1. **Lead statement.** The paper asks how industrial robot adoption affects energy security risk in economies at the automation frontier. It introduces a technology that no one designed as energy policy but that reshapes electricity demand.
2. **Research question / hypothesis.** It examines the non-monotonic relationship between robot density and energy security risk across the joint distribution of both variables, country by country. The gap is the assumed monotonic link between automation and energy outcomes.
3. **Methods & data.** Ten leading robot-adopting economies, 2000 to 2019, annual data, with the Global Energy Institute risk index as the outcome. Quantile cointegration and BDS tests precede multivariate quantile-on-quantile regression, supported by IVMQR with lagged robot density.
4. **Key findings.** In six economies the relationship passes through three phases: early automation raises risk, intermediate levels weaken and reverse the effect, and advanced adoption reduces risk substantially. Sweden reduces risk at every quantile, while Japan, South Korea and Singapore reverse at the frontier, where further automation raises risk. Across the ten economies the predominant effect is a reduction in risk, so automation improves energy security on balance, but the timing and the turning point differ by country.
5. **Contribution.** The paper documents non-monotonicity and stage dependence in the energy security domain, which is the sharpest form of the threshold pattern in the thesis. It establishes the pattern without explaining it, and P24 then tests the mechanisms, the institutional conditions and the geography that produce it.

### P24. Robotics, energy vulnerability, institutions and spillovers

Bergougui, B. Under review, *Energy Sources, Part B: Economics, Planning, and Policy*. Portfolio title "When Does Automation Secure Energy?"; manuscript title "Mitigating Energy Vulnerability with Industrial Robotics".

1. **Lead statement.** The paper asks through which channels and under which institutional conditions industrial robotics reduces energy vulnerability. It extends P23 to a wider sample and adds mechanism, threshold and spatial tests.
2. **Research question / hypothesis.** Five hypotheses cover the direct effect of robotics on vulnerability, mediation through green patents and industrial structure, institutional thresholds, and spillovers near Japan. The gap is the absence of tested channels, conditions and geography behind the automation pattern.
3. **Methods & data.** A balanced panel of 51 countries, 2000 to 2022, annual, with an entropy-weighted energy vulnerability index as the outcome. Two-way fixed effects and IV-GMM estimate the direct effect, mediation equations test the two channels, Hansen threshold regression tests institutional effectiveness, and sample splits test proximity to Japan and group heterogeneity.
4. **Key findings.** Robotics reduces energy vulnerability, and the effect is transmitted through green patent innovation and industrial structure upgrading. The institutional relationship is two-sided: below the first threshold robotics raises vulnerability, between the thresholds it reduces vulnerability most strongly, and above the second threshold gains diminish or reverse. Reductions are significant only near Japan and in middle-income, digitally advanced and small-population economies.
5. **Contribution.** The paper explains the pattern of P23 with named mechanisms and turns the institutional claim into a bounded condition rather than a simple monotonic one. It shows that both too little and too much institutional capacity can weaken the payoff, and it leaves the hydrocarbon case, where diversification is hardest, to P25.

### P25. Institutional quality, green technologies and Algeria's energy diversification

Bergougui, B., and Meziane, S. (2026). *Energy & Environment*, online first.

1. **Lead statement.** The paper asks whether institutional quality, green technologies and natural resource shocks diversify Algeria's energy mix. It closes the portfolio in the setting where diversification is both hardest and most consequential.
2. **Research question / hypothesis.** Three hypotheses are tested: institutional quality improves diversification, green technology improves it, and resource abundance works against it. The gap is that the drivers of energy diversification in a hydrocarbon economy, and the difference between positive and negative shocks, were previously untested.
3. **Methods & data.** Algeria, 1995Q1 to 2022Q4, quarterly, with an energy diversification index built from the inverse of a Herfindahl-Hirschman concentration measure. A Fourier nonlinear autoregressive distributed lag model, chosen after linearity was rejected for all series, separates positive and negative shocks in each driver.
4. **Key findings.** Institutional quality is the strongest driver, and negative shocks reduce diversification more than positive shocks raise it. Green technology shows the same asymmetry, with improvements raising diversification and deteriorations lowering it. Negative resource shocks reduce diversification, which points to fiscal volatility rather than abundance itself as the obstacle, while income and energy consumption are not significant.
5. **Contribution.** The paper tests the portfolio's main claims in the least favourable setting and finds that institutions and green technology move the energy mix only when they improve, with losses outweighing gains. It ties Theme 3 back to the Algerian evidence of Theme 1 and confirms that resource revenues can finance diversification while their volatility undermines it.

---

## Points to verify against the published versions

These are places where the extraction notes in `summaries/*.md` flag a conflict that could affect a statement made above.

- **P01.** The Note de Synthèse describes the paper as comparing budget increases with decreases; the paper estimates quantile-on-quantile marginal effects instead, and its thresholds are described only in words. The summary above follows the paper.
- **P03.** The text reports a GMM coefficient (1.767) that does not match the table (0.049) in sign or size. The summary above avoids the GMM number and relies on the baseline, instrumental-variable and mechanism results.
- **P05.** The abstract reports governance effects of 0.65 to 0.95 percent while Table 7 gives 0.067 to 0.145. The summary above reports the direction and the quantile pattern, not the magnitude.
- **P07.** The text cites a total-FDI effect on secondary emissions (1.054 percent) that does not appear in the table, which reports 2.146. The summary above reports the sign pattern across sectors.
- **P08.** The text gives a positive innovation shock of 0.43 percent while the table gives 0.344. The summary above uses the table value.
- **P09, P14, P16, P20, P23, P25.** Each has one internal inconsistency that does not change the headline finding, for example period statements that differ between sections or significance stars that conflict with the text. These are listed per paper in the extraction notes and should be checked before any coefficient is quoted in a chapter.
- **P24.** The portfolio title and the manuscript title differ, and the venue is given differently in the Note de Synthèse and in the submission file. The status line above follows the manuscript.
- **P13.** The journal prints the second author as "Brahim, Bergougui". The bibliography needs the candidate's usual form decided once.
