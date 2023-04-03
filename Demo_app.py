# import the main classes
import gradio as gr
import requests


# input examples list
ex_list = [["Women are not as capable as men in leadership roles."],["Women are capable as men in leadership roles."]]


API_URL_Switch = "https://api-inference.huggingface.co/models/google/flan-t5-base"
headers_Switch = {"Authorization": "Bearer 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"}


def query_Switch(payload):
    response = requests.post(API_URL_Switch, headers=headers_Switch, json=payload)
    return response.json()

def classify_gender_equality(input_sentence):
    # Here goes your code to classify gender equality from input_sentence
    # Return the result as a string

    # sub_text = 'Gender equality is important for the progress of society.'
    sub_text = input_sentence
    prompt = f"Please classify the this sentence ( {sub_text} ) as promoting or not promoting gender equality"

    output_temp = query_Switch({
    "inputs": prompt,
    })
   
    return "This sentence is " + output_temp[0]['generated_text'] + " for gender equality"
  



input_text = gr.inputs.Textbox(label="Input Sentence", default="Women deserve equal pay")

# Create the output text field
output_text = gr.outputs.Textbox(label="Gender Equality Classification")

# Create the Gradio interface
gr.Interface(fn=classify_gender_equality, inputs=[input_text], outputs=output_text, title='Gender Equality Classification', examples = ex_list).launch()
