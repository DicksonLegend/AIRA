"""
💰 Finance Agent - Financial Viability Analysis
RTX 4050 GPU Optimized with Phi-3.5-mini
"""
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import logging
from typing import Dict, Any, List
import asyncio

# Data pipeline imports
from app.data.financial_db import FinancialDB
from app.data.market_news import MarketNews
from app.data.vectore_store import VectorStore

logger = logging.getLogger(__name__)

class FinanceAgent:
    def __init__(self):
        # Finance Agent uses Phi-3.5-mini for financial calculations
        self.model_name = "microsoft/phi-3.5-mini-instruct"  # Correct model for finance
        self.model = None
        self.tokenizer = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.is_ready = False
        
        # Data pipeline connections
        self.financial_db = None
        self.market_news = None
        self.vector_store = None
        
        # Configure for optimal GPU performance
        if self.device == "cuda":
            self.quant_config = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_compute_dtype=torch.float16,
                bnb_4bit_use_double_quant=True,
                bnb_4bit_quant_type="nf4"
                # Removed CPU offload to avoid meta tensor issues
            )
        else:
            self.quant_config = None
        
    async def initialize(self):
        """Initialize the Finance Agent with data pipeline connections"""
        try:
            logger.info(f"💰 Initializing Finance Agent with {self.model_name} on {self.device.upper()}")
            
            # Initialize data pipeline connections first
            logger.info("🔗 Connecting Finance Agent to data sources...")
            self.financial_db = FinancialDB()
            self.market_news = MarketNews()
            self.vector_store = VectorStore()
            
            await self.financial_db.initialize()
            await self.market_news.initialize()
            await self.vector_store.initialize()
            
            # Load tokenizer
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            if self.tokenizer.pad_token is None:
                self.tokenizer.pad_token = self.tokenizer.eos_token
            
            # Load model with GPU/CPU optimization
            if self.device == "cuda":
                # GPU configuration with simpler quantization for RTX 4050
                self.model = AutoModelForCausalLM.from_pretrained(
                    self.model_name,
                    quantization_config=self.quant_config,
                    torch_dtype=torch.float16,
                    trust_remote_code=True,
                    low_cpu_mem_usage=True
                )
            else:
                # CPU fallback configuration
                self.model = AutoModelForCausalLM.from_pretrained(
                    self.model_name,
                    torch_dtype=torch.float32,
                    device_map={"": "cpu"},
                    trust_remote_code=True,
                    low_cpu_mem_usage=True,
                    use_cache=True
                )
            
            vram_info = "~2GB VRAM" if self.device == "cuda" else "~3.8GB RAM"
            self.is_ready = True
            logger.info(f"✅ Finance Agent ready on {self.device.upper()} - Phi-3.5-mini ({vram_info})")
            
        except Exception as e:
            logger.error(f"❌ Finance Agent initialization failed: {e}")
            raise
    
    async def analyze(self, scenario: str) -> Dict[str, Any]:
        """Analyze financial viability of business scenario with real data"""
        if not self.is_ready:
            raise RuntimeError("Finance Agent not initialized")
        
        try:
            # Get real financial data from data pipeline
            logger.info("💰 Gathering real financial data...")
            
            # Get financial metrics and government expenditure data
            financial_ratios = await self.financial_db.get_financial_ratios({
                'entity_id': 'scenario_analysis',
                'scenario': scenario
            })
            
            # Get market impact analysis
            market_impact = await self.market_news.get_government_expenditure_impact()
            
            # Search for similar financial scenarios using vector store
            similar_scenarios = await self.vector_store.search_financial_context(scenario, top_k=3)
            
            # Get economic indicators
            economic_data = await self.financial_db.get_economic_indicators()
            
            # Create enhanced financial analysis prompt with real data
            prompt = f"""
            Financial Analysis for Business Scenario:
            {scenario}
            
            Real Data Context:
            - Market Impact Score: {market_impact.get('impact_score', 'N/A')}
            - Economic Indicators: {economic_data.get('summary', 'Available')}
            - Similar Scenarios Found: {len(similar_scenarios)}
            
            Analyze the following financial aspects:
            1. Revenue projections and market potential
            2. Cost structure and operational expenses  
            3. ROI and profitability timeline
            4. Funding requirements and cash flow
            5. Financial risks and mitigation strategies
            
            Financial Assessment:"""
            
            # Tokenize input
            inputs = self.tokenizer.encode(prompt, return_tensors="pt", max_length=512, truncation=True)
            if self.device == "cuda":
                inputs = inputs.to(self.device)
            
            # Generate analysis
            with torch.no_grad():
                outputs = self.model.generate(
                    inputs,
                    max_length=inputs.shape[1] + 200,
                    num_return_sequences=1,
                    temperature=0.7,
                    do_sample=True,
                    pad_token_id=self.tokenizer.eos_token_id,
                    use_cache=False,  # Disable cache to avoid DynamicCache issues
                    attention_mask=torch.ones_like(inputs)  # Explicit attention mask
                )
            
            # Decode response
            generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            analysis = generated_text[len(prompt):].strip()
            
            # Combine AI analysis with real data
            result = {
                "agent": "Finance",
                "model": self.model_name,
                "analysis": analysis,
                "real_data": {
                    "financial_ratios": financial_ratios,
                    "market_impact": market_impact,
                    "economic_indicators": economic_data,
                    "similar_scenarios": len(similar_scenarios)
                },
                "metrics": {
                    "revenue_potential": self._extract_score(analysis, "revenue"),
                    "cost_efficiency": self._extract_score(analysis, "cost"),
                    "roi_projection": self._extract_score(analysis, "roi"),
                    "funding_requirement": self._extract_score(analysis, "funding")
                },
                "confidence": self._calculate_confidence(analysis, scenario, financial_ratios, market_impact),
                "device": self.device
            }
            
            logger.info("💰 Finance analysis completed")
            return result
            
        except Exception as e:
            logger.error(f"❌ Finance analysis failed: {e}")
            return {
                "agent": "Finance",
                "error": str(e),
                "analysis": "Financial analysis unavailable due to technical error"
            }
    
    def _extract_score(self, text: str, keyword: str) -> float:
        """Extract numerical score from analysis text"""
        # Simple scoring based on keyword presence and sentiment
        text_lower = text.lower()
        if keyword in text_lower:
            positive_indicators = ["high", "strong", "good", "excellent", "positive"]
            negative_indicators = ["low", "weak", "poor", "negative", "risk"]
            
            positive_count = sum(1 for indicator in positive_indicators if indicator in text_lower)
            negative_count = sum(1 for indicator in negative_indicators if indicator in text_lower)
            
            if positive_count > negative_count:
                return min(0.8 + (positive_count * 0.05), 1.0)
            else:
                return max(0.3 - (negative_count * 0.05), 0.1)
        
        return 0.5  # Neutral score
    
    def _calculate_confidence(self, analysis: str, scenario: str, financial_ratios: Dict, market_impact: Dict) -> float:
        """Calculate dynamic confidence score based on analysis quality and data availability"""
        confidence = 0.5  # Base confidence
        
        # Analysis quality factors
        analysis_lower = analysis.lower()
        
        # Length and detail indicators
        if len(analysis) > 500:
            confidence += 0.1
        if len(analysis) > 1000:
            confidence += 0.1
            
        # Content quality indicators
        quality_keywords = ["revenue", "cost", "profit", "funding", "investment", "roi", "break-even"]
        quality_count = sum(1 for keyword in quality_keywords if keyword in analysis_lower)
        confidence += min(quality_count * 0.05, 0.2)
        
        # Data availability factors
        if financial_ratios and len(financial_ratios) > 0:
            confidence += 0.1
        if market_impact and len(market_impact) > 0:
            confidence += 0.1
            
        # Scenario complexity factor
        scenario_lower = scenario.lower()
        if any(word in scenario_lower for word in ["startup", "new venture", "launch"]):
            confidence -= 0.05  # New ventures have higher uncertainty
        if any(word in scenario_lower for word in ["expansion", "growth", "scale"]):
            confidence += 0.05  # Established businesses have more data
            
        # Specific financial terms that indicate thorough analysis
        specific_terms = ["cash flow", "balance sheet", "income statement", "valuation", "dcf"]
        specific_count = sum(1 for term in specific_terms if term in analysis_lower)
        confidence += min(specific_count * 0.03, 0.15)
        
        return round(min(max(confidence, 0.3), 0.95), 2)
    
    def get_status(self) -> Dict[str, Any]:
        """Get agent status"""
        return {
            "agent": "Finance",
            "model": self.model_name,
            "device": self.device,
            "is_ready": self.is_ready,
            "gpu_enabled": self.device == "cuda"
        }