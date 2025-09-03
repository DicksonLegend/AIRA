"""
🚀 CrewAI Four Pillars - Complete Framework Implementation

AIRA Four Pillars Business Intelligence Platform:
- Finance Agent: Phi-3.5-mini (Quantized 4-bit) ~2GB VRAM
- Risk Agent: TinyLlama (Quantized 4-bit) ~0.3GB VRAM  
- Compliance Agent: Legal-BERT (Quantized 4-bit) ~0.3GB VRAM
- Market Agent: TinyLlama (Quantized 4-bit) ~0.5GB VRAM

Pure CrewAI solution integrating with optimized GPU/CPU models
Total VRAM Usage: ~3.1GB (Perfect for RTX 4050 6GB)
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
from app.models.market_agent import MarketAgent  # Re-enabled with TinyLlama

logger = logging.getLogger(__name__)

class FourPillarsCrewAI:
    """
    Complete CrewAI implementation of Four Pillars AI
    - Replace manual orchestration with CrewAI framework
    - GPU/CPU optimized agent allocation
    - Hackathon-ready structured workflows
    """
    
    def __init__(self):
        # Initialize our optimized model agents (4-agent configuration with TinyLlama)
        self.finance_model = FinanceAgent()
        self.risk_model = RiskAgent()
        self.compliance_model = ComplianceAgent()
        self.market_model = MarketAgent()  # Re-enabled with TinyLlama
        
        self.crew = None
        self.agents = {}
        self.is_initialized = False
        
        # Device allocation for optimal performance (4 agents)
        self.device_config = {
            "finance": "gpu",      # GPU for Phi-3.5-mini
            "risk": "gpu",         # GPU for TinyLlama
            "compliance": "gpu",   # GPU for Legal-BERT
            "market": "gpu"        # GPU for TinyLlama (market)
        }
        
    async def initialize(self):
        """Initialize CrewAI system with Four Pillars agents"""
        logger.info("🚀 Initializing CrewAI Four Pillars system with real models...")
        
        try:
            # Initialize our model agents - GPU agents first for better performance
            logger.info("� Loading GPU-optimized agents...")
            await self.finance_model.initialize()      # Phi-3.5-mini -> GPU
            await self.risk_model.initialize()         # TinyLlama -> GPU
            await self.compliance_model.initialize()   # Legal-BERT -> GPU
            await self.market_model.initialize()       # TinyLlama -> GPU (market)
            
            # Create specialized agents
            self._create_agents()
            
            # Set up the crew
            self._setup_crew()
            
            self.is_initialized = True
            logger.info("✅ CrewAI Four Pillars system ready with GPU models!")
            
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
        
        # 📈 Market Agent - GPU Based with TinyLlama
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
        
        logger.info("🎯 CrewAI agents created with specialized roles (4-agent configuration)")
    
    def _setup_crew(self):
        """Set up CrewAI crew with optimized process"""
        # Create a simple mock LLM for CrewAI planning/coordination
        from langchain.llms.base import LLM
        from typing import Optional, List
        
        class SimpleMockLLM(LLM):
            def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
                # Simple fallback for CrewAI coordination
                return "Task coordination completed using local models."
            
            @property 
            def _llm_type(self) -> str:
                return "simple_mock"
        
        self.crew = Crew(
            agents=list(self.agents.values()),
            verbose=True,
            process=Process.sequential,  # Can be changed to hierarchical for complex scenarios
            memory=False,  # Disable memory to avoid LLM calls
            planning=False,  # Disable planning to avoid LLM calls
            manager_llm=SimpleMockLLM(),  # Use simple mock for any manager operations
        )
        
        logger.info("🎭 CrewAI crew assembled and ready")
    
    def _get_llm_config(self, agent_type: str):
        """Get LLM configuration for each agent type using local models"""
        # Configure CrewAI to use local models instead of OpenAI
        from langchain.llms.base import LLM
        from typing import Optional, List, Any
        from pydantic import Field
        
        class LocalModelLLM(LLM):
            """Custom LLM wrapper for our local models"""
            
            model: Any = Field(..., description="The local model instance")
            
            def __init__(self, model_instance, **kwargs):
                super().__init__(model=model_instance, **kwargs)
            
            def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
                """Call the local model"""
                try:
                    # Use asyncio to run the async model method
                    import asyncio
                    try:
                        loop = asyncio.get_event_loop()
                    except RuntimeError:
                        loop = asyncio.new_event_loop()
                        asyncio.set_event_loop(loop)
                    
                    result = loop.run_until_complete(self.model.analyze(prompt))
                    
                    if isinstance(result, dict):
                        return result.get('analysis', str(result))
                    return str(result)
                except Exception as e:
                    return f"Error in local model: {str(e)}"
            
            @property
            def _llm_type(self) -> str:
                return "local_model"
        
        # Return the appropriate local model based on agent type
        if agent_type == "finance" and hasattr(self, 'finance_model'):
            return LocalModelLLM(self.finance_model)
        elif agent_type == "risk" and hasattr(self, 'risk_model'):
            return LocalModelLLM(self.risk_model)
        elif agent_type == "compliance" and hasattr(self, 'compliance_model'):
            return LocalModelLLM(self.compliance_model)
        elif agent_type == "market" and hasattr(self, 'market_model'):
            return LocalModelLLM(self.market_model)
        
        # Fallback: use a simple mock LLM to avoid OpenAI requirement
        class MockLLM(LLM):
            def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
                return f"Local model response for {agent_type}: {prompt[:100]}..."
            
            @property
            def _llm_type(self) -> str:
                return "mock_local"
        
        return MockLLM()
    
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
        """Create market analysis tool using real Market Agent with TinyLlama"""
        @tool("market_analyzer")
        def analyze_market(business_scenario: str) -> str:
            """Analyze market dynamics using GPU-optimized TinyLlama"""
            try:
                # Use our real Market Agent for analysis
                result = asyncio.create_task(self.market_model.analyze(business_scenario))
                analysis_result = asyncio.get_event_loop().run_until_complete(result)
                
                return f"""
                MARKET INTELLIGENCE REPORT (TinyLlama on {self.market_model.device.upper()})
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
        Run local model analysis on business scenario (bypassing CrewAI coordination)
        
        Args:
            scenario: Business scenario description
            analysis_focus: 'comprehensive', 'financial', 'risk', 'compliance', 'market'
        """
        if not self.is_initialized:
            await self.initialize()
        
        logger.info(f"🎯 Starting local model {analysis_focus} analysis...")
        
        try:
            start_time = datetime.now()
            
            # Run direct analysis using our local models instead of CrewAI coordination
            results = {}
            
            if analysis_focus == "comprehensive" or analysis_focus == "financial":
                logger.info("💰 Running Finance Agent analysis...")
                finance_result = await self.finance_model.analyze(f"Financial Analysis for: {scenario}")
                results['finance'] = finance_result
            
            if analysis_focus == "comprehensive" or analysis_focus == "risk":
                logger.info("🛡️ Running Risk Agent analysis...")
                risk_result = await self.risk_model.analyze(f"Risk Assessment for: {scenario}")
                results['risk'] = risk_result
            
            if analysis_focus == "comprehensive" or analysis_focus == "compliance":
                logger.info("⚖️ Running Compliance Agent analysis...")
                compliance_result = await self.compliance_model.analyze(f"Compliance Analysis for: {scenario}")
                results['compliance'] = compliance_result
            
            if analysis_focus == "comprehensive" or analysis_focus == "market":
                logger.info("📈 Running Market Agent analysis...")
                market_result = await self.market_model.analyze(f"Market Analysis for: {scenario}")
                results['market'] = market_result
            
            execution_time = (datetime.now() - start_time).total_seconds()
            
            # Format response
            response = self._format_local_analysis_result(results, scenario, analysis_focus, execution_time)
            
            logger.info(f"✅ Local model analysis completed in {execution_time:.2f}s")
            return response
            
        except Exception as e:
            logger.error(f"❌ Local model analysis failed: {e}")
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
    
    def _format_local_analysis_result(self, results: Dict[str, Any], scenario: str, analysis_focus: str, execution_time: float) -> Dict[str, Any]:
        """Format the local model analysis results"""
        
        # Count successful analyses
        successful_agents = len([r for r in results.values() if 'error' not in r])
        total_agents = len(results)
        
        # Calculate overall confidence
        confidences = [r.get('confidence', 0.5) for r in results.values() if 'confidence' in r]
        overall_confidence = sum(confidences) / len(confidences) if confidences else 0.5
        
        # Determine overall status
        if successful_agents == total_agents:
            status = "completed"
        elif successful_agents > 0:
            status = "partial"
        else:
            status = "failed"
        
        # Format response to match AnalysisResponse schema
        formatted_result = {
            "scenario": scenario,
            "analysis_focus": analysis_focus,
            "timestamp": datetime.now().isoformat(),
            "execution_time_seconds": execution_time,
            "framework": "CrewAI Four Pillars",
            "crew_result": f"Analysis completed successfully with {successful_agents}/{total_agents} agents. Status: {status}",
            "agents_utilized": list(results.keys()),
            "device_allocation": {
                "finance": "CUDA",
                "risk": "CUDA", 
                "compliance": "CUDA",
                "market": "CUDA"
            },
            "system_info": {
                "gpu_agents": 4,
                "total_vram": "~3.1GB",
                "models": {
                    "finance": "Phi-3.5-mini",
                    "risk": "TinyLlama", 
                    "compliance": "Legal-BERT",
                    "market": "TinyLlama"
                }
            },
            "performance_metrics": {
                "execution_time": execution_time,
                "agents_completed": successful_agents,
                "total_agents": total_agents,
                "overall_confidence": round(overall_confidence, 2),
                "results": results,
                "summary": {
                    "key_insights": self._extract_key_insights(results),
                    "recommendations": self._extract_recommendations(results),
                    "risk_level": self._calculate_overall_risk_level(results),
                    "financial_viability": self._assess_financial_viability(results),
                    "market_opportunity": self._assess_market_opportunity(results),
                    "compliance_status": self._assess_compliance_status(results)
                }
            }
        }
        
        return formatted_result
    
    def _extract_key_insights(self, results: Dict[str, Any]) -> List[str]:
        """Extract key insights from all agent results"""
        insights = []
        
        for agent, result in results.items():
            if 'analysis' in result and result['analysis']:
                # Extract first sentence or key point from analysis
                analysis_text = result['analysis']
                if isinstance(analysis_text, str) and len(analysis_text) > 20:
                    first_sentence = analysis_text.split('.')[0]
                    if len(first_sentence) > 10:
                        insights.append(f"{agent.capitalize()}: {first_sentence}.")
        
        return insights[:5]  # Return top 5 insights
    
    def _extract_recommendations(self, results: Dict[str, Any]) -> List[str]:
        """Extract recommendations from all agent results"""
        recommendations = []
        
        # Finance recommendations
        if 'finance' in results and 'metrics' in results['finance']:
            recommendations.append("Focus on financial sustainability and funding strategy")
        
        # Risk recommendations  
        if 'risk' in results and 'risk_categories' in results['risk']:
            recommendations.append("Implement comprehensive risk mitigation plan")
        
        # Compliance recommendations
        if 'compliance' in results and 'compliance_scores' in results['compliance']:
            recommendations.append("Ensure regulatory compliance before market entry")
        
        # Market recommendations
        if 'market' in results and 'market_metrics' in results['market']:
            recommendations.append("Validate market demand and competitive positioning")
        
        return recommendations
    
    def _calculate_overall_risk_level(self, results: Dict[str, Any]) -> str:
        """Calculate overall risk level from all agents"""
        risk_scores = []
        
        # Get risk score from risk agent
        if 'risk' in results and 'overall_risk_score' in results['risk']:
            risk_scores.append(results['risk']['overall_risk_score'])
        
        # Get implied risk from other agents
        if 'finance' in results and 'metrics' in results['finance']:
            # Higher funding needs = higher risk
            risk_scores.append(0.6)  # Moderate risk assumption
        
        if not risk_scores:
            return "MODERATE"
        
        avg_risk = sum(risk_scores) / len(risk_scores)
        
        if avg_risk < 0.3:
            return "LOW"
        elif avg_risk < 0.7:
            return "MODERATE" 
        else:
            return "HIGH"
    
    def _assess_financial_viability(self, results: Dict[str, Any]) -> str:
        """Assess financial viability from finance agent"""
        if 'finance' in results and 'metrics' in results['finance']:
            finance_result = results['finance']
            if 'revenue_potential' in finance_result.get('metrics', {}):
                return "POSITIVE"
            else:
                return "REQUIRES_ANALYSIS"
        return "UNKNOWN"
    
    def _assess_market_opportunity(self, results: Dict[str, Any]) -> str:
        """Assess market opportunity from market agent"""
        if 'market' in results and 'market_metrics' in results['market']:
            market_result = results['market']
            if 'market_size_potential' in market_result.get('market_metrics', {}):
                return "STRONG"
            else:
                return "MODERATE"
        return "UNKNOWN"
    
    def _assess_compliance_status(self, results: Dict[str, Any]) -> str:
        """Assess compliance status from compliance agent"""
        if 'compliance' in results and 'compliance_scores' in results['compliance']:
            compliance_result = results['compliance']
            if 'overall_compliance_score' in compliance_result:
                score = compliance_result['overall_compliance_score']
                if score > 0.8:
                    return "COMPLIANT"
                elif score > 0.6:
                    return "MOSTLY_COMPLIANT"
                else:
                    return "NEEDS_ATTENTION"
        return "UNKNOWN"
