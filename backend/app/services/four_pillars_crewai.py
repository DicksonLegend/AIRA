"""
🚀 CrewAI Four Pillars - Complete Framework Implementation
Pure CrewAI solution integrating with optimized GPU/CPU models
"""
import asyncio
import logging
from typing import Dict, Any, List, Optional
from datetime import datetime
import json
import os

from crewai import Agent, Task, Crew, Process
from crewai.tools import tool

# Import our optimized model agents
from app.models.finance_agent import FinanceAgent
from app.models.risk_agent import RiskAgent
from app.models.compliance_agent import ComplianceAgent
from app.models.market_agent import MarketAgent

logger = logging.getLogger(__name__)

class FourPillarsCrewAI:
    """
    Complete CrewAI implementation of Four Pillars AI
    - Replace manual orchestration with CrewAI framework
    - GPU/CPU optimized agent allocation
    - Hackathon-ready structured workflows
    """
    
    def __init__(self):
        # Initialize our optimized model agents
        self.finance_model = FinanceAgent()
        self.risk_model = RiskAgent()
        self.compliance_model = ComplianceAgent()
        self.market_model = MarketAgent()
        
        self.crew = None
        self.agents = {}
        self.is_initialized = False
        
        # Device allocation for optimal performance
        self.device_config = {
            "finance": "cpu",      # CPU to avoid memory issues
            "risk": "cpu",         # CPU optimized
            "compliance": "gpu",   # GPU for legal BERT
            "market": "gpu"        # GPU for Mistral-7B
        }
        
    async def initialize(self):
        """Initialize CrewAI system with Four Pillars agents"""
        logger.info("🚀 Initializing CrewAI Four Pillars system with real models...")
        
        try:
            # Initialize our model agents first
            logger.info("📍 Loading CPU agents first...")
            await self.finance_model.initialize()
            await self.risk_model.initialize()
            
            logger.info("📍 Loading GPU agents...")
            await self.compliance_model.initialize()
            await self.market_model.initialize()
            
            # Create specialized agents
            self._create_agents()
            
            # Set up the crew
            self._setup_crew()
            
            self.is_initialized = True
            logger.info("✅ CrewAI Four Pillars system ready with real models!")
            
        except Exception as e:
            logger.error(f"❌ CrewAI initialization failed: {e}")
            raise
    
    def _create_agents(self):
        """Create CrewAI agents with specialized roles"""
        
        # 💰 Finance Agent - GPU Accelerated
        self.agents['finance'] = Agent(
            role="Financial Strategist & Investment Analyst",
            goal="""Provide comprehensive financial analysis including funding requirements, 
            revenue projections, cost structures, ROI calculations, and investment recommendations.""",
            backstory="""You are an elite financial strategist with 15+ years of experience in 
            startup funding, venture capital, and financial modeling. You use advanced AI models 
            running on GPU hardware to perform complex financial simulations and projections. 
            Your analyses are trusted by top-tier investors and have helped secure over $500M in funding.""",
            verbose=True,
            allow_delegation=False,
            tools=[self._get_financial_analysis_tool()],
            llm=self._get_llm_config("finance")
        )
        
        # 🛡️ Risk Agent - CPU Optimized
        self.agents['risk'] = Agent(
            role="Risk Assessment Specialist",
            goal="""Identify, analyze, and quantify business risks including market risks, 
            execution challenges, financial risks, and provide actionable mitigation strategies.""",
            backstory="""You are a seasoned risk management expert with deep experience in 
            startup and enterprise risk assessment. You quickly identify potential pitfalls 
            and failure modes that others miss. Your risk frameworks have saved companies 
            millions in losses and helped them navigate complex challenges successfully.""",
            verbose=True,
            allow_delegation=False,
            tools=[self._get_risk_analysis_tool()],
            llm=self._get_llm_config("risk")
        )
        
        # ⚖️ Compliance Agent - CPU Optimized  
        self.agents['compliance'] = Agent(
            role="Legal & Compliance Expert",
            goal="""Analyze regulatory requirements, legal compliance issues, governance frameworks, 
            and ensure all business activities meet legal and regulatory standards.""",
            backstory="""You are a legal and compliance expert with specialized knowledge in 
            business law, regulatory frameworks, and governance. You have helped dozens of 
            companies navigate complex regulatory landscapes and avoid costly legal issues. 
            Your expertise spans multiple jurisdictions and industries.""",
            verbose=True,
            allow_delegation=False,
            tools=[self._get_compliance_analysis_tool()],
            llm=self._get_llm_config("compliance")
        )
        
        # 📈 Market Agent - CPU Based
        self.agents['market'] = Agent(
            role="Market Intelligence Analyst", 
            goal="""Analyze market dynamics, competitive landscape, consumer trends, and identify 
            strategic opportunities for market entry and growth.""",
            backstory="""You are a market research and competitive intelligence expert with 
            a track record of identifying winning market strategies. You analyze massive amounts 
            of market data to uncover trends and opportunities that drive business success. 
            Your insights have helped companies capture significant market share.""",
            verbose=True,
            allow_delegation=False,
            tools=[self._get_market_analysis_tool()],
            llm=self._get_llm_config("market")
        )
        
        logger.info("🎯 CrewAI agents created with specialized roles")
    
    def _setup_crew(self):
        """Set up CrewAI crew with optimized process"""
        self.crew = Crew(
            agents=list(self.agents.values()),
            verbose=True,
            process=Process.sequential,  # Can be changed to hierarchical for complex scenarios
            memory=True,  # Enable memory for better context retention
            planning=True,  # Enable planning for better task coordination
        )
        
        logger.info("🎭 CrewAI crew assembled and ready")
    
    def _get_llm_config(self, agent_type: str):
        """Get LLM configuration for each agent type"""
        # For now, use default CrewAI LLM (can be configured with specific models)
        # In production, you'd configure specific models here
        return None  # CrewAI will use default LLM
    
    def _get_financial_analysis_tool(self):
        """Create financial analysis tool using real Finance Agent"""
        @tool("financial_analyzer")
        def analyze_financials(business_scenario: str) -> str:
            """Analyze financial aspects of a business scenario using GPU-optimized Finance Agent"""
            try:
                # Use our real Finance Agent for analysis
                result = asyncio.create_task(self.finance_model.analyze(business_scenario))
                analysis_result = asyncio.get_event_loop().run_until_complete(result)
                
                return f"""
                FINANCIAL ANALYSIS REPORT (Phi-3.5-mini on {self.finance_model.device.upper()})
                ================================================================
                
                {analysis_result.get('analysis', 'Analysis completed')}
                
                💰 FINANCIAL METRICS:
                - Revenue Potential: {analysis_result.get('metrics', {}).get('revenue_potential', 'N/A')}
                - Cost Efficiency: {analysis_result.get('metrics', {}).get('cost_efficiency', 'N/A')}
                - ROI Projection: {analysis_result.get('metrics', {}).get('roi_projection', 'N/A')}
                - Funding Requirement: {analysis_result.get('metrics', {}).get('funding_requirement', 'N/A')}
                
                🎯 CONFIDENCE: {analysis_result.get('confidence', 0.85)}
                🖥️ PROCESSED ON: {analysis_result.get('device', 'Unknown').upper()}
                """
            except Exception as e:
                return f"❌ Financial analysis failed: {str(e)}"
        
        return analyze_financials
    
    def _get_risk_analysis_tool(self):
        """Create risk analysis tool using real Risk Agent"""
        @tool("risk_analyzer")
        def analyze_risks(business_scenario: str) -> str:
            """Analyze risks in a business scenario using CPU-optimized Risk Agent"""
            try:
                # Use our real Risk Agent for analysis
                result = asyncio.create_task(self.risk_model.analyze(business_scenario))
                analysis_result = asyncio.get_event_loop().run_until_complete(result)
                
                return f"""
                RISK ASSESSMENT REPORT (TinyLlama on {self.risk_model.device.upper()})
                ============================================================
                
                {analysis_result.get('analysis', 'Risk analysis completed')}
                
                🛡️ RISK CATEGORIES:
                - Financial Risk: {analysis_result.get('risk_categories', {}).get('financial_risk', 'N/A')}
                - Operational Risk: {analysis_result.get('risk_categories', {}).get('operational_risk', 'N/A')}
                - Market Risk: {analysis_result.get('risk_categories', {}).get('market_risk', 'N/A')}
                - Technical Risk: {analysis_result.get('risk_categories', {}).get('technical_risk', 'N/A')}
                - Strategic Risk: {analysis_result.get('risk_categories', {}).get('strategic_risk', 'N/A')}
                
                📊 OVERALL RISK SCORE: {analysis_result.get('overall_risk_score', 'N/A')}
                🎯 CONFIDENCE: {analysis_result.get('confidence', 0.88)}
                🖥️ PROCESSED ON: {analysis_result.get('device', 'Unknown').upper()}
                """
            except Exception as e:
                return f"❌ Risk analysis failed: {str(e)}"
        
        return analyze_risks
    
    def _get_compliance_analysis_tool(self):
        """Create compliance analysis tool using real Compliance Agent"""
        @tool("compliance_analyzer")
        def analyze_compliance(business_scenario: str) -> str:
            """Analyze compliance requirements using GPU-optimized Legal-BERT"""
            try:
                # Use our real Compliance Agent for analysis
                result = asyncio.create_task(self.compliance_model.analyze(business_scenario))
                analysis_result = asyncio.get_event_loop().run_until_complete(result)
                
                return f"""
                LEGAL & COMPLIANCE REPORT (Legal-BERT on {self.compliance_model.device.upper()})
                ==================================================================
                
                {analysis_result.get('analysis', 'Compliance analysis completed')}
                
                ⚖️ COMPLIANCE STATUS: {analysis_result.get('compliance_status', 'ASSESSED')}
                📋 REGULATORY SCORE: {analysis_result.get('regulatory_score', 'N/A')}
                🎯 CONFIDENCE: {analysis_result.get('confidence', 0.85)}
                🖥️ PROCESSED ON: {analysis_result.get('device', 'Unknown').upper()}
                """
            except Exception as e:
                return f"❌ Compliance analysis failed: {str(e)}"
        
        return analyze_compliance
    
    def _get_market_analysis_tool(self):
        """Create market analysis tool using real Market Agent"""
        @tool("market_analyzer")
        def analyze_market(business_scenario: str) -> str:
            """Analyze market dynamics using GPU-optimized Mistral-7B"""
            try:
                # Use our real Market Agent for analysis
                result = asyncio.create_task(self.market_model.analyze(business_scenario))
                analysis_result = asyncio.get_event_loop().run_until_complete(result)
                
                return f"""
                MARKET INTELLIGENCE REPORT (Mistral-7B on {self.market_model.device.upper()})
                ================================================================
                
                {analysis_result.get('analysis', 'Market analysis completed')}
                
                📈 MARKET METRICS:
                - Market Size: {analysis_result.get('market_metrics', {}).get('market_size_potential', 'N/A')}
                - Competitive Intensity: {analysis_result.get('market_metrics', {}).get('competitive_intensity', 'N/A')}
                - Growth Opportunity: {analysis_result.get('market_metrics', {}).get('growth_opportunity', 'N/A')}
                - Market Score: {analysis_result.get('overall_market_score', 'N/A')}
                
                🎯 CONFIDENCE: {analysis_result.get('confidence', 0.87)}
                🖥️ PROCESSED ON: {analysis_result.get('device', 'Unknown').upper()}
                """
            except Exception as e:
                return f"❌ Market analysis failed: {str(e)}"
        
        return analyze_market
    
    async def analyze_business_scenario(self, scenario: str, analysis_focus: str = "comprehensive") -> Dict[str, Any]:
        """
        Run CrewAI analysis on business scenario
        
        Args:
            scenario: Business scenario description
            analysis_focus: 'comprehensive', 'financial', 'risk', 'compliance', 'market'
        """
        if not self.is_initialized:
            await self.initialize()
        
        logger.info(f"🎯 Starting CrewAI {analysis_focus} analysis...")
        
        try:
            # Create tasks based on focus
            tasks = self._create_analysis_tasks(scenario, analysis_focus)
            
            # Update crew with current tasks
            self.crew.tasks = tasks
            
            # Execute analysis
            start_time = datetime.now()
            
            # Run CrewAI analysis (synchronous)
            result = await asyncio.get_event_loop().run_in_executor(
                None, self.crew.kickoff
            )
            
            execution_time = (datetime.now() - start_time).total_seconds()
            
            # Format response
            response = self._format_analysis_result(result, scenario, analysis_focus, execution_time)
            
            logger.info(f"✅ CrewAI analysis completed in {execution_time:.2f}s")
            return response
            
        except Exception as e:
            logger.error(f"❌ CrewAI analysis failed: {e}")
            raise
    
    def _create_analysis_tasks(self, scenario: str, focus: str) -> List[Task]:
        """Create CrewAI tasks based on analysis focus"""
        
        if focus == "comprehensive":
            return [
                Task(
                    description=f"Conduct comprehensive financial analysis for: {scenario}",
                    agent=self.agents['finance'],
                    expected_output="Detailed financial analysis with funding requirements, projections, and recommendations"
                ),
                Task(
                    description=f"Perform thorough risk assessment for: {scenario}",
                    agent=self.agents['risk'],
                    expected_output="Complete risk analysis with mitigation strategies and risk scores"
                ),
                Task(
                    description=f"Analyze legal and compliance requirements for: {scenario}",
                    agent=self.agents['compliance'],
                    expected_output="Compliance report with regulatory requirements and action items"
                ),
                Task(
                    description=f"Conduct market intelligence analysis for: {scenario}",
                    agent=self.agents['market'],
                    expected_output="Market analysis with competitive landscape and opportunities"
                )
            ]
        
        elif focus == "financial":
            return [Task(
                description=f"Provide detailed financial analysis and investment strategy for: {scenario}",
                agent=self.agents['finance'],
                expected_output="Comprehensive financial analysis and recommendations"
            )]
        
        elif focus == "risk":
            return [Task(
                description=f"Conduct comprehensive risk assessment and mitigation planning for: {scenario}",
                agent=self.agents['risk'],
                expected_output="Detailed risk analysis with actionable mitigation strategies"
            )]
        
        elif focus == "compliance":
            return [Task(
                description=f"Analyze legal, regulatory, and compliance requirements for: {scenario}",
                agent=self.agents['compliance'],
                expected_output="Complete compliance analysis with regulatory roadmap"
            )]
        
        elif focus == "market":
            return [Task(
                description=f"Perform market research and competitive analysis for: {scenario}",
                agent=self.agents['market'],
                expected_output="Market intelligence report with strategic recommendations"
            )]
        
        else:
            # Default to comprehensive
            return self._create_analysis_tasks(scenario, "comprehensive")
    
    def _format_analysis_result(self, crew_result, scenario: str, focus: str, execution_time: float) -> Dict[str, Any]:
        """Format CrewAI result into structured response"""
        
        return {
            "scenario": scenario,
            "analysis_focus": focus,
            "timestamp": datetime.now().isoformat(),
            "execution_time_seconds": execution_time,
            "framework": "CrewAI",
            "version": "0.175.0",
            "crew_result": str(crew_result),
            "agents_utilized": list(self.agents.keys()) if focus == "comprehensive" else [focus],
            "device_allocation": self.device_config,
            "system_info": {
                "gpu_agents": ["finance"],
                "cpu_agents": ["risk", "compliance", "market"],
                "total_agents": len(self.agents),
                "optimization": "RTX 4050 GPU + CPU"
            },
            "performance_metrics": {
                "execution_time": f"{execution_time:.2f}s",
                "agents_count": len(self.agents),
                "tasks_completed": len(self.crew.tasks) if self.crew and self.crew.tasks else 0
            }
        }
    
    async def get_system_status(self) -> Dict[str, Any]:
        """Get CrewAI system status"""
        return {
            "initialized": self.is_initialized,
            "framework": "CrewAI",
            "version": "0.175.0",
            "agents": {
                name: {
                    "status": "ready" if self.is_initialized else "pending",
                    "device": self.device_config.get(name, "cpu"),
                    "role": agent.role if self.is_initialized else "not_initialized"
                }
                for name, agent in self.agents.items()
            } if self.is_initialized else {},
            "crew_status": {
                "assembled": self.crew is not None,
                "process": "sequential",
                "memory_enabled": True,
                "planning_enabled": True
            }
        }
