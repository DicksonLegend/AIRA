"""
🚀 FOUR PILLARS AI - Pure CrewAI Framework Backend
Complete CrewAI Multi-Agent Business Intelligence Platform
RTX 4050 GPU Optimized - 4 Agent Configuration (Finance, Risk, Compliance, Market with TinyLlama)
"""
from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import asyncio
import logging
from typing import Dict, Any, List, Optional
import json
from datetime import datetime

from app.services.four_pillars_crewai import FourPillarsCrewAI

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Four Pillars AI - CrewAI Framework",
    description="Pure CrewAI Implementation of Multi-Agent Business Intelligence Platform (4-Agent Configuration with TinyLlama)",
    version="3.2.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global CrewAI system instance
crewai_system: Optional[FourPillarsCrewAI] = None

# Request/Response Models
class AnalysisRequest(BaseModel):
    scenario: str
    analysis_focus: str = "comprehensive"  # comprehensive, financial, risk, compliance, market

class AnalysisResponse(BaseModel):
    status: str
    analysis_results: Dict[str, Any]
    execution_time: float
    timestamp: str

class TaskRequest(BaseModel):
    scenario: str
    task_type: str  # single_agent, collaborative, competitive

class WebSocketMessage(BaseModel):
    type: str
    data: Dict[str, Any]

@app.on_event("startup")
async def startup_event():
    """Initialize CrewAI system on startup"""
    global crewai_system
    logger.info("🚀 Starting Four Pillars AI with Pure CrewAI Framework...")
    
    try:
        crewai_system = FourPillarsCrewAI()
        await crewai_system.initialize()
        
        logger.info("✅ Four Pillars AI CrewAI system ready!")
    except Exception as e:
        logger.error(f"❌ Startup failed: {e}")
        raise

@app.get("/")
async def root():
    """API root endpoint"""
    return {
        "message": "🚀 Four Pillars AI - Pure CrewAI Framework",
        "status": "operational", 
        "version": "3.2.0",
        "framework": "CrewAI v0.175.0",
        "agents": ["Finance", "Risk", "Compliance", "Market"],
        "models": ["Phi-3.5-mini", "TinyLlama", "Legal-BERT", "TinyLlama (Market)"],
        "gpu_optimization": "RTX 4050 6GB VRAM",
        "endpoints": ["/analyze", "/status", "/health", "/models"],
        "documentation": "/docs"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    if crewai_system is None:
        raise HTTPException(status_code=503, detail="CrewAI system not initialized")
    
    status = await crewai_system.get_system_status()
    return {
        "status": "healthy" if status["is_ready"] else "unhealthy",
        "timestamp": datetime.now().isoformat(),
        "agents": status["agents"],
        "crew_status": status["crew_status"],
        "gpu_enabled": True,
        "system_optimization": "RTX 4050 GPU Multi-Agent"
    }

@app.get("/status")
async def get_detailed_status():
    """Get detailed CrewAI system status"""
    if crewai_system is None:
        raise HTTPException(status_code=503, detail="CrewAI system not initialized")
    
    return await crewai_system.get_system_status()

@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_business_scenario(request: AnalysisRequest):
    """
    Analyze business scenario using CrewAI Four Pillars framework
    
    analysis_focus options:
    - comprehensive: All four pillars analysis (Finance, Risk, Compliance, Market)
    - financial: Financial analysis only (GPU accelerated)
    - risk: Risk assessment only (GPU optimized)
    - compliance: Legal/compliance analysis only (GPU optimized)
    - market: Market intelligence only (GPU optimized with TinyLlama)
    """
    
    if crewai_system is None:
        raise HTTPException(status_code=503, detail="CrewAI system not initialized")
    
    try:
        logger.info(f"🎯 Starting comprehensive CrewAI analysis for: {request.scenario[:50]}...")
        
        # Run CrewAI analysis
        start_time = datetime.now()
        result = await crewai_system.analyze_business_scenario(
            request.scenario, 
            request.analysis_focus
        )
        execution_time = (datetime.now() - start_time).total_seconds()
        
        return AnalysisResponse(
            status="success",
            analysis_results=result,
            execution_time=execution_time,
            timestamp=datetime.now().isoformat()
        )
        
    except Exception as e:
        logger.error(f"❌ CrewAI analysis failed: {e}")
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

@app.get("/models")
async def get_model_info():
    """Get information about loaded models"""
    if crewai_system is None:
        raise HTTPException(status_code=503, detail="CrewAI system not initialized")
    
    return {
        "finance_agent": {
            "model": "microsoft/phi-3.5-mini-instruct",
            "device": "GPU",
            "memory": "~2GB VRAM",
            "specialization": "Financial analysis and investment strategy"
        },
        "risk_agent": {
            "model": "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
            "device": "GPU", 
            "memory": "~0.3GB VRAM",
            "specialization": "Risk assessment and mitigation"
        },
        "compliance_agent": {
            "model": "nlpaueb/legal-bert-base-uncased",
            "device": "GPU",
            "memory": "~0.3GB VRAM", 
            "specialization": "Legal and regulatory compliance"
        },
        "market_agent": {
            "model": "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
            "device": "GPU",
            "memory": "~0.5GB VRAM",
            "specialization": "Market dynamics and competitive analysis"
        }
    }

# Example scenarios for testing
@app.get("/examples")
async def get_example_scenarios():
    """Get example business scenarios for testing"""
    return {
        "examples": [
            {
                "title": "AI Food Delivery Startup",
                "scenario": "A tech startup wants to launch an AI-powered food delivery app that optimizes delivery routes and predicts customer preferences in major urban markets. The platform will use machine learning for demand forecasting and real-time logistics optimization.",
                "analysis_focus": "comprehensive"
            },
            {
                "title": "Fintech Cross-Border Payments",
                "scenario": "A fintech startup is creating a blockchain-based cross-border payment solution for emerging markets with lower transaction fees, faster settlement times, and better exchange rates than traditional banks.",
                "analysis_focus": "comprehensive"
            },
            {
                "title": "Solar Energy Marketplace",
                "scenario": "An environmental startup is building an online marketplace connecting solar panel manufacturers with residential customers, including financing options, installation services, and energy monitoring systems.",
                "analysis_focus": "comprehensive"
            }
        ],
        "focus_options": [
            {
                "value": "comprehensive",
                "description": "Complete Four Pillars analysis with all agents",
                "agents": ["Finance", "Risk", "Compliance", "Market"]
            },
            {
                "value": "financial", 
                "description": "Financial analysis only",
                "agents": ["Finance"]
            },
            {
                "value": "risk",
                "description": "Risk assessment only", 
                "agents": ["Risk"]
            },
            {
                "value": "compliance",
                "description": "Legal/compliance analysis only",
                "agents": ["Compliance"] 
            },
            {
                "value": "market",
                "description": "Market intelligence only",
                "agents": ["Market"]
            }
        ]
    }

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0", 
        port=8000,
        reload=False,  # Disable reload for production model loading
        log_level="info"
    )
