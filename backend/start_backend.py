#!/usr/bin/env python3
"""
🚀 Four Pillars AI Backend Startup Script
RTX 4050 GPU Optimized with Real Data Pipeline Integration

This script starts the FastAPI backend with all four AI agents:
- Finance Agent: microsoft/phi-3.5-mini-instruct (2.1GB)
- Risk Agent: TinyLlama/TinyLlama-1.1B-Chat-v1.0 (0.55GB)  
- Compliance Agent: nlpaueb/legal-bert-base-uncased (0.4GB)
- Market Agent: TinyLlama/TinyLlama-1.1B-Chat-v1.0 (0.55GB)

Total GPU Memory Usage: ~3.7GB (fits in RTX 4050 6GB)
Real Data Pipeline: Financial DB, Market News, Vector Store, Compliance DB, Risk API
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
    ║         Multi-Agent Business Intelligence Platform           ║
    ║           GPU Optimized + Real Data Pipeline                ║
    ╠══════════════════════════════════════════════════════════════╣
    ║ 💰 Finance Agent:    microsoft/phi-3.5-mini-instruct  [GPU] ║
    ║ 🛡️  Risk Agent:      TinyLlama/TinyLlama-1.1B-Chat    [GPU] ║
    ║ ⚖️  Compliance Agent: nlpaueb/legal-bert-base-uncased [GPU] ║
    ║ 📈 Market Agent:     TinyLlama/TinyLlama-1.1B-Chat    [GPU] ║
    ╠══════════════════════════════════════════════════════════════╣
    ║ 🔧 GPU Memory: Finance(2.1GB) + Risk(0.55GB) + Market(0.55GB) + Compliance(0.4GB) ║
    ║ 💾 Total VRAM: ~3.7GB (Perfect for RTX 4050 6GB)           ║
    ║ 📊 Data Pipeline: FinancialDB + MarketNews + VectorStore    ║
    ║ 🌐 Backend: FastAPI + CrewAI + WebSocket + Async            ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def main():
    """Start the Four Pillars AI backend"""
    print_startup_banner()
    
    logger.info("🔧 Starting Four Pillars AI Backend with Real Data Pipeline...")
    logger.info("🤖 All 4 Agents: Finance (Phi-3.5) + Risk (TinyLlama) + Compliance (Legal-BERT) + Market (TinyLlama)")
    logger.info("💾 GPU Memory: ~3.7GB optimized for RTX 4050 (6GB)")
    logger.info("📊 Data Sources: FinancialDB + MarketNews + VectorStore + ComplianceDB + RiskAPI")
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
