# Revision evidence

## v0.1 → v0.2: instruction review
Type: design-review weakness, not an observed ChatGPT model failure.

The v0.1 instructions required Low/Moderate/High/Potentially Existential even when the ambiguous case supplied no incumbent revenue model or substitution mechanism. This could pressure the model to invent a rating. They also lacked a firm evidence gate for existential exposure and a distinction between conservative adoption and external competitive threat.

Revision: allow Undetermined when necessary facts are missing, require revenue/viability and adaptation evidence for Potentially Existential, separate technical novelty from business-model disruption, and separate immediate posture effects from external exposure.

Original instructions and the original synthetic ambiguous prompt are retained. They were not run in a separate ChatGPT session. Final runs must assess whether the corrected instructions abstain appropriately.

## Technology/application separation clarification
Added mandatory distinct baselines, evidence and implementation status in the existing general_et_finding and application_finding fields. General classification can change only with changed technology scope/version or general evidence. Active work/ packets regenerated. Earlier recorded prompts and responses remain historical evaluations; these strengthened packets have not been rerun in ChatGPT. Frozen core verification passed.
