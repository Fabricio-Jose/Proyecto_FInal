
from analyzer import diff_ast
from recommender import engine

def run_analysis(old_version_path, new_version_path):
    diffs = diff_ast.compare_versions(old_version_path, new_version_path)
    recommendations = engine.generate_recommendations(diffs)
    return recommendations

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print("Uso: python main.py <path_version_anterior> <path_version_nueva>")
        sys.exit(1)

    old_path = sys.argv[1]
    new_path = sys.argv[2]
    resultado = run_analysis(old_path, new_path)
    for rec in resultado:
        print(rec)
