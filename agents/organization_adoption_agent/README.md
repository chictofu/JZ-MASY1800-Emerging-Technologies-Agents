# Organization Adoption Agent

Defines eight organizational readiness dimensions, evidence requirements, stage-specific ratings and gates. Read specialist_instructions.md and readiness_framework.json.

From the repository root:

```sh
python tools/check_frozen_core.py
python tools/build_prompt.py --agent agents/organization_adoption_agent --case agents/organization_adoption_agent/cases/primary.json
```

The builder includes all analytical rules in the prompt. Run the generated prompt in your chosen model, save JSON under responses/, and validate with tools/validate_response.py. No model or API is invoked by the scaffold.

Synthetic case expectations: primary is conditionally pilot ready based on explicit assumptions, never scale ready; contrast_1 is not ready despite sponsor enthusiasm; contrast_2 requires ownership evidence and cannot declare readiness. These are test scenarios, not completed model evaluations.

Every assessment must identify evidence-backed current strengths and explain organizational failure gaps even assuming the technology works, including consequences, mitigation owners, closure evidence and warning triggers. Unknowns remain distinct from verified deficiencies.

Required separate findings: technology maturity/capability, technology/application fit, and organizational readiness, each with scope, evidence, confidence and unknowns. The management recommendation restates fit and readiness separately; organizational gaps cannot lower a technology-maturity finding. Synthetic paired cases hold technical assumptions constant while readiness changes.

Recommendations must include an ordered readiness action/condition plan: P0 mandatory gates, P1 material risks and prerequisites, P2 later improvements. Each item includes its rationale, accountable owner and ownership basis/confidence, dependencies, proposed timing, measurable acceptance evidence and blocked stage. Context-supported owner inferences must be labeled; ambiguous ownership requires an explicit assignment condition.
