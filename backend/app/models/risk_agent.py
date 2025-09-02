"""
🛡️ Risk Agent - Risk Assessment and Mitigation
RTX 4050 GPU Optimized with TinyLlama-1.1B-Chat
"""
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import logging
from typing import Dict, Any, List
import asyncio

# Data pipeline imports
from app.data.risk_api import RiskAPI
from app.data.financial_db import FinancialDB
from app.data.compliance_db import ComplianceDB
from app.data.market_news import MarketNews
from app.data.dataset_loader import DatasetLoader

logger = logging.getLogger(__name__)

class RiskAgent:
    def __init__(self):
        self.model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"  # Use your pre-downloaded model
        self.model = None
        self.tokenizer = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"  # Use GPU if available
        self.is_ready = False
        
        # Data pipeline connections
        self.risk_api = None
        self.financial_db = None
        self.compliance_db = None
        self.market_news = None
        self.dataset_loader = None
        
        # Configure 4-bit quantization for RTX 4050 (6GB VRAM) - Conservative settings
        if self.device == "cuda":
            self.quant_config = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_compute_dtype=torch.float16,
                bnb_4bit_use_double_quant=True,
                bnb_4bit_quant_type="nf4",
                llm_int8_enable_fp32_cpu_offload=True  # Enable CPU offload for tight VRAM
            )
        else:
            self.quant_config = None  # CPU doesn't need quantization
        
    async def initialize(self):
        """Initialize the Risk Agent with comprehensive data pipeline connections"""
        try:
            logger.info(f"🛡️ Initializing Risk Agent with {self.model_name} on {self.device.upper()}")
            
            # Initialize all data pipeline connections for comprehensive risk assessment
            logger.info("🔗 Connecting Risk Agent to all data sources...")
            self.risk_api = RiskAPI()
            self.financial_db = FinancialDB()
            self.compliance_db = ComplianceDB()
            self.market_news = MarketNews()
            self.dataset_loader = DatasetLoader()
            
            await self.risk_api.initialize()
            await self.financial_db.initialize()
            await self.compliance_db.initialize()
            await self.market_news.initialize()
            await self.dataset_loader.initialize()
            
            # Load tokenizer
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            if self.tokenizer.pad_token is None:
                self.tokenizer.pad_token = self.tokenizer.eos_token
            
            # Load model with GPU optimization
            if self.device == "cuda":
                self.model = AutoModelForCausalLM.from_pretrained(
                    self.model_name,
                    quantization_config=self.quant_config,
                    device_map="auto",  # Let transformers handle allocation
                    trust_remote_code=True,
                    torch_dtype=torch.float16,
                    max_memory={0: "800MB", "cpu": "4GB"}  # Very conservative + CPU fallback
                )
            else:
                self.model = AutoModelForCausalLM.from_pretrained(
                    self.model_name,
                    device_map={"": "cpu"},
                    torch_dtype=torch.float32,  # Use float32 for CPU stability
                    trust_remote_code=True,
                    low_cpu_mem_usage=True,
                    use_cache=True  # Enable KV cache for faster inference
                )
            
            self.is_ready = True
            logger.info(f"✅ Risk Agent ready on {self.device.upper()} - TinyLlama (~0.3GB {'VRAM' if self.device == 'cuda' else 'RAM'})")
            
        except Exception as e:
            logger.error(f"❌ Risk Agent initialization failed: {e}")
            raise
    
    async def analyze(self, scenario: str) -> Dict[str, Any]:
        """Analyze risks with comprehensive multi-source data"""
        if not self.is_ready:
            raise RuntimeError("Risk Agent not initialized")
        
        try:
            # Gather comprehensive risk data from all sources
            logger.info("🛡️ Conducting multi-dimensional risk assessment...")
            
            # Get fiscal and sovereign risk data
            fiscal_risk = await self.risk_api.assess_fiscal_risk({'country': 'India', 'scenario': scenario})
            
            # Get compliance and regulatory risks
            compliance_risk = await self.compliance_db.assess_compliance(scenario, 'India')
            
            # Get market volatility and performance risks
            market_performance = await self.market_news.get_market_performance()
            
            # Get financial stability indicators
            economic_indicators = await self.financial_db.get_economic_indicators()
            
            # Get government fiscal data for macroeconomic risk assessment
            # 3. Get fiscal risk data
            fiscal_data = await self.financial_db.analyze_expenditure_patterns()
            
            # Create enhanced risk analysis prompt with real data
            prompt = f"""
            Comprehensive Risk Assessment for Business Scenario:
            {scenario}
            
            Real Risk Data Context:
            - Sovereign Risk Score: {fiscal_risk.get('sovereign_risk_score', 'N/A')}
            - Compliance Risk Score: {compliance_risk.get('overall_compliance_score', 'N/A')}
            - Market Sentiment: {market_performance.get('sentiment', 'N/A')}
            - Economic Stability: {economic_indicators.get('summary', 'Available')}
            - Fiscal Health: {fiscal_data.get('summary', 'Available')}
            
            Identify and analyze the following risk categories:
            1. Financial risks (cash flow, funding, market volatility)
            2. Operational risks (execution, scalability, resource constraints)
            3. Market risks (competition, demand fluctuation, regulatory changes)
            4. Technical risks (technology failure, security breaches, compliance)
            5. Strategic risks (strategic misalignment, reputation, partnerships)
            
            Risk Analysis:"""
            
            # Tokenize input and move to correct device
            inputs = self.tokenizer.encode(prompt, return_tensors="pt", max_length=512, truncation=True)
            inputs = inputs.to(self.device)  # Move inputs to same device as model
            
            # Generate analysis
            with torch.no_grad():
                outputs = self.model.generate(
                    inputs,
                    max_length=inputs.shape[1] + 250,
                    num_return_sequences=1,
                    temperature=0.7,
                    do_sample=True,
                    pad_token_id=self.tokenizer.eos_token_id,
                    attention_mask=torch.ones_like(inputs)  # Explicit attention mask
                )
            
            # Decode response
            generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            analysis = generated_text[len(prompt):].strip()
            
            # Combine AI analysis with comprehensive real risk data
            result = {
                "agent": "Risk",
                "model": self.model_name,
                "analysis": analysis,
                "real_risk_data": {
                    "fiscal_risk": fiscal_risk,
                    "compliance_risk": compliance_risk,
                    "market_performance": market_performance,
                    "economic_indicators": economic_indicators,
                    "fiscal_data": fiscal_data
                },
                "risk_categories": {
                    "financial_risk": self._assess_risk_level(analysis, "financial"),
                    "operational_risk": self._assess_risk_level(analysis, "operational"),
                    "market_risk": self._assess_risk_level(analysis, "market"),
                    "technical_risk": self._assess_risk_level(analysis, "technical"),
                    "strategic_risk": self._assess_risk_level(analysis, "strategic")
                },
                "overall_risk_score": self._calculate_overall_risk(analysis),
                "mitigation_priority": self._identify_priority_risks(analysis),
                "confidence": 0.88,
                "device": self.device
            }
            
            logger.info("🛡️ Risk analysis completed")
            return result
            
        except Exception as e:
            logger.error(f"❌ Risk analysis failed: {e}")
            return {
                "agent": "Risk",
                "error": str(e),
                "analysis": "Risk analysis unavailable due to technical error"
            }
    
    def _assess_risk_level(self, text: str, risk_type: str) -> str:
        """Assess risk level for specific category"""
        text_lower = text.lower()
        high_risk_indicators = ["high risk", "critical", "severe", "major threat", "significant risk"]
        medium_risk_indicators = ["moderate", "medium risk", "potential risk", "some risk"]
        low_risk_indicators = ["low risk", "minimal", "minor", "manageable", "low impact"]
        
        high_count = sum(1 for indicator in high_risk_indicators if indicator in text_lower)
        medium_count = sum(1 for indicator in medium_risk_indicators if indicator in text_lower)
        low_count = sum(1 for indicator in low_risk_indicators if indicator in text_lower)
        
        if high_count > medium_count and high_count > low_count:
            return "HIGH"
        elif medium_count > low_count:
            return "MEDIUM"
        else:
            return "LOW"
    
    def _calculate_overall_risk(self, text: str) -> float:
        """Calculate overall risk score from 0.0 (low) to 1.0 (high)"""
        risk_indicators = ["risk", "threat", "danger", "concern", "challenge"]
        mitigation_indicators = ["mitigation", "control", "manage", "reduce", "minimize"]
        
        risk_count = sum(text.lower().count(indicator) for indicator in risk_indicators)
        mitigation_count = sum(text.lower().count(indicator) for indicator in mitigation_indicators)
        
        # Calculate score based on risk vs mitigation mentions
        if risk_count + mitigation_count == 0:
            return 0.5  # Neutral
        
        risk_ratio = risk_count / (risk_count + mitigation_count)
        return min(max(risk_ratio, 0.1), 0.9)  # Bound between 0.1 and 0.9
    
    def _identify_priority_risks(self, text: str) -> List[str]:
        """Identify priority risks that need immediate attention"""
        priorities = []
        text_lower = text.lower()
        
        if any(indicator in text_lower for indicator in ["cash flow", "funding", "financial"]):
            priorities.append("Financial Risk")
        if any(indicator in text_lower for indicator in ["competition", "market", "regulatory"]):
            priorities.append("Market Risk")
        if any(indicator in text_lower for indicator in ["operational", "execution", "scalability"]):
            priorities.append("Operational Risk")
        if any(indicator in text_lower for indicator in ["technical", "security", "technology"]):
            priorities.append("Technical Risk")
        if any(indicator in text_lower for indicator in ["strategic", "reputation", "partnership"]):
            priorities.append("Strategic Risk")
        
        return priorities[:3]  # Return top 3 priority risks
    
    def get_status(self) -> Dict[str, Any]:
        """Get agent status"""
        return {
            "agent": "Risk",
            "model": self.model_name,
            "device": self.device,
            "is_ready": self.is_ready,
            "gpu_enabled": self.device == "cuda"
        }