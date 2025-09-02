"""
🎯 Four Pillars AI - Device Allocation Configuration
Optimized GPU/CPU distribution for RTX 4050 (6GB VRAM)
"""

# =============================================================================
# DEVICE ALLOCATION STRATEGY
# =============================================================================

DEVICE_ALLOCATION = {
    # GPU Models - High compute requirements
    "gpu_models": {
        "finance": {
            "model": "microsoft/phi-3.5-mini-instruct",
            "reason": "3.8B parameters, financial calculations need GPU acceleration",
            "memory": "~2.1GB VRAM",
            "quantization": "4-bit"
        }
    },
    
    # Hybrid Models - GPU/CPU split for large models
    "hybrid_models": {
        "market": {
            "model": "mistralai/Mistral-7B-Instruct-v0.3",
            "reason": "7B parameters, too large for full GPU but benefits from GPU layers",
            "memory": "~2-3GB VRAM + 2-3GB RAM", 
            "quantization": "4-bit with CPU offloading"
        }
    },
    
    # CPU Models - Lightweight, fast inference
    "cpu_models": {
        "risk": {
            "model": "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
            "reason": "1.1B parameters, lightweight for fast risk scoring",
            "memory": "~0.55GB RAM",
            "quantization": "none"
        },
        "compliance": {
            "model": "nlpaueb/legal-bert-base-uncased",
            "reason": "110M parameters, BERT model optimized for CPU",
            "memory": "~0.4GB RAM",
            "quantization": "none"
        }
    }
}

# =============================================================================
# PERFORMANCE OPTIMIZATIONS
# =============================================================================

PERFORMANCE_CONFIG = {
    "gpu_optimizations": {
        "mixed_precision": "FP16 for memory efficiency",
        "quantization": "4-bit BitsAndBytesConfig",
        "memory_mapping": "Auto device mapping",
        "max_memory": "Careful VRAM allocation per model"
    },
    
    "cpu_optimizations": {
        "precision": "FP32 for CPU stability",
        "threading": "CPU multi-threading enabled",
        "memory": "System RAM allocation",
        "inference": "Optimized for fast lightweight inference"
    }
}

# =============================================================================
# EXPECTED PERFORMANCE GAINS
# =============================================================================

PERFORMANCE_BENEFITS = {
    "memory_efficiency": "~60% better GPU memory utilization",
    "parallel_processing": "GPU and CPU can work simultaneously",
    "inference_speed": "Faster overall system response",
    "stability": "Reduced GPU memory pressure and OOM errors",
    "scalability": "Better resource distribution for multiple requests"
}

# =============================================================================
# MONITORING METRICS
# =============================================================================

MONITORING_TARGETS = {
    "gpu_memory": "Target: <5.5GB VRAM usage (90% of 6GB)",
    "cpu_memory": "Target: <1GB RAM for AI models",
    "inference_time": {
        "finance_gpu": "Target: <2s for financial analysis",
        "market_gpu": "Target: <3s for market analysis", 
        "risk_cpu": "Target: <1s for risk scoring",
        "compliance_cpu": "Target: <1s for compliance check"
    }
}

def print_device_allocation():
    """Print the current device allocation strategy"""
    print("🎯 Four Pillars AI - Device Allocation Strategy")
    print("=" * 60)
    
    print("\n🔥 GPU MODELS (RTX 4050 - 6GB VRAM):")
    for agent, config in DEVICE_ALLOCATION["gpu_models"].items():
        print(f"  {agent.upper()}: {config['model']}")
        print(f"    Memory: {config['memory']}")
        print(f"    Reason: {config['reason']}\n")
    
    print("🧠 CPU MODELS (System RAM):")
    for agent, config in DEVICE_ALLOCATION["cpu_models"].items():
        print(f"  {agent.upper()}: {config['model']}")
        print(f"    Memory: {config['memory']}")
        print(f"    Reason: {config['reason']}\n")
    
    print("📊 EXPECTED BENEFITS:")
    for benefit, description in PERFORMANCE_BENEFITS.items():
        print(f"  • {benefit.replace('_', ' ').title()}: {description}")

if __name__ == "__main__":
    print_device_allocation()
