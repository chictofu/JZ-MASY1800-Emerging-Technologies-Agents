# Primary and context-contrast test results

Date: 2026-11-07
Method: The current Codex assistant applied the specialist instructions to two synthetic case profiles and authored the saved JSON assessments. Python serialized those assessments and validated them; it did not invoke a separate model/API. These are single-pass qualitative scenario evaluations, not independent model replication or evidence about real organizations. No API credentials or external sources were used.

## Controlled comparison

The same generative AI assistant drafts internal help-desk replies with mandatory human review in both cases. Sector, stakeholders, business need, risk scope, adoption stage, management question and four-week ten-user horizon are held constant. Shared T1 assumes bounded technical requirements are met, without establishing general technology maturity. Cases contain factual synthetic profiles, without expected-answer cues.

| Finding | Primary: Harbor Services, prepared | Contrast: Ridge Services, constrained |
|---|---|---|
| Technology maturity | Unknown: no rubric or independent evidence | Same |
| Technology/application fit | Conditional on shared T1 and scope | Same |
| Leadership/sponsorship | 2: signed charter, escalation rights | 1: enthusiasm without charter/decision practice |
| Skills | 2: demonstrated review competence | 0: no training or demonstrated competence |
| Workflow/process | 2: SOP, review, exceptions, fallback rehearsed | 0: no agreed workflow or fallback |
| Infrastructure/data | 2: approved sandbox and tested access/recovery | 0: no approved environment or tests |
| Resources/budget | 2: funded pilot and reviewer time | 0: no approved support funding or allocation |
| Governance/risk | 2: approvals and stop authority | 0: no risk review, approvals or stop authority |
| Culture/change | 2: user participation and support | 0: no user participation or support plan |
| Operating ownership | 2: accepted RACI and exercised runbook | 0: no accepted owner or incident/exit duties |
| Readiness conclusion | Pilot ready within stipulated synthetic scope; scale unproven | Not ready for pilot; mandatory gates unmet |
| Immediate management action | Confirm continuing gate validity; monitor pilot and assess expansion separately | Sponsor assigns risk and service owners; close approval, access, funding, review and workflow gates before launch |

## Qualitative assessment

PASS: readiness changes with capabilities and constraints while technology maturity and application fit remain identical. The constrained organization's working drafting tool would still face blocked access, review queues, unsupported incidents and staff abandonment. The primary's strengths are actual demonstrated capabilities within the fictional profile, not vendor promises. Neither case establishes production-scale readiness.

PASS: actions specify priorities, causal rationale, owners, owner-inference basis/confidence, dependencies, proposed timing, acceptance evidence and blocked stage. Operations Director ownership of workflow/staffing and Head of IT ownership of access/integration are supported inferences. Risk/service ownership and funding approval authority require explicit assignment or confirmation. No personal names or accepted commitments were invented.

PASS: no unrelated strength offsets a blocker. Unknown maturity remains unknown rather than becoming low maturity. Recommendations preserve the distinction between fit and readiness.

## Validation and limits

Both case files pass the frozen intake JSON schema. Both responses pass the scaffold validator and the full Draft 2020-12 output schema. Controlled-field, identical technical-finding and changed-readiness assertions passed. Frozen-core checksums are intact. Prompt packets were rebuilt for both cases.

These deterministic checks verify artifact structure and the reported comparison; they do not independently establish analytical quality or model robustness. No repeated sampling, blinded independent evaluation, API execution or real organizational document verification occurred. Technical acceptance thresholds and final approval/funding authority remain unresolved for a real deployment. A real launch requires verification of the stipulated facts.

## Artifact hashes (SHA-256)

- `cases/primary.json`: `66ca79e0732cab783cb8dde15270df0f28ca1328de250c147108cad291869bf8`
- `cases/contrast_1.json`: `0187a0a94f0a9e089674d5981d845768d0538384d5cd34d328e9705b179e2fcb`
- `responses/primary_response.json`: `9929273261ccd02339ee4d7985a96da15de061e64337981e948528600e53f13e`
- `responses/contrast_1_response.json`: `f27541b19fdeef449ab41a22506c47a13645722fd6277d6225215f7cd1fba26e`
- `specialist_instructions.md`: `dab3adc2ce90c776e7d3fb12394e23cf25327472607293e87631956ff7e049cf`

Revision review: funding approval authority is explicitly unknown in both profiles. Saved responses now ask for a current delegation/approval record with role, limit, scope and effective date. Primary pilot readiness relies on stipulated budget approval and does not independently certify spending authorization; authority evidence is required before new expenditure, budget changes or expansion. Contrast funding absence remains a blocker. Responses and rebuilt prompts revalidated after revision; no independent model rerun. Hashes above reflect revised artifacts.
