# Security Considerations

This project is designed with regulated environments in mind.

## Principles
- Least-privilege access
- Human-in-the-loop validation
- Output traceability
- Audit-ready logging

## AI Safety
- LLM outputs are treated as drafts
- Confidence thresholds flag risky responses
- Human approval required before use

## Data Handling
- No training on user-uploaded documents
- Clear separation between ingestion and inference