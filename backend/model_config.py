"""
🚀 Four Pillars AI - Model Configuration Summary
RTX 4050 GPU Optimized Model Selection

This file documents the exact Hugging Face models used for each agent,
optimized for RTX 4050 Laptop GPU (6GB VRAM).
"""

# =============================================================================
# MODEL SPECIFICATIONS
# =============================================================================

AGENT_MODELS = {
    "finance": {
        "model_name": "microsoft/phi-3.5-mini-instruct",
        "size_4bit": "2.1GB",
        "parameters": "3.8B",
        "features": [
            "Optimized for numerical reasoning",
            "Excellent for financial KPIs and ROI calculations",
            "Microsoft's instruction-tuned model"
        ],
        "memory_usage": "~2.1GB VRAM with 4-bit quantization"
    },
    
    "risk": {
        "model_name": "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        "size_4bit": "0.55GB", 
        "parameters": "1.1B",
        "features": [
            "Lightweight for fast risk scoring",
            "Optimized for fast inference",
            "Good chat/instruction following"
        ],
        "memory_usage": "~0.55GB VRAM with 4-bit quantization"
    },
    
    "compliance": {
        "model_name": "nlpaueb/legal-bert-base-uncased",
        "size": "0.4GB",
        "parameters": "110M (BERT-base)",
        "features": [
            "Fine-tuned on legal and regulatory text",
            "Perfect for compliance checks",
            "Specialized legal domain knowledge"
        ],
        "memory_usage": "~0.4GB VRAM"
    },
    
    "market": {
        "model_name": "mistralai/Mistral-7B-Instruct-v0.3", 
        "size_4bit": "4-6GB",
        "parameters": "7B (quantized from ~13GB full)",
        "features": [
            "Large language model for complex market analysis",
            "Excellent instruction following",
            "Advanced reasoning for market dynamics"
        ],
        "memory_usage": "~4-6GB VRAM with 4-bit quantization"
    }
}

# =============================================================================
# TOTAL MEMORY USAGE
# =============================================================================

TOTAL_MEMORY_ESTIMATE = """
Expected GPU Memory Usage (Sequential Loading):
- Finance Agent (Phi-3.5-mini): 2.1GB
- Risk Agent (TinyLlama): 0.55GB  
- Compliance Agent (Legal-BERT): 0.4GB
- Market Agent (Mistral-7B): 4-6GB

Total if all loaded simultaneously: ~7-9GB
RTX 4050 Available: 6GB
⚠️  NOTE: May need sequential loading or CPU offload for Market Agent
"""

# =============================================================================
# DOWNLOAD INSTRUCTIONS
# =============================================================================

DOWNLOAD_COMMANDS = """
The models will be automatically downloaded from Hugging Face on first use.
To pre-download them manually, you can use:

# Finance Agent
huggingface-hub download microsoft/phi-3.5-mini-instruct

# Risk Agent  
huggingface-hub download TinyLlama/TinyLlama-1.1B-Chat-v1.0

# Compliance Agent
huggingface-hub download nlpaueb/legal-bert-base-uncased

# Market Agent (Large - ~13GB full model)
huggingface-hub download mistralai/Mistral-7B-Instruct-v0.3

Or they will download automatically when the agents initialize.
"""

# =============================================================================
# OPTIMIZATION FEATURES
# =============================================================================

OPTIMIZATION_FEATURES = {
    "quantization": "4-bit quantization using BitsAndBytesConfig for larger models",
    "mixed_precision": "FP16 for GPU inference to save memory",
    "device_mapping": "Automatic device mapping to utilize GPU efficiently", 
    "memory_management": "Careful memory allocation with max_memory limits",
    "sequential_loading": "Models loaded on-demand to prevent OOM errors"
}

if __name__ == "__main__":
    print("🚀 Four Pillars AI - Model Configuration")
    print("=" * 50)
    
    for agent_name, config in AGENT_MODELS.items():
        print(f"\n{agent_name.upper()} AGENT:")
        print(f"  Model: {config['model_name']}")
        print(f"  Size: {config.get('size_4bit', config.get('size'))}")
        print(f"  Parameters: {config['parameters']}")
        print(f"  Memory: {config['memory_usage']}")
        
    print(TOTAL_MEMORY_ESTIMATE)
    print("\n✅ All models configured for RTX 4050 optimization!")
