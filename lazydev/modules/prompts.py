
from typing import List


class PromptBook:
    @staticmethod
    def expand_requirements(question: str) -> str:
        return f"""
you are a senior programmer below is what your client have asked you to do:
---
{question}
---

your current task is to list down all the clarifications you need from the client:
dont ask anything like budget or timelines and other business related stuff.

As your response will go to an automated parser, things to keep in mind all the time:
* write one questions per line
* don't write anything other than the questions.
* use emojis in the question to make them fun.
* Remember the client is a non technical person so ask question accordingly

Begin!
"""

    @staticmethod
    def plan_project(question: str, clarification: str) -> str:
        return f"""
you are a senior programmer below is what your client have asked you to do:
---
{question}
---
here are some clarrification on the requirements
---
{clarification}
---
your current task is to design the folder and and files structure for this project
you should follow the below format to answer this question 

Plan : <your plan here> //tell us a very detailed, verbose plan or thought on how you want to proceed before writing the files  for example which framework you are going to use,dont forget to mention framewark related configuration files. Discuss project architecture so junior developer can understand very easily

As your response will go to an automated parser, things to keep in mind all the time:
* follow the exact format provided above without fail
* be detailed so junior developer can understand very easily
Begin!
"""

    @staticmethod
    def design_folder_structure(question: str, plan: str, clarifications: str) -> str:
        return f"""
you are a senior programmer below is what your client have asked you to do:
---
{question}
---
here are some clarrification on the requirements
---
{clarifications}
---
below is the what you have already planed what to do:
---
{plan}
---
Now based on this write a json object to design file tree.

```
{{
    "root_dir_name": "name of the project",
    "files": [
        {{
        "name": "name of the file",
        "type":"file/directory",
        "files": [...] //repeat the same pattern if its a directory
        }}
    ]
}}
```
As your response will go to an automated parser, things to keep in mind all the time:
* follow the exact format provided above without fail
* only write the json nothing else, no expiation, no pretext 
* only write the folders and files structure
Begin!
"""

    @staticmethod
    def prioritise_file_list(filelist: List[str], plan: str | None = None) -> List[str]:
        list_string = '\n'.join(filelist)
        plan = 'below is the project plan:\n---'+plan+"\n---" if plan != None else ""
        return f"""
you are a senior programmer. you going to write a program for client.

{plan}
below are the file list that you are going to complete in future.

reorder them in a way that most suitable based on how one will be dependent on other

{list_string}

As your response will go to an automated parser, things to keep in mind all the time:
* only write file list in order nothing else
* do not write any explanation
Begin!
        """

    @staticmethod
    def write_file(question, clarifications: str, plan: str, files_written: List[List[str]], file_path_to_write: str, file_paths: List[str]) -> str:
        file_with_conent = "\n\n".join(
            [f"File:{file_path}\nContent:\n{content}" for file_path, content in files_written])
        all_files_list = "\n".join(file_paths)
        return f"""
you are a senior programmer below is what your client have asked you to do:
---
{question}
---
here are some clarrification on the requirements
---
{clarifications}
---
below is the what you have already planed what to do:
---
{plan}
---
Below are the full files list that already has been or will be written
--
{all_files_list}
--

you are now writing the code below are the files that already written with content as follows:
---
{file_with_conent}
---

now you are about to write content the following file:
{file_path_to_write}

As your response will go to an automated parser, things to keep in mind all the time:
* follow the exact format provided above without fail
* only write the file content, no expiation, no pretext.
* code should be readable.
* if the language support, add comments at steps, which expains what you are about to do, dont add comment if comment is not supported by the file type example json file
* keep in mind there wont be any additional files other then the full files list given above, only use files that are mentioned in that list
Begin!

File:{file_path_to_write}
Content:
"""

    def get_code_feedback(
            draft: str,
            question,
            clarifications: str,
            plan: str,
            files_written: List[List[str]],
            file_path_to_write: str,
            file_paths: List[str]) -> str:
        file_with_conent = "\n\n".join(
            [f"File:{file_path}\nContent:\n{content}" for file_path, content in files_written])
        all_files_list = "\n".join(file_paths)
        return f"""
you are a senior programmer below is what your client have asked you to do:
---
{question}
---
here are some clarrification on the requirements
---
{clarifications}
---
below is the what you have already planed what to do:
---
{plan}
---
Below are the full files list that already has been or will be written
--
{all_files_list}
--

you are now writing the code below are the files that already written with content as follows:
---
{file_with_conent}
---

now you are about to write content the following file:
{file_path_to_write}

below is one of the draft version of the code:
---
{draft}
---

your job is to find problems with the code and refine it. 

As your response will go to an automated parser, things to keep in mind all the time:
* if no refinement is required then just say "NONE", and nothing else
* only write the file content, no expiation, no pretext as this will directly go as code.
* if the language support, add comments at steps, which expains what you are about to do, dont add comment if comment is not supported by the file type example json file
* keep in mind there wont be any additional files other then the full files list given above, only use files that are mentioned in that list
Begin!

File: {file_path_to_write}

Refined code:
"""

    def get_compressed_code(code: str):
        return f"""
compress the code below as best as you can, dont rename any data:
```
{code}
```
As your response will go to an automated parser, things to keep in mind all the time:
* only output code and nothing else
* do not rename and content of the code suck as variable names and public function names
Begin!
        """

    def get_compressed_text(text: str):
        return f"""
compress the content of the text below as best as you can:
```
{text}
```
As your response will go to an automated parser, things to keep in mind all the time:
* only respond with the compressed text and nothing else
Begin!
        """

    def generate_instruction(question, clarifications: str, plan: str, files_written: List[List[str]], file_paths: List[str]) -> str:
        file_with_conent = "\n\n".join(
            [f"File:{file_path}\nContent:\n{content}" for file_path, content in files_written])
        all_files_list = "\n".join(file_paths)
        return f"""
you are a senior programmer below is what your client have asked you to do:
---
{question}
---
here are some clarrification on the requirements
---
{clarifications}
---
below is the what you have already planed what to do:
---
{plan}
---
Below are the full files list that already has been or will be written
--
{all_files_list}
--

you are now writing the code below are the files that already written with content as follows:
---
{file_with_conent}
---

now you are need to give client further instruction on what you have developped and how to use it, basically write instruction for the client

As your response will go to an automated parser, things to keep in mind all the time:
* make the instruction clear and simple 

Begin!
"""
