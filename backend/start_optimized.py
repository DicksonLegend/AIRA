#!/usr/bin/env python3
"""
🚀 Start Four Pillars AI with Local Models
Uses pre-downloaded models from ./models/ directory
"""
import os
import sys
from pathlib import Path

# Set environment variables to use local models
current_dir = Path(__file__).parent
models_dir = current_dir / "models"

# Set Hugging Face cache to use local models
os.environ["TRANSFORMERS_CACHE"] = str(models_dir / "transformers")
os.environ["HF_HOME"] = str(models_dir)
os.environ["HF_HUB_CACHE"] = str(models_dir / "hub")

# Allow local model access but prefer cached versions
os.environ["HF_HUB_OFFLINE"] = "0"  # Allow API access for model info

# Set dummy OpenAI key to bypass CrewAI validation (we use local models)
os.environ["OPENAI_API_KEY"] = "local-model-key"
os.environ["TRANSFORMERS_OFFLINE"] = "0"  # Allow fallback to cache
os.environ["HF_DATASETS_OFFLINE"] = "1"  # Keep datasets offline

print("🔧 Environment configured for local models:")
print(f"   📁 TRANSFORMERS_CACHE: {os.environ.get('TRANSFORMERS_CACHE')}")
print(f"   📁 HF_HOME: {os.environ.get('HF_HOME')}")
print(f"   📁 HF_HUB_CACHE: {os.environ.get('HF_HUB_CACHE')}")
print(f"   🌐 ONLINE MODE: {os.environ.get('HF_HUB_OFFLINE')}")

# Start the application
if __name__ == "__main__":
    # Import and run the main application
    from app.main import app
    import uvicorn
    
    print("\n🚀 Starting Four Pillars AI with local models...")
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=False,  # Disable reload in production
        log_level="info"
    )