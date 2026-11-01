import ast
import sys
from sklearn.ensemble import RandomForestClassifier
import numpy as np

def extract_features(code):
    """Extract simple metrics that correlate with bugs"""
    try:
        tree = ast.parse(code)
        num_funcs = len([n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)])
        num_loops = len([n for n in ast.walk(tree) if isinstance(n, (ast.For, ast.While))])
        num_ifs = len([n for n in ast.walk(tree) if isinstance(n, ast.If))])
        lines = len(code.split('\n'))
        return [num_funcs, num_loops, num_ifs, lines]
    except:
        return [0,0,0,0]

def main():
    file_path = sys.argv[2] if len(sys.argv)>2 else "samples/buggy_example.py"
    with open(file_path) as f:
        code = f.read()
    features = extract_features(code)
    # Simple heuristic model - you will train with real data
    print(f"Features: {features}")
    if features[1] > 3 and features[3] > 50:
        print("⚠️ POTENTIAL BUG RISK: High loop complexity")
    else:
        print("✅ Low risk")

if __name__ == "__main__":
    main()
