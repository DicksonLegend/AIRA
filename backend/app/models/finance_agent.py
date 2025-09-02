"""
💰 Finance Agent - Financial Viability Analysis
RTX 4050 GPU Optimized with Mistral-7B
"""
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import logging
from typing import Dict, Any, List
import asyncio

logger = logging.getLogger(__name__)

class FinanceAgent:
    def __init__(self):
        self.model_name = "microsoft/phi-3.5-mini-instruct"  # Use your pre-downloaded model
        self.model = None
        self.tokenizer = None
        self.device = "cpu"  # Force CPU to avoid GPU memory issues
        self.is_ready = False
        
        # Configure 4-bit quantization for RTX 4050 (6GB VRAM) - GPU optimized
        if self.device == "cuda":
            self.quant_config = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_compute_dtype=torch.float16,
                bnb_4bit_use_double_quant=True,
                bnb_4bit_quant_type="nf4"
            )
        else:
            self.quant_config = None
        
    async def initialize(self):
        """Initialize the Finance Agent with RTX 4050 optimization"""
        try:
            logger.info(f"💰 Initializing Finance Agent with {self.model_name} on {self.device.upper()}")
            
            # Load tokenizer
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            if self.tokenizer.pad_token is None:
                self.tokenizer.pad_token = self.tokenizer.eos_token
            
            # Load model with optimized settings for CPU/GPU
            if self.device == "cpu":
                # CPU configuration with strict memory limits
                self.model = AutoModelForCausalLM.from_pretrained(
                    self.model_name,
                    torch_dtype=torch.float16,  # Use float16 for memory efficiency
                    device_map={"": "cpu"},  # Force CPU device mapping
                    trust_remote_code=True,
                    low_cpu_mem_usage=True,  # Optimize CPU memory usage
                    offload_folder=None,  # Disable disk offloading
                    max_memory={"cpu": "6GB"}  # Reduced memory limit
                )
            else:
                # GPU configuration with quantization
                self.model = AutoModelForCausalLM.from_pretrained(
                    self.model_name,
                    quantization_config=self.quant_config,
                    device_map={"": "cuda:0"},  # Force GPU device mapping
                    dtype=torch.float16,
                    trust_remote_code=True,
                    max_memory={"0": "3GB"},  # Strict GPU memory limit
                    offload_folder=None  # Disable disk offloading
                )
            
            self.is_ready = True
            logger.info(f"✅ Finance Agent ready on {self.device.upper()} - Phi-3.5-mini")
            
        except Exception as e:
            logger.error(f"❌ Finance Agent initialization failed: {e}")
            raise
    
    async def analyze(self, scenario: str) -> Dict[str, Any]:
        """Analyze financial viability of business scenario"""
        if not self.is_ready:
            raise RuntimeError("Finance Agent not initialized")
        
        try:
            # Create financial analysis prompt
            prompt = f"""
            Financial Analysis for Business Scenario:
            {scenario}
            
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
            
            # Structure the response
            result = {
                "agent": "Finance",
                "model": self.model_name,
                "analysis": analysis,
                "metrics": {
                    "revenue_potential": self._extract_score(analysis, "revenue"),
                    "cost_efficiency": self._extract_score(analysis, "cost"),
                    "roi_projection": self._extract_score(analysis, "roi"),
                    "funding_requirement": self._extract_score(analysis, "funding")
                },
                "confidence": 0.85,
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
    
    def get_status(self) -> Dict[str, Any]:
        """Get agent status"""
        return {
            "agent": "Finance",
            "model": self.model_name,
            "device": self.device,
            "is_ready": self.is_ready,
            "gpu_enabled": self.device == "cuda"
        }