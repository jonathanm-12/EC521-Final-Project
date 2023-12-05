from transformers import GPT2ForSequenceClassification, GPT2Tokenizer
import json
import torch
# Load the fine-tuned model
# model_path = "results/checkpoint-1000/"
# model = GPT2ForSequenceClassification.from_pretrained(model_path)
# model = GPT2ForSequenceClassification.from_pretrained("fine_tuned_gpt_model", num_labels=2,
#                                                       output_attentions=False,
#                                                       output_hidden_states=False,
#                                                       ignore_mismatched_sizes=True)
# model.config.label2id = {"LABEL_0": 0, "LABEL_1": 1}  # Replace with your label mapping
# model.config.id2label = {0: "LABEL_0", 1: "LABEL_1"}  # Replace with your label mapping
# model.config.num_labels = 2  # Replace with the number of labels in your task
# Load the pre-trained weights without considering the checkpoint
# model.load_state_dict(torch.load('D:\\Code\\BU\\SC\\fine_tuned_gpt_model\\pytorch_model.bin'))
# Load the tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("fine_tuned_gpt_model3")
# tokenizer.pad_token = tokenizer.eos_token
# Prepare the input sequence

model = GPT2ForSequenceClassification.from_pretrained("fine_tuned_gpt_model3" )


# model.config.label2id = {"LABEL_0": 0, "LABEL_1": 1}  # Replace with your label mapping
# model.config.id2label = {0: "LABEL_0", 1: "LABEL_1"}  # Replace with your label mapping
# model.config.num_labels = 2  # Replace with the number of labels in your task
# model.load_state_dict(torch.load("fine_tuned_gpt_model3/pytorch_model.bin"))
# model.train


# input_sequences = ["testing1", "test2","tewmp","a"]
# with open("codes.txt", 'r') as f:
#     input_sequences += f.readlines()[:10]
# input_sequences += ["a","b","math"]
# with open("keys3.json", 'r') as file:
#         input_sequences = json.load(file)
input_sequences = ["6znW_k\\lub\\NW7lj_rem2n4LGmZcLjbm_LOX2wE6D1vHAECPBwSs6MDYaMK-NFrSG3d", "temp", "4e333a348dba92b830700ac78671918a"]
# input_sequence = "This"

# Tokenize the input sequence
# inputs = tokenizer.encode_plus(input_sequence, add_special_tokens=True, padding="max_length", truncation=True, return_tensors="pt")
# input_ids = inputs['input_ids']
# attention_mask = inputs['attention_mask']

# # Perform the inference
# outputs = model(input_ids=input_ids, attention_mask=attention_mask)
# logits = outputs.logits
# predictions = logits.argmax(dim=1)

# # Print the predicted label
# print("Predicted Label:", predictions.item())
print(input_sequences)
for input_sequence in input_sequences:
    # Remove leading/trailing whitespace and newline characters
    # print(input_sequence)
    input_sequence = input_sequence.strip()
    
    # Tokenize the input sequence
    inputs = tokenizer.encode_plus(input_sequence, add_special_tokens=True, padding="max_length", truncation=True, return_tensors="pt")
    input_ids = inputs['input_ids']
    attention_mask = inputs['attention_mask']

    

    # Perform the inference
    outputs = model(input_ids=input_ids, attention_mask=attention_mask)

    input_ids = tokenizer.encode(input_sequence, add_special_tokens=True, return_tensors="pt")

    # Generate inference using the loaded model
    outputs = model(input_ids=input_ids)

    logits = outputs.logits
    predictions = logits.argmax(dim=1)

    # Print the input sequence and predicted label
    print("Input:", input_sequence)
    print("Predicted Label:", predictions.item())
    print("---")