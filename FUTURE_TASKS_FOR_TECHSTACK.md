# TechStack - Future Tasks

## Current stopping point

The data-preparation work in this task stops at:

**Raw data -> cleaned/standardized master dataset -> filtered model dataset -> feature selection**

Do not start model training in this phase.

## Completed by this task

- [x] Raw data exploration
- [x] Water-quality standardization
- [x] Water-quality master dataset
- [x] Weather standardization
- [x] Model-data filtering
- [x] Feature selection
- [x] Model-ready dataset
- [x] Preserve `source_file` lineage for processed water-quality rows
- [x] Keep the raw files unchanged
- [x] Document that `RS_Session_255_AU_90.2.csv` has no year field
- [x] Document that the weather files are standardized separately and not merged with historical water-quality data

## Future team tasks

1. ML training
2. Model comparison
3. Validation on unseen data
4. Select best reliable model
5. Save trained model
6. IoT/n8n integration
7. DSS/risk logic
8. CLI integration
9. Final system testing
10. Satellite as future version enhancement

## Explicit constraint

Do not include satellite in the initial ML model.

## Notes for the next team

- Historical water-quality data and weather data are standardized into separate master files.
- No satellite features are included in the initial model-ready dataset.
- Synthetic IoT data remains clearly labeled as simulated data for the demo pipeline.

