"""
🔍 Vector Store Implementation
Handles embeddings and similarity search for Four Pillars AI
"""
import logging
import json
import os
from typing import Dict, Any, List, Optional, Tuple
import asyncio
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

logger = logging.getLogger(__name__)

class VectorStore:
    def __init__(self):
        self.embeddings = {}
        self.index = {}
        self.model = None
        self.legal_embeddings = None
        self.financial_embeddings = None
        self.market_embeddings = None
        self.dataset_loader = None
        
    async def initialize(self, dataset_loader=None):
        """Initialize Vector Store with embeddings"""
        logger.info("🔍 Initializing Vector Store...")
        
        try:
            # Load sentence transformer model
            self.model = SentenceTransformer('all-MiniLM-L6-v2')
            self.dataset_loader = dataset_loader
            
            if dataset_loader:
                await self._generate_legal_embeddings()
                await self._generate_financial_embeddings()
                await self._generate_market_embeddings()
            
            logger.info("✅ Vector Store ready with embeddings")
            
        except Exception as e:
            logger.error(f"❌ Error initializing Vector Store: {e}")
            # Fallback to basic functionality
            logger.info("⚠️ Vector Store running in basic mode")
    
    async def search(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Generic search method for compatibility"""
        try:
            # Try different search methods based on query content
            if any(term in query.lower() for term in ['legal', 'compliance', 'regulation']):
                return await self.search_legal_knowledge(query, top_k=limit)
            elif any(term in query.lower() for term in ['financial', 'finance', 'investment']):
                return await self.search_financial_context(query, top_k=limit)
            elif any(term in query.lower() for term in ['market', 'economic', 'industry']):
                market_result = await self.search_market_context(query)
                # Convert to list format
                return [{"content": str(market_result), "score": 0.8}]
            else:
                # Default to legal search
                return await self.search_legal_knowledge(query, top_k=limit)
        except Exception as e:
            logger.warning(f"Search failed: {e}")
            return [{"content": f"Search results for: {query}", "score": 0.5}]
    
    async def _generate_legal_embeddings(self):
        """Generate embeddings for legal Q&A data"""
        if not self.dataset_loader:
            return
        
        legal_data = self.dataset_loader.get_legal_data()
        if not legal_data or "processed_qa" not in legal_data:
            logger.warning("No legal data available for embeddings")
            return
        
        try:
            qa_pairs = legal_data["processed_qa"]
            texts = []
            metadata = []
            
            for i, qa in enumerate(qa_pairs[:500]):  # Limit for performance
                # Combine question and answer for embedding
                combined_text = f"Q: {qa.get('question', '')} A: {qa.get('answer', '')}"
                texts.append(combined_text)
                metadata.append({
                    "id": i,
                    "question": qa.get('question', ''),
                    "answer": qa.get('answer', ''),
                    "category": qa.get('category', 'general'),
                    "keywords": qa.get('keywords', []),
                    "complexity": qa.get('complexity', 'medium')
                })
            
            if texts:
                embeddings = self.model.encode(texts)
                self.legal_embeddings = {
                    "embeddings": embeddings,
                    "metadata": metadata,
                    "texts": texts
                }
                
                logger.info(f"📖 Generated embeddings for {len(texts)} legal Q&A pairs")
            
        except Exception as e:
            logger.error(f"Error generating legal embeddings: {e}")
    
    async def _generate_financial_embeddings(self):
        """Generate embeddings for financial data summaries"""
        if not self.dataset_loader:
            return
        
        try:
            financial_data = self.dataset_loader.get_financial_data()
            texts = []
            metadata = []
            
            for data_type, data_info in financial_data.items():
                if "summary" in data_info and "error" not in data_info:
                    summary = data_info["summary"]
                    
                    # Create descriptive text from summary
                    text = f"Financial data: {data_type.replace('_', ' ').title()}. "
                    text += f"Total records: {summary.get('total_records', 0)}. "
                    
                    if "summary_stats" in summary:
                        for col, stats in summary["summary_stats"].items():
                            text += f"{col}: mean {stats.get('mean', 0):.2f}, "
                    
                    texts.append(text)
                    metadata.append({
                        "data_type": data_type,
                        "summary": summary,
                        "category": "financial"
                    })
            
            if texts:
                embeddings = self.model.encode(texts)
                self.financial_embeddings = {
                    "embeddings": embeddings,
                    "metadata": metadata,
                    "texts": texts
                }
                
                logger.info(f"💰 Generated embeddings for {len(texts)} financial datasets")
            
        except Exception as e:
            logger.error(f"Error generating financial embeddings: {e}")
    
    async def _generate_market_embeddings(self):
        """Generate embeddings for market data"""
        if not self.dataset_loader:
            return
        
        try:
            market_data = self.dataset_loader.get_market_data()
            if not market_data or "summary" not in market_data:
                return
            
            summary = market_data["summary"]
            indicators = market_data.get("technical_indicators", {})
            
            # Create market analysis text
            price_stats = summary.get("price_stats", {})
            text = f"Market Analysis for NSE TATA Global. "
            text += f"Current price: {price_stats.get('current_price', 0)}, "
            text += f"Volatility: {price_stats.get('volatility', 0):.2f}, "
            text += f"Average price: {price_stats.get('average_price', 0):.2f}. "
            
            if indicators:
                if indicators.get("sma_20"):
                    text += f"20-day SMA: {indicators['sma_20']:.2f}, "
                if indicators.get("sharpe_ratio"):
                    text += f"Sharpe ratio: {indicators['sharpe_ratio']:.2f}. "
            
            embeddings = self.model.encode([text])
            self.market_embeddings = {
                "embeddings": embeddings,
                "metadata": [{"type": "market_analysis", "symbol": "NSE-TATAGLOBAL11"}],
                "texts": [text]
            }
            
            logger.info("📈 Generated embeddings for market data")
            
        except Exception as e:
            logger.error(f"Error generating market embeddings: {e}")
    
    async def search_legal_knowledge(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        """Search legal knowledge base using semantic similarity"""
        if not self.legal_embeddings or not self.model:
            # Fallback to basic text search
            if self.dataset_loader:
                return self.dataset_loader.search_legal_qa(query, top_k)
            return []
        
        try:
            # Generate query embedding
            query_embedding = self.model.encode([query])
            
            # Calculate similarities
            similarities = cosine_similarity(
                query_embedding, 
                self.legal_embeddings["embeddings"]
            )[0]
            
            # Get top-k most similar
            top_indices = np.argsort(similarities)[::-1][:top_k]
            
            results = []
            for idx in top_indices:
                metadata = self.legal_embeddings["metadata"][idx]
                similarity_score = float(similarities[idx])
                
                result = {
                    "question": metadata["question"],
                    "answer": metadata["answer"],
                    "category": metadata["category"],
                    "keywords": metadata["keywords"],
                    "complexity": metadata["complexity"],
                    "similarity_score": similarity_score,
                    "relevance": "high" if similarity_score > 0.7 else "medium" if similarity_score > 0.5 else "low"
                }
                results.append(result)
            
            logger.info(f"📖 Found {len(results)} relevant legal documents for query")
            return results
            
        except Exception as e:
            logger.error(f"Error in legal knowledge search: {e}")
            return []
    
    async def search_financial_context(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        """Search financial data context"""
        if not self.financial_embeddings or not self.model:
            return []
        
        try:
            query_embedding = self.model.encode([query])
            similarities = cosine_similarity(
                query_embedding, 
                self.financial_embeddings["embeddings"]
            )[0]
            
            top_indices = np.argsort(similarities)[::-1][:top_k]
            
            results = []
            for idx in top_indices:
                metadata = self.financial_embeddings["metadata"][idx]
                similarity_score = float(similarities[idx])
                
                result = {
                    "data_type": metadata["data_type"],
                    "summary": metadata["summary"],
                    "similarity_score": similarity_score,
                    "text": self.financial_embeddings["texts"][idx]
                }
                results.append(result)
            
            logger.info(f"💰 Found {len(results)} relevant financial datasets")
            return results
            
        except Exception as e:
            logger.error(f"Error in financial context search: {e}")
            return []
    
    async def search_market_context(self, query: str) -> Dict[str, Any]:
        """Search market analysis context"""
        if not self.market_embeddings or not self.model:
            return {}
        
        try:
            query_embedding = self.model.encode([query])
            similarity = cosine_similarity(
                query_embedding, 
                self.market_embeddings["embeddings"]
            )[0][0]
            
            if similarity > 0.3:  # Threshold for relevance
                return {
                    "market_analysis": self.market_embeddings["texts"][0],
                    "similarity_score": float(similarity),
                    "metadata": self.market_embeddings["metadata"][0]
                }
            
            return {}
            
        except Exception as e:
            logger.error(f"Error in market context search: {e}")
            return {}
    
    async def get_similar_scenarios(self, scenario: str, agent_type: str = None) -> List[Dict[str, Any]]:
        """Get similar business scenarios from knowledge base"""
        results = []
        
        if agent_type == "compliance" or not agent_type:
            legal_results = await self.search_legal_knowledge(scenario, 3)
            results.extend([{"type": "legal", **result} for result in legal_results])
        
        if agent_type == "finance" or not agent_type:
            financial_results = await self.search_financial_context(scenario, 2)
            results.extend([{"type": "financial", **result} for result in financial_results])
        
        if agent_type == "market" or not agent_type:
            market_result = await self.search_market_context(scenario)
            if market_result:
                results.append({"type": "market", **market_result})
        
        # Sort by similarity score
        results.sort(key=lambda x: x.get("similarity_score", 0), reverse=True)
        
        return results[:5]  # Return top 5 most relevant
    
    async def add_custom_embedding(self, text: str, metadata: Dict[str, Any], category: str):
        """Add custom embedding to the store"""
        if not self.model:
            return
        
        try:
            embedding = self.model.encode([text])
            
            if category not in self.index:
                self.index[category] = {
                    "embeddings": [],
                    "metadata": [],
                    "texts": []
                }
            
            self.index[category]["embeddings"].append(embedding[0])
            self.index[category]["metadata"].append(metadata)
            self.index[category]["texts"].append(text)
            
            logger.info(f"Added custom embedding to {category} category")
            
        except Exception as e:
            logger.error(f"Error adding custom embedding: {e}")
    
    def save_embeddings(self, filepath: str):
        """Save embeddings to disk"""
        try:
            data = {
                "legal_embeddings": self.legal_embeddings,
                "financial_embeddings": self.financial_embeddings,
                "market_embeddings": self.market_embeddings,
                "custom_index": self.index
            }
            
            with open(filepath, 'wb') as f:
                pickle.dump(data, f)
            
            logger.info(f"Embeddings saved to {filepath}")
            
        except Exception as e:
            logger.error(f"Error saving embeddings: {e}")
    
    def load_embeddings(self, filepath: str):
        """Load embeddings from disk"""
        try:
            if os.path.exists(filepath):
                with open(filepath, 'rb') as f:
                    data = pickle.load(f)
                
                self.legal_embeddings = data.get("legal_embeddings")
                self.financial_embeddings = data.get("financial_embeddings")
                self.market_embeddings = data.get("market_embeddings")
                self.index = data.get("custom_index", {})
                
                logger.info(f"Embeddings loaded from {filepath}")
                return True
            
        except Exception as e:
            logger.error(f"Error loading embeddings: {e}")
        
        return False
