# 🚀 Four Pillars AI - CrewAI Framework Backend

**Pure CrewAI Multi-Agent Business Intelligence Platform**  
*RTX 4050 Compatible - CrewAI Framework Implementation*

---

## 📋 Overview

This backend implements a complete **CrewAI-powered multi-agent system** for business intelligence analysis. The system uses CrewAI's structured framework for agent coordination while maintaining memory-efficient AI models optimized for Windows and mid-range hardware.

### 🏗️ Architecture

```
Four Pillars AI Backend (CrewAI Framework)
├── 💰 Finance Agent (CPU) - TinyLlama 1.1B with CrewAI coordination
├── 🛡️ Risk Agent (CPU) - TinyLlama 1.1B with CrewAI coordination
├── ⚖️ Compliance Agent (GPU/CPU) - Legal-BERT with CrewAI coordination
└── 📈 Market Agent (CPU) - Mistral-7B with CrewAI coordination
```

---

## 🎯 Key Features

- **🤖 CrewAI Framework**: Structured agent coordination and task management
- **🧠 Memory Optimized**: Designed for 16GB RAM systems with 6GB GPU
- **🪟 Windows Compatible**: Optimized for Windows virtual memory management
- **📊 Multi-Analysis Types**: Comprehensive, focused, or single-agent analysis
- **🔄 Real-time API**: FastAPI with WebSocket support
- **📚 Auto Documentation**: Interactive API docs with Swagger UI

---

## 🛠️ Technical Stack

| Component | Technology | Version |
|-----------|------------|---------|
| **Framework** | CrewAI | 0.83.0 |
| **Backend** | FastAPI | 0.115.4 |
| **AI Models** | PyTorch + Transformers | 2.6.0 + 4.56.0 |
| **GPU Support** | CUDA | 11.8+ |
| **Python** | Python | 3.9+ |
| **Environment** | Windows Virtual Env | .venv |

### 🤖 AI Models Used

| Agent | Model | Size | Device | Memory |
|-------|-------|------|--------|---------|
| Finance | TinyLlama-1.1B-Chat | 2.2GB | CPU | ~3GB RAM |
| Risk | TinyLlama-1.1B-Chat | 2.2GB | CPU | ~3GB RAM |
| Compliance | legal-bert-base-uncased | 0.4GB | GPU/CPU | ~1GB |
| Market | Mistral-7B-Instruct | 13GB | CPU | ~15GB RAM |

---

## 🚀 Quick Start

### Prerequisites

- **Hardware**: 16GB+ RAM, RTX 4050 (6GB VRAM) or compatible NVIDIA GPU (optional)
- **Software**: Python 3.9+, CUDA 11.8+ (for GPU), Git
- **OS**: Windows 10/11 (optimized), Linux compatible

### Installation

1. **Clone Repository**
   ```bash
   git clone https://github.com/DicksonLegend/AIRA.git
   cd AIRA/backend
   ```

2. **Setup Virtual Environment**
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # Linux/Mac
   source .venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start Backend**
   ```bash
   # Optimized startup script
   python start_optimized.py
   
   # Or direct FastAPI
   python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
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
│   ├── main.py                    # FastAPI application entry point
│   ├── services/
│   │   ├── four_pillars_crewai.py # Full CrewAI implementation (ACTIVE)
│   │   └── simple_crewai.py       # [UNUSED] Direct model orchestration
│   ├── models/
│   │   ├── finance_agent.py       # TinyLlama CPU-optimized Finance Agent
│   │   ├── risk_agent.py          # TinyLlama CPU-optimized Risk Agent
│   │   ├── compliance_agent.py    # Legal-BERT GPU/CPU Compliance Agent
│   │   └── market_agent.py        # Mistral-7B CPU Market Agent
│   └── schemas/
│       └── schemas.py             # Pydantic request/response models
├── .venv/                         # Virtual environment
├── requirements.txt               # CrewAI + essential dependencies
├── start_optimized.py            # Memory-optimized startup script
└── README.md                     # This file
```

---

## 🎯 CrewAI Framework Benefits

### 🚀 **Framework Advantages**

1. **Structured Agent Coordination**: CrewAI manages agent interactions and task delegation
2. **Memory & Context Management**: Persistent context across multi-agent workflows
3. **Error Handling & Recovery**: Built-in retry mechanisms and failure recovery
4. **Scalable Task Planning**: Intelligent task distribution and parallel execution

### 🏢 **Production Benefits**

1. **Framework Reliability**: Built on proven CrewAI architecture for agent coordination
2. **Memory Efficiency**: Combines CrewAI structure with optimized model loading
3. **Maintainable Code**: Clean separation of concerns between framework and models
4. **Easy Extension**: Add new agents or modify workflows using CrewAI patterns

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

| Agent | Device | Model | Memory Usage |
|-------|--------|-------|-------------|
| Finance | CPU | TinyLlama-1.1B | ~3GB RAM |
| Risk | CPU | TinyLlama-1.1B | ~3GB RAM |
| Compliance | GPU/CPU | Legal-BERT | ~1GB VRAM/RAM |
| Market | CPU | Mistral-7B | ~15GB RAM |

**💡 Memory Optimization Tips:**
- Finance + Risk agents can share memory efficiently (same model)
- Compliance agent automatically falls back to CPU if GPU memory insufficient
- Market agent requires most memory - monitor system RAM availability

### Environment Variables

```bash
# GPU optimization (optional)
CUDA_VISIBLE_DEVICES=0
PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:512

# Memory management
TRANSFORMERS_CACHE=D:\models_cache
HF_HOME=D:\huggingface_cache
```

---

## 🧪 Testing

### System Test
```bash
python start_optimized.py
```

### API Testing
```bash
# Health check
curl http://localhost:8000/health

# System status
curl http://localhost:8000/status

# Sample analysis
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{"scenario": "Test startup scenario", "analysis_focus": "financial"}'
```

### Memory Monitoring
```bash
# Check available RAM
python -c "import psutil; print(f'Available RAM: {psutil.virtual_memory().available / (1024**3):.1f} GB')"

# Monitor GPU memory (if available)
nvidia-smi
```

---

## 🔧 Troubleshooting

### Common Issues

#### **Model Loading Stuck at "Loading checkpoint shards: 0%"**
```bash
# Solution: Insufficient RAM for large models
# Switch to smaller models or add more RAM
# Check available memory before startup
```

#### **CUDA Out of Memory**
```bash
# Solution: Reduce GPU allocation or use CPU fallback
export PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:256
# Compliance agent will automatically use CPU
```

#### **Virtual Environment Issues**
```bash
# Solution: Use correct Python path
.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

#### **Windows Virtual Memory Errors**
```bash
# Solution: Close other applications to free RAM
# Consider using Linux for better memory management
# Check Windows paging file settings
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

### Analysis Speed (16GB RAM + RTX 4050)

| Analysis Type | Duration | Agents Used | Memory Required |
|---------------|----------|-------------|-----------------|
| Comprehensive | 45-90s | All 4 | ~22GB RAM, 1GB VRAM |
| Financial | 15-30s | Finance | ~3GB RAM |
| Risk | 15-30s | Risk | ~3GB RAM |
| Compliance | 10-20s | Compliance | ~1GB RAM/VRAM |
| Market | 30-60s | Market | ~15GB RAM |

**⚠️ Memory Constraints:**
- Market agent (Mistral-7B) requires significant RAM
- Comprehensive analysis may exceed 16GB RAM capacity
- Consider sequential agent loading for memory-constrained systems

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

- **Minimum**: 8GB RAM, Intel i5 or AMD Ryzen 5
- **Recommended**: 16GB+ RAM, RTX 4050 or GTX 1660 Ti
- **Optimal**: 32GB RAM, RTX 4080+ for simultaneous model loading
- **Storage**: 50GB+ free space for model downloads

---

**🚀 Ready to revolutionize business intelligence with direct AI model implementation!**
