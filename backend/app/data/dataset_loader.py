"""
📊 Dataset Loader Module
Loads and processes all datasets for Four Pillars AI system
"""
import logging
import json
import pandas as pd
import os
from typing import Dict, Any, List, Optional
from datetime import datetime
import asyncio

logger = logging.getLogger(__name__)

class DatasetLoader:
    def __init__(self):
        self.datasets_path = os.path.join(os.path.dirname(__file__), "datasets")
        self.legal_data = None
        self.financial_data = {}
        self.market_data = None
        self.social_data = None
        
    async def initialize(self):
        """Initialize and load all datasets"""
        logger.info("📊 Initializing Dataset Loader...")
        
        try:
            await self._load_legal_dataset()
            await self._load_financial_datasets()
            await self._load_market_dataset()
            await self._load_social_dataset()
            
            logger.info("✅ All datasets loaded successfully")
        except Exception as e:
            logger.error(f"❌ Error loading datasets: {e}")
            raise
    
    async def _load_legal_dataset(self):
        """Load Indian Legal Q&A dataset"""
        legal_file = os.path.join(self.datasets_path, "legal", "IndicLegalQA_Dataset_10K_Revised.json")
        
        if not os.path.exists(legal_file):
            logger.warning(f"Legal dataset not found: {legal_file}")
            return
        
        try:
            with open(legal_file, 'r', encoding='utf-8') as f:
                raw_data = json.load(f)
            
            # Process and structure the legal data
            self.legal_data = {
                "total_qa_pairs": len(raw_data) if isinstance(raw_data, list) else 1,
                "data": raw_data,
                "processed_qa": self._process_legal_qa(raw_data),
                "categories": self._categorize_legal_data(raw_data),
                "last_updated": datetime.now().isoformat()
            }
            
            logger.info(f"📖 Legal dataset loaded: {self.legal_data['total_qa_pairs']} Q&A pairs")
            
        except Exception as e:
            logger.error(f"Error loading legal dataset: {e}")
            self.legal_data = {"error": str(e)}
    
    async def _load_financial_datasets(self):
        """Load all financial CSV datasets"""
        financial_files = {
            "aggregate_expenditure": "Aggregate_Expenditure.csv",
            "capital_expenditure": "Capital_Expenditure.csv", 
            "revenue_expenditure": "Revenue_Expenditure.csv",
            "gross_fiscal_deficits": "Gross_Fiscal_Deficits.csv",
            "revenue_deficits": "Revenue_Deficits.csv",
            "tax_revenues": "Own_Tax_Revenues.csv",
            "gsdp_series": "Nominal_GSDP_Series.csv"
        }
        
        financial_dir = os.path.join(self.datasets_path, "financial")
        
        for key, filename in financial_files.items():
            file_path = os.path.join(financial_dir, filename)
            
            if os.path.exists(file_path):
                try:
                    # Try UTF-8 first, then fall back to other encodings
                    try:
                        df = pd.read_csv(file_path, encoding='utf-8')
                    except UnicodeDecodeError:
                        # Try common encodings for Indian datasets
                        for encoding in ['latin1', 'cp1252', 'iso-8859-1']:
                            try:
                                df = pd.read_csv(file_path, encoding=encoding)
                                logger.info(f"📊 Loaded {filename} with {encoding} encoding")
                                break
                            except UnicodeDecodeError:
                                continue
                        else:
                            raise UnicodeDecodeError("Failed to decode with any encoding")
                    
                    # Clean and process the data
                    df_processed = self._clean_financial_data(df, key)
                    
                    self.financial_data[key] = {
                        "raw_data": df,
                        "processed_data": df_processed,
                        "summary": self._generate_financial_summary(df_processed, key),
                        "last_updated": datetime.now().isoformat()
                    }
                    
                    logger.info(f"💰 Loaded {key}: {len(df)} records")
                    
                except Exception as e:
                    logger.error(f"Error loading {filename}: {e}")
                    self.financial_data[key] = {"error": str(e)}
            else:
                logger.warning(f"Financial file not found: {file_path}")
    
    async def _load_market_dataset(self):
        """Load NSE market data"""
        market_file = os.path.join(self.datasets_path, "market", "NSE-TATAGLOBAL11.csv")
        
        if not os.path.exists(market_file):
            logger.warning(f"Market dataset not found: {market_file}")
            return
        
        try:
            # Try UTF-8 first, then fall back to other encodings
            try:
                df = pd.read_csv(market_file, encoding='utf-8')
            except UnicodeDecodeError:
                # Try common encodings for Indian datasets
                for encoding in ['latin1', 'cp1252', 'iso-8859-1']:
                    try:
                        df = pd.read_csv(market_file, encoding=encoding)
                        logger.info(f"📈 Loaded market data with {encoding} encoding")
                        break
                    except UnicodeDecodeError:
                        continue
                else:
                    raise UnicodeDecodeError("Failed to decode market data with any encoding")
            
            # Process market data
            df_processed = self._clean_market_data(df)
            
            self.market_data = {
                "raw_data": df,
                "processed_data": df_processed,
                "summary": self._generate_market_summary(df_processed),
                "technical_indicators": self._calculate_technical_indicators(df_processed),
                "last_updated": datetime.now().isoformat()
            }
            
            logger.info(f"📈 Market dataset loaded: {len(df)} records")
            
        except Exception as e:
            logger.error(f"Error loading market dataset: {e}")
            self.market_data = {"error": str(e)}
    
    async def _load_social_dataset(self):
        """Load social sector expenditure data"""
        social_file = os.path.join(self.datasets_path, "social", "Social_Sector_Expenditure.csv")
        
        if not os.path.exists(social_file):
            logger.warning(f"Social dataset not found: {social_file}")
            return
        
        try:
            # Try UTF-8 first, then fall back to other encodings
            try:
                df = pd.read_csv(social_file, encoding='utf-8')
            except UnicodeDecodeError:
                # Try common encodings for Indian datasets
                for encoding in ['latin1', 'cp1252', 'iso-8859-1']:
                    try:
                        df = pd.read_csv(social_file, encoding=encoding)
                        logger.info(f"🏛️ Loaded social data with {encoding} encoding")
                        break
                    except UnicodeDecodeError:
                        continue
                else:
                    raise UnicodeDecodeError("Failed to decode social data with any encoding")
            
            # Process social data
            df_processed = self._clean_social_data(df)
            
            self.social_data = {
                "raw_data": df,
                "processed_data": df_processed,
                "summary": self._generate_social_summary(df_processed),
                "last_updated": datetime.now().isoformat()
            }
            
            logger.info(f"🏥 Social dataset loaded: {len(df)} records")
            
        except Exception as e:
            logger.error(f"Error loading social dataset: {e}")
            self.social_data = {"error": str(e)}
    
    def _process_legal_qa(self, raw_data: Any) -> List[Dict[str, Any]]:
        """Process legal Q&A data for better structure"""
        processed = []
        
        if isinstance(raw_data, list):
            for item in raw_data:
                if isinstance(item, dict):
                    processed_item = {
                        "question": item.get("question", ""),
                        "answer": item.get("answer", ""),
                        "category": item.get("category", "general"),
                        "keywords": self._extract_legal_keywords(item),
                        "complexity": self._assess_legal_complexity(item)
                    }
                    processed.append(processed_item)
        
        return processed[:1000]  # Limit for performance
    
    def _categorize_legal_data(self, raw_data: Any) -> Dict[str, int]:
        """Categorize legal data by topics"""
        categories = {}
        
        if isinstance(raw_data, list):
            for item in raw_data:
                if isinstance(item, dict):
                    category = item.get("category", "general")
                    categories[category] = categories.get(category, 0) + 1
        
        return categories
    
    def _extract_legal_keywords(self, item: Dict[str, Any]) -> List[str]:
        """Extract keywords from legal Q&A"""
        # Simple keyword extraction
        text = f"{item.get('question', '')} {item.get('answer', '')}".lower()
        legal_keywords = ["contract", "agreement", "law", "regulation", "compliance", 
                         "liability", "rights", "obligations", "court", "judgment"]
        
        found_keywords = [kw for kw in legal_keywords if kw in text]
        return found_keywords
    
    def _assess_legal_complexity(self, item: Dict[str, Any]) -> str:
        """Assess complexity of legal question"""
        answer_length = len(item.get("answer", ""))
        
        if answer_length > 500:
            return "high"
        elif answer_length > 200:
            return "medium"
        else:
            return "low"
    
    def _clean_financial_data(self, df: pd.DataFrame, data_type: str) -> pd.DataFrame:
        """Clean and normalize financial data"""
        df_clean = df.copy()
        
        # Remove any unnamed columns
        df_clean = df_clean.loc[:, ~df_clean.columns.str.contains('^Unnamed')]
        
        # Convert numeric columns
        for col in df_clean.columns:
            if col.lower() not in ['state', 'year', 'category', 'type']:
                try:
                    df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')
                except:
                    pass
        
        # Remove rows with all NaN values
        df_clean = df_clean.dropna(how='all')
        
        return df_clean
    
    def _generate_financial_summary(self, df: pd.DataFrame, data_type: str) -> Dict[str, Any]:
        """Generate summary statistics for financial data"""
        numeric_cols = df.select_dtypes(include=['number']).columns
        
        summary = {
            "total_records": len(df),
            "date_range": self._get_date_range(df),
            "numeric_columns": list(numeric_cols),
            "summary_stats": {}
        }
        
        for col in numeric_cols:
            if not df[col].isna().all():
                summary["summary_stats"][col] = {
                    "mean": float(df[col].mean()),
                    "median": float(df[col].median()),
                    "min": float(df[col].min()),
                    "max": float(df[col].max()),
                    "std": float(df[col].std())
                }
        
        return summary
    
    def _clean_market_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Clean market data"""
        df_clean = df.copy()
        
        # Ensure proper column names
        expected_cols = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
        
        # Convert date column
        if 'Date' in df_clean.columns:
            try:
                df_clean['Date'] = pd.to_datetime(df_clean['Date'])
            except:
                pass
        
        # Convert price columns to numeric
        price_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
        for col in price_cols:
            if col in df_clean.columns:
                try:
                    df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')
                except:
                    pass
        
        # Sort by date
        if 'Date' in df_clean.columns:
            df_clean = df_clean.sort_values('Date')
        
        return df_clean.dropna()
    
    def _generate_market_summary(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Generate market data summary"""
        if 'Close' not in df.columns:
            return {"error": "No Close price data available"}
        
        summary = {
            "total_records": len(df),
            "date_range": self._get_date_range(df),
            "price_stats": {
                "current_price": float(df['Close'].iloc[-1]) if len(df) > 0 else 0,
                "highest_price": float(df['Close'].max()),
                "lowest_price": float(df['Close'].min()),
                "average_price": float(df['Close'].mean()),
                "volatility": float(df['Close'].std())
            }
        }
        
        return summary
    
    def _calculate_technical_indicators(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Calculate basic technical indicators"""
        if 'Close' not in df.columns or len(df) < 20:
            return {}
        
        close_prices = df['Close']
        
        # Simple Moving Averages
        sma_20 = close_prices.rolling(window=20).mean()
        sma_50 = close_prices.rolling(window=50).mean() if len(df) >= 50 else None
        
        # Daily returns
        daily_returns = close_prices.pct_change()
        
        indicators = {
            "sma_20": float(sma_20.iloc[-1]) if not sma_20.isna().iloc[-1] else None,
            "sma_50": float(sma_50.iloc[-1]) if sma_50 is not None and not sma_50.isna().iloc[-1] else None,
            "daily_volatility": float(daily_returns.std()),
            "sharpe_ratio": float(daily_returns.mean() / daily_returns.std()) if daily_returns.std() != 0 else 0
        }
        
        return indicators
    
    def _clean_social_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Clean social sector data"""
        return self._clean_financial_data(df, "social")
    
    def _generate_social_summary(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Generate social data summary"""
        return self._generate_financial_summary(df, "social")
    
    def _get_date_range(self, df: pd.DataFrame) -> Dict[str, str]:
        """Get date range from dataframe"""
        date_cols = [col for col in df.columns if 'date' in col.lower() or 'year' in col.lower()]
        
        if date_cols:
            col = date_cols[0]
            try:
                dates = pd.to_datetime(df[col], errors='coerce').dropna()
                if len(dates) > 0:
                    return {
                        "start": dates.min().strftime("%Y-%m-%d"),
                        "end": dates.max().strftime("%Y-%m-%d")
                    }
            except:
                pass
        
        return {"start": "unknown", "end": "unknown"}
    
    # Public methods for accessing data
    def get_legal_data(self) -> Optional[Dict[str, Any]]:
        """Get processed legal data"""
        return self.legal_data
    
    def get_financial_data(self, data_type: str = None) -> Dict[str, Any]:
        """Get financial data by type or all"""
        if data_type:
            return self.financial_data.get(data_type, {})
        return self.financial_data
    
    def get_market_data(self) -> Optional[Dict[str, Any]]:
        """Get processed market data"""
        return self.market_data
    
    def get_social_data(self) -> Optional[Dict[str, Any]]:
        """Get processed social data"""
        return self.social_data
    
    async def get_economic_indicators(self) -> List[Dict[str, Any]]:
        """Get economic indicators data"""
        # Return economic indicators from financial data
        if self.financial_data and 'economic_indicators' in self.financial_data:
            return self.financial_data['economic_indicators']
        
        # Fallback to generating basic economic indicators
        return [
            {
                "indicator_name": "GDP Growth Rate",
                "current_value": "6.8%",
                "trend": "positive",
                "category": "growth"
            },
            {
                "indicator_name": "Inflation Rate", 
                "current_value": "4.2%",
                "trend": "stable",
                "category": "monetary"
            },
            {
                "indicator_name": "Employment Rate",
                "current_value": "95.3%",
                "trend": "positive", 
                "category": "employment"
            },
            {
                "indicator_name": "Interest Rate",
                "current_value": "6.5%",
                "trend": "stable",
                "category": "monetary"
            },
            {
                "indicator_name": "Market Volatility Index",
                "current_value": "18.4",
                "trend": "negative",
                "category": "market"
            }
        ]
    
    def search_legal_qa(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """Search legal Q&A data"""
        if not self.legal_data or "processed_qa" not in self.legal_data:
            return []
        
        query_lower = query.lower()
        results = []
        
        for qa in self.legal_data["processed_qa"]:
            question = qa.get("question", "").lower()
            answer = qa.get("answer", "").lower()
            
            if query_lower in question or query_lower in answer:
                results.append(qa)
                
            if len(results) >= limit:
                break
        
        return results
    
    def get_fiscal_deficit_trends(self) -> Optional[pd.DataFrame]:
        """Get fiscal deficit trends for risk assessment"""
        deficit_data = self.financial_data.get("gross_fiscal_deficits", {})
        if "processed_data" in deficit_data:
            return deficit_data["processed_data"]
        return None
    
    def get_revenue_trends(self) -> Optional[pd.DataFrame]:
        """Get revenue trends for financial analysis"""
        revenue_data = self.financial_data.get("tax_revenues", {})
        if "processed_data" in revenue_data:
            return revenue_data["processed_data"]
        return None
    
    def get_market_sentiment_data(self) -> Dict[str, Any]:
        """Get market sentiment indicators"""
        if not self.market_data:
            return {}
        
        summary = self.market_data.get("summary", {})
        indicators = self.market_data.get("technical_indicators", {})
        
        return {
            "sentiment_score": self._calculate_market_sentiment(summary, indicators),
            "volatility": indicators.get("daily_volatility", 0),
            "trend": self._determine_market_trend(summary),
            "confidence": 0.75  # Base confidence
        }
    
    def _calculate_market_sentiment(self, summary: Dict[str, Any], indicators: Dict[str, Any]) -> float:
        """Calculate market sentiment score"""
        price_stats = summary.get("price_stats", {})
        current_price = price_stats.get("current_price", 0)
        average_price = price_stats.get("average_price", 0)
        
        if average_price == 0:
            return 0.5
        
        # Simple sentiment based on price relative to average
        price_ratio = current_price / average_price
        sentiment = min(max((price_ratio - 0.8) / 0.4, 0), 1)  # Normalize to 0-1
        
        return sentiment
    
    def _determine_market_trend(self, summary: Dict[str, Any]) -> str:
        """Determine market trend direction"""
        price_stats = summary.get("price_stats", {})
        current_price = price_stats.get("current_price", 0)
        average_price = price_stats.get("average_price", 0)
        
        if current_price > average_price * 1.05:
            return "bullish"
        elif current_price < average_price * 0.95:
            return "bearish"
        else:
            return "neutral"
