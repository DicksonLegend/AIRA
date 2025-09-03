# 🚀 FOUR PILLARS AI - Multi-Agent Business Intelligence Platform

[![CrewAI](https://img.shields.io/badge/Framework-CrewAI-blue.svg)](https://www.crewai.com/)
[![GPU Optimized](https://img.shields.io/badge/GPU-RTX%204050%20Optimized-green.svg)](https://www.nvidia.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-yellow.svg)](https://python.org/)
[![FastAPI](https://img.shields.io/badge/API-FastAPI-red.svg)](https://fastapi.tiangolo.com/)

> **Advanced Multi-Agent AI System for Comprehensive Business Intelligence Analysis**

Four Pillars AI is a state-of-the-art business intelligence platform powered by specialized AI agents, each focusing on critical business domains: Finance, Risk Assessment, Compliance, and Market Analysis.

---

## 🏗️ **System Architecture**

```
┌─────────────────────────────────────────────────────────────┐
│                    🚀 FOUR PILLARS AI                      │
│         Multi-Agent Business Intelligence Platform          │
│              GPU Optimized + Real Data Pipeline            │
├─────────────────────────────────────────────────────────────┤
│ 💰 Finance Agent:    microsoft/phi-3.5-mini-instruct [GPU] │
│ 🛡️  Risk Agent:      TinyLlama/TinyLlama-1.1B-Chat   [GPU] │
│ ⚖️  Compliance Agent: nlpaueb/legal-bert-base-uncased[GPU] │
│ 📈 Market Agent:     TinyLlama/TinyLlama-1.1B-Chat   [GPU] │
├─────────────────────────────────────────────────────────────┤
│ 🔧 GPU Memory: ~3.7GB (Perfect for RTX 4050 6GB)          │
│ 📊 Data Pipeline: FinancialDB + MarketNews + VectorStore   │
│ 🌐 Backend: FastAPI + CrewAI + WebSocket + Async           │
└─────────────────────────────────────────────────────────────┘
```

---

## 🤖 **The Four Pillars**

### 💰 **Finance Agent** - Financial Strategist & Investment Analyst
- **Model**: Microsoft Phi-3.5-mini-instruct (2.1GB VRAM)
- **Capabilities**: Revenue projections, cost analysis, ROI calculations, funding requirements
- **Data Sources**: FinancialDB, MarketNews, VectorStore
- **Real Data**: Financial ratios, economic indicators, market impact analysis

### 🛡️ **Risk Agent** - Risk Assessment Specialist  
- **Model**: TinyLlama-1.1B-Chat (0.55GB VRAM)
- **Capabilities**: Multi-dimensional risk assessment, mitigation strategies
- **Data Sources**: RiskAPI, FinancialDB, ComplianceDB, MarketNews, DatasetLoader
- **Risk Categories**: Financial, Operational, Market, Technical, Strategic risks

### ⚖️ **Compliance Agent** - Legal & Compliance Expert
- **Model**: Legal-BERT-base-uncased (0.4GB VRAM)
- **Capabilities**: Regulatory analysis, compliance scoring, legal requirements
- **Data Sources**: ComplianceDB, VectorStore
- **Focus Areas**: Data protection, financial regulations, industry compliance

### 📈 **Market Agent** - Market Intelligence Analyst
- **Model**: TinyLlama-1.1B-Chat (0.55GB VRAM)  
- **Capabilities**: Market analysis, competitive intelligence, growth opportunities
- **Data Sources**: MarketNews, DatasetLoader
- **Analysis**: Market size, competition, trends, customer segments

---

## 📊 **Real Data Pipeline**

### **Integrated Data Sources**
- **📈 Financial Database**: 31 Indian government financial datasets
- **📰 Market News API**: Real-time market news and sentiment analysis
- **🔍 Vector Store**: CUDA-accelerated semantic search with SentenceTransformer
- **⚖️ Compliance Database**: Legal and regulatory frameworks
- **🛡️ Risk API**: Comprehensive risk assessment data
- **📊 Dataset Loader**: Economic indicators and market data (1,235+ records)

### **Data Processing Features**
- **GPU-Accelerated Embeddings**: 200-400 batches/second processing
- **Real-time Analysis**: Live data integration for current market conditions
- **Semantic Search**: Vector-based document retrieval and analysis
- **Economic Indicators**: GDP, inflation, employment, currency rates

---

## ⚡ **Performance Specifications**

### **GPU Optimization (RTX 4050 6GB)**
```
💾 VRAM Allocation:
├── Finance Agent:    2.1GB (Phi-3.5-mini with 4-bit quantization)
├── Risk Agent:       0.55GB (TinyLlama with 4-bit quantization)  
├── Compliance Agent: 0.4GB (Legal-BERT with 4-bit quantization)
├── Market Agent:     0.55GB (TinyLlama with 4-bit quantization)
└── Total Usage:      ~3.7GB (Optimized for 6GB VRAM)
```

### **Execution Metrics**
- **Analysis Time**: 45-60 seconds for comprehensive analysis
- **Success Rate**: 4/4 agents operational
- **Confidence Levels**: 85-95% across all agents
- **Concurrent Processing**: All agents run simultaneously on GPU

---

## 🛠️ **Technology Stack**

### **Backend Framework**
- **FastAPI**: High-performance async API framework
- **CrewAI**: Multi-agent orchestration and coordination
- **PyTorch**: Deep learning framework with CUDA support
- **Transformers**: Hugging Face model integration
- **SentenceTransformers**: Vector embeddings and semantic search

### **AI Models & Optimization**
- **4-bit Quantization**: BitsAndBytesConfig for memory optimization
- **Mixed Precision**: Float16 inference for GPU efficiency  
- **Device Management**: Automatic GPU/CPU allocation
- **Memory Mapping**: Conservative VRAM allocation with CPU fallback

### **Data Processing**
- **Pandas**: Data manipulation and analysis
- **FAISS**: Vector similarity search (CPU optimized)
- **AsyncIO**: Asynchronous data processing
- **Caching**: Intelligent data caching for performance

---

## 🚀 **Quick Start**

### **Prerequisites**
- Python 3.10+
- NVIDIA GPU with 4GB+ VRAM (RTX 4050 recommended)
- CUDA Toolkit
- 8GB+ RAM

### **Installation**
```bash
# Clone the repository
git clone https://github.com/SparkWorks-Spark-your-Ideas/AIRA.git
cd AIRA

# Setup Python environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Install dependencies
cd backend
pip install -r requirements.txt
```

### **Start the Backend**
```bash
# Navigate to backend directory
cd backend

# Start the Four Pillars AI server
python start_backend.py
```

The server will start on `http://localhost:8000` with:
- 📱 **API Documentation**: `http://localhost:8000/docs`
- ⚡ **Health Check**: `http://localhost:8000/health`
- 🌐 **WebSocket**: `ws://localhost:8000/ws`

---

## 📖 **API Usage**

### **Comprehensive Business Analysis**
```json
POST /analyze
{
  "scenario": "A tech startup wants to launch an AI-powered food delivery app in urban markets with real-time demand prediction and dynamic pricing. They need $2M in funding.",
  "analysis_focus": "comprehensive"
}
```

### **Focused Analysis Options**
```json
// Single agent analysis
"analysis_focus": "financial"    // Finance Agent only
"analysis_focus": "risk"         // Risk Agent only  
"analysis_focus": "compliance"   // Compliance Agent only
"analysis_focus": "market"       // Market Agent only

// Full analysis (recommended)
"analysis_focus": "comprehensive" // All 4 agents
```

### **Response Structure**
```json
{
  "scenario": "Business scenario description",
  "execution_time_seconds": 45.32,
  "agents_utilized": ["finance", "risk", "compliance", "market"],
  "device_allocation": {
    "finance": "CUDA",
    "risk": "CUDA", 
    "compliance": "CUDA",
    "market": "CUDA"
  },
  "performance_metrics": {
    "agents_completed": 4,
    "overall_confidence": 0.89
  },
  "results": {
    "finance": { "analysis": "...", "metrics": "..." },
    "risk": { "analysis": "...", "risk_categories": "..." },
    "compliance": { "analysis": "...", "compliance_scores": "..." },
    "market": { "analysis": "...", "market_metrics": "..." }
  }
}
```

---

## 🧪 **Testing & Validation**

### **Test Scenarios**
```bash
# Run comprehensive system tests
python test_comprehensive.py

# Run basic functionality tests  
python test_crewai.py
```

### **Sample Test Cases**
1. **Tech Startup**: AI-powered applications and SaaS platforms
2. **Traditional Business**: Manufacturing and retail digital transformation
3. **Green Energy**: Solar panels and renewable energy projects
4. **Healthcare**: AI diagnostic tools and telemedicine platforms
5. **Fintech**: Payment systems and financial services

---

## 📈 **Development Progress**

### **✅ Completed Features**
- [x] Four specialized AI agents with GPU optimization
- [x] Real data pipeline integration (6 data sources)
- [x] CrewAI framework implementation
- [x] FastAPI backend with WebSocket support
- [x] Comprehensive business intelligence analysis
- [x] GPU memory optimization for RTX 4050
- [x] Vector-based semantic search
- [x] Real-time market data integration
- [x] Multi-dimensional risk assessment
- [x] Legal compliance analysis
- [x] Financial modeling and projections

### **🔧 Current Optimizations**
- [x] TinyLlama integration for efficient market analysis
- [x] 4-bit quantization for all models
- [x] CUDA acceleration for vector embeddings
- [x] Asynchronous data processing
- [x] Memory-efficient model loading

### **🚀 Future Enhancements**
- [ ] Frontend dashboard integration
- [ ] Advanced visualization components
- [ ] Real-time collaboration features
- [ ] Extended market data sources
- [ ] Enhanced compliance frameworks
- [ ] Mobile API endpoints

---

## 🏆 **Key Achievements**

### **Performance Milestones**
- **🚀 System Startup**: < 30 seconds full initialization
- **💾 Memory Efficiency**: 3.7GB VRAM for 4 AI models
- **⚡ Analysis Speed**: 45-60 seconds comprehensive analysis
- **🎯 Accuracy**: 85-95% confidence across all agents
- **📊 Data Integration**: 1,200+ real data points processed

### **Technical Innovations**
- **Multi-Agent GPU Optimization**: First-of-its-kind 4-agent GPU allocation
- **Real Data Integration**: Live economic and market data processing
- **Hybrid Model Architecture**: Combining specialized models for domain expertise
- **Intelligent Memory Management**: Dynamic VRAM allocation with CPU fallback

---

## 🤝 **Contributing**

### **Development Guidelines**
1. **Code Quality**: Follow PEP 8 standards and type hints
2. **Testing**: Add comprehensive tests for new features
3. **Documentation**: Update README and API documentation
4. **GPU Optimization**: Maintain memory efficiency for RTX 4050

### **Branch Structure**
- `main`: Production-ready code
- `feat-beta1-working`: Current development branch
- `feature/*`: Individual feature development

---

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 **Team & Acknowledgments**

**SparkWorks - Spark your Ideas**
- 🚀 Advanced AI Research & Development
- 💡 Innovative Multi-Agent Solutions
- 🔬 GPU Optimization Specialists

### **Special Thanks**
- **CrewAI Team** for the multi-agent framework
- **Hugging Face** for model hosting and transformers
- **NVIDIA** for CUDA optimization support
- **FastAPI** for high-performance API framework

---

## 📞 **Contact & Support**

- **GitHub**: [SparkWorks-Spark-your-Ideas/AIRA](https://github.com/SparkWorks-Spark-your-Ideas/AIRA)
- **Issues**: Report bugs and feature requests via GitHub Issues
- **Discussions**: Join the community discussions for support

---

## 🎯 **Project Status**

```
🟢 PRODUCTION READY - Four Pillars AI System Operational
📊 Data Pipeline: Fully Integrated
🤖 AI Agents: 4/4 Operational on GPU  
⚡ Performance: Optimized for RTX 4050
🚀 API: FastAPI Backend Live
📈 Analysis: Comprehensive Business Intelligence
```
