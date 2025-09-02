"""
🚀 FOUR PILLARS AI - FastAPI Backend
Multi-Agent Business Intelligence Platform
RTX 4050 GPU Optimized
"""
from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import asyncio
import logging
from typing import Dict, Any, List
import json
from datetime import datetime

from app.services.agent_orchestrator import AgentOrchestrator
from app.services.decision_engine import DecisionEngine
from app.schemas.schemas import AnalysisRequest, AnalysisResponse

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
orchestrator = None
decision_engine = None

@app.on_event("startup")
async def startup_event():
    """Initialize AI agents on startup"""
    global orchestrator, decision_engine
    logger.info("🚀 Starting Four Pillars AI System...")
    
    try:
        orchestrator = AgentOrchestrator()
        await orchestrator.initialize_agents()
        
        decision_engine = DecisionEngine()
        
        logger.info("✅ Four Pillars AI System ready!")
    except Exception as e:
        logger.error(f"❌ Startup failed: {e}")
        raise

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "message": "🏗️ Four Pillars AI - Multi-Agent System",
        "status": "operational",
        "version": "2.0.0",
        "gpu_optimized": True
    }

@app.get("/health")
async def health_check():
    """System health check"""
    if orchestrator is None:
        raise HTTPException(status_code=503, detail="System not initialized")
    
    agent_status = await orchestrator.get_agent_status()
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "agents": agent_status,
        "gpu_enabled": True
    }

@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_scenario(request: AnalysisRequest):
    """Run Four Pillars analysis on business scenario"""
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
    """Get detailed status of all agents"""
    if orchestrator is None:
        raise HTTPException(status_code=503, detail="System not initialized")
    
    return await orchestrator.get_detailed_status()

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
