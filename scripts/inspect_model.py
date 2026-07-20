import pickle, sys
try:
    with open("RFmodel.pkl","rb") as f:
        m = pickle.load(f)
except Exception as e:
    print("ERROR loading model:",e)
    sys.exit(1)
print("model_type:", type(m))
fn = getattr(m, 'feature_names_in_', None)
print("feature_names_in_:", fn)
print("n_features_in_:", getattr(m, 'n_features_in_', None))
# If it's a pipeline, inspect steps
try:
    from sklearn.pipeline import Pipeline
    if isinstance(m, Pipeline):
        for name, step in m.named_steps.items():
            print("pipeline step:", name, type(step), getattr(step, 'feature_names_in_', None))
except Exception:
    pass
print("has predict:", hasattr(m, 'predict'))
