
from typing import List


class PromptBook:
    @staticmethod
    def expand_requirements(question:str)->str:
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
    def plan_project(question:str, clarification:str)->str:
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

Plan : <your plan here> //tell us a very detailed, verbose plan or thought on how you want to proceed before writing the files  for example which framework you are going to use

As your response will go to an automated parser, things to keep in mind all the time:
* follow the exact format provided above without fail
* the folder and files structure should be complete, means means no additional files will be required to create to run the program, for example if its nodejs project add package.json if its a python project add requirements.txt etc..
* do not write the contents of the files that will be done by the next devepoler
Begin!
"""
    @staticmethod
    def design_folder_structure(question:str,plan:str,clarifications:str)->str:
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
* do not write the contents of the files that will be done by the next developer
Begin!
"""
    @staticmethod
    def prioritise_file_list(filelist:List[str])->List[str]:
        list_string='\n'.join(filelist)
        return f"""
you are a senior programmer. you going to write a api service.
below are the file list that you are going to complete in future.

reorder them in a way that most suitable based on how one will be dependent on other

{list_string}

As your response will go to an automated parser, things to keep in mind all the time:
* only write file list in order nothing else
* do not write any explanation
Begin!
        """

