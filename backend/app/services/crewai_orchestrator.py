"""
🚀 CrewAI Orchestrator - Next-Gen Multi-Agent Business Intelligence
CrewAI-powered coordination of Four Pillars agents for hackathon-ready analysis
"""
import asyncio
import logging
from typing import Dict, Any, List, Optional
from datetime import datetime
import json

from crewai import Agent, Task, Crew, Process

from app.models.finance_agent import FinanceAgent
from app.models.risk_agent import RiskAgent
from app.models.compliance_agent import ComplianceAgent
from app.models.market_agent import MarketAgent

logger = logging.getLogger(__name__)

class CrewAIOrchestrator:
    """
    CrewAI-powered orchestrator for Four Pillars AI system
    - Parallel execution for time-bound hackathons
    - Structured outputs for judges
    - Clear role separation
    - Scalable model swapping
    """
    
    def __init__(self):
        # Initialize our existing agents
        self.finance_model = FinanceAgent()
        self.risk_model = RiskAgent()
        self.compliance_model = ComplianceAgent()
        self.market_model = MarketAgent()
        
        # CrewAI agents (will be initialized after models are ready)
        self.crew_agents = {}
        self.crew = None
        self.is_initialized = False
        
    async def initialize_agents(self):
        """Initialize all Four Pillars agents and set up CrewAI crew"""
        logger.info("🚀 Initializing CrewAI Four Pillars system...")
        
        try:
            # Initialize our existing model agents first
            tasks = [
                self.finance_model.initialize(),
                self.risk_model.initialize(),
                self.compliance_model.initialize(),
                self.market_model.initialize()
            ]
            await asyncio.gather(*tasks)
            
            # Set up CrewAI agents
            self._setup_crewai_agents()
            
            self.is_initialized = True
            logger.info("✅ CrewAI Four Pillars system initialized successfully")
            
        except Exception as e:
            logger.error(f"❌ CrewAI initialization failed: {e}")
            raise
    
    def _setup_crewai_agents(self):
        """Set up CrewAI agents with custom LLM wrappers"""
        
        # Finance Agent - GPU-accelerated for complex financial modeling
        self.crew_agents['finance'] = Agent(
            role="Finance Agent",
            goal="Analyze funding strategy, KPIs, ROI projections, and financial viability",
            backstory="""You are an expert financial analyst with deep expertise in startup 
            funding, financial modeling, and investment analysis. You use advanced AI models 
            to provide comprehensive financial insights.""",
            verbose=True,
            allow_delegation=False,
            llm=CustomLLMWrapper(self.finance_model, "Finance", "💰")
        )
        
        # Risk Agent - CPU-optimized for fast risk assessment
        self.crew_agents['risk'] = Agent(
            role="Risk Assessment Specialist",
            goal="Evaluate market risks, execution challenges, and mitigation strategies",
            backstory="""You are a risk management expert specializing in startup and 
            business risk assessment. You quickly identify potential pitfalls and provide 
            actionable mitigation strategies.""",
            verbose=True,
            allow_delegation=False,
            llm=CustomLLMWrapper(self.risk_model, "Risk", "🛡️")
        )
        
        # Compliance Agent - CPU-optimized for legal compliance
        self.crew_agents['compliance'] = Agent(
            role="Compliance & Legal Expert",
            goal="Check regulatory compliance, legal requirements, and governance issues",
            backstory="""You are a legal and compliance expert with deep knowledge of 
            business regulations, legal requirements, and governance frameworks. You ensure 
            all business activities comply with relevant laws and standards.""",
            verbose=True,
            allow_delegation=False,
            llm=CustomLLMWrapper(self.compliance_model, "Compliance", "⚖️")
        )
        
        # Market Agent - CPU-based for comprehensive market analysis
        self.crew_agents['market'] = Agent(
            role="Market Intelligence Analyst",
            goal="Analyze market trends, competition, and opportunities",
            backstory="""You are a market research and competitive intelligence expert. 
            You analyze market dynamics, competitive landscapes, and identify strategic 
            opportunities for business growth.""",
            verbose=True,
            allow_delegation=False,
            llm=CustomLLMWrapper(self.market_model, "Market", "📈")
        )
        
        logger.info("🎯 CrewAI agents configured with GPU/CPU optimization")
    
    async def analyze_scenario_with_crew(self, scenario: str, analysis_type: str = "comprehensive") -> Dict[str, Any]:
        """
        Run CrewAI-orchestrated analysis of business scenario
        
        Args:
            scenario: Business scenario to analyze
            analysis_type: Type of analysis ('comprehensive', 'financial', 'risk', 'market')
        """
        if not self.is_initialized:
            await self.initialize_agents()
        
        logger.info(f"🎯 Starting CrewAI analysis: {analysis_type}")
        
        try:
            # Define tasks based on analysis type
            tasks = self._create_tasks(scenario, analysis_type)
            
            # Create crew with appropriate process
            crew = Crew(
                agents=list(self.crew_agents.values()),
                tasks=tasks,
                process=Process.hierarchical if analysis_type == "comprehensive" else Process.sequential,
                verbose=True,
                manager_llm=CustomLLMWrapper(self.finance_model, "Manager", "🎯")  # Finance agent as manager
            )
            
            # Execute the crew
            start_time = datetime.now()
            logger.info("🚀 CrewAI crew starting execution...")
            
            # Run crew synchronously (CrewAI doesn't support async yet)
            result = await asyncio.get_event_loop().run_in_executor(
                None, crew.kickoff
            )
            
            execution_time = (datetime.now() - start_time).total_seconds()
            
            # Format results for API response
            formatted_result = self._format_crew_results(result, execution_time, analysis_type)
            
            logger.info(f"✅ CrewAI analysis completed in {execution_time:.2f}s")
            return formatted_result
            
        except Exception as e:
            logger.error(f"❌ CrewAI analysis failed: {e}")
            raise
    
    def _create_tasks(self, scenario: str, analysis_type: str) -> List[Task]:
        """Create CrewAI tasks based on analysis type"""
        
        base_scenario = f"Business Scenario: {scenario}"
        
        if analysis_type == "comprehensive":
            return [
                Task(
                    description=f"{base_scenario}\n\nProvide comprehensive financial analysis including funding requirements, revenue projections, cost structure, and ROI calculations.",
                    agent=self.crew_agents['finance']
                ),
                Task(
                    description=f"{base_scenario}\n\nConduct thorough risk assessment covering market risks, execution challenges, financial risks, and provide mitigation strategies.",
                    agent=self.crew_agents['risk']
                ),
                Task(
                    description=f"{base_scenario}\n\nAnalyze regulatory compliance requirements, legal considerations, and governance frameworks needed.",
                    agent=self.crew_agents['compliance']
                ),
                Task(
                    description=f"{base_scenario}\n\nPerform market analysis including competitive landscape, market size, trends, and strategic opportunities.",
                    agent=self.crew_agents['market']
                )
            ]
        
        elif analysis_type == "financial":
            return [
                Task(
                    description=f"{base_scenario}\n\nProvide detailed financial analysis and recommendations.",
                    agent=self.crew_agents['finance']
                )
            ]
        
        elif analysis_type == "risk":
            return [
                Task(
                    description=f"{base_scenario}\n\nConduct comprehensive risk assessment and mitigation planning.",
                    agent=self.crew_agents['risk']
                )
            ]
        
        elif analysis_type == "market":
            return [
                Task(
                    description=f"{base_scenario}\n\nAnalyze market dynamics and competitive positioning.",
                    agent=self.crew_agents['market']
                )
            ]
        
        else:
            # Default to comprehensive
            return self._create_tasks(scenario, "comprehensive")
    
    def _format_crew_results(self, crew_result, execution_time: float, analysis_type: str) -> Dict[str, Any]:
        """Format CrewAI results into our API response format"""
        
        return {
            "analysis_type": analysis_type,
            "timestamp": datetime.now().isoformat(),
            "execution_time": execution_time,
            "orchestrator": "CrewAI",
            "crew_result": str(crew_result),
            "agents_used": list(self.crew_agents.keys()),
            "system_info": {
                "total_agents": len(self.crew_agents),
                "gpu_agents": ["finance"],
                "cpu_agents": ["risk", "compliance", "market"],
                "framework": "CrewAI v0.175.0"
            },
            "formatted_summary": self._extract_summary_from_crew_result(crew_result)
        }
    
    def _extract_summary_from_crew_result(self, crew_result) -> Dict[str, str]:
        """Extract key insights from crew result"""
        result_str = str(crew_result)
        
        # Simple extraction logic (can be enhanced with proper parsing)
        return {
            "executive_summary": result_str[:500] + "..." if len(result_str) > 500 else result_str,
            "key_insights": "Multi-agent analysis completed successfully",
            "recommendations": "Review detailed analysis from each specialized agent",
            "next_steps": "Implement recommendations based on priority and resource availability"
        }
    
    async def get_crew_status(self) -> Dict[str, Any]:
        """Get status of CrewAI system"""
        return {
            "initialized": self.is_initialized,
            "agents": {
                name: "ready" if self.is_initialized else "pending"
                for name in ["finance", "risk", "compliance", "market"]
            },
            "framework": "CrewAI",
            "version": "0.175.0",
            "optimization": {
                "finance": "GPU (RTX 4050)",
                "risk": "CPU",
                "compliance": "CPU", 
                "market": "CPU"
            }
        }


class CustomLLMWrapper:
    """
    Custom LLM wrapper to integrate our existing agents with CrewAI
    Bridges between CrewAI's LLM interface and our model implementations
    """
    
    def __init__(self, agent_model, agent_name: str, emoji: str):
        self.agent_model = agent_model
        self.agent_name = agent_name
        self.emoji = emoji
        
    def __call__(self, prompt: str) -> str:
        """Call the underlying agent model synchronously"""
        try:
            logger.info(f"{self.emoji} {self.agent_name} Agent processing via CrewAI...")
            
            # Run async method in sync context
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            try:
                result = loop.run_until_complete(self.agent_model.analyze(prompt))
                return result
            finally:
                loop.close()
                
        except Exception as e:
            logger.error(f"❌ {self.agent_name} Agent error: {e}")
            return f"Error in {self.agent_name} analysis: {str(e)}"
    
    def invoke(self, prompt: str) -> str:
        """Alternative method name for CrewAI compatibility"""
        return self.__call__(prompt)
    
    @property
    def model_name(self) -> str:
        """Return model name for CrewAI logging"""
        return f"FourPillars{self.agent_name}Agent"
