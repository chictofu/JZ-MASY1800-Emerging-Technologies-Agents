# Diffusion Agent

Assesses relevant adopter categories and all five diffusion characteristics using the scaffold's common output contract.

Add case inputs under `cases/` and build a prompt from the scaffold root with:

```sh
python tools/build_prompt.py --agent agents/diffusion_agent --case agents/diffusion_agent/cases/primary.json
```

Case inputs and model responses have not yet been supplied. A built prompt requires qualitative review for the required diffusion assessments; common schema validation alone does not check analytical completeness.
