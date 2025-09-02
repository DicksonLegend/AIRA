#!/usr/bin/env python3
"""
🚀 Four Pillars AI Backend Startup Script
RTX 4050 GPU Optimized with Specified Hugging Face Models

This script starts the FastAPI backend with all four AI agents:
- Finance Agent: microsoft/phi-3.5-mini-instruct (2.1GB)
- Risk Agent: TinyLlama/TinyLlama-1.1B-Chat-v1.0 (0.55GB)  
- Compliance Agent: nlpaueb/legal-bert-base-uncased (0.4GB)
- Market Agent: distilgpt2 (0.35GB)

Total GPU Memory Usage: ~3.4GB (fits in RTX 4050 6GB)
"""

import asyncio
import logging
import uvicorn
from app.main import app

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def print_startup_banner():
    """Print the Four Pillars AI startup banner"""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                    🚀 FOUR PILLARS AI                       ║
    ║                Multi-Agent Business Intelligence             ║
    ║                  RTX 4050 GPU Optimized                     ║
    ╠══════════════════════════════════════════════════════════════╣
    ║ 💰 Finance Agent:    microsoft/phi-3.5-mini-instruct        ║
    ║ 🛡️  Risk Agent:      TinyLlama/TinyLlama-1.1B-Chat-v1.0     ║
    ║ ⚖️  Compliance Agent: nlpaueb/legal-bert-base-uncased       ║
    ║ 📈 Market Agent:     mistralai/Mistral-7B-Instruct-v0.3     ║
    ╠══════════════════════════════════════════════════════════════╣
    ║ GPU Memory Usage: ~7-9GB total (sequential loading)         ║
    ║ Backend: FastAPI + WebSocket + Async Processing             ║
    ║ Models: Hugging Face with 4-bit Quantization                ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def main():
    """Start the Four Pillars AI backend"""
    print_startup_banner()
    
    logger.info("🔧 Starting Four Pillars AI Backend...")
    logger.info("📱 API Documentation: http://localhost:8000/docs")
    logger.info("🌐 WebSocket Endpoint: ws://localhost:8000/ws")
    logger.info("⚡ Health Check: http://localhost:8000/health")
    
    # Start the FastAPI server
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info",
        access_log=True
    )

if __name__ == "__main__":
    main()
