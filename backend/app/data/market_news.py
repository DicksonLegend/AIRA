"""
📈 Market News and Data Interface
Provides access to market intelligence and news sources
"""
import logging
from typing import Dict, Any, List, Optional
import asyncio
from datetime import datetime, timedelta
import json

logger = logging.getLogger(__name__)

class MarketNews:
    def __init__(self):
        self.news_sources = {
            "reuters": "https://api.reuters.com/news",
            "bloomberg": "https://api.bloomberg.com/news",
            "market_watch": "https://api.marketwatch.com/news",
            "financial_times": "https://api.ft.com/news"
        }
        self.cache = {}
        self.cache_ttl = 900  # 15 minutes
        self.dataset_loader = None
        
    async def initialize(self, dataset_loader=None):
        """Initialize Market News API connections"""
        logger.info("📈 Initializing Market News API...")
        self.dataset_loader = dataset_loader
        # Placeholder for actual API initialization
        logger.info("✅ Market News API ready")
    
    async def get_market_sentiment(self, keywords: List[str], timeframe: str = "24h") -> Dict[str, Any]:
        """Get market sentiment analysis for given keywords"""
        cache_key = f"sentiment_{'_'.join(keywords)}_{timeframe}"
        
        if self._is_cached(cache_key):
            return self.cache[cache_key]["data"]
        
        # Simulate sentiment analysis
        sentiment_data = {
            "keywords": keywords,
            "timeframe": timeframe,
            "overall_sentiment": self._calculate_sentiment_score(keywords),
            "sentiment_breakdown": {
                "positive": 0.45,
                "neutral": 0.35,
                "negative": 0.20
            },
            "sentiment_trend": "improving",  # improving, declining, stable
            "confidence_score": 0.78,
            "article_count": 156,
            "social_media_mentions": 2847,
            "key_themes": self._extract_key_themes(keywords),
            "influential_articles": self._get_influential_articles(keywords),
            "timestamp": datetime.now().isoformat()
        }
        
        self._cache_data(cache_key, sentiment_data)
        logger.info("📊 Market trend analysis completed")
        return sentiment_data
    
    async def analyze_nse_market_data(self) -> Dict[str, Any]:
        """Analyze NSE market data from dataset"""
        if not self.dataset_loader:
            return {"error": "No dataset loader available"}
        
        try:
            market_data = self.dataset_loader.get_market_data()
            if not market_data or "processed_data" not in market_data:
                return {"error": "No NSE market data available"}
            
            df = market_data["processed_data"]
            summary = market_data.get("summary", {})
            indicators = market_data.get("technical_indicators", {})
            
            analysis = {
                "symbol": "NSE-TATAGLOBAL11",
                "market_performance": self._analyze_market_performance(df, summary),
                "price_trends": self._analyze_price_trends(df),
                "volatility_analysis": self._analyze_market_volatility(df, indicators),
                "trading_patterns": self._analyze_trading_patterns(df),
                "technical_indicators": indicators,
                "market_sentiment": self._calculate_market_sentiment_from_data(df, summary),
                "support_resistance": self._identify_support_resistance_levels(df),
                "investment_signals": self._generate_investment_signals(df, indicators),
                "risk_metrics": self._calculate_market_risk_metrics(df),
                "comparative_analysis": self._compare_with_market_indices(df),
                "market_outlook": self._assess_market_outlook(df, indicators),
                "timestamp": datetime.now().isoformat()
            }
            
            logger.info("📈 NSE market data analysis completed")
            return analysis
            
        except Exception as e:
            logger.error(f"Error in NSE market analysis: {e}")
            return {"error": str(e)}
    
    async def get_government_expenditure_impact(self) -> Dict[str, Any]:
        """Analyze government expenditure impact on markets"""
        if not self.dataset_loader:
            return {"error": "No dataset loader available"}
        
        try:
            # Get social sector expenditure data
            social_data = self.dataset_loader.get_social_data()
            if not social_data or "processed_data" not in social_data:
                return {"error": "No social expenditure data available"}
            
            df = social_data["processed_data"]
            
            impact_analysis = {
                "expenditure_type": "social_sector",
                "market_impact": self._assess_expenditure_market_impact(df),
                "sector_beneficiaries": self._identify_beneficiary_sectors(df),
                "investment_opportunities": self._identify_investment_opportunities(df),
                "policy_implications": self._assess_policy_market_implications(df),
                "economic_multiplier_effects": self._calculate_multiplier_effects(df),
                "market_sectors_affected": self._identify_affected_market_sectors(df),
                "investment_recommendations": self._generate_expenditure_based_recommendations(df),
                "timestamp": datetime.now().isoformat()
            }
            
            logger.info("🏛️ Government expenditure market impact analysis completed")
            return impact_analysis
            
        except Exception as e:
            logger.error(f"Error in expenditure impact analysis: {e}")
            return {"error": str(e)}
    
    def _analyze_market_performance(self, df, summary: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze overall market performance"""
        try:
            if 'Close' not in df.columns or len(df) == 0:
                return {"performance": "no_data"}
            
            price_stats = summary.get("price_stats", {})
            current_price = price_stats.get("current_price", 0)
            highest_price = price_stats.get("highest_price", 0)
            lowest_price = price_stats.get("lowest_price", 0)
            average_price = price_stats.get("average_price", 0)
            
            # Calculate performance metrics
            price_range = highest_price - lowest_price if highest_price and lowest_price else 0
            current_position = ((current_price - lowest_price) / price_range * 100) if price_range > 0 else 50
            
            performance_vs_avg = ((current_price - average_price) / average_price * 100) if average_price > 0 else 0
            
            return {
                "current_price": current_price,
                "price_range": price_range,
                "current_position_in_range": round(current_position, 2),
                "performance_vs_average": round(performance_vs_avg, 2),
                "performance_rating": "strong" if performance_vs_avg > 10 else "moderate" if performance_vs_avg > 0 else "weak",
                "volatility": price_stats.get("volatility", 0)
            }
            
        except Exception as e:
            return {"performance": "analysis_error", "error": str(e)}
    
    def _analyze_price_trends(self, df) -> Dict[str, Any]:
        """Analyze price trends"""
        try:
            if 'Close' not in df.columns or len(df) < 10:
                return {"trend": "insufficient_data"}
            
            close_prices = df['Close']
            
            # Short-term trend (last 10 days)
            short_term_slope = self._calculate_trend_slope(close_prices.tail(10))
            
            # Medium-term trend (last 30 days)
            medium_term_slope = self._calculate_trend_slope(close_prices.tail(30)) if len(close_prices) >= 30 else short_term_slope
            
            # Long-term trend (all data)
            long_term_slope = self._calculate_trend_slope(close_prices)
            
            return {
                "short_term_trend": "bullish" if short_term_slope > 0.1 else "bearish" if short_term_slope < -0.1 else "sideways",
                "medium_term_trend": "bullish" if medium_term_slope > 0.1 else "bearish" if medium_term_slope < -0.1 else "sideways",
                "long_term_trend": "bullish" if long_term_slope > 0.1 else "bearish" if long_term_slope < -0.1 else "sideways",
                "trend_strength": abs(long_term_slope),
                "trend_consistency": "high" if abs(short_term_slope - long_term_slope) < 0.2 else "low"
            }
            
        except Exception as e:
            return {"trend": "analysis_error", "error": str(e)}
    
    def _calculate_trend_slope(self, prices) -> float:
        """Calculate trend slope for price series"""
        try:
            if len(prices) < 2:
                return 0
            
            # Simple linear regression slope
            x = list(range(len(prices)))
            y = list(prices)
            
            n = len(x)
            sum_x = sum(x)
            sum_y = sum(y)
            sum_xy = sum(x[i] * y[i] for i in range(n))
            sum_x_squared = sum(x[i] ** 2 for i in range(n))
            
            if n * sum_x_squared - sum_x ** 2 == 0:
                return 0
            
            slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
            return slope
            
        except:
            return 0
    
    def _analyze_market_volatility(self, df, indicators: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze market volatility"""
        try:
            daily_volatility = indicators.get("daily_volatility", 0)
            
            # Classify volatility
            if daily_volatility > 0.03:
                volatility_level = "high"
            elif daily_volatility > 0.015:
                volatility_level = "medium"
            else:
                volatility_level = "low"
            
            return {
                "daily_volatility": daily_volatility,
                "volatility_level": volatility_level,
                "volatility_percentile": self._calculate_volatility_percentile(df),
                "volatility_trend": "increasing"  # Simplified
            }
            
        except Exception as e:
            return {"volatility": "analysis_error", "error": str(e)}
    
    def _calculate_volatility_percentile(self, df) -> float:
        """Calculate current volatility percentile"""
        try:
            if 'Close' not in df.columns or len(df) < 30:
                return 50.0
            
            # Calculate rolling 30-day volatility
            returns = df['Close'].pct_change().dropna()
            rolling_vol = returns.rolling(window=30).std()
            
            if len(rolling_vol.dropna()) == 0:
                return 50.0
            
            current_vol = rolling_vol.iloc[-1]
            percentile = (rolling_vol < current_vol).mean() * 100
            
            return round(percentile, 1)
            
        except:
            return 50.0
    
    def _analyze_trading_patterns(self, df) -> Dict[str, Any]:
        """Analyze trading patterns"""
        try:
            if 'Volume' not in df.columns or len(df) == 0:
                return {"patterns": "no_volume_data"}
            
            avg_volume = df['Volume'].mean()
            recent_volume = df['Volume'].tail(5).mean()
            
            volume_trend = "increasing" if recent_volume > avg_volume * 1.2 else "decreasing" if recent_volume < avg_volume * 0.8 else "stable"
            
            return {
                "average_volume": float(avg_volume),
                "recent_volume": float(recent_volume),
                "volume_trend": volume_trend,
                "liquidity_assessment": "high" if avg_volume > 1000000 else "medium" if avg_volume > 100000 else "low"
            }
            
        except Exception as e:
            return {"patterns": "analysis_error", "error": str(e)}
    
    def _calculate_market_sentiment_from_data(self, df, summary: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate market sentiment from price data"""
        try:
            price_stats = summary.get("price_stats", {})
            current_price = price_stats.get("current_price", 0)
            average_price = price_stats.get("average_price", 0)
            
            if average_price == 0:
                return {"sentiment": "neutral", "score": 0.5}
            
            # Simple sentiment based on price relative to average
            price_ratio = current_price / average_price
            
            if price_ratio > 1.1:
                sentiment = "bullish"
                score = min(0.8, 0.5 + (price_ratio - 1) * 2)
            elif price_ratio < 0.9:
                sentiment = "bearish"
                score = max(0.2, 0.5 - (1 - price_ratio) * 2)
            else:
                sentiment = "neutral"
                score = 0.5
            
            return {
                "sentiment": sentiment,
                "score": round(score, 2),
                "confidence": 0.7,
                "factors": ["price_performance", "technical_indicators"]
            }
            
        except Exception as e:
            return {"sentiment": "neutral", "score": 0.5, "error": str(e)}
    
    def _identify_support_resistance_levels(self, df) -> Dict[str, Any]:
        """Identify support and resistance levels"""
        try:
            if 'High' not in df.columns or 'Low' not in df.columns or len(df) < 20:
                return {"levels": "insufficient_data"}
            
            # Simple support/resistance identification
            recent_high = df['High'].tail(20).max()
            recent_low = df['Low'].tail(20).min()
            current_price = df['Close'].iloc[-1]
            
            return {
                "resistance_level": float(recent_high),
                "support_level": float(recent_low),
                "current_price": float(current_price),
                "distance_to_resistance": round(((recent_high - current_price) / current_price * 100), 2),
                "distance_to_support": round(((current_price - recent_low) / current_price * 100), 2)
            }
            
        except Exception as e:
            return {"levels": "analysis_error", "error": str(e)}
    
    def _generate_investment_signals(self, df, indicators: Dict[str, Any]) -> Dict[str, Any]:
        """Generate investment signals"""
        try:
            signals = []
            signal_strength = 0
            
            # SMA signals
            current_price = df['Close'].iloc[-1]
            sma_20 = indicators.get("sma_20")
            sma_50 = indicators.get("sma_50")
            
            if sma_20 and current_price > sma_20:
                signals.append("Price above 20-day SMA (bullish)")
                signal_strength += 1
            
            if sma_50 and sma_20 and sma_20 > sma_50:
                signals.append("20-day SMA above 50-day SMA (bullish)")
                signal_strength += 1
            
            # Volume signals
            if 'Volume' in df.columns:
                avg_volume = df['Volume'].mean()
                recent_volume = df['Volume'].iloc[-1]
                
                if recent_volume > avg_volume * 1.5:
                    signals.append("High trading volume (increased interest)")
                    signal_strength += 0.5
            
            # Overall signal
            if signal_strength > 1.5:
                overall_signal = "buy"
            elif signal_strength < 0.5:
                overall_signal = "sell"
            else:
                overall_signal = "hold"
            
            return {
                "overall_signal": overall_signal,
                "signal_strength": round(signal_strength, 1),
                "individual_signals": signals,
                "confidence": min(signal_strength / 2, 1.0)
            }
            
        except Exception as e:
            return {"signal": "hold", "error": str(e)}
    
    # Placeholder methods for comprehensive analysis
    def _calculate_market_risk_metrics(self, df) -> Dict[str, Any]:
        return {"risk_metrics": "calculated"}
    
    def _compare_with_market_indices(self, df) -> Dict[str, Any]:
        return {"comparison": "completed"}
    
    def _assess_market_outlook(self, df, indicators: Dict[str, Any]) -> Dict[str, Any]:
        return {"outlook": "neutral"}
    
    def _assess_expenditure_market_impact(self, df) -> Dict[str, Any]:
        return {"impact": "positive"}
    
    def _identify_beneficiary_sectors(self, df) -> List[str]:
        return ["healthcare", "education", "infrastructure"]
    
    def _identify_investment_opportunities(self, df) -> List[str]:
        return ["Healthcare technology", "Educational services", "Infrastructure development"]
    
    def _assess_policy_market_implications(self, df) -> Dict[str, Any]:
        return {"implications": "positive_for_social_sectors"}
    
    def _calculate_multiplier_effects(self, df) -> Dict[str, Any]:
        return {"multiplier": 1.5}
    
    def _identify_affected_market_sectors(self, df) -> List[str]:
        return ["Healthcare", "Education", "Construction", "Technology"]
    
    def _generate_expenditure_based_recommendations(self, df) -> List[str]:
        return [
            "Consider healthcare sector investments",
            "Monitor education technology companies",
            "Watch infrastructure development stocks"
        ]
        return sentiment_data
    
    async def get_industry_trends(self, industry: str, period: str = "1m") -> Dict[str, Any]:
        """Get industry-specific trends and analysis"""
        cache_key = f"industry_trends_{industry}_{period}"
        
        if self._is_cached(cache_key):
            return self.cache[cache_key]["data"]
        
        # Simulate industry trend analysis
        trends_data = {
            "industry": industry,
            "analysis_period": period,
            "growth_trend": "positive",  # positive, negative, stable
            "growth_rate": 0.08,
            "market_size": self._estimate_market_size(industry),
            "key_drivers": self._identify_growth_drivers(industry),
            "challenges": self._identify_industry_challenges(industry),
            "emerging_opportunities": self._identify_opportunities(industry),
            "competitive_landscape": self._analyze_competition(industry),
            "regulatory_changes": self._track_regulatory_changes(industry),
            "technology_trends": self._identify_tech_trends(industry),
            "investment_activity": self._track_investment_activity(industry),
            "timestamp": datetime.now().isoformat()
        }
        
        self._cache_data(cache_key, trends_data)
        logger.info(f"📈 Industry trends analysis completed for {industry}")
        return trends_data
    
    async def get_competitor_analysis(self, company_name: str, industry: str) -> Dict[str, Any]:
        """Get competitive intelligence and analysis"""
        cache_key = f"competitor_analysis_{company_name}_{industry}"
        
        if self._is_cached(cache_key):
            return self.cache[cache_key]["data"]
        
        # Simulate competitor analysis
        analysis = {
            "target_company": company_name,
            "industry": industry,
            "direct_competitors": self._identify_competitors(company_name, industry),
            "market_share_analysis": self._analyze_market_share(company_name, industry),
            "competitive_positioning": self._analyze_positioning(company_name, industry),
            "strength_weakness_analysis": self._analyze_strengths_weaknesses(company_name),
            "competitive_threats": self._identify_threats(company_name, industry),
            "opportunities_gaps": self._identify_market_gaps(industry),
            "pricing_analysis": self._analyze_pricing_strategy(company_name, industry),
            "innovation_trends": self._track_innovation(industry),
            "merger_acquisition_activity": self._track_ma_activity(industry),
            "timestamp": datetime.now().isoformat()
        }
        
        self._cache_data(cache_key, analysis)
        logger.info(f"🏆 Competitor analysis completed for {company_name}")
        return analysis
    
    async def get_market_news(self, query: str = None, category: str = "general", limit: int = 20) -> List[Dict[str, Any]]:
        """Get latest market news by category and query"""
        cache_key = f"market_news_{category}_{query}_{limit}"
        
        if self._is_cached(cache_key):
            return self.cache[cache_key]["data"]
        
        # Generate news articles based on query and category
        articles = self._generate_news_articles(category, limit, query)
        
        self._cache_data(cache_key, articles)
        logger.info(f"📰 Market news retrieved for {category} (query: {query})")
        return articles
    
    async def get_market_performance(self, timeframe: str = "1d") -> Dict[str, Any]:
        """Get market performance metrics"""
        cache_key = f"market_performance_{timeframe}"
        
        if self._is_cached(cache_key):
            return self.cache[cache_key]["data"]
        
        # Simulate market performance data
        performance_data = {
            "timeframe": timeframe,
            "overall_performance": {
                "change_percent": 2.3,
                "trend": "positive",
                "volume": "high"
            },
            "sector_performance": {
                "technology": {"change": 3.1, "trend": "bullish"},
                "finance": {"change": 1.8, "trend": "stable"},
                "energy": {"change": -0.5, "trend": "bearish"}
            },
            "market_indicators": {
                "volatility": "medium",
                "sentiment": "optimistic",
                "risk_level": "moderate"
            }
        }
        
        self._cache_data(cache_key, performance_data)
        logger.info(f"📊 Market performance retrieved for {timeframe}")
        return performance_data
    
    async def get_economic_calendar(self, timeframe: str = "week") -> Dict[str, Any]:
        """Get economic calendar and events"""
        cache_key = f"economic_calendar_{timeframe}"
        
        if self._is_cached(cache_key):
            return self.cache[cache_key]["data"]
        
        # Simulate economic calendar
        calendar_data = {
            "timeframe": timeframe,
            "upcoming_events": self._generate_economic_events(timeframe),
            "high_impact_events": self._identify_high_impact_events(timeframe),
            "market_expectations": self._get_market_expectations(),
            "historical_impact": self._analyze_historical_impact(),
            "regional_focus": self._get_regional_calendar(),
            "event_countdown": self._calculate_event_countdown(),
            "timestamp": datetime.now().isoformat()
        }
        
        self._cache_data(cache_key, calendar_data)
        logger.info(f"📅 Economic calendar retrieved for {timeframe}")
        return calendar_data
    
    async def analyze_market_impact(self, scenario: str) -> Dict[str, Any]:
        """Analyze potential market impact of a business scenario"""
        # Simulate market impact analysis
        impact_analysis = {
            "scenario": scenario[:200] + "..." if len(scenario) > 200 else scenario,
            "market_impact_score": self._calculate_market_impact_score(scenario),
            "affected_sectors": self._identify_affected_sectors(scenario),
            "geographic_impact": self._analyze_geographic_impact(scenario),
            "timeline_analysis": {
                "short_term": self._analyze_short_term_impact(scenario),
                "medium_term": self._analyze_medium_term_impact(scenario),
                "long_term": self._analyze_long_term_impact(scenario)
            },
            "risk_factors": self._identify_market_risks(scenario),
            "opportunity_factors": self._identify_market_opportunities(scenario),
            "volatility_impact": self._assess_volatility_impact(scenario),
            "liquidity_impact": self._assess_liquidity_impact(scenario),
            "regulatory_implications": self._assess_regulatory_impact(scenario),
            "recommendations": self._generate_market_recommendations(scenario),
            "timestamp": datetime.now().isoformat()
        }
        
        logger.info("📊 Market impact analysis completed")
        return impact_analysis
    
    def _calculate_sentiment_score(self, keywords: List[str]) -> float:
        """Calculate overall sentiment score"""
        # Simplified sentiment calculation
        positive_keywords = ["growth", "profit", "success", "innovation", "opportunity"]
        negative_keywords = ["loss", "decline", "risk", "threat", "challenge"]
        
        positive_count = sum(1 for keyword in keywords if any(pos in keyword.lower() for pos in positive_keywords))
        negative_count = sum(1 for keyword in keywords if any(neg in keyword.lower() for neg in negative_keywords))
        
        if positive_count + negative_count == 0:
            return 0.5  # Neutral
        
        sentiment = positive_count / (positive_count + negative_count)
        return round(sentiment, 2)
    
    def _extract_key_themes(self, keywords: List[str]) -> List[str]:
        """Extract key themes from keywords"""
        themes = []
        keyword_str = " ".join(keywords).lower()
        
        if any(term in keyword_str for term in ["ai", "artificial intelligence", "machine learning"]):
            themes.append("Artificial Intelligence")
        if any(term in keyword_str for term in ["climate", "green", "sustainable", "renewable"]):
            themes.append("Sustainability")
        if any(term in keyword_str for term in ["digital", "technology", "tech", "innovation"]):
            themes.append("Digital Transformation")
        if any(term in keyword_str for term in ["crypto", "blockchain", "bitcoin"]):
            themes.append("Cryptocurrency")
        
        return themes[:5]
    
    def _get_influential_articles(self, keywords: List[str]) -> List[Dict[str, Any]]:
        """Get influential articles related to keywords"""
        return [
            {
                "title": f"Market Analysis: {' '.join(keywords[:2])}",
                "source": "Financial Times",
                "sentiment": "positive",
                "impact_score": 0.8,
                "publication_date": datetime.now().isoformat()
            },
            {
                "title": f"Industry Trends: {' '.join(keywords[:2])} Outlook",
                "source": "Bloomberg",
                "sentiment": "neutral",
                "impact_score": 0.6,
                "publication_date": (datetime.now() - timedelta(hours=2)).isoformat()
            }
        ]
    
    def _estimate_market_size(self, industry: str) -> Dict[str, Any]:
        """Estimate market size for industry"""
        size_estimates = {
            "fintech": {"value": 150000000000, "currency": "USD", "growth_rate": 0.12},
            "healthcare": {"value": 350000000000, "currency": "USD", "growth_rate": 0.08},
            "technology": {"value": 500000000000, "currency": "USD", "growth_rate": 0.15},
            "retail": {"value": 250000000000, "currency": "USD", "growth_rate": 0.06}
        }
        
        return size_estimates.get(industry.lower(), {"value": 100000000000, "currency": "USD", "growth_rate": 0.05})
    
    def _identify_growth_drivers(self, industry: str) -> List[str]:
        """Identify key growth drivers for industry"""
        drivers_map = {
            "fintech": ["Digital adoption", "Regulatory support", "Consumer demand", "Innovation"],
            "healthcare": ["Aging population", "Technology advancement", "Chronic diseases", "Preventive care"],
            "technology": ["AI advancement", "Cloud adoption", "Digital transformation", "Remote work"],
            "retail": ["E-commerce growth", "Omnichannel experience", "Personalization", "Mobile commerce"]
        }
        
        return drivers_map.get(industry.lower(), ["Market demand", "Innovation", "Economic growth"])
    
    def _generate_news_articles(self, category: str, limit: int, query: str = None) -> List[Dict[str, Any]]:
        """Generate simulated news articles based on category and query"""
        articles = []
        
        # Customize content based on query
        if query:
            search_terms = query.lower().split()
            title_context = f"Market Analysis: {' '.join(search_terms[:3]).title()}"
            summary_context = f"Analysis of {query} shows emerging trends in market dynamics..."
        else:
            title_context = f"{category.title()} Market Update - Key Developments"
            summary_context = f"Latest developments in {category} sector showing mixed signals..."
        
        for i in range(min(limit, 10)):  # Limit simulation
            articles.append({
                "id": f"article_{i+1}",
                "headline": f"{title_context} - Update {i+1}",
                "title": f"{title_context} - Update {i+1}",
                "summary": summary_context,
                "content": f"Detailed analysis of {query or category} market conditions with focus on recent developments...",
                "source": ["Reuters", "Bloomberg", "MarketWatch", "Financial Times"][i % 4],
                "sentiment": ["positive", "neutral", "negative"][i % 3],
                "impact_score": round(0.3 + (i % 7) * 0.1, 1),
                "score": round(0.5 + (i % 5) * 0.1, 1),  # For compatibility with search expectations
                "publication_date": (datetime.now() - timedelta(hours=i)).isoformat(),
                "tags": [category, "market", "analysis"] + (search_terms[:2] if query else [])
            })
        
        return articles
    
    def _calculate_market_impact_score(self, scenario: str) -> float:
        """Calculate market impact score for scenario"""
        # Simplified impact scoring
        impact_keywords = ["billion", "global", "major", "significant", "revolutionary"]
        low_impact_keywords = ["local", "small", "minor", "limited", "niche"]
        
        scenario_lower = scenario.lower()
        high_impact = sum(1 for keyword in impact_keywords if keyword in scenario_lower)
        low_impact = sum(1 for keyword in low_impact_keywords if keyword in scenario_lower)
        
        base_score = 0.5
        if high_impact > low_impact:
            base_score += min(high_impact * 0.1, 0.4)
        elif low_impact > high_impact:
            base_score -= min(low_impact * 0.1, 0.3)
        
        return round(base_score, 2)
    
    def _is_cached(self, key: str) -> bool:
        """Check if data is cached and still valid"""
        if key not in self.cache:
            return False
        
        cache_time = self.cache[key]["timestamp"]
        return (datetime.now() - cache_time).seconds < self.cache_ttl
    
    def _cache_data(self, key: str, data: Any):
        """Cache data with timestamp"""
        self.cache[key] = {
            "data": data,
            "timestamp": datetime.now()
        }
    
    # Additional placeholder methods for comprehensive market analysis
    def _identify_competitors(self, company: str, industry: str) -> List[str]:
        return ["Competitor A", "Competitor B", "Competitor C"]
    
    def _analyze_market_share(self, company: str, industry: str) -> Dict[str, Any]:
        return {"market_share": 0.15, "rank": 3, "trend": "growing"}
    
    def _get_trending_topics(self, category: str) -> List[str]:
        return ["Market volatility", "Interest rates", "Technology adoption"]
    
    def _identify_market_movers(self) -> List[Dict[str, Any]]:
        return [{"event": "Fed announcement", "impact": "high", "sector": "financial"}]
