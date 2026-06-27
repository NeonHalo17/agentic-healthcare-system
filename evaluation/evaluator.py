import json 
import time 
from pathlib import Path 
from agents.healthcare_agent import HealthcareAgent 
from evaluation.metrics import Metrics 
from evaluation.performance_logger import PerformanceLogger 
from evaluation.qa_eval_chain import QAEvaluator 

class Evaluator: 
    def __init__(self): 
        self.agent = HealthcareAgent() 
        self.metrics = Metrics() 
        self.logger = PerformanceLogger() 
        self.qa = QAEvaluator() 
        self.test_cases = self.load_test_cases() 
        
    def load_test_cases(self): 
        path = (Path(__file__).parent / "test_cases.json") 
            
        with open(path) as f: 
            return json.load(f) 
            
    def run(self): 
        details = [] 
        for index, case in enumerate(self.test_cases): 
            question = case["question"] 
            reference = case["reference"] 
            session = f"evaluation_{index}" 
            self.logger.start("total") 
            start = time.perf_counter() 
            response = self.agent.run( query=question, session_id=session ) 
            latency = ( time.perf_counter() - start ) * 1000 
            self.logger.stop("total") 
            prediction = response["answer"] 
            evaluation = self.qa.evaluate( question=question, prediction=prediction, reference=reference ) 
            passed = ( evaluation["results"] .strip() .upper() == "CORRECT" ) 
            self.metrics.add_case( passed, latency ) 
            tool_results = response.get( "tool_results", {} ) 
            if "appointment_confirmation" in tool_results: 
                booking = tool_results[ "appointment_confirmation" ] 
                success = ( booking.get("status") == "success" ) 
                self.metrics.add_booking( success ) 
                details.append( { "question": question, "reference": reference, "prediction": prediction, "evaluation": evaluation, "latency_ms": round( latency, 2 ) } ) 
            
        return { "metrics": self.metrics.summary(), "timings": self.logger.results(), "details": details }