# Scholarly Wikidata: Population and Exploration of Conference Data in Wikidata using Large Language Models and Semantic Web Techniques

This repository provides the implementation of Large Language Models (LLM) based extractions of facts from conference proceedings front matter and conference websites. 

## Prompt Templates
The prompts used to extract the number of submitted and accepted papers, members of the organization committee and their roles, members of the programme committee with the corresponding track and role (PC/SPC), important dates (deadline) along with their activity and corresponding track, conference topics, etc. are found in [prompt_templates.py](https://github.com/scholarly-wikidata/scholarly-wikidata/blob/main/src/prompt_templates.py).

## LLM extractors 
[scholarly-wikidata](https://github.com/scholarly-wikidata/scholarly-wikidata/tree/main/src) repo currently implements the following extractors. 
- acceptance_ratio_processor
- conference_topic_processor.py
- important_dates_processor.py
- organization_committee_role_processor.py
- program_committee_processor.py

## DBLP to OpenRefine transformation 
[dblp_to_open_refine.ipynb](https://github.com/scholarly-wikidata/scholarly-wikidata/blob/main/src/dblp_to_open_refine.ipynb) provides the code needed to extract the papers and their corresponding authors from DBLP for a given conference series and prepare CSV files that can be imported to OpenRefine for entity linking / reconciliation to Wikidata and prepare the Quick Statements to be submitted to Wikidata.

## Source Data
The source data required to run the different extractors are distributed in [Zenodo](https://zenodo.org/records/10989709). 
