"""
🚀 FOUR PILLARS AI - CrewAI Framework Backend
Pure CrewAI Multi-Agent Business Intelligence Platform
RTX 4050 GPU Optimized
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
    title="Four Pillars AI - Multi-Agent System",
    description="AI-Powered Business Intelligence Platform with RTX 4050 GPU Optimization",
    version="2.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global instances
crewai_system = None

@app.on_event("startup")
async def startup_event():
    """Initialize CrewAI system on startup"""
    global crewai_system
    logger.info("🚀 Starting Four Pillars AI with CrewAI Framework...")
    
    try:
        crewai_system = FourPillarsCrewAI()
        await crewai_system.initialize()
        
        logger.info("✅ Four Pillars AI CrewAI system ready!")
    except Exception as e:
        logger.error(f"❌ Startup failed: {e}")
        raise

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "message": "🚀 Four Pillars AI - CrewAI Enhanced Multi-Agent System",
        "status": "operational",
        "version": "2.0.0",
        "features": {
            "gpu_optimized": True,
            "crewai_enabled": True,
            "dual_orchestration": True
        },
        "endpoints": {
            "original_analysis": "/analyze",
            "crewai_analysis": "/crewai/analyze",
            "health_check": "/health",
            "documentation": "/docs"
        }
    }

@app.get("/health")
async def health_check():
    """System health check"""
    if orchestrator is None or crewai_orchestrator is None:
        raise HTTPException(status_code=503, detail="System not fully initialized")
    
    agent_status = await orchestrator.get_agent_status()
    crewai_status = await crewai_orchestrator.get_crew_status()
    
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "original_system": {
            "agents": agent_status,
            "initialized": True
        },
        "crewai_system": crewai_status,
        "gpu_enabled": True,
        "framework_versions": {
            "fastapi": "latest",
            "crewai": "0.175.0",
            "pytorch": "2.7.1+cu118"
        }
    }

@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_scenario(request: AnalysisRequest):
    """Run Four Pillars analysis on business scenario (Original Orchestrator)"""
    if orchestrator is None:
        raise HTTPException(status_code=503, detail="System not initialized")
    
    try:
        logger.info(f"🔍 Starting analysis for: {request.scenario[:50]}...")
        
        # Run multi-agent analysis
        results = await orchestrator.analyze_scenario(request.scenario)
        
        # Process through decision engine
        recommendation = decision_engine.generate_recommendation(results)
        
        response = AnalysisResponse(
            scenario=request.scenario,
            results=results,
            recommendation=recommendation,
            timestamp=datetime.now().isoformat(),
            confidence_score=recommendation.get("confidence", 0.0)
        )
        
        logger.info(f"✅ Analysis complete - Score: {response.confidence_score}")
        return response
        
    except Exception as e:
        logger.error(f"❌ Analysis failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/crewai/analyze")
async def analyze_with_crewai(request: AnalysisRequest):
    """Run CrewAI-orchestrated Four Pillars analysis (Next-Gen)"""
    if crewai_orchestrator is None:
        raise HTTPException(status_code=503, detail="CrewAI system not initialized")
    
    try:
        logger.info(f"🎯 Starting CrewAI analysis for: {request.scenario[:50]}...")
        
        # Use 'comprehensive' as default analysis type
        analysis_type = getattr(request, 'analysis_type', 'comprehensive')
        
        # Run CrewAI multi-agent analysis
        results = await crewai_orchestrator.analyze_scenario_with_crew(
            request.scenario, 
            analysis_type
        )
        
        logger.info(f"✅ CrewAI analysis complete in {results.get('execution_time', 0):.2f}s")
        return results
        
    except Exception as e:
        logger.error(f"❌ CrewAI analysis failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/crewai/analyze/{analysis_type}")
async def analyze_with_crewai_typed(analysis_type: str, request: AnalysisRequest):
    """Run specific type of CrewAI analysis"""
    if crewai_orchestrator is None:
        raise HTTPException(status_code=503, detail="CrewAI system not initialized")
    
    valid_types = ["comprehensive", "financial", "risk", "market", "compliance"]
    if analysis_type not in valid_types:
        raise HTTPException(
            status_code=400, 
            detail=f"Invalid analysis type. Must be one of: {valid_types}"
        )
    
    try:
        logger.info(f"🎯 Starting {analysis_type} CrewAI analysis...")
        
        results = await crewai_orchestrator.analyze_scenario_with_crew(
            request.scenario, 
            analysis_type
        )
        
        return results
        
    except Exception as e:
        logger.error(f"❌ CrewAI {analysis_type} analysis failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket for real-time analysis updates"""
    await websocket.accept()
    logger.info("🔌 WebSocket connected")
    
    try:
        while True:
            # Wait for scenario data
            data = await websocket.receive_text()
            scenario_data = json.loads(data)
            
            # Run analysis with real-time updates
            async for update in orchestrator.analyze_with_updates(scenario_data["scenario"]):
                await websocket.send_text(json.dumps(update))
                
    except WebSocketDisconnect:
        logger.info("🔌 WebSocket disconnected")
    except Exception as e:
        logger.error(f"❌ WebSocket error: {e}")
        await websocket.close()

@app.get("/agents/status")
async def get_agents_status():
    """Get detailed status of all agents (Original)"""
    if orchestrator is None:
        raise HTTPException(status_code=503, detail="System not initialized")
    
    return await orchestrator.get_detailed_status()

@app.get("/crewai/status")
async def get_crewai_status():
    """Get CrewAI system status"""
    if crewai_orchestrator is None:
        raise HTTPException(status_code=503, detail="CrewAI system not initialized")
    
    return await crewai_orchestrator.get_crew_status()

@app.get("/systems/compare")
async def compare_systems():
    """Compare Original vs CrewAI orchestrators"""
    return {
        "original_orchestrator": {
            "status": "ready" if orchestrator else "not_initialized",
            "description": "Direct agent coordination",
            "strengths": ["Fast initialization", "Direct control", "Custom optimization"],
            "use_case": "Production deployments"
        },
        "crewai_orchestrator": {
            "status": "ready" if crewai_orchestrator else "not_initialized", 
            "description": "CrewAI framework coordination",
            "strengths": ["Structured workflows", "Role-based agents", "Hackathon-ready"],
            "use_case": "Demos, prototypes, structured analysis"
        },
        "recommendation": "Use CrewAI for hackathons and demos, Original for production"
    }

@app.post("/agents/reload")
async def reload_agents():
    """Reload all AI agents"""
    global orchestrator
    
    try:
        logger.info("🔄 Reloading agents...")
        await orchestrator.reload_agents()
        logger.info("✅ Agents reloaded successfully")
        return {"message": "Agents reloaded successfully"}
    except Exception as e:
        logger.error(f"❌ Agent reload failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
