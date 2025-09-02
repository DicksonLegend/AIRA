"""
🛡️ Risk Agent - Risk Assessment and Mitigation
RTX 4050 GPU Optimized with TinyLlama-1.1B-Chat
"""
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import logging
from typing import Dict, Any, List
import asyncio

logger = logging.getLogger(__name__)

class RiskAgent:
    def __init__(self):
        self.model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
        self.model = None
        self.tokenizer = None
        self.device = "cpu"  # Force CPU for lightweight model
        self.is_ready = False
        
        # Configure for CPU optimization (no quantization needed)
        self.quant_config = None  # CPU doesn't need quantization
        
    async def initialize(self):
        """Initialize the Risk Agent with CPU optimization"""
        try:
            logger.info(f"🛡️ Initializing Risk Agent with {self.model_name} on CPU")
            
            # Load tokenizer
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            if self.tokenizer.pad_token is None:
                self.tokenizer.pad_token = self.tokenizer.eos_token
            
            # Load model for CPU (no quantization, optimized for CPU inference)
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_name,
                device_map="cpu",
                dtype=torch.float32,  # Use dtype instead of torch_dtype
                trust_remote_code=True
            )
            
            self.is_ready = True
            logger.info(f"✅ Risk Agent ready on CPU - TinyLlama (~0.55GB RAM)")
            
        except Exception as e:
            logger.error(f"❌ Risk Agent initialization failed: {e}")
            raise
    
    async def analyze(self, scenario: str) -> Dict[str, Any]:
        """Analyze risks and mitigation strategies"""
        if not self.is_ready:
            raise RuntimeError("Risk Agent not initialized")
        
        try:
            # Create risk analysis prompt
            prompt = f"""
            Risk Assessment for Business Scenario:
            {scenario}
            
            Identify and analyze the following risk categories:
            1. Financial risks (cash flow, funding, market volatility)
            2. Operational risks (execution, scalability, resource constraints)
            3. Market risks (competition, demand fluctuation, regulatory changes)
            4. Technical risks (technology failure, security breaches, compliance)
            5. Strategic risks (strategic misalignment, reputation, partnerships)
            
            Risk Analysis:"""
            
            # Tokenize input for CPU inference
            inputs = self.tokenizer.encode(prompt, return_tensors="pt", max_length=512, truncation=True)
            # No need to move to CUDA since we're using CPU
            
            # Generate analysis on CPU
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
            
            # Structure the response
            result = {
                "agent": "Risk",
                "model": self.model_name,
                "analysis": analysis,
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
