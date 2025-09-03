"""
🔧 Local Model Loader Utility
Maps model names to local cached paths for offline loading
"""
import os
from typing import Optional

def get_local_model_path(model_name: str) -> Optional[str]:
    """
    Get the local path for a cached HuggingFace model
    
    Args:
        model_name: The HuggingFace model name (e.g., "microsoft/phi-3.5-mini-instruct")
    
    Returns:
        Local path to the model snapshot or None if not found
    """
    # Base models directory
    models_base = os.path.join(os.path.dirname(__file__), "..", "..", "models")
    
    # Model name to cache directory mapping
    model_mappings = {
        "microsoft/phi-3.5-mini-instruct": {
            "cache_dir": "models--microsoft--phi-3.5-mini-instruct",
            "snapshot": "3145e03a9fd4cdd7cd953c34d9bbf7ad606122ca"
        },
        "TinyLlama/TinyLlama-1.1B-Chat-v1.0": {
            "cache_dir": "models--TinyLlama--TinyLlama-1.1B-Chat-v1.0", 
            "snapshot": "fe8a4ea1ffedaf415f4da2f062534de366a451e6"
        },
        "nlpaueb/legal-bert-base-uncased": {
            "cache_dir": "models--nlpaueb--legal-bert-base-uncased",
            "snapshot": "15b570cbf88259610b082a167dacc190124f60f6"
        },
        "mistralai/Mistral-7B-Instruct-v0.3": {
            "cache_dir": "models--mistralai--Mistral-7B-Instruct-v0.3",
            "snapshot": "0d4b76e1efeb5eb6f6b5e757c79870472e04bd3a"
        }
    }
    
    if model_name in model_mappings:
        mapping = model_mappings[model_name]
        local_path = os.path.join(
            models_base,
            mapping["cache_dir"],
            "snapshots", 
            mapping["snapshot"]
        )
        
        # Check if the path exists
        if os.path.exists(local_path):
            return local_path
        else:
            print(f"⚠️ Local model path not found: {local_path}")
            return None
    
    print(f"⚠️ Model mapping not found for: {model_name}")
    return None

def load_model_with_fallback(model_name: str, load_fn, **kwargs):
    """
    Try to load a model from local cache first, fallback to online if needed
    
    Args:
        model_name: The HuggingFace model name
        load_fn: The loading function (e.g., AutoTokenizer.from_pretrained)
        **kwargs: Additional arguments for the loading function
    
    Returns:
        Loaded model/tokenizer
    """
    # First try local path
    local_path = get_local_model_path(model_name)
    if local_path:
        try:
            print(f"📁 Loading {model_name} from local cache...")
            return load_fn(local_path, **kwargs)
        except Exception as e:
            print(f"⚠️ Failed to load from local cache: {e}")
    
    # Fallback to original model name (will try online if allowed)
    print(f"🌐 Loading {model_name} from HuggingFace...")
    return load_fn(model_name, **kwargs)
