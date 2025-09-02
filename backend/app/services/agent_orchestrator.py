"""
🎯 Agent Orchestrator - Coordinates Multi-Agent Analysis
Manages the Four Pillars agents and their interactions
"""
import asyncio
import logging
from typing import Dict, Any, List, AsyncGenerator
from datetime import datetime
import json

from app.models.finance_agent import FinanceAgent
from app.models.risk_agent import RiskAgent
from app.models.compliance_agent import ComplianceAgent
from app.models.market_agent import MarketAgent

logger = logging.getLogger(__name__)

class AgentOrchestrator:
    def __init__(self):
        self.finance_agent = FinanceAgent()
        self.risk_agent = RiskAgent()
        self.compliance_agent = ComplianceAgent()
        self.market_agent = MarketAgent()
        
        self.agents = [
            self.finance_agent,
            self.risk_agent,
            self.compliance_agent,
            self.market_agent
        ]
        
        self.is_initialized = False
        
    async def initialize_agents(self):
        """Initialize all Four Pillars agents sequentially to avoid GPU memory spikes"""
        logger.info("🚀 Initializing Four Pillars agents...")
        
        try:
            # Initialize CPU agents first (Finance, Risk)
            logger.info("📍 Initializing CPU agents first...")
            await self.finance_agent.initialize()
            await self.risk_agent.initialize()
            
            # Then initialize GPU agents sequentially (Compliance, Market)
            logger.info("📍 Initializing GPU agents...")
            await self.compliance_agent.initialize()
            await self.market_agent.initialize()
            
            self.is_initialized = True
            logger.info("✅ All Four Pillars agents initialized successfully")
            
        except Exception as e:
            logger.error(f"❌ Agent initialization failed: {e}")
            raise
    
    async def analyze_scenario(self, scenario: str) -> Dict[str, Any]:
        """Run complete Four Pillars analysis"""
        if not self.is_initialized:
            raise RuntimeError("Agents not initialized")
        
        logger.info("🔍 Starting Four Pillars analysis...")
        start_time = datetime.now()
        
        try:
            # Run all agents in parallel
            tasks = [
                self.finance_agent.analyze(scenario),
                self.risk_agent.analyze(scenario),
                self.compliance_agent.analyze(scenario),
                self.market_agent.analyze(scenario)
            ]
            
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            # Process results
            analysis_results = {}
            for i, result in enumerate(results):
                agent_name = ["finance", "risk", "compliance", "market"][i]
                
                if isinstance(result, Exception):
                    logger.error(f"❌ {agent_name.title()} agent failed: {result}")
                    analysis_results[agent_name] = {
                        "agent": agent_name.title(),
                        "error": str(result),
                        "analysis": f"{agent_name.title()} analysis failed"
                    }
                else:
                    analysis_results[agent_name] = result
            
            # Calculate execution time
            execution_time = (datetime.now() - start_time).total_seconds()
            
            # Compile final results
            final_results = {
                "scenario": scenario,
                "agents": analysis_results,
                "execution_time": execution_time,
                "timestamp": datetime.now().isoformat(),
                "successful_agents": len([r for r in results if not isinstance(r, Exception)]),
                "total_agents": len(self.agents)
            }
            
            logger.info(f"✅ Four Pillars analysis completed in {execution_time:.2f}s")
            return final_results
            
        except Exception as e:
            logger.error(f"❌ Analysis orchestration failed: {e}")
            raise
    
    async def analyze_with_updates(self, scenario: str) -> AsyncGenerator[Dict[str, Any], None]:
        """Run analysis with real-time updates via WebSocket"""
        if not self.is_initialized:
            raise RuntimeError("Agents not initialized")
        
        logger.info("🔍 Starting streaming Four Pillars analysis...")
        
        # Send start notification
        yield {
            "type": "analysis_start",
            "message": "Four Pillars analysis started",
            "timestamp": datetime.now().isoformat()
        }
        
        # Run agents sequentially for streaming
        agents_config = [
            (self.finance_agent, "finance", "💰"),
            (self.risk_agent, "risk", "🛡️"),
            (self.compliance_agent, "compliance", "⚖️"),
            (self.market_agent, "market", "📈")
        ]
        
        results = {}
        
        for agent, name, emoji in agents_config:
            try:
                # Send agent start notification
                yield {
                    "type": "agent_start",
                    "agent": name,
                    "emoji": emoji,
                    "message": f"{emoji} {name.title()} Agent analyzing...",
                    "timestamp": datetime.now().isoformat()
                }
                
                # Run agent analysis
                result = await agent.analyze(scenario)
                results[name] = result
                
                # Send agent completion
                yield {
                    "type": "agent_complete",
                    "agent": name,
                    "emoji": emoji,
                    "result": result,
                    "message": f"{emoji} {name.title()} Agent completed",
                    "timestamp": datetime.now().isoformat()
                }
                
            except Exception as e:
                logger.error(f"❌ {name.title()} agent failed: {e}")
                yield {
                    "type": "agent_error",
                    "agent": name,
                    "error": str(e),
                    "message": f"❌ {name.title()} Agent failed: {e}",
                    "timestamp": datetime.now().isoformat()
                }
        
        # Send final results
        yield {
            "type": "analysis_complete",
            "results": results,
            "message": "🎉 Four Pillars analysis complete!",
            "timestamp": datetime.now().isoformat()
        }
    
    async def get_agent_status(self) -> Dict[str, Any]:
        """Get status of all agents"""
        return {
            "finance": self.finance_agent.get_status(),
            "risk": self.risk_agent.get_status(),
            "compliance": self.compliance_agent.get_status(),
            "market": self.market_agent.get_status()
        }
    
    async def get_detailed_status(self) -> Dict[str, Any]:
        """Get detailed system status"""
        agent_status = await self.get_agent_status()
        
        return {
            "system": {
                "is_initialized": self.is_initialized,
                "total_agents": len(self.agents),
                "ready_agents": sum(1 for status in agent_status.values() if status.get("is_ready", False)),
                "gpu_enabled": any(status.get("gpu_enabled", False) for status in agent_status.values())
            },
            "agents": agent_status,
            "timestamp": datetime.now().isoformat()
        }
    
    async def reload_agents(self):
        """Reload all agents"""
        logger.info("🔄 Reloading Four Pillars agents...")
        
        # Reset initialization
        self.is_initialized = False
        
        # Reinitialize agents
        await self.initialize_agents()
        
        logger.info("✅ Agents reloaded successfully")
    
    def get_system_info(self) -> Dict[str, Any]:
        """Get system information"""
        return {
            "name": "Four Pillars AI - Multi-Agent System",
            "version": "2.0.0",
            "agents": [
                {"name": "Finance", "emoji": "💰", "model": "gpt2"},
                {"name": "Risk", "emoji": "🛡️", "model": "gpt2-medium"},
                {"name": "Compliance", "emoji": "⚖️", "model": "distilbert-base-uncased"},
                {"name": "Market", "emoji": "📈", "model": "gpt2-large"}
            ],
            "gpu_optimized": True,
            "hardware": "RTX 4050 Laptop GPU"
        }
