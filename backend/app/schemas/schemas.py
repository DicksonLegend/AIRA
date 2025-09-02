"""
📋 Pydantic Schemas for Four Pillars AI API
Data validation and serialization models
"""
from pydantic import BaseModel, Field, validator
from typing import Dict, Any, List, Optional, Union
from datetime import datetime
from enum import Enum

# Enums for standardized values
class RecommendationType(str, Enum):
    STRONGLY_RECOMMEND = "STRONGLY_RECOMMEND"
    RECOMMEND = "RECOMMEND"
    CONDITIONAL = "CONDITIONAL"
    CAUTION = "CAUTION"
    NOT_RECOMMENDED = "NOT_RECOMMENDED"

class RiskLevel(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

class AgentStatus(str, Enum):
    READY = "READY"
    INITIALIZING = "INITIALIZING"
    ERROR = "ERROR"
    OFFLINE = "OFFLINE"

# Request Models
class AnalysisRequest(BaseModel):
    scenario: str = Field(..., description="Business scenario to analyze", min_length=50, max_length=5000)
    priority_weights: Optional[Dict[str, float]] = Field(
        default={"finance": 0.3, "risk": 0.25, "compliance": 0.2, "market": 0.25},
        description="Custom weights for each pillar (must sum to 1.0)"
    )
    analysis_depth: Optional[str] = Field(default="standard", description="Analysis depth: quick, standard, or comprehensive")
    include_recommendations: Optional[bool] = Field(default=True, description="Include actionable recommendations")
    
    @validator('priority_weights')
    def weights_must_sum_to_one(cls, v):
        if v and abs(sum(v.values()) - 1.0) > 0.01:
            raise ValueError('Priority weights must sum to 1.0')
        return v

class AgentAnalysisRequest(BaseModel):
    scenario: str = Field(..., description="Scenario to analyze")
    agent_type: str = Field(..., description="Type of agent: finance, risk, compliance, or market")
    additional_context: Optional[Dict[str, Any]] = Field(default=None, description="Additional context for analysis")

class ComplianceCheckRequest(BaseModel):
    business_scenario: str = Field(..., description="Business scenario for compliance check")
    jurisdiction: str = Field(default="US", description="Legal jurisdiction")
    industry: Optional[str] = Field(default=None, description="Industry sector")
    data_handling: Optional[Dict[str, Any]] = Field(default=None, description="Data handling practices")

# Response Models
class AgentResult(BaseModel):
    agent: str = Field(..., description="Agent name")
    model: str = Field(..., description="AI model used")
    analysis: str = Field(..., description="Analysis text")
    confidence: float = Field(..., description="Confidence score", ge=0.0, le=1.0)
    device: str = Field(..., description="Processing device (CPU/GPU)")
    metrics: Optional[Dict[str, Any]] = Field(default=None, description="Agent-specific metrics")
    timestamp: str = Field(..., description="Analysis timestamp")
    execution_time: Optional[float] = Field(default=None, description="Execution time in seconds")

class FinanceAgentResult(AgentResult):
    metrics: Dict[str, float] = Field(..., description="Financial metrics")
    revenue_analysis: Optional[Dict[str, Any]] = Field(default=None)
    profitability: Optional[Dict[str, Any]] = Field(default=None)
    roi_analysis: Optional[Dict[str, Any]] = Field(default=None)

class RiskAgentResult(AgentResult):
    overall_risk_score: float = Field(..., description="Overall risk score", ge=0.0, le=1.0)
    risk_categories: Dict[str, str] = Field(..., description="Risk levels by category")
    mitigation_priority: List[str] = Field(..., description="Priority risks for mitigation")

class ComplianceAgentResult(AgentResult):
    overall_compliance_score: float = Field(..., description="Overall compliance score", ge=0.0, le=1.0)
    compliance_scores: Dict[str, float] = Field(..., description="Compliance scores by area")
    regulatory_requirements: List[str] = Field(..., description="Key regulatory requirements")
    compliance_gaps: List[str] = Field(..., description="Identified compliance gaps")
    recommended_actions: List[str] = Field(..., description="Recommended compliance actions")

class MarketAgentResult(AgentResult):
    overall_market_score: float = Field(..., description="Overall market attractiveness score", ge=0.0, le=1.0)
    market_metrics: Dict[str, Union[str, float]] = Field(..., description="Market analysis metrics")
    competitive_analysis: Dict[str, Any] = Field(..., description="Competitive landscape analysis")
    market_segments: List[str] = Field(..., description="Target market segments")
    growth_drivers: List[str] = Field(..., description="Key growth drivers")

class DecisionRecommendation(BaseModel):
    overall_score: float = Field(..., description="Overall weighted score", ge=0.0, le=1.0)
    recommendation: RecommendationType = Field(..., description="Final recommendation")
    confidence: float = Field(..., description="Confidence in recommendation", ge=0.0, le=1.0)
    agent_scores: Dict[str, float] = Field(..., description="Individual agent scores")
    key_insights: List[str] = Field(..., description="Key insights from analysis")
    action_items: List[str] = Field(..., description="Prioritized action items")
    risk_assessment: Dict[str, Any] = Field(..., description="Overall risk assessment")
    decision_rationale: str = Field(..., description="Rationale for the decision")
    next_steps: List[str] = Field(..., description="Suggested next steps")
    timestamp: str = Field(..., description="Decision timestamp")

class AnalysisResponse(BaseModel):
    scenario: str = Field(..., description="Original business scenario")
    results: Dict[str, AgentResult] = Field(..., description="Results from all agents")
    recommendation: DecisionRecommendation = Field(..., description="Final recommendation")
    execution_summary: Dict[str, Any] = Field(..., description="Execution summary")
    timestamp: str = Field(..., description="Analysis completion timestamp")
    confidence_score: float = Field(..., description="Overall confidence score", ge=0.0, le=1.0)

# System Status Models
class AgentStatusInfo(BaseModel):
    agent: str = Field(..., description="Agent name")
    model: str = Field(..., description="AI model")
    device: str = Field(..., description="Processing device")
    is_ready: bool = Field(..., description="Ready status")
    gpu_enabled: bool = Field(..., description="GPU acceleration status")
    memory_usage: Optional[float] = Field(default=None, description="Memory usage in GB")
    last_activity: Optional[str] = Field(default=None, description="Last activity timestamp")

class SystemStatus(BaseModel):
    is_initialized: bool = Field(..., description="System initialization status")
    total_agents: int = Field(..., description="Total number of agents")
    ready_agents: int = Field(..., description="Number of ready agents")
    gpu_enabled: bool = Field(..., description="GPU acceleration status")
    system_load: Optional[float] = Field(default=None, description="System load percentage")
    uptime: Optional[str] = Field(default=None, description="System uptime")
    timestamp: str = Field(..., description="Status check timestamp")

class DetailedSystemStatus(BaseModel):
    system: SystemStatus = Field(..., description="System status information")
    agents: Dict[str, AgentStatusInfo] = Field(..., description="Individual agent status")
    performance_metrics: Optional[Dict[str, Any]] = Field(default=None, description="Performance metrics")
    resource_usage: Optional[Dict[str, Any]] = Field(default=None, description="Resource usage statistics")

# WebSocket Message Models
class WebSocketMessage(BaseModel):
    type: str = Field(..., description="Message type")
    timestamp: str = Field(..., description="Message timestamp")
    data: Optional[Dict[str, Any]] = Field(default=None, description="Message data")

class AnalysisStartMessage(WebSocketMessage):
    type: str = Field(default="analysis_start", description="Message type")
    message: str = Field(..., description="Start message")

class AgentUpdateMessage(WebSocketMessage):
    type: str = Field(default="agent_update", description="Message type")
    agent: str = Field(..., description="Agent name")
    emoji: str = Field(..., description="Agent emoji")
    message: str = Field(..., description="Update message")
    progress: Optional[float] = Field(default=None, description="Progress percentage")

class AnalysisCompleteMessage(WebSocketMessage):
    type: str = Field(default="analysis_complete", description="Message type")
    results: Dict[str, Any] = Field(..., description="Analysis results")
    message: str = Field(..., description="Completion message")

class ErrorMessage(WebSocketMessage):
    type: str = Field(default="error", description="Message type")
    error: str = Field(..., description="Error description")
    agent: Optional[str] = Field(default=None, description="Agent that caused error")

# Data Source Models
class MarketData(BaseModel):
    symbol: str = Field(..., description="Market symbol")
    current_price: float = Field(..., description="Current price")
    price_change: float = Field(..., description="Price change")
    price_change_percent: float = Field(..., description="Price change percentage")
    volume: int = Field(..., description="Trading volume")
    market_cap: Optional[float] = Field(default=None, description="Market capitalization")
    timestamp: str = Field(..., description="Data timestamp")

class FinancialRatios(BaseModel):
    company_id: str = Field(..., description="Company identifier")
    liquidity_ratios: Dict[str, float] = Field(..., description="Liquidity ratios")
    profitability_ratios: Dict[str, float] = Field(..., description="Profitability ratios")
    leverage_ratios: Dict[str, float] = Field(..., description="Leverage ratios")
    efficiency_ratios: Dict[str, float] = Field(..., description="Efficiency ratios")
    timestamp: str = Field(..., description="Data timestamp")

class ComplianceAssessment(BaseModel):
    business_scenario: str = Field(..., description="Business scenario")
    jurisdiction: str = Field(..., description="Legal jurisdiction")
    applicable_regulations: List[Dict[str, Any]] = Field(..., description="Applicable regulations")
    compliance_score: float = Field(..., description="Overall compliance score", ge=0.0, le=1.0)
    compliance_gaps: List[str] = Field(..., description="Identified compliance gaps")
    required_actions: List[str] = Field(..., description="Required compliance actions")
    risk_level: RiskLevel = Field(..., description="Compliance risk level")
    timestamp: str = Field(..., description="Assessment timestamp")

class MarketSentiment(BaseModel):
    keywords: List[str] = Field(..., description="Analysis keywords")
    overall_sentiment: float = Field(..., description="Overall sentiment score", ge=0.0, le=1.0)
    sentiment_breakdown: Dict[str, float] = Field(..., description="Sentiment breakdown")
    confidence_score: float = Field(..., description="Analysis confidence", ge=0.0, le=1.0)
    article_count: int = Field(..., description="Number of articles analyzed")
    key_themes: List[str] = Field(..., description="Key themes identified")
    timestamp: str = Field(..., description="Analysis timestamp")

# Configuration Models
class AgentConfiguration(BaseModel):
    model_name: str = Field(..., description="AI model name")
    device: str = Field(default="auto", description="Processing device preference")
    max_memory: Optional[str] = Field(default=None, description="Maximum memory allocation")
    temperature: float = Field(default=0.7, description="Model temperature", ge=0.0, le=2.0)
    max_tokens: int = Field(default=200, description="Maximum output tokens", ge=50, le=1000)

class SystemConfiguration(BaseModel):
    agent_configs: Dict[str, AgentConfiguration] = Field(..., description="Agent configurations")
    decision_weights: Dict[str, float] = Field(..., description="Decision engine weights")
    cache_ttl: int = Field(default=300, description="Cache TTL in seconds")
    log_level: str = Field(default="INFO", description="Logging level")
    gpu_memory_fraction: float = Field(default=0.9, description="GPU memory allocation fraction")

# Health Check Models
class HealthCheck(BaseModel):
    status: str = Field(..., description="Health status")
    timestamp: str = Field(..., description="Check timestamp")
    agents: Dict[str, str] = Field(..., description="Agent health status")
    gpu_enabled: bool = Field(..., description="GPU availability")
    memory_usage: Optional[Dict[str, float]] = Field(default=None, description="Memory usage statistics")
    uptime_seconds: Optional[float] = Field(default=None, description="System uptime in seconds")

# Error Models
class ErrorDetail(BaseModel):
    error_type: str = Field(..., description="Error type")
    error_message: str = Field(..., description="Error message")
    error_code: Optional[str] = Field(default=None, description="Error code")
    timestamp: str = Field(..., description="Error timestamp")
    agent: Optional[str] = Field(default=None, description="Agent that caused error")
    traceback: Optional[str] = Field(default=None, description="Error traceback")

class ValidationError(BaseModel):
    field: str = Field(..., description="Field with validation error")
    message: str = Field(..., description="Validation error message")
    value: Optional[Any] = Field(default=None, description="Invalid value")

# Export all models
__all__ = [
    # Request Models
    "AnalysisRequest",
    "AgentAnalysisRequest", 
    "ComplianceCheckRequest",
    
    # Response Models
    "AgentResult",
    "FinanceAgentResult",
    "RiskAgentResult", 
    "ComplianceAgentResult",
    "MarketAgentResult",
    "DecisionRecommendation",
    "AnalysisResponse",
    
    # Status Models
    "AgentStatusInfo",
    "SystemStatus",
    "DetailedSystemStatus",
    "HealthCheck",
    
    # WebSocket Models
    "WebSocketMessage",
    "AnalysisStartMessage",
    "AgentUpdateMessage", 
    "AnalysisCompleteMessage",
    "ErrorMessage",
    
    # Data Models
    "MarketData",
    "FinancialRatios",
    "ComplianceAssessment",
    "MarketSentiment",
    
    # Configuration Models
    "AgentConfiguration",
    "SystemConfiguration",
    
    # Error Models
    "ErrorDetail",
    "ValidationError",
    
    # Enums
    "RecommendationType",
    "RiskLevel", 
    "AgentStatus"
]
