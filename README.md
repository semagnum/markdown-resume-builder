# Markdown Resume Builder

Originally based on [markdown-resume](https://github.com/vidluther/markdown-resume): this repo allows you to build/maintain your resume in a Markdown file, and then publish it into an HTML or PDF file.

At any given point in time, I have multiple resumes for different cases, job types, etc. Updating each one can be difficult to keep the info the same. I wanted *one* resume and build *multiple* polished resumes to hand to businesses - all based on my interests and use case.

To resolve this, I created an intermediary Python script to look for comment tags within the included resume.md file. Based on the tags given by user input, it would filter out different parts of my resume. With the filtered result, then Pandoc will build the resume. One resume codebase, multiple resume deploys.

# Workflow

The workflow is pretty simple, noted from [markdown-resume](https://github.com/vidluther/markdown-resume). See his README for prerequisites on how to install both Pandoc and Wkhtmltopdf.

1. **Edit the resume.md file.**

Along with typical Markdown workflow, you can use comments to represent sections for specific tags:

```markdown
## Awards & Recognition

<!--filmmaking-->
  * Screenplay Contest Finalist
<!--end-->
  * Dean's List (2019)
  * Eagle Scout
```

In this case, the first bullet point will only appear if no tags are given by the user, or if the user includes `filmmaking` as a tag. Otherwise, it will be parsed out by the Python. You can also use multiple tags for the same section:

```markdown
## Awards & Recognition

<!--filmmaking, copywriting-->
  * Screenplay Contest Finalist
<!--end-->
  * Dean's List (2019)
  * Eagle Scout
```

In this case, either `filmmaking` or `copywriting` tags will include this block.

If *no* tags are given by the user, then *all* of the resume will be printed. Now you have a CV!

**Note: Be sure to keep spacing in mind for use cases when tags are included and excluded.**

2. Run pandoc to convert the Markdown file to HTML. OR 
3. Run pandoc to convert the Markdown file into a PDF.

I used npm for convenience with node.js and running the scripts. Here is an example of creating a resume:
```bash
npm run html -- <tags>
# for example...
npm run html -- programming vfx
# or give no tags to print the whole resume!
npm run html
```