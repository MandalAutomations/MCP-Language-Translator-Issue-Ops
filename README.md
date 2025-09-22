# Translator

This repository provides an IssueOps workflow for translating text between languages using GitHub Issues and Comments.

## Features

- Translate text between languages using OpenAI models.
- Trigger translations by creating issues or commenting on issues with a specific template.
- Automatically updates issue comments with the original and translated text.

## Usage

### 1. Configure Secrets

Add a repository secret named `GH_TOKEN` with a GitHub token that has `repo` and `issues` permissions.

### 2. Create a Translation Issue

Open a new issue using the **Translation** template.  
Fill in the `source_lang` and `target_lang` fields, for example:

```yaml
source_lang: English
target_lang: French
```

### 3. Add a Comment to Translate
Comment on the issue with the text you want to translate.
The GitHub Actions workflow will:

Detect the comment.
Parse the issue for source and target languages.
Translate the comment text.
Edit your comment to include both the original and translated text.

### 4. Manual Workflow Dispatch
You can also run the workflow manually from the Actions tab, providing the text to translate as input.