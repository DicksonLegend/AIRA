#!/usr/bin/env python3
"""
� Start Four Pillars AI with 100% LOCAL MODELS ONLY
Forces offline mode to use only pre-downloaded models from ./models/ directory
"""
import os
import sys
from pathlib import Path

# Set environment variables to use local models ONLY
current_dir = Path(__file__).parent
models_dir = current_dir / "models"

print("� FORCING ALL DOWNLOADS TO LOCAL MODELS DIRECTORY")

# Set Hugging Face cache to use local models directory - MULTIPLE VARIABLES FOR SAFETY
os.environ["TRANSFORMERS_CACHE"] = str(models_dir / "transformers")
os.environ["HF_HOME"] = str(models_dir)
os.environ["HF_HUB_CACHE"] = str(models_dir / "hub")
os.environ["HF_DATASETS_CACHE"] = str(models_dir / "datasets")

# CRITICAL: Additional cache variables to ensure downloads go to our directory
os.environ["HUGGINGFACE_HUB_CACHE"] = str(models_dir / "hub")  # Alternative cache variable
os.environ["XDG_CACHE_HOME"] = str(models_dir)  # System cache directory  
os.environ["TORCH_HOME"] = str(models_dir / "torch")  # PyTorch cache
os.environ["SENTENCE_TRANSFORMERS_HOME"] = str(models_dir / "sentence-transformers")  # Sentence transformers

# FORCE downloads to go to our directory (NOT home directory)
os.environ["HF_HUB_OFFLINE"] = "0"  # Allow downloads for missing models like Legal-BERT
os.environ["TRANSFORMERS_OFFLINE"] = "0"  # Allow downloads for missing models
os.environ["HF_DATASETS_OFFLINE"] = "1"  # Keep datasets offline

# REMOVE LOCAL_FILES_ONLY to allow downloads
# os.environ["LOCAL_FILES_ONLY"] = "1"  # Commented out to allow downloads
# ENSURE ALL DOWNLOADS GO TO OUR MODELS DIRECTORY (NOT HOME DIRECTORY)
# Clear any existing cache environment variables that might point to home directory
import os
for key in list(os.environ.keys()):
    if 'HUGGINGFACE' in key or 'HF_' in key:
        if key not in ['HF_HOME', 'HF_HUB_CACHE', 'HF_HUB_OFFLINE', 'TRANSFORMERS_OFFLINE', 'HF_DATASETS_OFFLINE', 'HF_HUB_DISABLE_TELEMETRY', 'HF_HUB_DISABLE_PROGRESS_BARS', 'HUGGINGFACE_HUB_CACHE']:
            del os.environ[key]

# Create directories if they don't exist
(models_dir / "hub").mkdir(parents=True, exist_ok=True)
(models_dir / "transformers").mkdir(parents=True, exist_ok=True)
(models_dir / "datasets").mkdir(parents=True, exist_ok=True)
(models_dir / "torch").mkdir(parents=True, exist_ok=True)
(models_dir / "sentence-transformers").mkdir(parents=True, exist_ok=True)

print("📁 Created/verified all cache directories in models folder")

# Disable telemetry and progress bars for cleaner output
os.environ["HF_HUB_DISABLE_TELEMETRY"] = "1"
os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "0"  # Enable progress bars to see download progress

# Set dummy OpenAI key to bypass CrewAI validation (we use local models)
os.environ["OPENAI_API_KEY"] = "local-model-key"

# Memory optimization for your hardware
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "max_split_size_mb:512"
os.environ["TOKENIZERS_PARALLELISM"] = "false"

print("🔧 Environment configured to DOWNLOAD MISSING MODELS TO LOCAL DIRECTORY:")
print(f"   📁 TRANSFORMERS_CACHE: {os.environ.get('TRANSFORMERS_CACHE')}")
print(f"   📁 HF_HOME: {os.environ.get('HF_HOME')}")
print(f"   📁 HF_HUB_CACHE: {os.environ.get('HF_HUB_CACHE')}")
print(f"   � HUGGINGFACE_HUB_CACHE: {os.environ.get('HUGGINGFACE_HUB_CACHE')}")
print(f"   📁 XDG_CACHE_HOME: {os.environ.get('XDG_CACHE_HOME')}")
print(f"   🌐 HF_HUB_OFFLINE: {os.environ.get('HF_HUB_OFFLINE')} (0=allow downloads)")
print(f"   🔒 LOCAL_FILES_ONLY: {os.environ.get('LOCAL_FILES_ONLY', 'None')} (None=allow downloads)")

print("\n🎯 DOWNLOAD STRATEGY:")
print("   ✅ Existing models: Use from local cache")
print("   ⬇️  Missing models: Download to local models directory") 
print("   ❌ Home directory cache: Disabled")

# Verify models directory exists
if not models_dir.exists():
    print(f"❌ ERROR: Models directory not found: {models_dir}")
    print("Please ensure your models are downloaded to the correct location!")
    sys.exit(1)

hub_dir = models_dir / "hub" 
transformers_dir = models_dir / "transformers"

if hub_dir.exists():
    print(f"   ✅ Hub directory found: {len(list(hub_dir.iterdir()))} items")
else:
    print(f"   ⚠️  Hub directory not found: {hub_dir}")

if transformers_dir.exists():
    print(f"   ✅ Transformers directory found: {len(list(transformers_dir.iterdir()))} items")
else:
    print(f"   ⚠️  Transformers directory not found: {transformers_dir}")

# Start the application
if __name__ == "__main__":
    # Import and run the main application
    from app.main import app
    import uvicorn
    
    print("\n🚀 Starting Four Pillars AI - DOWNLOAD MODE...")
    print("📊 API Documentation: http://localhost:8000/docs")
    print("⚡ Health Check: http://localhost:8000/health")
    print("⬇️  Mode: Download missing models to local directory")
    print("📁 All downloads will go to: /media/dickson/New Volume/AIRA/backend/models/")
    print("-" * 70)
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=False,  # Disable reload in production
        log_level="info"
    )