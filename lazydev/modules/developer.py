
from typing import List
from .prompts import PrompBook
from langchain.llms import OpenAI
import json

from .utils import Utilities

class Developer():
    def __init__(self, requirement:str,root_dir:str, openai_api_key:str):
        self.requirement=requirement
        self.root_dir=root_dir
        self.api_key=openai_api_key
        self.brain = OpenAI(
            model_name="gpt-3.5-turbo",
            openai_api_key=self.api_key,
            temperature=0,
            streaming=False
            )

    def clear_doubts(self):
        prompt=PrompBook.expand_requirements(self.requirement)
        doubts:str=self.brain(prompt)
        doubt_list:List[str]=doubts.split("\n")
        doubt_list=[doubt.strip() for doubt in doubt_list if doubt.strip()!=""]
        print("""
Hey there! 😄 It's Lazy Dev, your friendly neighborhood programmer, here to make your API service dreams come true! 🎉 
But before I dive into coding magic, I have a few fun and important questions for you. 
So, grab a cup of coffee ☕️, sit back, and let's clarify some details, shall we? Here we go! 🚀
        """)
        answer_list=[]
        for doubt in doubt_list:
            answer = input(f"{doubt}\n>>")
            answer_list.append(answer)

        print("""
Thats all I need! 😄

Sit back and relax while I work my coding magic for you! ✨✨✨

🚀 I've got this! 🎉

Cheers! 👨‍💻
        """)
        return doubt_list,answer_list

    def plan_project(self):
        prompt=PrompBook.plan_project(self.requirement,self.clarifications)
        plannings:str=self.brain(prompt)
        return plannings
    
    def generate_folder_structure(self):
        prompt=PrompBook.design_folder_structure(
            question=self.requirement,
            plan=self.plannings,
            clarifications=self.clarifications
            )
        folder_tree_str:str=self.brain(prompt)
        folder_tree:dict=json.loads(folder_tree_str)
        Utilities.generate_files_and_folders(structure=folder_tree,root_dir=self.root_dir)


    def develop(self):
        # clearing all doubts
        doubts,answers=self.clear_doubts()
        self.clarifications:str=""
        for i in range(len(doubts)):
            self.clarifications=f"{self.clarifications}\n\n{i+1}. {doubts[i]}\n Ans: {answers[i]}"

        # planning the project
        print("Planning...")
        self.plannings=self.plan_project()
        # creating files and folders for the project
        print("Creating files...")
        self.generate_folder_structure()



        