"""
📈 Market Agent - Market Dynamics and Competitive Analysis
RTX 4050 GPU Optimized with Mistral-7B-Instruct
"""
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import logging
from typing import Dict, Any, List
import asyncio

logger = logging.getLogger(__name__)

class MarketAgent:
    def __init__(self):
        self.model_name = "mistralai/Mistral-7B-Instruct-v0.3"
        self.model = None
        self.tokenizer = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.is_ready = False
        
        # Configure 4-bit quantization for RTX 4050 (6GB VRAM)
        self.quant_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.float16,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4"
        )
        
    async def initialize(self):
        """Initialize the Market Agent with RTX 4050 optimization"""
        try:
            logger.info(f"📈 Initializing Market Agent with {self.model_name}")
            
            # Load tokenizer
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            if self.tokenizer.pad_token is None:
                self.tokenizer.pad_token = self.tokenizer.eos_token
            
            # Load Mistral-7B model with 4-bit quantization for RTX 4050
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_name,
                quantization_config=self.quant_config,
                device_map="auto",
                dtype=torch.float16,
                max_memory={0: "5GB"} if self.device == "cuda" else None
            )
            
            self.is_ready = True
            logger.info(f"✅ Market Agent ready on {self.device} - Mistral-7B (~4-6GB VRAM)")
            
        except Exception as e:
            logger.error(f"❌ Market Agent initialization failed: {e}")
            raise
    
    async def analyze(self, scenario: str) -> Dict[str, Any]:
        """Analyze market dynamics and competitive positioning"""
        if not self.is_ready:
            raise RuntimeError("Market Agent not initialized")
        
        try:
            # Create market analysis prompt
            prompt = f"""
            Market Analysis for Business Scenario:
            {scenario}
            
            Analyze the following market aspects:
            1. Market size and growth potential
            2. Competitive landscape and positioning
            3. Target customer segments and demand
            4. Market trends and emerging opportunities
            5. Barriers to entry and market challenges
            6. Geographic market considerations
            7. Pricing strategy and market penetration
            
            Market Assessment:"""
            
            # Tokenize input
            inputs = self.tokenizer.encode(prompt, return_tensors="pt", max_length=512, truncation=True)
            if self.device == "cuda":
                inputs = inputs.to(self.device)
            
            # Generate analysis
            with torch.no_grad():
                outputs = self.model.generate(
                    inputs,
                    max_length=inputs.shape[1] + 300,
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
                "agent": "Market",
                "model": self.model_name,
                "analysis": analysis,
                "market_metrics": {
                    "market_size_potential": self._assess_market_size(analysis),
                    "competitive_intensity": self._assess_competition(analysis),
                    "growth_opportunity": self._assess_growth_potential(analysis),
                    "market_entry_difficulty": self._assess_entry_barriers(analysis),
                    "customer_demand": self._assess_demand(analysis)
                },
                "competitive_analysis": self._analyze_competition(scenario, analysis),
                "market_segments": self._identify_target_segments(analysis),
                "growth_drivers": self._identify_growth_drivers(analysis),
                "market_challenges": self._identify_challenges(analysis),
                "strategic_recommendations": self._generate_market_recommendations(analysis),
                "overall_market_score": self._calculate_market_attractiveness(analysis),
                "confidence": 0.87,
                "device": self.device
            }
            
            logger.info("📈 Market analysis completed")
            return result
            
        except Exception as e:
            logger.error(f"❌ Market analysis failed: {e}")
            return {
                "agent": "Market",
                "error": str(e),
                "analysis": "Market analysis unavailable due to technical error"
            }
    
    def _assess_market_size(self, text: str) -> str:
        """Assess market size potential"""
        text_lower = text.lower()
        large_indicators = ["large market", "billion", "massive", "huge", "enormous", "significant market"]
        medium_indicators = ["medium market", "million", "moderate", "substantial", "growing market"]
        small_indicators = ["small market", "niche", "limited", "narrow", "specialized"]
        
        large_count = sum(1 for indicator in large_indicators if indicator in text_lower)
        medium_count = sum(1 for indicator in medium_indicators if indicator in text_lower)
        small_count = sum(1 for indicator in small_indicators if indicator in text_lower)
        
        if large_count > medium_count and large_count > small_count:
            return "LARGE"
        elif medium_count > small_count:
            return "MEDIUM"
        else:
            return "SMALL"
    
    def _assess_competition(self, text: str) -> str:
        """Assess competitive intensity"""
        text_lower = text.lower()
        high_competition = ["intense competition", "highly competitive", "saturated", "many competitors"]
        medium_competition = ["moderate competition", "some competitors", "competitive landscape"]
        low_competition = ["low competition", "few competitors", "emerging market", "blue ocean"]
        
        high_count = sum(1 for indicator in high_competition if indicator in text_lower)
        medium_count = sum(1 for indicator in medium_competition if indicator in text_lower)
        low_count = sum(1 for indicator in low_competition if indicator in text_lower)
        
        if high_count > medium_count and high_count > low_count:
            return "HIGH"
        elif medium_count > low_count:
            return "MEDIUM"
        else:
            return "LOW"
    
    def _assess_growth_potential(self, text: str) -> float:
        """Assess growth potential score"""
        growth_indicators = ["growth", "expanding", "increasing", "rising", "growing", "opportunity"]
        decline_indicators = ["declining", "shrinking", "decreasing", "falling", "stagnant"]
        
        growth_count = sum(text.lower().count(indicator) for indicator in growth_indicators)
        decline_count = sum(text.lower().count(indicator) for indicator in decline_indicators)
        
        if growth_count + decline_count == 0:
            return 0.5
        
        growth_ratio = growth_count / (growth_count + decline_count)
        return round(growth_ratio, 2)
    
    def _assess_entry_barriers(self, text: str) -> str:
        """Assess market entry barriers"""
        text_lower = text.lower()
        high_barriers = ["high barriers", "difficult entry", "complex", "regulated", "capital intensive"]
        medium_barriers = ["moderate barriers", "some challenges", "established players"]
        low_barriers = ["low barriers", "easy entry", "open market", "accessible"]
        
        high_count = sum(1 for indicator in high_barriers if indicator in text_lower)
        medium_count = sum(1 for indicator in medium_barriers if indicator in text_lower)
        low_count = sum(1 for indicator in low_barriers if indicator in text_lower)
        
        if high_count > medium_count and high_count > low_count:
            return "HIGH"
        elif medium_count > low_count:
            return "MEDIUM"
        else:
            return "LOW"
    
    def _assess_demand(self, text: str) -> float:
        """Assess customer demand level"""
        demand_indicators = ["high demand", "strong demand", "increasing demand", "growing interest"]
        weak_demand_indicators = ["low demand", "weak demand", "declining interest", "limited demand"]
        
        strong_demand = sum(1 for indicator in demand_indicators if indicator in text.lower())
        weak_demand = sum(1 for indicator in weak_demand_indicators if indicator in text.lower())
        
        if strong_demand + weak_demand == 0:
            return 0.5
        
        demand_ratio = strong_demand / (strong_demand + weak_demand)
        return round(demand_ratio, 2)
    
    def _analyze_competition(self, scenario: str, analysis: str) -> Dict[str, Any]:
        """Analyze competitive landscape"""
        return {
            "competitive_intensity": self._assess_competition(analysis),
            "key_competitors": self._extract_competitors(scenario, analysis),
            "competitive_advantages": self._identify_advantages(analysis),
            "competitive_threats": self._identify_threats(analysis),
            "differentiation_opportunities": self._identify_differentiation(analysis)
        }
    
    def _extract_competitors(self, scenario: str, analysis: str) -> List[str]:
        """Extract potential competitors from analysis"""
        # Simple competitor identification based on common business terms
        competitors = []
        scenario_lower = scenario.lower()
        
        if "fintech" in scenario_lower:
            competitors.extend(["Traditional Banks", "Payment Processors", "Digital Wallets"])
        if "e-commerce" in scenario_lower:
            competitors.extend(["Amazon", "Local E-commerce", "Retail Chains"])
        if "ai" in scenario_lower or "artificial intelligence" in scenario_lower:
            competitors.extend(["Tech Giants", "AI Startups", "Software Companies"])
        if "healthcare" in scenario_lower:
            competitors.extend(["Healthcare Providers", "Medical Tech", "Pharma Companies"])
        
        return competitors[:3] if competitors else ["Established Players", "New Entrants", "Substitute Products"]
    
    def _identify_target_segments(self, analysis: str) -> List[str]:
        """Identify target market segments"""
        segments = []
        analysis_lower = analysis.lower()
        
        if any(term in analysis_lower for term in ["young", "millennial", "gen z"]):
            segments.append("Young Adults/Digital Natives")
        if any(term in analysis_lower for term in ["business", "enterprise", "b2b"]):
            segments.append("Business/Enterprise")
        if any(term in analysis_lower for term in ["consumer", "individual", "personal"]):
            segments.append("Individual Consumers")
        if any(term in analysis_lower for term in ["small business", "sme", "startup"]):
            segments.append("Small and Medium Enterprises")
        
        return segments if segments else ["General Market", "Early Adopters", "Mainstream Users"]
    
    def _identify_growth_drivers(self, analysis: str) -> List[str]:
        """Identify key growth drivers"""
        drivers = []
        analysis_lower = analysis.lower()
        
        if any(term in analysis_lower for term in ["technology", "digital", "innovation"]):
            drivers.append("Technological Innovation")
        if any(term in analysis_lower for term in ["demand", "need", "requirement"]):
            drivers.append("Market Demand")
        if any(term in analysis_lower for term in ["regulation", "policy", "government"]):
            drivers.append("Regulatory Changes")
        if any(term in analysis_lower for term in ["economic", "growth", "expansion"]):
            drivers.append("Economic Growth")
        
        return drivers[:3] if drivers else ["Market Expansion", "Customer Adoption", "Product Innovation"]
    
    def _identify_challenges(self, analysis: str) -> List[str]:
        """Identify market challenges"""
        challenges = []
        analysis_lower = analysis.lower()
        
        if any(term in analysis_lower for term in ["competition", "competitive"]):
            challenges.append("Intense Competition")
        if any(term in analysis_lower for term in ["regulation", "compliance"]):
            challenges.append("Regulatory Complexity")
        if any(term in analysis_lower for term in ["cost", "expensive", "pricing"]):
            challenges.append("Cost Pressures")
        if any(term in analysis_lower for term in ["technology", "technical"]):
            challenges.append("Technical Challenges")
        
        return challenges[:3] if challenges else ["Market Entry", "Customer Acquisition", "Scalability"]
    
    def _identify_advantages(self, analysis: str) -> List[str]:
        """Identify competitive advantages"""
        return ["Innovation Capability", "Market Timing", "Resource Access"]
    
    def _identify_threats(self, analysis: str) -> List[str]:
        """Identify competitive threats"""
        return ["New Entrants", "Technology Disruption", "Market Saturation"]
    
    def _identify_differentiation(self, analysis: str) -> List[str]:
        """Identify differentiation opportunities"""
        return ["Unique Value Proposition", "Customer Experience", "Technology Leadership"]
    
    def _generate_market_recommendations(self, analysis: str) -> List[str]:
        """Generate strategic market recommendations"""
        recommendations = [
            "Conduct detailed market research and validation",
            "Develop strong competitive positioning strategy",
            "Focus on customer acquisition and retention",
            "Monitor market trends and adapt quickly",
            "Build strategic partnerships and alliances"
        ]
        return recommendations
    
    def _calculate_market_attractiveness(self, analysis: str) -> float:
        """Calculate overall market attractiveness score"""
        # Simple scoring based on positive vs negative indicators
        positive_indicators = ["opportunity", "growth", "potential", "attractive", "promising"]
        negative_indicators = ["challenge", "difficult", "risk", "threat", "barrier"]
        
        positive_count = sum(analysis.lower().count(indicator) for indicator in positive_indicators)
        negative_count = sum(analysis.lower().count(indicator) for indicator in negative_indicators)
        
        if positive_count + negative_count == 0:
            return 0.5
        
        attractiveness = positive_count / (positive_count + negative_count)
        return round(min(max(attractiveness, 0.1), 0.9), 2)
    
    def get_status(self) -> Dict[str, Any]:
        """Get agent status"""
        return {
            "agent": "Market",
            "model": self.model_name,
            "device": self.device,
            "is_ready": self.is_ready,
            "gpu_enabled": self.device == "cuda"
        }
