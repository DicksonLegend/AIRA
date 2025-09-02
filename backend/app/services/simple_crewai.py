"""
🚀 Four Pillars AI - Real Model Implementation
Direct GPU/CPU optimized model usage without CrewAI dependency
"""
import asyncio
import logging
from typing import Dict, Any
from datetime import datetime

# Import our real optimized model agents
from app.models.finance_agent import FinanceAgent
from app.models.risk_agent import RiskAgent
from app.models.compliance_agent import ComplianceAgent
from app.models.market_agent import MarketAgent

logger = logging.getLogger(__name__)

class FourPillarsCrewAI:
    """
    Four Pillars AI implementation using real GPU/CPU optimized models
    """
    
    def __init__(self):
        # Initialize our real model agents
        self.finance_model = FinanceAgent()
        self.risk_model = RiskAgent()
        self.compliance_model = ComplianceAgent()
        self.market_model = MarketAgent()
        
        self.is_initialized = False
        
    async def initialize(self):
        """Initialize real model agents with GPU/CPU optimization"""
        logger.info("🚀 Initializing Four Pillars AI with real GPU/CPU models...")
        
        try:
            # Initialize CPU agents first (Finance, Risk)
            logger.info("📍 Loading CPU agents first...")
            await self.finance_model.initialize()
            await self.risk_model.initialize()
            
            # Then initialize GPU agents (Compliance, Market)
            logger.info("📍 Loading GPU agents...")
            await self.compliance_model.initialize()
            await self.market_model.initialize()
            
            self.is_initialized = True
            logger.info("✅ Four Pillars AI system ready with real models!")
            logger.info(f"💰 Finance Agent: {self.finance_model.model_name} on {self.finance_model.device.upper()}")
            logger.info(f"🛡️ Risk Agent: {self.risk_model.model_name} on {self.risk_model.device.upper()}")
            logger.info(f"⚖️ Compliance Agent: {self.compliance_model.model_name} on {self.compliance_model.device.upper()}")
            logger.info(f"📈 Market Agent: {self.market_model.model_name} on {self.market_model.device.upper()}")
            
        except Exception as e:
            logger.error(f"❌ Model initialization failed: {e}")
            raise
    
    async def analyze_business_scenario(self, scenario: str, analysis_focus: str = "comprehensive") -> Dict[str, Any]:
        """
        Run real Four Pillars analysis using GPU/CPU optimized models
        """
        if not self.is_initialized:
            await self.initialize()
        
        logger.info(f"🎯 Starting {analysis_focus} analysis with real models...")
        start_time = datetime.now()
        
        try:
            results = {}
            
            if analysis_focus == "comprehensive" or analysis_focus == "financial":
                logger.info("💰 Running Finance Agent analysis...")
                finance_result = await self.finance_model.analyze(scenario)
                results["finance"] = finance_result
                
            if analysis_focus == "comprehensive" or analysis_focus == "risk":
                logger.info("🛡️ Running Risk Agent analysis...")
                risk_result = await self.risk_model.analyze(scenario)
                results["risk"] = risk_result
                
            if analysis_focus == "comprehensive" or analysis_focus == "compliance":
                logger.info("⚖️ Running Compliance Agent analysis...")
                compliance_result = await self.compliance_model.analyze(scenario)
                results["compliance"] = compliance_result
                
            if analysis_focus == "comprehensive" or analysis_focus == "market":
                logger.info("📈 Running Market Agent analysis...")
                market_result = await self.market_model.analyze(scenario)
                results["market"] = market_result
            
            execution_time = (datetime.now() - start_time).total_seconds()
            
            # Compile final results
            result = {
                "scenario": scenario,
                "analysis_focus": analysis_focus,
                "timestamp": datetime.now().isoformat(),
                "execution_time_seconds": execution_time,
                "framework": "Four Pillars AI - Direct Models",
                "crew_result": f"Real {analysis_focus} analysis completed using GPU/CPU optimized models",
                "agents_utilized": list(results.keys()),
                "device_allocation": {
                    "finance": self.finance_model.device,
                    "risk": self.risk_model.device,
                    "compliance": self.compliance_model.device,
                    "market": self.market_model.device
                },
                "system_info": {
                    "gpu_agents": [name for name, agent in [
                        ("finance", self.finance_model),
                        ("risk", self.risk_model), 
                        ("compliance", self.compliance_model),
                        ("market", self.market_model)
                    ] if agent.device == "cuda"],
                    "cpu_agents": [name for name, agent in [
                        ("finance", self.finance_model),
                        ("risk", self.risk_model),
                        ("compliance", self.compliance_model), 
                        ("market", self.market_model)
                    ] if agent.device == "cpu"],
                    "total_agents": len(results),
                    "optimization": "RTX 4050 GPU + CPU Distribution"
                },
                "performance_metrics": {
                    "execution_time": f"{execution_time:.2f}s",
                    "agents_count": len(results),
                    "tasks_completed": len(results)
                },
                "detailed_results": results
            }
            
            logger.info(f"✅ Real Four Pillars analysis completed in {execution_time:.2f}s")
            return result
            
        except Exception as e:
            logger.error(f"❌ Analysis failed: {e}")
            raise
    
    def _get_agents_for_focus(self, focus: str):
        """Get agents based on analysis focus"""
        if focus == "comprehensive":
            return ["finance", "risk", "compliance", "market"]
        elif focus == "financial":
            return ["finance"]
        elif focus == "risk":
            return ["risk"]
        elif focus == "compliance":
            return ["compliance"]
        elif focus == "market":
            return ["market"]
        else:
            return ["finance", "risk", "compliance", "market"]
    
    async def get_system_status(self) -> Dict[str, Any]:
        """Get real system status with GPU/CPU allocation"""
        return {
            "initialized": self.is_initialized,
            "framework": "Four Pillars AI - Direct Models",
            "version": "3.0.0",
            "agents": {
                "finance": {
                    "model": self.finance_model.model_name,
                    "device": self.finance_model.device,
                    "ready": self.finance_model.is_ready,
                    "role": "Financial Strategist"
                },
                "risk": {
                    "model": self.risk_model.model_name,
                    "device": self.risk_model.device,
                    "ready": self.risk_model.is_ready,
                    "role": "Risk Assessment Specialist"
                },
                "compliance": {
                    "model": self.compliance_model.model_name,
                    "device": self.compliance_model.device,
                    "ready": self.compliance_model.is_ready,
                    "role": "Legal & Compliance Expert"
                },
                "market": {
                    "model": self.market_model.model_name,
                    "device": self.market_model.device,
                    "ready": self.market_model.is_ready,
                    "role": "Market Intelligence Analyst"
                }
            },
            "crew_status": {
                "assembled": True,
                "process": "sequential",
                "real_models": True,
                "gpu_optimization": True
            }
        }
