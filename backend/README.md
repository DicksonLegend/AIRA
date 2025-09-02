# 🚀 Four Pillars AI - CrewAI Framework Backend

**Pure CrewAI Multi-Agent Business Intelligence Platform**  
*RTX 4050 GPU Optimized - No Manual Orchestrator*

---

## 📋 Overview

This backend implements a complete **CrewAI-powered multi-agent system** for business intelligence analysis. The system replaces traditional manual orchestration with CrewAI's structured framework, providing hackathon-ready, production-quality AI analysis across four key business pillars.

### 🏗️ Architecture

```
Four Pillars AI Backend
├── 💰 Finance Agent (GPU) - Financial analysis & investment strategy
├── 🛡️ Risk Agent (CPU) - Risk assessment & mitigation planning  
├── ⚖️ Compliance Agent (CPU) - Legal & regulatory compliance
└── 📈 Market Agent (CPU) - Market intelligence & competitive analysis
```

---

## 🎯 Key Features

- **🤖 Pure CrewAI Framework**: Complete replacement of manual orchestration
- **⚡ GPU Acceleration**: RTX 4050 optimization for Finance Agent
- **🎪 Hackathon Ready**: Structured workflows and clear role separation
- **📊 Multi-Analysis Types**: Comprehensive, focused, or single-agent analysis
- **🔄 Real-time Updates**: WebSocket support for live analysis streaming
- **📚 Auto Documentation**: FastAPI with interactive API docs

---

## 🛠️ Technical Stack

| Component | Technology | Version |
|-----------|------------|---------|
| **Framework** | CrewAI | 0.175.0 |
| **Backend** | FastAPI | Latest |
| **AI/ML** | PyTorch | 2.7.1+cu118 |
| **GPU** | CUDA | 11.8 |
| **Python** | Python | 3.13+ |
| **Environment** | Virtual Env | venv_gpu |

---

## 🚀 Quick Start

### Prerequisites

- **Hardware**: RTX 4050 (6GB VRAM) or compatible NVIDIA GPU
- **Software**: Python 3.13+, CUDA 11.8, Git

### Installation

1. **Clone Repository**
   ```bash
   git clone https://github.com/SparkWorks-Spark-your-Ideas/AIRA.git
   cd AIRA/backend
   ```

2. **Setup Virtual Environment**
   ```bash
   python -m venv venv_gpu
   # Windows
   venv_gpu\Scripts\activate
   # Linux/Mac
   source venv_gpu/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   pip install crewai
   ```

4. **Start Backend**
   ```bash
   # Method 1: Direct Python
   venv_gpu\Scripts\python.exe -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   
   # Method 2: Using start script
   python start_backend.py
   ```

### Verification

- **API Root**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health
- **System Status**: http://localhost:8000/status

---

## 📖 API Documentation

### Core Endpoints

#### **POST** `/analyze`
**Primary Analysis Endpoint**
```json
{
  "scenario": "Your business scenario description",
  "analysis_focus": "comprehensive"
}
```

**Analysis Types:**
- `comprehensive` - All four pillars (30-60s)
- `financial` - GPU-accelerated financial analysis (10-20s)
- `risk` - CPU-optimized risk assessment (10-20s)
- `compliance` - Legal/regulatory analysis (10-20s)
- `market` - Market intelligence analysis (10-20s)

#### **GET** `/analyze/types`
**Available Analysis Types**
```json
{
  "analysis_types": {
    "comprehensive": {
      "description": "Complete Four Pillars analysis",
      "agents": ["finance", "risk", "compliance", "market"],
      "duration": "30-60 seconds",
      "device_allocation": "GPU (Finance) + CPU (Others)"
    }
  }
}
```

#### **GET** `/examples`
**Example Scenarios for Testing**
```json
{
  "example_scenarios": [
    {
      "title": "AI Food Delivery Startup",
      "scenario": "A tech startup wants to launch...",
      "recommended_analysis": "comprehensive"
    }
  ]
}
```

#### **WebSocket** `/ws`
**Real-time Analysis Updates**
```javascript
const ws = new WebSocket('ws://localhost:8000/ws');
ws.send(JSON.stringify({
  "scenario": "Your scenario",
  "analysis_focus": "comprehensive"
}));
```

---

## 🏗️ Project Structure

```
backend/
├── app/
│   ├── main.py                    # FastAPI application (CrewAI only)
│   ├── services/
│   │   ├── four_pillars_crewai.py # Full CrewAI implementation
│   │   ├── simple_crewai.py       # Simplified testing version
│   │   └── agent_orchestrator.py  # [DEPRECATED] Manual orchestrator
│   ├── models/
│   │   ├── finance_agent.py       # GPU-optimized Finance Agent
│   │   ├── risk_agent.py          # CPU-optimized Risk Agent
│   │   ├── compliance_agent.py    # CPU-optimized Compliance Agent
│   │   └── market_agent.py        # CPU-optimized Market Agent
│   └── schemas/
│       └── schemas.py             # Pydantic models
├── venv_gpu/                      # GPU-enabled virtual environment
├── requirements.txt               # Python dependencies
├── start_backend.py              # Backend startup script
├── test_crewai.py                # CrewAI integration tests
└── README.md                     # This file
```

---

## 🎯 CrewAI Framework Benefits

### 🚀 **Hackathon Advantages**

1. **Structured Workflows**: Clear agent roles and task definitions
2. **Parallel Coordination**: Efficient multi-agent task distribution  
3. **Live Demonstrations**: Real-time analysis with visual feedback
4. **Scalable Architecture**: Easy to swap models or add new agents

### 🏢 **Production Benefits**

1. **Framework Reliability**: Built on proven CrewAI architecture
2. **Memory & Planning**: Persistent context and intelligent task planning
3. **Error Handling**: Robust failure recovery and logging
4. **Performance Optimization**: GPU/CPU allocation for optimal speed

---

## ⚙️ Configuration

### GPU Optimization

The system automatically detects and utilizes RTX 4050 GPU:

```python
device_config = {
    "finance": "gpu",      # Complex financial modeling
    "risk": "cpu",         # Fast risk assessment  
    "compliance": "cpu",   # Legal analysis
    "market": "cpu"        # Market analysis
}
```

### Memory Requirements

| Agent | Device | Memory Usage |
|-------|--------|-------------|
| Finance | GPU | ~2.1GB VRAM |
| Risk | CPU | ~0.55GB RAM |
| Compliance | CPU | ~0.4GB RAM |
| Market | CPU | ~13GB RAM |

### Environment Variables

```bash
# Optional configuration
CUDA_VISIBLE_DEVICES=0
PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:512
```

---

## 🧪 Testing

### Unit Tests
```bash
python test_crewai.py
```

### API Testing
```bash
# Health check
curl http://localhost:8000/health

# Sample analysis
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{"scenario": "Test scenario", "analysis_focus": "financial"}'
```

### Load Testing
```bash
# Install dependencies
pip install locust

# Run load tests (create locustfile.py first)
locust -f locustfile.py --host=http://localhost:8000
```

---

## 🔧 Troubleshooting

### Common Issues

#### **ModuleNotFoundError: crewai**
```bash
# Solution: Install CrewAI in correct environment
pip install crewai
```

#### **CUDA Out of Memory**
```bash
# Solution: Reduce model batch size or use CPU fallback
export PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:512
```

#### **Virtual Environment Issues**
```bash
# Solution: Use direct Python path
venv_gpu\Scripts\python.exe -m uvicorn app.main:app --reload
```

### Performance Optimization

1. **GPU Memory Management**
   - Monitor VRAM usage with `nvidia-smi`
   - Adjust model quantization settings
   - Use gradient checkpointing for large models

2. **CPU Optimization**
   - Set optimal thread counts for CPU agents
   - Use memory mapping for large models
   - Enable model quantization where appropriate

3. **Network Optimization**
   - Use HTTP/2 for better concurrent request handling
   - Implement request queuing for high load
   - Configure appropriate timeout values

---

## 📊 Performance Benchmarks

### Analysis Speed (RTX 4050)

| Analysis Type | Duration | Agents Used | Memory |
|---------------|----------|-------------|---------|
| Comprehensive | 30-60s | All 4 | 16GB+ RAM, 2.1GB VRAM |
| Financial | 10-20s | Finance | 2GB RAM, 2.1GB VRAM |
| Risk | 10-20s | Risk | 1GB RAM |
| Compliance | 10-20s | Compliance | 1GB RAM |
| Market | 10-20s | Market | 14GB RAM |

### Concurrent Requests

- **Maximum**: 10 concurrent analyses
- **Recommended**: 3-5 concurrent for optimal performance
- **Queue Management**: Automatic request queuing

---

## 🔄 Migration Guide

### From Manual Orchestrator to CrewAI

The new backend completely replaces the manual orchestration system:

#### **Before (Manual)**
```python
orchestrator = AgentOrchestrator()
await orchestrator.initialize_agents()
results = await orchestrator.analyze_scenario(scenario)
```

#### **After (CrewAI)**
```python
crewai_system = FourPillarsCrewAI()
await crewai_system.initialize()
results = await crewai_system.analyze_business_scenario(scenario, "comprehensive")
```

#### **Benefits of Migration**
- ✅ Structured agent coordination
- ✅ Built-in memory and planning
- ✅ Better error handling
- ✅ Hackathon-ready demonstrations
- ✅ Easier scaling and maintenance

---

## 🎮 Usage Examples

### Example 1: Comprehensive Analysis
```python
import requests

response = requests.post("http://localhost:8000/analyze", json={
    "scenario": "A fintech startup creating blockchain payments for emerging markets",
    "analysis_focus": "comprehensive"
})

print(response.json())
```

### Example 2: Focused Financial Analysis
```python
response = requests.post("http://localhost:8000/analyze/financial", json={
    "scenario": "SaaS platform targeting SMEs with $50/month subscription"
})

print(f"Analysis completed in {response.json()['execution_time_seconds']}s")
```

### Example 3: WebSocket Real-time Updates
```javascript
const ws = new WebSocket('ws://localhost:8000/ws');

ws.onmessage = function(event) {
    const data = JSON.parse(event.data);
    console.log(`Update: ${data.type}`, data);
};

ws.send(JSON.stringify({
    "scenario": "EdTech platform for personalized K-12 learning",
    "analysis_focus": "risk"
}));
```

---

## 📚 API Reference

### Request Models

```python
class AnalysisRequest(BaseModel):
    scenario: str
    analysis_focus: Optional[str] = "comprehensive"
```

### Response Models

```python
class AnalysisResponse(BaseModel):
    scenario: str
    analysis_focus: str
    timestamp: str
    execution_time_seconds: float
    framework: str
    crew_result: str
    agents_utilized: list
    device_allocation: dict
    system_info: dict
    performance_metrics: dict
```

---

## 🤝 Contributing

### Development Setup

1. **Fork Repository**
2. **Create Feature Branch**
   ```bash
   git checkout -b feature/new-agent
   ```
3. **Install Development Dependencies**
   ```bash
   pip install -r requirements-dev.txt
   ```
4. **Run Tests**
   ```bash
   pytest tests/
   ```
5. **Submit Pull Request**

### Code Standards

- **Formatting**: Black, isort
- **Linting**: flake8, mypy
- **Documentation**: Docstrings for all public methods
- **Testing**: Minimum 80% test coverage

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](../LICENSE) file for details.

---

## 🙋‍♂️ Support

### Getting Help

- **Issues**: [GitHub Issues](https://github.com/SparkWorks-Spark-your-Ideas/AIRA/issues)
- **Discussions**: [GitHub Discussions](https://github.com/SparkWorks-Spark-your-Ideas/AIRA/discussions)
- **Documentation**: [API Docs](http://localhost:8000/docs)

### System Requirements

- **Minimum**: 8GB RAM, GTX 1060 or better
- **Recommended**: 16GB+ RAM, RTX 4050 or better
- **Optimal**: 32GB RAM, RTX 4090

---

**🚀 Ready to revolutionize business intelligence with AI-powered multi-agent analysis!**

*Built with ❤️ using CrewAI Framework*
