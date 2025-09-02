"""
🚀 Four Pillars AI - Pure CrewAI Implementation
FastAPI backend powered entirely by CrewAI framework
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import asyncio
import logging
from typing import Dict, Any, Optional
from datetime import datetime

from app.services.four_pillars_crewai import FourPillarsCrewAI

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Four Pillars AI - CrewAI Framework",
    description="Pure CrewAI Implementation of Multi-Agent Business Intelligence",
    version="3.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global CrewAI instance
crew_system = None

# Request/Response Models
class AnalysisRequest(BaseModel):
    scenario: str
    analysis_focus: Optional[str] = "comprehensive"

class AnalysisResponse(BaseModel):
    scenario: str
    analysis_focus: str
    timestamp: str
    execution_time_seconds: float
    framework: str
    crew_result: str
    agents_utilized: list
    device_allocation: dict
    system_info: dict
    performance_metrics: dict

@app.on_event("startup")
async def startup_event():
    """Initialize CrewAI system on startup"""
    global crew_system
    logger.info("🚀 Starting Four Pillars AI with CrewAI Framework...")
    
    try:
        crew_system = FourPillarsCrewAI()
        await crew_system.initialize()
        
        logger.info("✅ Four Pillars AI CrewAI system ready!")
    except Exception as e:
        logger.error(f"❌ Startup failed: {e}")
        raise

@app.get("/")
async def root():
    """API root endpoint"""
    return {
        "message": "🚀 Four Pillars AI - CrewAI Framework",
        "status": "operational", 
        "version": "3.0.0",
        "framework": "CrewAI v0.175.0",
        "features": {
            "multi_agent_analysis": True,
            "gpu_optimized": True,
            "hackathon_ready": True,
            "structured_workflows": True
        },
        "endpoints": {
            "analyze": "/analyze",
            "health": "/health",
            "status": "/status",
            "docs": "/docs"
        }
    }

@app.get("/health")
async def health_check():
    """System health check"""
    if crew_system is None:
        raise HTTPException(status_code=503, detail="CrewAI system not initialized")
    
    status = await crew_system.get_system_status()
    
    return {
        "status": "healthy" if status["initialized"] else "initializing",
        "timestamp": datetime.now().isoformat(),
        "framework": status["framework"],
        "version": status["version"],
        "agents": status["agents"],
        "crew_status": status["crew_status"]
    }

@app.get("/status")
async def get_detailed_status():
    """Get detailed system status"""
    if crew_system is None:
        raise HTTPException(status_code=503, detail="CrewAI system not initialized")
    
    return await crew_system.get_system_status()

@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_business_scenario(request: AnalysisRequest):
    """
    Analyze business scenario using CrewAI Four Pillars framework
    
    analysis_focus options:
    - comprehensive: All four pillars analysis
    - financial: Financial analysis only
    - risk: Risk assessment only
    - compliance: Legal/compliance analysis only
    - market: Market intelligence only
    """
    if crew_system is None:
        raise HTTPException(status_code=503, detail="CrewAI system not initialized")
    
    try:
        logger.info(f"🎯 Starting {request.analysis_focus} analysis for: {request.scenario[:50]}...")
        
        # Run CrewAI analysis
        result = await crew_system.analyze_business_scenario(
            request.scenario, 
            request.analysis_focus
        )
        
        logger.info(f"✅ Analysis completed in {result['execution_time_seconds']:.2f}s")
        
        return AnalysisResponse(**result)
        
    except Exception as e:
        logger.error(f"❌ Analysis failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/analyze/types")
async def get_analysis_types():
    """Get available analysis types"""
    return {
        "analysis_types": {
            "comprehensive": {
                "description": "Complete Four Pillars analysis",
                "agents": ["finance", "risk", "compliance", "market"],
                "duration": "30-60 seconds",
                "use_case": "Full business evaluation"
            },
            "financial": {
                "description": "Financial analysis and investment strategy",
                "agents": ["finance"],
                "duration": "10-20 seconds", 
                "use_case": "Funding and financial planning"
            },
            "risk": {
                "description": "Risk assessment and mitigation",
                "agents": ["risk"],
                "duration": "10-20 seconds",
                "use_case": "Risk management and planning"
            },
            "compliance": {
                "description": "Legal and regulatory compliance",
                "agents": ["compliance"],
                "duration": "10-20 seconds",
                "use_case": "Legal requirements and governance"
            },
            "market": {
                "description": "Market intelligence and competitive analysis",
                "agents": ["market"],
                "duration": "10-20 seconds",
                "use_case": "Market strategy and positioning"
            }
        }
    }

# Example scenarios endpoint for testing
@app.get("/examples")
async def get_example_scenarios():
    """Get example business scenarios for testing"""
    return {
        "example_scenarios": [
            {
                "title": "AI Food Delivery Startup",
                "scenario": "A tech startup wants to launch an AI-powered food delivery app that optimizes delivery routes and predicts customer preferences in major urban markets.",
                "recommended_analysis": "comprehensive"
            },
            {
                "title": "SaaS Analytics Platform",
                "scenario": "A B2B SaaS company is developing a business intelligence platform for small to medium enterprises with real-time analytics and automated reporting.",
                "recommended_analysis": "financial"
            },
            {
                "title": "FinTech Payment Solution",
                "scenario": "A fintech startup is creating a blockchain-based cross-border payment solution for emerging markets with lower transaction fees.",
                "recommended_analysis": "compliance"
            },
            {
                "title": "Green Energy Marketplace",
                "scenario": "An environmental startup is building a marketplace connecting solar panel manufacturers with residential customers, including financing options.",
                "recommended_analysis": "market"
            }
        ]
    }

if __name__ == "__main__":
    uvicorn.run(
        "crewai_main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
