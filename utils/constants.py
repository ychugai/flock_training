qwen_template = {
    "system_format": "<|im_start|>system\n{content}<|im_end|>\n",
    "user_format": "<|im_start|>user\n{content}<|im_end|>\n<|im_start|>assistant\n",
    "assistant_format": "{content}<|im_end|>\n",
    "tool_format": "{content}",
    "function_format": "{content}",
    "observation_format": "<|im_start|>tool\n{content}<|im_end|>\n<|im_start|>assistant\n",
    "system": "You are a helpful assistant.",
}

gemma_template = {
    "system_format": "<bos>",
    "user_format": "<start_of_turn>user\n{content}<end_of_turn>\n<start_of_turn>model\n",
    "assistant_format": "{content}<eos>\n",
    "tool_format": "{content}",
    "function_format": "{content}",
    "observation_format": "<start_of_turn>tool\n{content}<end_of_turn>\n<start_of_turn>model\n",
    "system": None,
}

phi_template = {
    "system_format": "<system>{content}</system>\n",
    "user_format": "<user>{content}</user>\n<assistant>",
    "assistant_format": "{content}</assistant>\n",
    "tool_format": "{content}",
    "function_format": "{content}",
    "observation_format": "<tool>{content}</tool>\n<assistant>",
    "system": "You are a helpful assistant capable of handling complex queries and tasks.",
}

llama_template = {
    "system_format": "<s>[INST] <<SYS>>\n{content}\n<</SYS>>\n\n",
    "user_format": "{content} [/INST]",
    "assistant_format": " {content} </s>",
    "tool_format": "{content}",
    "function_format": "{content}",
    "observation_format": "{content}",
    "system": "You are a helpful assistant capable of handling a wide variety of questions and tasks.",
}

model2template = {
    "Qwen/Qwen1.5-0.5B": qwen_template,
    "Qwen/Qwen1.5-1.8B": qwen_template,
    "Qwen/Qwen1.5-7B": qwen_template,
    "google/gemma-2b": gemma_template,
    "google/gemma-7b": gemma_template,
    "google/gemma-7b-it": gemma_template,
    "microsoft/Phi-3-mini-4k-instruct": phi_template,
    "meta-llama/Llama-2-7b-chat-hf": llama_template,
}

model2size = {
    "Qwen/Qwen1.5-0.5B": 620_000_000,
    "Qwen/Qwen1.5-1.8B": 1_840_000_000,
    "Qwen/Qwen1.5-7B": 7_720_000_000,
    "google/gemma-2b": 2_510_000_000,
    "google/gemma-7b": 8_540_000_000,
    "google/gemma-7b-it": 8_540_000_000,
    "microsoft/Phi-3-mini-4k-instruct": 3_000_000_000,
    "meta-llama/Llama-2-7b-chat-hf": 7_000_000_000,
}

model2base_model = {
    "Qwen/Qwen1.5-0.5B": "qwen1.5",
    "Qwen/Qwen1.5-1.8B": "qwen1.5",
    "Qwen/Qwen1.5-7B": "qwen1.5",
    "google/gemma-2b": "gemma",
    "google/gemma-7b": "gemma",
    "google/gemma-7b-it": "gemma",
    "microsoft/Phi-3-mini-4k-instruct": "phi",
    "meta-llama/Llama-2-7b-chat-hf": "llama-2",
}
