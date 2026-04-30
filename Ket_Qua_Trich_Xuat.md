# Markdown Toolkit

Welcome to Markdown Toolkit! Markdown Toolkit is an application to convert Markdown to different types of files such as HTML and PDF. Here is a sample web application of Markdown Toolkit.

## Example Table of contents
- Deployment
- Do you want a new feature?
- Feature List
- Download
- Environment Setup
- Run Code
- Syntax Support
  - Header
  - Math
  - Code
  - Code Segment
  - Tables
  - Insert image
  - Insert link
  - Strong, italics, and scratch
  - Horizontal Rule
  - Unordered List
  - Ordered List
  - Paragraph
  - Checkbox
  - Highlight
  - Block quote
- Support Packages

## Do you want a new feature
If you want a new feature, you can open an issue in this github repository.
If you want to contribute to this repository, you are welcome to do so!

### Cloning the repo
```bash
git clone https://github.com/zhu-y/markdown-toolkit.git
```

### Set up the environment
```bash
pip install -r requirements.txt
```

### Run the program
```bash
python run.py
```
You can also use Gunicorn to run the program:
With default number of workers:
```bash
sh gunicorn.sh
```
You can also change the number of workers as you want:
```bash
gunicorn -w [number of workers] -b [host]:[port] app:app
```
For example, if you want four workers, 127.0.0.1 as host, 4000 as port:
```bash
gunicorn -w 4 -b 127.0.0.1:4000 app:app
```

## Feature Lists
### Completed
- Headers
- Horizontal Rule
- Unordered List
- Ordered List
- Paragraph
- Strong, Scratch, and Italics
- Images
- Links(in markdown file/websites)
- Code Segment/Inline Code
- MathJax Support
- Download as Markdown/HTML
- Local Storage
- Checkbox
- Highlight Text
- Upload Markdown File
- Code Highlight
- Table

### To do
- Workflow
- Download as PDF
- Convert HTML to Markdown
- Login
- Save Notes into User's Private Notebook

## Syntax supported

### Header
Markdown:
```markdown
# H1
## H2
### H3
#### H4
##### H5
###### H6
```

### Math formula
More syntax about MathJax please refer Here.

Math formula itself as a line
Markdown:
```markdown
$$S_{j,k} = L - \sum_{i=j}^{k-1}(c_i + 1)-C_k$$
$$\sum_{i=0}^n i^2 = \frac{(n^2+n)(2n+1)}{6}$$
```

inline math formula
Markdown:
```markdown
$\begin{bmatrix}a & b\\c & d\end{bmatrix}$
```

### Tables
You can insert a table by coding:
```markdown
| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |
```

### Strong, Italics, and Scratch
Markdown:
```markdown
This is **strong**
~~Scratch this.~~
__Italics this.__
```

### Image
**Online Source**
If you want to insert an image from online source, include your image address in the parentheses. For example, if you want to include the logo of google in your markdown, you can write:
Markdown:
```markdown
![alt text](https://i.redd.it/zo9z3a5b0vky.gif)
```

**Local Source**
If you want to insert an image from the same path, include the path in the parentheses. Here is an example:
Markdown:
```markdown
![alt text](docs/hello.png)
```

**Scale**
When the image is too large or too small, you can scale the image by adding '#[scale number]' to the end of the image link. For example, if you originally insert image by coding:
```markdown
![](https://media.wired.com/photos/598e35fb99d76447c4eb1f28/master/pass/phonepicutres-TA.jpg)
```
And you want to scale it, you can use:
```markdown
![](https://media.wired.com/photos/598e35fb99d76447c4eb1f28/master/pass/phonepicutres-TA.jpg#scale=40)
![](https://media.wired.com/photos/598e35fb99d76447c4eb1f28/master/pass/phonepicutres-TA.jpg#scale=50)
```

### Link
Markdown:
```markdown
[Markdown Toolkit Github Repo](https://github.com/zhu-y/markdown-toolkit)
```

### Code Segment
Markdown(Python code):
```markdown
def foo():
    pass
```

Markdown(C++ code):
```markdown
#include<iostream>
using namespace std;
int main(){
    cout << "Hello World";
}
```

### Horizontal Rule
Markdown:
```markdown
Text
---
Text
```

### Paragraph
Markdown:
```markdown
Text
⋅⋅⋅This is a sample of a paragraph. You can have properly indented paragraphs within list items. Notice the blank line above, and the leading spaces (at least one, but we'll use three here to also align the raw Markdown).
Text
```

### Ordered List
Markdown:
```markdown
1. First Line
2. Second Line
3. Third Line
```

### Unordered List
Markdown:
```markdown
- First Level 1
  * Second Level 1
- Second Level 2
- Third Level
  - Second Level 3
    + First Level 2
```

### Checkbox
Markdown:
```markdown
- [ ] not checked
- [x] checked
```

### Highlight
Markdown:
```markdown
##Highlight my text##
```

### Block quote
Markdown:
```markdown
> This is a blockquote
This is the normal text.
```

## Packages
- Math Support: MathJax
- Frontend Support: Bootstrap
- Backend: Flask
- To do: Code highlight support: highlight.js