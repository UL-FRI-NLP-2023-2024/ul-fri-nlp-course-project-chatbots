# Natural language processing course 2023/24: `Parameter-Efficient Fine-Tuning of Language Models`

## Overview
This repository contains the research project on Parameter-Efficient Fine-Tuning (PEFT) techniques applied to Language Models, developed for the FRI Natural Language Processing course 2024. This project evaluates different PEFT methods, comparing their efficiency and performance against traditional fine-tuning methods across several NLP tasks.

## Research Objective
To investigate and compare the efficiency of various PEFT methods (including Prompt-tuning and Low Rank Adaptation) in fine-tuning pre-trained language models (PLMs) for task-specific data, aiming to reduce computational demands while maintaining competitive performance.

## Dataset and Models
- **Datasets:** Slovene SuperGLUE, Slobench (Machine Translation task)
- **Models:** EMBEDDIA/sloberta, EMBEDDIA/crosloengual-bert, FacebookAI/xlm-roberta-base, OPUS-MT model

## PEFT Techniques Explored
- Low-Rank Adaptation (LoRA)
- Low-Rank Hadamard Product (LoHa)
- Prompt-Tuning

## Results
Results indicate that PEFT methods can achieve comparable performance to traditional fine-tuning with significantly reduced computational resource usage. Results and comparisons are documented in the project report.

## Usage
All used datasets and trained models are accessible on Hugging Face. <br>
Their names can be found inside corresponding jupyter notebooks, where they were used (`report/code/...`).
