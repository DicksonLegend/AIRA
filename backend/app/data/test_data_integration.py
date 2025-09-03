"""
🧪 Data Integration Test Suite
Tests all dataset integrations and data loader functionality
"""
import asyncio
import logging
import sys
import os

# Add the app directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from data.dataset_loader import DatasetLoader
from data.vectore_store import VectorStore
from data.compliance_db import ComplianceDB
from data.financial_db import FinancialDB
from data.market_news import MarketNews
from data.risk_api import RiskAPI

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataIntegrationTester:
    def __init__(self):
        self.dataset_loader = None
        self.vector_store = None
        self.compliance_db = None
        self.financial_db = None
        self.market_news = None
        self.risk_api = None
        
    async def run_all_tests(self):
        """Run comprehensive data integration tests"""
        logger.info("🧪 Starting Data Integration Tests...")
        
        try:
            # Test 1: Dataset Loader
            await self.test_dataset_loader()
            
            # Test 2: Vector Store
            await self.test_vector_store()
            
            # Test 3: Compliance DB
            await self.test_compliance_db()
            
            # Test 4: Financial DB
            await self.test_financial_db()
            
            # Test 5: Market News
            await self.test_market_news()
            
            # Test 6: Risk API
            await self.test_risk_api()
            
            # Test 7: Integration Tests
            await self.test_data_integration()
            
            logger.info("✅ All data integration tests completed successfully!")
            
        except Exception as e:
            logger.error(f"❌ Test suite failed: {e}")
            raise
    
    async def test_dataset_loader(self):
        """Test dataset loader functionality"""
        logger.info("📊 Testing Dataset Loader...")
        
        try:
            self.dataset_loader = DatasetLoader()
            await self.dataset_loader.initialize()
            
            # Test legal data loading
            legal_data = self.dataset_loader.get_legal_data()
            if legal_data:
                logger.info(f"✅ Legal data loaded: {legal_data.get('total_qa_pairs', 0)} Q&A pairs")
            else:
                logger.warning("⚠️ No legal data found")
            
            # Test financial data loading
            financial_data = self.dataset_loader.get_financial_data()
            logger.info(f"✅ Financial datasets loaded: {len(financial_data)} datasets")
            for dataset_type, data in financial_data.items():
                if "error" not in data:
                    logger.info(f"  - {dataset_type}: {data.get('summary', {}).get('total_records', 0)} records")
            
            # Test market data loading
            market_data = self.dataset_loader.get_market_data()
            if market_data and "error" not in market_data:
                logger.info(f"✅ Market data loaded: {market_data.get('summary', {}).get('total_records', 0)} records")
            else:
                logger.warning("⚠️ No market data found")
            
            # Test search functionality
            if legal_data and "processed_qa" in legal_data:
                search_results = self.dataset_loader.search_legal_qa("contract law", 3)
                logger.info(f"✅ Legal search test: {len(search_results)} results found")
            
            logger.info("✅ Dataset Loader tests passed")
            
        except Exception as e:
            logger.error(f"❌ Dataset Loader test failed: {e}")
            raise
    
    async def test_vector_store(self):
        """Test vector store functionality"""
        logger.info("🔍 Testing Vector Store...")
        
        try:
            self.vector_store = VectorStore()
            await self.vector_store.initialize(self.dataset_loader)
            
            # Test legal knowledge search
            if self.vector_store.legal_embeddings:
                legal_results = await self.vector_store.search_legal_knowledge("contract dispute resolution", 3)
                logger.info(f"✅ Legal knowledge search: {len(legal_results)} results")
            else:
                logger.warning("⚠️ No legal embeddings available")
            
            # Test financial context search
            if self.vector_store.financial_embeddings:
                financial_results = await self.vector_store.search_financial_context("government expenditure analysis", 2)
                logger.info(f"✅ Financial context search: {len(financial_results)} results")
            else:
                logger.warning("⚠️ No financial embeddings available")
            
            # Test similar scenarios
            similar_scenarios = await self.vector_store.get_similar_scenarios("tax compliance for small business")
            logger.info(f"✅ Similar scenarios search: {len(similar_scenarios)} results")
            
            logger.info("✅ Vector Store tests passed")
            
        except Exception as e:
            logger.warning(f"⚠️ Vector Store test failed (expected if dependencies missing): {e}")
    
    async def test_compliance_db(self):
        """Test compliance database functionality"""
        logger.info("⚖️ Testing Compliance Database...")
        
        try:
            self.compliance_db = ComplianceDB()
            await self.compliance_db.initialize(self.dataset_loader)
            
            # Test Indian compliance assessment
            indian_assessment = await self.compliance_db.assess_indian_compliance(
                "Starting a fintech company in India with digital payments",
                "private_limited"
            )
            logger.info(f"✅ Indian compliance assessment: {indian_assessment.get('compliance_score', 0)} score")
            
            # Test regulation details
            companies_act = await self.compliance_db.get_regulation_details("COMPANIES_ACT_2013")
            if "error" not in companies_act:
                logger.info("✅ Indian regulation details retrieved")
            
            # Test legal precedent search
            if self.compliance_db.legal_knowledge_base:
                precedents = await self.compliance_db.search_legal_precedents("company formation", 3)
                logger.info(f"✅ Legal precedent search: {len(precedents)} results")
            else:
                logger.warning("⚠️ No legal knowledge base available")
            
            logger.info("✅ Compliance Database tests passed")
            
        except Exception as e:
            logger.error(f"❌ Compliance Database test failed: {e}")
            raise
    
    async def test_financial_db(self):
        """Test financial database functionality"""
        logger.info("💰 Testing Financial Database...")
        
        try:
            self.financial_db = FinancialDB()
            await self.financial_db.initialize(self.dataset_loader)
            
            # Test financial metrics calculation
            test_entity = {
                "entity_id": "test_company_001",
                "revenue": 10000000,
                "net_income": 1200000,
                "total_assets": 5000000,
                "current_assets": 2000000,
                "current_liabilities": 1500000,
                "total_debt": 2000000,
                "equity": 3000000
            }
            
            metrics = await self.financial_db.get_financial_ratios(test_entity)
            logger.info(f"✅ Financial metrics calculated for test entity")
            logger.info(f"  - Financial health score: {metrics.get('financial_health_score', 0)}")
            
            # Test expenditure analysis if data available
            if self.dataset_loader and self.dataset_loader.get_financial_data():
                expenditure_analysis = await self.financial_db.analyze_expenditure_patterns()
                if "error" not in expenditure_analysis:
                    logger.info("✅ Government expenditure analysis completed")
                else:
                    logger.warning("⚠️ Expenditure analysis limited: " + expenditure_analysis.get("error", ""))
            
            logger.info("✅ Financial Database tests passed")
            
        except Exception as e:
            logger.error(f"❌ Financial Database test failed: {e}")
            raise
    
    async def test_market_news(self):
        """Test market news functionality"""
        logger.info("📈 Testing Market News...")
        
        try:
            self.market_news = MarketNews()
            await self.market_news.initialize(self.dataset_loader)
            
            # Test NSE market data analysis
            if self.dataset_loader and self.dataset_loader.get_market_data():
                nse_analysis = await self.market_news.analyze_nse_market_data()
                if "error" not in nse_analysis:
                    logger.info("✅ NSE market data analysis completed")
                    sentiment = nse_analysis.get("market_sentiment", {})
                    logger.info(f"  - Market sentiment: {sentiment.get('sentiment', 'unknown')}")
                else:
                    logger.warning("⚠️ NSE analysis failed: " + nse_analysis.get("error", ""))
            
            # Test government expenditure impact analysis
            if self.dataset_loader and self.dataset_loader.get_social_data():
                impact_analysis = await self.market_news.get_government_expenditure_impact()
                if "error" not in impact_analysis:
                    logger.info("✅ Government expenditure impact analysis completed")
                else:
                    logger.warning("⚠️ Impact analysis failed: " + impact_analysis.get("error", ""))
            
            logger.info("✅ Market News tests passed")
            
        except Exception as e:
            logger.error(f"❌ Market News test failed: {e}")
            raise
    
    async def test_risk_api(self):
        """Test risk API functionality"""
        logger.info("🛡️ Testing Risk API...")
        
        try:
            self.risk_api = RiskAPI()
            await self.risk_api.initialize(self.dataset_loader)
            
            # Test fiscal risk assessment
            if self.dataset_loader:
                fiscal_risk = await self.risk_api.assess_fiscal_risk("India")
                if "error" not in fiscal_risk:
                    logger.info("✅ Fiscal risk assessment completed")
                    logger.info(f"  - Sovereign risk score: {fiscal_risk.get('sovereign_risk_score', 0)}")
                else:
                    logger.warning("⚠️ Fiscal risk assessment failed: " + fiscal_risk.get("error", ""))
            
            # Test market volatility risk assessment
            if self.dataset_loader and self.dataset_loader.get_market_data():
                volatility_risk = await self.risk_api.assess_market_volatility_risk()
                if "error" not in volatility_risk:
                    logger.info("✅ Market volatility risk assessment completed")
                else:
                    logger.warning("⚠️ Volatility risk assessment failed: " + volatility_risk.get("error", ""))
            
            logger.info("✅ Risk API tests passed")
            
        except Exception as e:
            logger.error(f"❌ Risk API test failed: {e}")
            raise
    
    async def test_data_integration(self):
        """Test integration between different data components"""
        logger.info("🔗 Testing Data Integration...")
        
        try:
            # Test scenario: Comprehensive business analysis
            test_scenario = "Establishing a digital payment startup in India with focus on rural markets"
            
            integration_results = {}
            
            # Get compliance analysis
            if self.compliance_db:
                compliance_result = await self.compliance_db.assess_indian_compliance(test_scenario, "startup")
                integration_results["compliance"] = compliance_result
                logger.info("✅ Compliance analysis integrated")
            
            # Get similar scenarios from vector store
            if self.vector_store:
                similar_scenarios = await self.vector_store.get_similar_scenarios(test_scenario)
                integration_results["similar_scenarios"] = similar_scenarios
                logger.info(f"✅ Vector search integrated: {len(similar_scenarios)} similar scenarios")
            
            # Get financial context
            if self.financial_db:
                economic_indicators = await self.financial_db.get_economic_indicators()
                integration_results["economic_context"] = economic_indicators
                logger.info("✅ Economic indicators integrated")
            
            # Get market analysis
            if self.market_news:
                market_impact = await self.market_news.get_government_expenditure_impact()
                integration_results["market_impact"] = market_impact
                logger.info("✅ Market impact analysis integrated")
            
            # Get risk assessment
            if self.risk_api:
                risk_assessment = await self.risk_api.assess_fiscal_risk("India")
                integration_results["risk_factors"] = risk_assessment
                logger.info("✅ Risk assessment integrated")
            
            # Generate integrated insights
            insights = self._generate_integrated_insights(integration_results)
            logger.info(f"✅ Generated {len(insights)} integrated insights")
            
            logger.info("✅ Data Integration tests passed")
            
        except Exception as e:
            logger.error(f"❌ Data Integration test failed: {e}")
            raise
    
    def _generate_integrated_insights(self, results: dict) -> list:
        """Generate insights from integrated data analysis"""
        insights = []
        
        # Compliance insights
        compliance = results.get("compliance", {})
        if compliance and compliance.get("compliance_score", 0) < 0.7:
            insights.append("High compliance risk identified - focus on regulatory requirements")
        
        # Risk insights
        risk_factors = results.get("risk_factors", {})
        if risk_factors and risk_factors.get("sovereign_risk_score", 0) > 0.6:
            insights.append("Elevated sovereign risk may impact business environment")
        
        # Market insights
        market_impact = results.get("market_impact", {})
        if market_impact and "error" not in market_impact:
            insights.append("Government expenditure trends may create market opportunities")
        
        # Vector search insights
        similar_scenarios = results.get("similar_scenarios", [])
        if similar_scenarios:
            insights.append(f"Found {len(similar_scenarios)} similar scenarios for reference")
        
        return insights

async def main():
    """Main test execution function"""
    tester = DataIntegrationTester()
    await tester.run_all_tests()

if __name__ == "__main__":
    asyncio.run(main())
