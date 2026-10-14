# Innovation and Disruption Agent — Assignment 3

Student-editable specialist; frozen common files remain unchanged.

From the repository root:
```sh
python tools/check_frozen_core.py
python tools/build_prompt.py --agent agents/innovation_disruption_agent --case agents/innovation_disruption_agent/cases/primary.json
python tools/validate_response.py agents/innovation_disruption_agent/responses/primary_response.json
```
Repeat for contrast_1, contrast_2, and ambiguous. Prompt packets appear in work/.

Submit each complete prompt packet to ChatGPT, request the supplied JSON contract, and save the response under this agent’s responses/ folder. Preserve existing Codex outputs under distinct filenames rather than overwriting their provenance. No API key is required.

The supplied validator checks basic required fields/types, not all JSON Schema restrictions or analytical quality. Assess the three levels, evidence, business-model causality, competing interpretations, and uncertainty separately.

records/ contains the Agent Record, test results, revision evidence, and provenance. Cases marked synthetic are scenario assumptions, not evidence about a real company.
