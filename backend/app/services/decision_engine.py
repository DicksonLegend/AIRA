"""
🧠 Decision Engine - Processes Multi-Agent Results
Generates final recommendations and scores from Four Pillars analysis
"""
import logging
from typing import Dict, Any, List
from datetime import datetime
import statistics

logger = logging.getLogger(__name__)

class DecisionEngine:
    def __init__(self):
        self.weights = {
            "finance": 0.3,
            "risk": 0.25,
            "compliance": 0.2,
            "market": 0.25
        }
        
    def generate_recommendation(self, analysis_results: Dict[str, Any]) -> Dict[str, Any]:
        """Generate final recommendation from Four Pillars analysis"""
        try:
            logger.info("🧠 Generating final recommendation...")
            
            agents_data = analysis_results.get("agents", {})
            
            # Extract scores from each agent
            scores = self._extract_scores(agents_data)
            
            # Calculate weighted overall score
            overall_score = self._calculate_weighted_score(scores)
            
            # Generate recommendation category
            recommendation = self._determine_recommendation(overall_score, scores)
            
            # Identify key insights
            insights = self._extract_key_insights(agents_data)
            
            # Generate action items
            action_items = self._generate_action_items(agents_data, scores)
            
            # Risk assessment
            risk_assessment = self._assess_overall_risk(agents_data)
            
            result = {
                "overall_score": round(overall_score, 2),
                "recommendation": recommendation,
                "confidence": self._calculate_confidence(scores),
                "agent_scores": scores,
                "key_insights": insights,
                "action_items": action_items,
                "risk_assessment": risk_assessment,
                "decision_rationale": self._generate_rationale(overall_score, scores),
                "next_steps": self._suggest_next_steps(recommendation),
                "timestamp": datetime.now().isoformat()
            }
            
            logger.info(f"✅ Recommendation generated - Score: {overall_score:.2f}, Decision: {recommendation}")
            return result
            
        except Exception as e:
            logger.error(f"❌ Decision generation failed: {e}")
            return {
                "overall_score": 0.5,
                "recommendation": "REVIEW_REQUIRED",
                "confidence": 0.0,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
    
    def _extract_scores(self, agents_data: Dict[str, Any]) -> Dict[str, float]:
        """Extract numerical scores from agent analyses"""
        scores = {}
        
        for agent_name, agent_data in agents_data.items():
            if "error" in agent_data:
                scores[agent_name] = 0.5  # Neutral score for failed agents
                continue
            
            if agent_name == "finance":
                scores[agent_name] = self._extract_finance_score(agent_data)
            elif agent_name == "risk":
                scores[agent_name] = self._extract_risk_score(agent_data)
            elif agent_name == "compliance":
                scores[agent_name] = self._extract_compliance_score(agent_data)
            elif agent_name == "market":
                scores[agent_name] = self._extract_market_score(agent_data)
            else:
                scores[agent_name] = 0.5
        
        return scores
    
    def _extract_finance_score(self, finance_data: Dict[str, Any]) -> float:
        """Extract score from finance agent analysis"""
        try:
            metrics = finance_data.get("metrics", {})
            if metrics:
                # Average of financial metrics
                metric_values = [v for v in metrics.values() if isinstance(v, (int, float))]
                if metric_values:
                    return statistics.mean(metric_values)
            
            # Fallback to confidence or default
            return finance_data.get("confidence", 0.5)
        except:
            return 0.5
    
    def _extract_risk_score(self, risk_data: Dict[str, Any]) -> float:
        """Extract score from risk agent analysis (inverted - lower risk = higher score)"""
        try:
            overall_risk = risk_data.get("overall_risk_score", 0.5)
            # Invert risk score (high risk = low score)
            return 1.0 - overall_risk
        except:
            return 0.5
    
    def _extract_compliance_score(self, compliance_data: Dict[str, Any]) -> float:
        """Extract score from compliance agent analysis"""
        try:
            return compliance_data.get("overall_compliance_score", 0.5)
        except:
            return 0.5
    
    def _extract_market_score(self, market_data: Dict[str, Any]) -> float:
        """Extract score from market agent analysis"""
        try:
            return market_data.get("overall_market_score", 0.5)
        except:
            return 0.5
    
    def _calculate_weighted_score(self, scores: Dict[str, float]) -> float:
        """Calculate weighted overall score"""
        if not scores:
            return 0.5
        
        weighted_sum = 0.0
        total_weight = 0.0
        
        for agent, score in scores.items():
            weight = self.weights.get(agent, 0.25)
            weighted_sum += score * weight
            total_weight += weight
        
        return weighted_sum / total_weight if total_weight > 0 else 0.5
    
    def _determine_recommendation(self, overall_score: float, scores: Dict[str, float]) -> str:
        """Determine recommendation based on scores"""
        if overall_score >= 0.8:
            return "STRONGLY_RECOMMEND"
        elif overall_score >= 0.65:
            return "RECOMMEND"
        elif overall_score >= 0.5:
            return "CONDITIONAL"
        elif overall_score >= 0.35:
            return "CAUTION"
        else:
            return "NOT_RECOMMENDED"
    
    def _calculate_confidence(self, scores: Dict[str, float]) -> float:
        """Calculate confidence in the recommendation"""
        if not scores:
            return 0.0
        
        # Confidence based on score consistency and agent success
        score_values = list(scores.values())
        if len(score_values) < 2:
            return 0.5
        
        # Lower standard deviation = higher confidence
        std_dev = statistics.stdev(score_values)
        consistency_score = max(0, 1 - (std_dev * 2))
        
        # Higher average score = higher confidence
        avg_score = statistics.mean(score_values)
        
        # Combine factors
        confidence = (consistency_score * 0.6) + (avg_score * 0.4)
        return round(confidence, 2)
    
    def _extract_key_insights(self, agents_data: Dict[str, Any]) -> List[str]:
        """Extract key insights from all agents"""
        insights = []
        
        # Finance insights
        finance_data = agents_data.get("finance", {})
        if "metrics" in finance_data:
            metrics = finance_data["metrics"]
            if metrics.get("revenue_potential", 0) > 0.7:
                insights.append("Strong revenue potential identified")
            if metrics.get("roi_projection", 0) > 0.7:
                insights.append("Positive ROI projections")
        
        # Risk insights
        risk_data = agents_data.get("risk", {})
        if "risk_categories" in risk_data:
            high_risks = [k for k, v in risk_data["risk_categories"].items() if v == "HIGH"]
            if high_risks:
                insights.append(f"High risk areas: {', '.join(high_risks)}")
        
        # Compliance insights
        compliance_data = agents_data.get("compliance", {})
        if "compliance_gaps" in compliance_data:
            gaps = compliance_data["compliance_gaps"]
            if gaps:
                insights.append(f"Compliance attention needed: {len(gaps)} areas")
        
        # Market insights
        market_data = agents_data.get("market", {})
        if "market_metrics" in market_data:
            metrics = market_data["market_metrics"]
            if metrics.get("market_size_potential") == "LARGE":
                insights.append("Large market opportunity identified")
            if metrics.get("competitive_intensity") == "LOW":
                insights.append("Low competitive intensity - favorable entry conditions")
        
        return insights[:5]  # Top 5 insights
    
    def _generate_action_items(self, agents_data: Dict[str, Any], scores: Dict[str, float]) -> List[str]:
        """Generate prioritized action items"""
        actions = []
        
        # Priority based on lowest scores
        sorted_agents = sorted(scores.items(), key=lambda x: x[1])
        
        for agent, score in sorted_agents[:2]:  # Focus on lowest 2 scores
            if agent == "finance" and score < 0.6:
                actions.append("Conduct detailed financial modeling and projections")
            elif agent == "risk" and score < 0.6:
                actions.append("Develop comprehensive risk mitigation strategies")
            elif agent == "compliance" and score < 0.6:
                actions.append("Complete compliance assessment and gap analysis")
            elif agent == "market" and score < 0.6:
                actions.append("Perform thorough market research and validation")
        
        # General actions
        actions.extend([
            "Develop detailed implementation timeline",
            "Secure stakeholder alignment and approval",
            "Establish monitoring and review processes"
        ])
        
        return actions[:5]
    
    def _assess_overall_risk(self, agents_data: Dict[str, Any]) -> Dict[str, Any]:
        """Assess overall risk level"""
        risk_data = agents_data.get("risk", {})
        compliance_data = agents_data.get("compliance", {})
        
        risk_level = "MEDIUM"
        risk_factors = []
        
        # Risk agent assessment
        if "overall_risk_score" in risk_data:
            risk_score = risk_data["overall_risk_score"]
            if risk_score > 0.7:
                risk_level = "HIGH"
                risk_factors.append("High risk score from risk analysis")
            elif risk_score < 0.3:
                risk_level = "LOW"
        
        # Compliance assessment
        if "overall_compliance_score" in compliance_data:
            compliance_score = compliance_data["overall_compliance_score"]
            if compliance_score < 0.4:
                risk_level = "HIGH"
                risk_factors.append("Low compliance score")
        
        return {
            "level": risk_level,
            "factors": risk_factors,
            "mitigation_required": risk_level in ["HIGH", "MEDIUM"]
        }
    
    def _generate_rationale(self, overall_score: float, scores: Dict[str, float]) -> str:
        """Generate decision rationale"""
        if overall_score >= 0.8:
            return "Strong performance across all four pillars with minimal risks identified."
        elif overall_score >= 0.65:
            return "Good overall assessment with manageable risks and strong opportunities."
        elif overall_score >= 0.5:
            return "Mixed assessment requiring careful consideration and risk mitigation."
        elif overall_score >= 0.35:
            return "Significant concerns identified requiring major improvements before proceeding."
        else:
            return "Multiple critical issues identified across pillars - not recommended without major changes."
    
    def _suggest_next_steps(self, recommendation: str) -> List[str]:
        """Suggest next steps based on recommendation"""
        steps_map = {
            "STRONGLY_RECOMMEND": [
                "Proceed with implementation planning",
                "Secure funding and resources",
                "Begin stakeholder communication",
                "Establish project timeline"
            ],
            "RECOMMEND": [
                "Address minor concerns identified",
                "Finalize implementation strategy",
                "Secure necessary approvals",
                "Begin pilot or phased rollout"
            ],
            "CONDITIONAL": [
                "Address key concerns before proceeding",
                "Conduct additional analysis in weak areas",
                "Develop risk mitigation strategies",
                "Seek expert consultation"
            ],
            "CAUTION": [
                "Major improvements required before proceeding",
                "Conduct comprehensive review",
                "Address critical risk factors",
                "Consider alternative approaches"
            ],
            "NOT_RECOMMENDED": [
                "Significant restructuring required",
                "Address fundamental issues",
                "Consider alternative strategies",
                "Conduct thorough reassessment"
            ]
        }
        
        return steps_map.get(recommendation, ["Review analysis and seek expert guidance"])
    
    def update_weights(self, new_weights: Dict[str, float]):
        """Update agent weights for scoring"""
        if sum(new_weights.values()) != 1.0:
            raise ValueError("Weights must sum to 1.0")
        
        self.weights.update(new_weights)
        logger.info(f"Decision engine weights updated: {self.weights}")
