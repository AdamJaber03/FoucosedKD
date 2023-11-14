import random
import uuid
from datetime import datetime
from pathlib import Path
from copy import deepcopy
import pandas

from utils import gptConnector
import pandas as pd
from tqdm import tqdm


DATA_PATH = Path(r"C:\Users\adamj\PycharmProjects\focousedKD\outputs\DataGenerator")
PREV_LIMIT = 3
PREV_DESC_LIMIT = 50

class DataGenerator:
    def __init__(self, model_name, model_desc, temp=0.6):
        self.model_name = model_name
        self.model_desc = model_desc
        self.gpt = gptConnector()
        self.temp = temp
        #self.model_id = uuid.uuid4()
        self.creation_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def generate_dataset_for_cnn(self, size, examples=None, additional_instructions=None):
        data_path = DATA_PATH / fr"{self.model_name}_{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}"
        messages = [
            {
                "role": f"you are generating detailed image descriptions for images to be used when training a Convolutional Neural Network model. \n\nYou will be given a high-level description of the model we want to train, and from that, you will generate data samples, each containing an input-output pair\n\n you will do so in this format:\n```\ninput\n-----------\n$detailed_description_of_the_input_image_for_later_generation\n-----------\noutput\n-----------\n$the_desired_model_result_for_this_input_image\n-----------\n```\n\nonly one input-output pair should be generated per turn.\n\nFor each turn, make the example slightly more complex than the last, while ensuring diversity.\n\nMake sure your samples are unique and diverse, yet high-quality and complex enough to train a well-performing model, make sure the image descriptions you create for the generation are detailed enough to be used with a text-to-image model to create a dataset for the model training.\n\nHere is the type of model we want to train:\n`{self.model_desc}`"
            }
        ]
        if additional_instructions:
            messages[0]['content'] += f"\n\ninstructions for data generation: {additional_instructions}"
        if examples:
            for example in examples:
                formatted_example = f"\ninput\n-----------\n{example['input']}\n-----------\noutput\n-----------\n{example['output']}\n-----------\n"
                messages.append({
                    "role": "assistant",
                    "content": formatted_example
                })
        df = pandas.DataFrame(columns=["input", "output"])
        prev_list = []
        for i in tqdm(size):
            curr_messages = deepcopy(messages)
            prev_2_include = prev_list[-PREV_LIMIT:] if len(prev_list) > PREV_LIMIT else prev_list
            for prev in prev_2_include:
                curr_messages.append({
                    "role": "assistant",
                    "content": prev
                })
            completion = self.gpt.chat_predict(
                msgs=curr_messages,
                # model="gpt-4-1106-preview",
                model="gpt-3.5-turbo-1106",
                temp=self.temp - 0.1 + (random.random() / 5)
            )
            try:
                _, gen_input, _, gen_output, _ = completion.split("-----------\n")
            except ValueError:
                _, gen_input, _, gen_output = completion.split("-----------\n")
            df = pd.concat(
                [df, pd.DataFrame({"input": [gen_input], "output": [gen_output]})],
                ignore_index=True)
            df.to_excel(data_path / "description_data.xlsx")
        return df




    def generate_dataset(self, size, examples=None, additional_instructions=None):
        data_path = DATA_PATH/fr"{self.model_name}_{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.xlsx"
        messages = [
            {
                "role": "system",
                "content": f"You are generating data which will be used to train a machine learning model.\n\nYou will be given a high-level description of the model we want to train, and from that, you will generate data samples, each with a prompt/response pair.\n\nYou will do so in this format:\n```\ndescription\n-----------\n$very_brief_description_of_this_unique_example\n-----------\n\nprompt\n-----------\n$prompt_goes_here\n-----------\n\nresponse\n-----------\n$response_goes_here\n-----------\n```\n\nOnly one prompt/response pair should be generated per turn.\n\nFor each turn, make the example slightly more complex than the last, while ensuring diversity.\n\nMake sure your samples are unique and diverse, yet high-quality and complex enough to train a well-performing model.\n\nHere is the type of model we want to train:\n`{self.model_desc}`"
            }
        ]
        if additional_instructions:
            messages[0]['content'] += f"\n\ninstructions for data generation: {additional_instructions}"
        if examples:
            for example in examples:
                formatted_example = f"\ndescription\n-----------\n{example['description']}\n-----------\n\nprompt\n-----------\n{example['input']}\n-----------\n\nresponse\n-----------\n{example['output']}\n-----------\n"
                messages.append({
                    "role": "assistant",
                    "content": formatted_example
                })
        df = pandas.DataFrame(columns=["description", "input", "output"])
        prev_list = []
        prev_descriptions = []
        for i in tqdm(range(size)):
            curr_messages = deepcopy(messages)

            if PREV_LIMIT != 0:
                included_desc = prev_descriptions[-PREV_DESC_LIMIT - PREV_LIMIT:-PREV_LIMIT] if len(prev_descriptions[:-PREV_LIMIT]) > PREV_DESC_LIMIT else prev_descriptions[:-PREV_LIMIT]
            else:
                included_desc = prev_descriptions[-PREV_DESC_LIMIT:] if len(prev_descriptions) > PREV_DESC_LIMIT else prev_descriptions
            #curr_messages[0]['content'] += f"\n\n\n the following is a list of forbidden descriptions, they are already a part of the dataset so do not generate new data that match any of these descriptions. forbiden descriptions not to be reused: {included_desc}"
            prev_2_include = prev_list[-PREV_LIMIT:] if len(prev_list) > PREV_LIMIT else prev_list
            for prev in prev_2_include:
                curr_messages.append({
                    "role": "assistant",
                    "content": prev
                })
            completion = self.gpt.chat_predict(
                msgs=curr_messages,
                #model="gpt-4-1106-preview",
                model="gpt-3.5-turbo-1106",
                temp=self.temp - 0.1 + (random.random() / 5)
            )
            prev_list.append(completion)
            try:
                _, gen_desc, _, gen_input, _, gen_output, _ = completion.split("-----------\n")
            except ValueError:
                _, gen_desc, _, gen_input, _, gen_output = completion.split("-----------\n")
            gen_desc = gen_desc[:-1] if gen_desc[-1] == '\n' else gen_desc
            prev_descriptions.append(gen_desc)
            df = pd.concat([df, pd.DataFrame({"description": [gen_desc], "input": [gen_input], "output": [gen_output]})], ignore_index=True)
            df.to_excel(data_path)
        return df
