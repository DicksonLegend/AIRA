#!/usr/bin/env python3
"""
🚀 Four Pillars AI - Memory Optimized Startup
Prevents virtual memory usage and ensures GPU/CPU physical memory allocation
"""
import os
import sys
import gc
import psutil
import logging

# Set memory optimization environment variables BEFORE importing torch
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "max_split_size_mb:256,expandable_segments:True"
os.environ["HF_HOME"] = "D:\\AIRA\\backend\\models"
os.environ["TRANSFORMERS_CACHE"] = "D:\\AIRA\\backend\\models\\transformers"
os.environ["HF_HUB_CACHE"] = "D:\\AIRA\\backend\\models\\hub"

# Disable torch multiprocessing to prevent memory issues
os.environ["OMP_NUM_THREADS"] = "4"
os.environ["MKL_NUM_THREADS"] = "4"
os.environ["NUMEXPR_NUM_THREADS"] = "4"

# Force garbage collection
gc.collect()

# Check available memory
memory = psutil.virtual_memory()
print(f"💾 Available RAM: {memory.available / (1024**3):.1f} GB / {memory.total / (1024**3):.1f} GB")

if memory.available < 4 * (1024**3):  # Less than 4GB available
    print("⚠️ WARNING: Low memory available. Consider closing other applications.")

print("🚀 Starting Four Pillars AI with memory optimization...")

try:
    # Import and start the application
    from app.main import app
    import uvicorn
    
    # Start with memory-optimized settings
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=False,  # Disable reload to save memory
        workers=1,     # Single worker to prevent memory duplication
        log_level="info"
    )
    
except Exception as e:
    print(f"❌ Startup failed: {e}")
    sys.exit(1)
