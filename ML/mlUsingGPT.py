from transformers import GPT2Tokenizer, GPT2ForSequenceClassification, Trainer, TrainingArguments
import torch
from torch.utils.data import Dataset
import random
import json




class CustomDataset(Dataset):
    def __init__(self, dataset, tokenizer):
        self.dataset = dataset
        self.tokenizer = tokenizer

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        text, label = self.dataset[idx]
        encoded_inputs = self.tokenizer.encode_plus(
            text,
            add_special_tokens=True,
            padding="max_length",
            truncation=True,
            return_attention_mask=True,
            return_tensors="pt",
        )
        return {
            'input_ids': encoded_inputs['input_ids'].flatten(),
            'attention_mask': encoded_inputs['attention_mask'].flatten(),
            'labels': torch.tensor(label, dtype=torch.float)
        }
# Preprocessing
def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data
def main():
    # Define the dataset
    positive_data = load_json('true.json')
    negative_data = load_json('false.json')
    # Assign labels: positive=1, negative=0
    positive_labels = [1] * len(positive_data)
    negative_labels = [0] * len(negative_data)

    # Combine data and labels
    data = positive_data + negative_data
    labels = positive_labels + negative_labels

    # Convert strings to numerical representations (e.g., word embeddings)

    # Split data into training and testing sets
    data_with_labels = list(zip(data, labels))
    random.shuffle(data_with_labels)

    train_data = data_with_labels[:int(0.8 * len(data))]
    test_data = data_with_labels[int(0.8 * len(data)):]
    print(train_data[0])
    print(train_data[0:2])
    dataset = train_data
    # Load and tokenize the pre-trained GPT2 model
    tokenizer = GPT2Tokenizer.from_pretrained("distilgpt2")
    tokenizer.pad_token = tokenizer.eos_token

    model = GPT2ForSequenceClassification.from_pretrained("distilgpt2")

    # Preprocess the dataset and tokenize the input text
    tokenized_dataset = CustomDataset(dataset, tokenizer)

    # Define the fine-tuning training arguments
    training_args = TrainingArguments(
        output_dir='./results',
        evaluation_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        gradient_accumulation_steps=2,
        num_train_epochs=3,
        weight_decay=0.01
    )

    # Initialize the Trainer with the model, training arguments, and dataset
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
    )

    # Fine-tune the model
    trainer.train()

    # Save the fine-tuned model for later use
    trainer.save_model("fine_tuned_gpt_model")
    

    # model = GPT2ForSequenceClassification.from_pretrained("fine_tuned_gpt_model")

    # # Load the tokenizer
    # tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

    # # Prepare the input sequence
    # input_sequence = "This"

    # # Tokenize the input sequence
    # inputs = tokenizer.encode_plus(input_sequence, add_special_tokens=True, padding="max_length", truncation=True, return_tensors="pt")
    # input_ids = inputs['input_ids']
    # attention_mask = inputs['attention_mask']

    # # Perform the inference
    # outputs = model(input_ids=input_ids, attention_mask=attention_mask)
    # logits = outputs.logits
    # predictions = logits.argmax(dim=1)

    # # Print the predicted label
    # print("Predicted Label:", predictions.item())

if __name__ == "__main__":
    main()