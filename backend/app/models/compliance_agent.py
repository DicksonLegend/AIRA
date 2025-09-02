"""
⚖️ Compliance Agent - Legal and Regulatory Analysis
RTX 4050 GPU Optimized with Legal-BERT
"""
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoModel
import logging
from typing import Dict, Any, List
import asyncio

logger = logging.getLogger(__name__)

class ComplianceAgent:
    def __init__(self):
        self.model_name = "nlpaueb/legal-bert-base-uncased"
        self.model = None
        self.tokenizer = None
        self.device = "cpu"  # Force CPU for lightweight BERT model
        self.is_ready = False
        
    async def initialize(self):
        """Initialize the Compliance Agent with CPU optimization"""
        try:
            logger.info(f"⚖️ Initializing Compliance Agent with {self.model_name} on CPU")
            
            # Load tokenizer
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            
            # Load Legal-BERT model optimized for CPU compliance analysis
            self.model = AutoModel.from_pretrained(
                self.model_name,
                dtype=torch.float32,  # Use dtype instead of torch_dtype for CPU
                device_map="cpu",
                use_safetensors=True,
                trust_remote_code=True
            )
            
            self.is_ready = True
            logger.info(f"✅ Compliance Agent ready on CPU - Legal-BERT (~0.4GB RAM)")
            
        except Exception as e:
            logger.error(f"❌ Compliance Agent initialization failed: {e}")
            raise
    
    async def analyze(self, scenario: str) -> Dict[str, Any]:
        """Analyze compliance and regulatory requirements"""
        if not self.is_ready:
            raise RuntimeError("Compliance Agent not initialized")
        
        try:
            # Analyze compliance aspects
            compliance_areas = [
                "Data Protection and Privacy (GDPR, CCPA)",
                "Financial Services Regulations (SOX, Basel III)",
                "Industry-Specific Compliance (FDA, FCC, EPA)",
                "International Trade and Export Controls",
                "Labor and Employment Laws",
                "Intellectual Property Protection",
                "Anti-Money Laundering (AML)",
                "Cybersecurity and Data Security Standards"
            ]
            
            # Analyze scenario for compliance indicators
            compliance_scores = {}
            for area in compliance_areas:
                score = await self._analyze_compliance_area(scenario, area)
                compliance_scores[area.split(" (")[0].lower().replace(" ", "_")] = score
            
            # Generate comprehensive analysis
            analysis = await self._generate_compliance_report(scenario, compliance_scores)
            
            # Structure the response
            result = {
                "agent": "Compliance",
                "model": self.model_name,
                "analysis": analysis,
                "compliance_scores": compliance_scores,
                "regulatory_requirements": self._identify_key_regulations(scenario),
                "compliance_gaps": self._identify_compliance_gaps(compliance_scores),
                "recommended_actions": self._generate_recommendations(compliance_scores),
                "overall_compliance_score": self._calculate_overall_compliance(compliance_scores),
                "confidence": 0.82,
                "device": self.device
            }
            
            logger.info("⚖️ Compliance analysis completed")
            return result
            
        except Exception as e:
            logger.error(f"❌ Compliance analysis failed: {e}")
            return {
                "agent": "Compliance",
                "error": str(e),
                "analysis": "Compliance analysis unavailable due to technical error"
            }
    
    async def _analyze_compliance_area(self, scenario: str, area: str) -> float:
        """Analyze specific compliance area"""
        try:
            # Create analysis prompt
            text = f"Analyzing {area} compliance for: {scenario}"
            
            # Tokenize for CPU inference
            inputs = self.tokenizer(
                text, 
                return_tensors="pt", 
                max_length=512, 
                truncation=True, 
                padding=True
            )
            # No need to move to CUDA since we're using CPU
            
            # Get embeddings on CPU
            with torch.no_grad():
                outputs = self.model(**inputs)
                embeddings = outputs.last_hidden_state.mean(dim=1)
            
            # Simple compliance scoring based on keywords and context
            scenario_lower = scenario.lower()
            area_keywords = self._get_area_keywords(area)
            
            keyword_matches = sum(1 for keyword in area_keywords if keyword in scenario_lower)
            keyword_score = min(keyword_matches / len(area_keywords), 1.0)
            
            # Combine with embedding-based analysis
            embedding_score = torch.sigmoid(embeddings.mean()).item()
            
            final_score = (keyword_score * 0.6) + (embedding_score * 0.4)
            return round(final_score, 2)
            
        except Exception as e:
            logger.warning(f"Compliance area analysis failed: {e}")
            return 0.5  # Default neutral score
    
    def _get_area_keywords(self, area: str) -> List[str]:
        """Get keywords for specific compliance area"""
        keyword_map = {
            "Data Protection and Privacy": ["data", "privacy", "personal", "gdpr", "ccpa", "consent"],
            "Financial Services Regulations": ["financial", "banking", "securities", "sox", "basel", "audit"],
            "Industry-Specific Compliance": ["industry", "regulation", "standard", "certification", "fda", "fcc"],
            "International Trade": ["international", "export", "import", "trade", "customs", "tariff"],
            "Labor and Employment": ["employment", "labor", "worker", "workplace", "discrimination", "safety"],
            "Intellectual Property": ["patent", "trademark", "copyright", "intellectual", "property", "license"],
            "Anti-Money Laundering": ["aml", "money", "laundering", "kyc", "suspicious", "transaction"],
            "Cybersecurity": ["cybersecurity", "security", "data", "breach", "encryption", "access"]
        }
        
        for key, keywords in keyword_map.items():
            if key in area:
                return keywords
        return ["compliance", "regulation", "requirement"]
    
    async def _generate_compliance_report(self, scenario: str, scores: Dict[str, float]) -> str:
        """Generate comprehensive compliance analysis report"""
        high_risk_areas = [area for area, score in scores.items() if score > 0.7]
        medium_risk_areas = [area for area, score in scores.items() if 0.4 <= score <= 0.7]
        low_risk_areas = [area for area, score in scores.items() if score < 0.4]
        
        report = f"""
        Compliance Analysis Report:
        
        Scenario Overview: {scenario[:200]}...
        
        High Compliance Risk Areas ({len(high_risk_areas)}):
        {', '.join(high_risk_areas) if high_risk_areas else 'None identified'}
        
        Medium Compliance Risk Areas ({len(medium_risk_areas)}):
        {', '.join(medium_risk_areas) if medium_risk_areas else 'None identified'}
        
        Low Compliance Risk Areas ({len(low_risk_areas)}):
        {', '.join(low_risk_areas) if low_risk_areas else 'None identified'}
        
        Regulatory Considerations:
        - Ensure proper legal review before implementation
        - Establish compliance monitoring procedures
        - Regular compliance audits recommended
        - Stay updated on regulatory changes
        """
        
        return report.strip()
    
    def _identify_key_regulations(self, scenario: str) -> List[str]:
        """Identify key regulations that apply"""
        regulations = []
        scenario_lower = scenario.lower()
        
        if any(word in scenario_lower for word in ["data", "privacy", "personal"]):
            regulations.append("GDPR/CCPA Data Protection")
        if any(word in scenario_lower for word in ["financial", "banking", "payment"]):
            regulations.append("Financial Services Regulations")
        if any(word in scenario_lower for word in ["international", "export", "global"]):
            regulations.append("International Trade Regulations")
        if any(word in scenario_lower for word in ["employee", "worker", "employment"]):
            regulations.append("Labor and Employment Laws")
        if any(word in scenario_lower for word in ["technology", "software", "platform"]):
            regulations.append("Technology and IP Regulations")
        
        return regulations if regulations else ["General Business Regulations"]
    
    def _identify_compliance_gaps(self, scores: Dict[str, float]) -> List[str]:
        """Identify areas with compliance gaps"""
        gaps = []
        for area, score in scores.items():
            if score > 0.6:  # High risk areas
                gaps.append(f"{area.replace('_', ' ').title()} - High Priority")
        return gaps
    
    def _generate_recommendations(self, scores: Dict[str, float]) -> List[str]:
        """Generate compliance recommendations"""
        recommendations = []
        
        for area, score in scores.items():
            if score > 0.7:
                recommendations.append(f"Immediate review required for {area.replace('_', ' ')}")
            elif score > 0.5:
                recommendations.append(f"Monitor {area.replace('_', ' ')} compliance closely")
        
        # General recommendations
        recommendations.extend([
            "Conduct regular compliance audits",
            "Establish compliance monitoring system",
            "Train staff on relevant regulations",
            "Maintain documentation for regulatory review"
        ])
        
        return recommendations[:5]  # Return top 5 recommendations
    
    def _calculate_overall_compliance(self, scores: Dict[str, float]) -> float:
        """Calculate overall compliance score"""
        if not scores:
            return 0.5
        
        # Weight higher scores more heavily (compliance risk)
        weighted_sum = sum(score ** 2 for score in scores.values())
        weighted_average = weighted_sum / len(scores)
        
        # Convert to compliance score (lower risk = higher compliance)
        compliance_score = 1.0 - weighted_average
        return round(max(compliance_score, 0.1), 2)
    
    def get_status(self) -> Dict[str, Any]:
        """Get agent status"""
        return {
            "agent": "Compliance",
            "model": self.model_name,
            "device": self.device,
            "is_ready": self.is_ready,
            "gpu_enabled": self.device == "cuda"
        }