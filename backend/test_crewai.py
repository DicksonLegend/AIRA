"""
🧪 CrewAI Integration Test Script
Quick test to verify CrewAI orchestrator works correctly
"""
import asyncio
import sys
import os

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services.four_pillars_crewai import FourPillarsCrewAI

async def test_crewai_orchestrator():
    """Test CrewAI orchestrator functionality"""
    print("🧪 Testing CrewAI Orchestrator...")
    
    try:
        # Initialize orchestrator
        orchestrator = FourPillarsCrewAI()
        print("✅ CrewAI Orchestrator created")
        
        # Initialize agents
        await orchestrator.initialize()
        print("✅ Agents initialized")
        
        # Test status
        status = await orchestrator.get_system_status()
        print(f"✅ Status check: {status}")
        
        # Test simple analysis
        test_scenario = "A tech startup wants to launch an AI-powered food delivery app in urban markets."
        
        print(f"🎯 Testing analysis with scenario: {test_scenario}")
        
        result = await orchestrator.analyze_business_scenario(test_scenario, "financial")
        print("✅ Financial analysis completed")
        print(f"📊 Result summary: {result.get('crew_output', {}).get('summary', 'No summary')}")
        
        print("\n🚀 CrewAI integration test successful!")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(test_crewai_orchestrator())
    sys.exit(0 if success else 1)
