"""
🚀 FOUR PILLARS AI - Pure CrewAI Framework Backend
Complete CrewAI Multi-Agent Business Intelligence Platform
RTX 4050 GPU Optimized - No Manual Orchestrator
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
    description="Pure CrewAI Implementation of Multi-Agent Business Intelligence Platform",
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

# Global CrewAI instance (No manual orchestrator)
crewai_system = None

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
        "version": "3.0.0",
        "framework": "CrewAI v0.175.0",
        "orchestration": "Pure CrewAI (No Manual Orchestrator)",
        "features": {
            "multi_agent_crews": True,
            "gpu_optimized": True,
            "hackathon_ready": True,
            "structured_workflows": True,
            "crew_coordination": True,
            "memory_enabled": True,
            "planning_enabled": True
        },
        "endpoints": {
            "analyze": "/analyze",
            "health": "/health",
            "status": "/status",
            "types": "/analyze/types",
            "examples": "/examples",
            "system_info": "/system/info",
            "docs": "/docs"
        }
    }

@app.get("/health")
async def health_check():
    """System health check"""
    if crewai_system is None:
        raise HTTPException(status_code=503, detail="CrewAI system not initialized")
    
    status = await crewai_system.get_system_status()
    
    return {
        "status": "healthy" if status["initialized"] else "initializing",
        "timestamp": datetime.now().isoformat(),
        "framework": status["framework"],
        "version": status["version"],
        "orchestration": "Pure CrewAI Framework",
        "agents": status["agents"],
        "crew_status": status["crew_status"],
        "gpu_enabled": True,
        "system_optimization": "RTX 4050 GPU + CPU Multi-Agent"
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
    - risk: Risk assessment only (CPU optimized)
    - compliance: Legal/compliance analysis only (CPU optimized)
    - market: Market intelligence only (CPU optimized)
    """
    if crewai_system is None:
        raise HTTPException(status_code=503, detail="CrewAI system not initialized")
    
    try:
        logger.info(f"🎯 Starting {request.analysis_focus} CrewAI analysis for: {request.scenario[:50]}...")
        
        # Run CrewAI analysis
        result = await crewai_system.analyze_business_scenario(
            request.scenario, 
            request.analysis_focus
        )
        
        logger.info(f"✅ CrewAI analysis completed in {result['execution_time_seconds']:.2f}s")
        
        return AnalysisResponse(**result)
        
    except Exception as e:
        logger.error(f"❌ CrewAI analysis failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/analyze/{analysis_type}")
async def analyze_with_specific_type(analysis_type: str, request: AnalysisRequest):
    """Run specific type of CrewAI analysis"""
    valid_types = ["comprehensive", "financial", "risk", "compliance", "market"]
    if analysis_type not in valid_types:
        raise HTTPException(
            status_code=400, 
            detail=f"Invalid analysis type. Must be one of: {valid_types}"
        )
    
    if crewai_system is None:
        raise HTTPException(status_code=503, detail="CrewAI system not initialized")
    
    try:
        logger.info(f"🎯 Starting {analysis_type} CrewAI analysis...")
        
        result = await crewai_system.analyze_business_scenario(
            request.scenario, 
            analysis_type
        )
        
        return AnalysisResponse(**result)
        
    except Exception as e:
        logger.error(f"❌ CrewAI {analysis_type} analysis failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/analyze/types")
async def get_analysis_types():
    """Get available analysis types and their descriptions"""
    return {
        "analysis_types": {
            "comprehensive": {
                "description": "Complete Four Pillars analysis with all agents",
                "agents": ["finance", "risk", "compliance", "market"],
                "duration": "30-60 seconds",
                "use_case": "Full business evaluation and strategy",
                "output": "Complete business assessment with all aspects covered",
                "device_allocation": "GPU (Finance) + CPU (Risk, Compliance, Market)"
            },
            "financial": {
                "description": "GPU-accelerated financial analysis and investment strategy",
                "agents": ["finance"],
                "duration": "10-20 seconds", 
                "use_case": "Funding, revenue projections, financial planning",
                "output": "Detailed financial analysis and recommendations",
                "device_allocation": "GPU (RTX 4050)"
            },
            "risk": {
                "description": "CPU-optimized risk assessment and mitigation strategies",
                "agents": ["risk"],
                "duration": "10-20 seconds",
                "use_case": "Risk management and contingency planning",
                "output": "Comprehensive risk analysis with mitigation plans",
                "device_allocation": "CPU"
            },
            "compliance": {
                "description": "CPU-optimized legal and regulatory compliance analysis",
                "agents": ["compliance"],
                "duration": "10-20 seconds",
                "use_case": "Legal requirements and governance frameworks",
                "output": "Compliance roadmap and legal considerations",
                "device_allocation": "CPU"
            },
            "market": {
                "description": "CPU-based market intelligence and competitive analysis",
                "agents": ["market"],
                "duration": "10-20 seconds",
                "use_case": "Market strategy, competition, and positioning",
                "output": "Market analysis with strategic recommendations",
                "device_allocation": "CPU"
            }
        },
        "framework_info": {
            "orchestration": "Pure CrewAI Framework",
            "process": "Sequential with memory and planning",
            "optimization": "RTX 4050 GPU (Finance) + CPU (Risk, Compliance, Market)",
            "version": "CrewAI v0.175.0"
        }
    }

@app.get("/examples")
async def get_example_scenarios():
    """Get example business scenarios for testing CrewAI analysis"""
    return {
        "example_scenarios": [
            {
                "title": "AI Food Delivery Startup",
                "scenario": "A tech startup wants to launch an AI-powered food delivery app that optimizes delivery routes and predicts customer preferences in major urban markets. The platform will use machine learning for demand forecasting and real-time logistics optimization.",
                "recommended_analysis": "comprehensive",
                "focus_areas": ["financial modeling", "market entry strategy", "regulatory compliance", "operational risks"],
                "estimated_duration": "45-60 seconds"
            },
            {
                "title": "SaaS Analytics Platform",
                "scenario": "A B2B SaaS company is developing a business intelligence platform for small to medium enterprises with real-time analytics, automated reporting, and predictive insights. The platform targets companies with 50-500 employees.",
                "recommended_analysis": "financial",
                "focus_areas": ["subscription pricing", "customer acquisition", "revenue projections", "market sizing"],
                "estimated_duration": "15-20 seconds"
            },
            {
                "title": "FinTech Payment Solution",
                "scenario": "A fintech startup is creating a blockchain-based cross-border payment solution for emerging markets with lower transaction fees, faster settlement times, and better exchange rates than traditional banks.",
                "recommended_analysis": "compliance", 
                "focus_areas": ["regulatory requirements", "financial licensing", "data protection", "international compliance"],
                "estimated_duration": "15-20 seconds"
            },
            {
                "title": "Green Energy Marketplace",
                "scenario": "An environmental startup is building an online marketplace connecting solar panel manufacturers with residential customers, including financing options, installation services, and energy monitoring systems.",
                "recommended_analysis": "market",
                "focus_areas": ["competitive landscape", "market trends", "customer segments", "growth opportunities"],
                "estimated_duration": "15-20 seconds"
            },
            {
                "title": "EdTech Learning Platform",
                "scenario": "An education technology company is developing an AI-powered personalized learning platform for K-12 students that adapts to individual learning styles and provides real-time progress tracking for parents and teachers.",
                "recommended_analysis": "risk",
                "focus_areas": ["market risks", "technology risks", "regulatory risks", "execution challenges"],
                "estimated_duration": "15-20 seconds"
            }
        ],
        "usage_tips": {
            "comprehensive": "Best for complete business evaluation and investor presentations",
            "specific_focus": "Use targeted analysis for specific decision-making needs",
            "iterative": "Run multiple focused analyses to deep-dive into specific areas",
            "gpu_optimization": "Financial analysis uses GPU acceleration for complex modeling"
        }
    }

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket for real-time CrewAI analysis updates"""
    await websocket.accept()
    logger.info("🔌 WebSocket connected for CrewAI real-time updates")
    
    try:
        while True:
            # Wait for scenario data
            data = await websocket.receive_text()
            scenario_data = json.loads(data)
            
            # Send start notification
            await websocket.send_text(json.dumps({
                "type": "analysis_started",
                "scenario": scenario_data["scenario"],
                "framework": "CrewAI",
                "analysis_focus": scenario_data.get("analysis_focus", "comprehensive"),
                "timestamp": datetime.now().isoformat()
            }))
            
            # Run CrewAI analysis
            try:
                result = await crewai_system.analyze_business_scenario(
                    scenario_data["scenario"],
                    scenario_data.get("analysis_focus", "comprehensive")
                )
                
                # Send result
                await websocket.send_text(json.dumps({
                    "type": "analysis_complete",
                    "result": result,
                    "timestamp": datetime.now().isoformat()
                }))
                
            except Exception as e:
                await websocket.send_text(json.dumps({
                    "type": "analysis_error",
                    "error": str(e),
                    "timestamp": datetime.now().isoformat()
                }))
                
    except WebSocketDisconnect:
        logger.info("🔌 WebSocket disconnected")
    except Exception as e:
        logger.error(f"❌ WebSocket error: {e}")
        await websocket.close()

@app.get("/system/info")
async def get_system_info():
    """Get detailed system information"""
    return {
        "framework": "CrewAI v0.175.0",
        "orchestration": "Pure CrewAI Framework (No Manual Orchestrator)",
        "architecture": "Multi-Agent Crew System",
        "optimization": {
            "gpu_agent": "Finance (RTX 4050 6GB VRAM)",
            "cpu_agents": ["Risk", "Compliance", "Market"],
            "memory_enabled": True,
            "planning_enabled": True,
            "sequential_processing": True
        },
        "capabilities": {
            "parallel_agent_coordination": True,
            "structured_workflows": True,
            "role_based_agents": True,
            "memory_persistence": True,
            "hackathon_ready": True,
            "gpu_acceleration": True
        },
        "deployment": {
            "backend": "FastAPI",
            "ai_framework": "CrewAI",
            "gpu_support": "RTX 4050 6GB VRAM",
            "python_version": "3.13+",
            "pytorch": "2.7.1+cu118",
            "cuda_version": "11.8"
        },
        "performance": {
            "comprehensive_analysis": "30-60 seconds",
            "single_agent_analysis": "10-20 seconds",
            "gpu_acceleration": "Finance Agent only",
            "concurrent_requests": "Supported"
        }
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
